from typing import Any, Dict, Union, Optional

import httpx


class Response:
    def __init__(self, response: httpx.Response):
        self._response = response
        self.status_code = response.status_code
        self.headers = response.headers
        self.url = str(response.url)
        self.reason = response.reason_phrase
        self.ok = response.status_code < 400

    async def text(self) -> str:
        return self._response.text

    async def read(self) -> bytes:
        return self._response.content

    async def content(self) -> bytes:
        return self.read()

    async def json(self) -> Any:
        return self._response.json()


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
        ssl: Optional[bool] = None,
    ) -> Response:
        async with httpx.AsyncClient(verify=ssl) as client:
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
            return Response(response)

    async def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
        allow_redirects: bool = True,
        ssl: Optional[bool] = None,
    ) -> Response:
        return await self._request(
            "GET",
            url,
            headers=headers,
            params=params,
            timeout=timeout,
            allow_redirects=allow_redirects,
            ssl=ssl,
        )

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
        ssl: Optional[bool] = None,
    ) -> Response:
        return await self._request(
            "POST",
            url,
            headers=headers,
            params=params,
            data=data,
            json=json,
            files=files,
            timeout=timeout,
            allow_redirects=allow_redirects,
            ssl=ssl,
        )

    async def put(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Union[Dict[str, Any], bytes]] = None,
        json: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        allow_redirects: bool = True,
        ssl: Optional[bool] = None,
    ) -> Response:
        return await self._request(
            "PUT",
            url,
            headers=headers,
            params=params,
            data=data,
            json=json,
            timeout=timeout,
            allow_redirects=allow_redirects,
            ssl=ssl,
        )

    async def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Union[Dict[str, Any], bytes]] = None,
        json: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        allow_redirects: bool = True,
        ssl: Optional[bool] = None,
    ) -> Response:
        return await self._request(
            "DELETE",
            url,
            headers=headers,
            params=params,
            data=data,
            json=json,
            timeout=timeout,
            allow_redirects=allow_redirects,
            ssl=ssl,
        )
