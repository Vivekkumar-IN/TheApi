from typing import Any, Dict, Union, Optional

from httpx import Response, AsyncClient


class Request:
    async def _request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Union[Dict[str, Any], bytes]] = None,
        json: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, bytes]] = None,
        timeout: Optional[int] = None,
        allow_redirects: bool = True,
        verify: Optional[bool] = None,
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
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
        allow_redirects: bool = True,
        verify: Optional[bool] = None,
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
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Union[Dict[str, Any], bytes]] = None,
        json: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, bytes]] = None,
        timeout: Optional[int] = None,
        allow_redirects: bool = True,
        verify: Optional[bool] = None,
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
