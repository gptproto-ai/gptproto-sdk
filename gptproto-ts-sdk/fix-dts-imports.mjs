// Post-process generated .d.ts files so their relative imports use explicit
// ".js" extensions. This is required for consumers using TypeScript's
// "nodenext" module resolution (Node-style ESM), which does not resolve
// extension-less or directory imports the way "bundler" mode does.
//
// openapi-typescript-codegen emits extension-less imports (e.g. from './models/X');
// tsc with moduleResolution=bundler keeps them as-is. We rewrite them to
// from './models/X.js', which TypeScript maps back to X.d.ts under nodenext.
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';

const EXT_RE = /from\s+'(\.\.?\/[^']*)'/g;

async function walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, entry.name);
    if (entry.isDirectory()) {
      await walk(p);
    } else if (entry.name.endsWith('.d.ts')) {
      const content = await readFile(p, 'utf8');
      const fixed = content.replace(EXT_RE, (match, spec) => {
        if (/\.(js|json|mjs|cjs)$/.test(spec)) return match; // already has ext
        return `from '${spec}.js'`;
      });
      if (fixed !== content) {
        await writeFile(p, fixed);
        console.log(`fixed: ${p}`);
      }
    }
  }
}

await walk('dist');
console.log('dts import fix done');
