from typing import Any

from httpx import AsyncClient, Response


class Request:
    async def _request(
        self,
        method: str,
        url: str,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        data: dict[str, Any] | bytes | None = None,
        json: dict[str, Any] | None = None,
        files: dict[str, bytes] | None = None,
        timeout: int | None = None,
        allow_redirects: bool = True,
        verify: bool | None = None,
    ) -> Response:
        async with AsyncClient(verify=verify) as client:
            response = await client.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                content=data,
                json=json,
                files=files,
                timeout=timeout,
                follow_redirects=allow_redirects,
            )
            return response

    async def get(
        self,
        url: str,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        timeout: int | None = None,
        allow_redirects: bool = True,
        verify: bool | None = None,
    ) -> Response:
        r = await self._request(
            "GET",
            url,
            headers=headers,
            params=params,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=verify,
        )
        return r

    async def post(
        self,
        url: str,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        data: dict[str, Any] | bytes | None = None,
        json: dict[str, Any] | None = None,
        files: dict[str, bytes] | None = None,
        timeout: int | None = None,
        allow_redirects: bool = True,
        verify: bool | None = None,
    ) -> Response:
        r = await self._request(
            "POST",
            url,
            headers=headers,
            params=params,
            data=data,
            json=json,
            files=files,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=verify,
        )
        return r
