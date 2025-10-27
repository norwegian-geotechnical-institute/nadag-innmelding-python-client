from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.diagnostics_dto import DiagnosticsDto
from ...types import Response


def _get_kwargs(
    root_lokal_id: UUID,
    root_versjon_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/validation/diagnosticsFromRoot/{root_lokal_id}/{root_versjon_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DiagnosticsDto]]:
    if response.status_code == 200:
        response_200 = DiagnosticsDto.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DiagnosticsDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    root_lokal_id: UUID,
    root_versjon_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DiagnosticsDto]]:
    """Fetches a DiagnosticsDto from root ID.

     Fetches all diagnostics from the Identifikasjon of a root.

    Args:
        root_lokal_id (UUID):
        root_versjon_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DiagnosticsDto]]
    """

    kwargs = _get_kwargs(
        root_lokal_id=root_lokal_id,
        root_versjon_id=root_versjon_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    root_lokal_id: UUID,
    root_versjon_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DiagnosticsDto]]:
    """Fetches a DiagnosticsDto from root ID.

     Fetches all diagnostics from the Identifikasjon of a root.

    Args:
        root_lokal_id (UUID):
        root_versjon_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DiagnosticsDto]
    """

    return sync_detailed(
        root_lokal_id=root_lokal_id,
        root_versjon_id=root_versjon_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    root_lokal_id: UUID,
    root_versjon_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DiagnosticsDto]]:
    """Fetches a DiagnosticsDto from root ID.

     Fetches all diagnostics from the Identifikasjon of a root.

    Args:
        root_lokal_id (UUID):
        root_versjon_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DiagnosticsDto]]
    """

    kwargs = _get_kwargs(
        root_lokal_id=root_lokal_id,
        root_versjon_id=root_versjon_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    root_lokal_id: UUID,
    root_versjon_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DiagnosticsDto]]:
    """Fetches a DiagnosticsDto from root ID.

     Fetches all diagnostics from the Identifikasjon of a root.

    Args:
        root_lokal_id (UUID):
        root_versjon_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DiagnosticsDto]
    """

    return (
        await asyncio_detailed(
            root_lokal_id=root_lokal_id,
            root_versjon_id=root_versjon_id,
            client=client,
        )
    ).parsed
