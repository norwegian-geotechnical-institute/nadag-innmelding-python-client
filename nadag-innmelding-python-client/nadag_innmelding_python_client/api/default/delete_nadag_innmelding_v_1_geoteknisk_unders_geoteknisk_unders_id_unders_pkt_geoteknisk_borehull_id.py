from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validated_geoteknisk_unders import ValidatedGeotekniskUnders
from ...types import Response


def _get_kwargs(
    geoteknisk_unders_id: str,
    geoteknisk_borehull_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/nadag/innmelding/v1/GeotekniskUnders/{geoteknisk_unders_id}/undersPkt/{geoteknisk_borehull_id}".format(
            geoteknisk_unders_id=quote(str(geoteknisk_unders_id), safe=""),
            geoteknisk_borehull_id=quote(str(geoteknisk_borehull_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ValidatedGeotekniskUnders | None:
    if response.status_code == 200:
        response_200 = ValidatedGeotekniskUnders.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ValidatedGeotekniskUnders]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    geoteknisk_unders_id: str,
    geoteknisk_borehull_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ValidatedGeotekniskUnders]:
    """Deletes a GeotekniskBorehull.

     Deletes a GeotekniskBorehull.

    Args:
        geoteknisk_unders_id (str):
        geoteknisk_borehull_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidatedGeotekniskUnders]
    """

    kwargs = _get_kwargs(
        geoteknisk_unders_id=geoteknisk_unders_id,
        geoteknisk_borehull_id=geoteknisk_borehull_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    geoteknisk_unders_id: str,
    geoteknisk_borehull_id: str,
    *,
    client: AuthenticatedClient,
) -> ValidatedGeotekniskUnders | None:
    """Deletes a GeotekniskBorehull.

     Deletes a GeotekniskBorehull.

    Args:
        geoteknisk_unders_id (str):
        geoteknisk_borehull_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidatedGeotekniskUnders
    """

    return sync_detailed(
        geoteknisk_unders_id=geoteknisk_unders_id,
        geoteknisk_borehull_id=geoteknisk_borehull_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    geoteknisk_unders_id: str,
    geoteknisk_borehull_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ValidatedGeotekniskUnders]:
    """Deletes a GeotekniskBorehull.

     Deletes a GeotekniskBorehull.

    Args:
        geoteknisk_unders_id (str):
        geoteknisk_borehull_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidatedGeotekniskUnders]
    """

    kwargs = _get_kwargs(
        geoteknisk_unders_id=geoteknisk_unders_id,
        geoteknisk_borehull_id=geoteknisk_borehull_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    geoteknisk_unders_id: str,
    geoteknisk_borehull_id: str,
    *,
    client: AuthenticatedClient,
) -> ValidatedGeotekniskUnders | None:
    """Deletes a GeotekniskBorehull.

     Deletes a GeotekniskBorehull.

    Args:
        geoteknisk_unders_id (str):
        geoteknisk_borehull_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidatedGeotekniskUnders
    """

    return (
        await asyncio_detailed(
            geoteknisk_unders_id=geoteknisk_unders_id,
            geoteknisk_borehull_id=geoteknisk_borehull_id,
            client=client,
        )
    ).parsed
