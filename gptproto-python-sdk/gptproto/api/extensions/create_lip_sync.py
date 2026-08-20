from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unified_error_response import UnifiedErrorResponse
from ...models.unified_lip_sync_request import UnifiedLipSyncRequest
from ...models.unified_task_result import UnifiedTaskResult
from ...types import Response


def _get_kwargs(
    *,
    body: UnifiedLipSyncRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/lip-sync",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UnifiedErrorResponse | UnifiedTaskResult | None:
    if response.status_code == 202:
        response_202 = UnifiedTaskResult.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UnifiedErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UnifiedErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UnifiedErrorResponse | UnifiedTaskResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UnifiedLipSyncRequest,
) -> Response[UnifiedErrorResponse | UnifiedTaskResult]:
    """Submit an asynchronous lip-sync task

    Args:
        body (UnifiedLipSyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnifiedErrorResponse | UnifiedTaskResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UnifiedLipSyncRequest,
) -> UnifiedErrorResponse | UnifiedTaskResult | None:
    """Submit an asynchronous lip-sync task

    Args:
        body (UnifiedLipSyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnifiedErrorResponse | UnifiedTaskResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UnifiedLipSyncRequest,
) -> Response[UnifiedErrorResponse | UnifiedTaskResult]:
    """Submit an asynchronous lip-sync task

    Args:
        body (UnifiedLipSyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnifiedErrorResponse | UnifiedTaskResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UnifiedLipSyncRequest,
) -> UnifiedErrorResponse | UnifiedTaskResult | None:
    """Submit an asynchronous lip-sync task

    Args:
        body (UnifiedLipSyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnifiedErrorResponse | UnifiedTaskResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
