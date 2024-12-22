"""from typing import Any, Dict, Union, Optional

import aiohttp


class Response:
    def __init__(self, response: aiohttp.ClientResponse):
        self._response = response
        self.status_code = response.status
        self.headers = response.headers
        self.url = str(response.url)
        self.reason = response.reason
        self.ok = response.status < 400

    async def text(self) -> str:
        """
        Returns:
            str: The response content as text.
        """
        result = await self._response.text()
        return result

    async def read(self) -> bytes:
        """
        Returns:
            bytes: The raw response content.
        """
        result = await self._response.read()
        return result

    async def content(self) -> bytes:
        """
        Returns:
            bytes: The raw response content.
        """
        result = await self.read()
        return result

    async def json(self) -> Any:
        """
        Returns:
            Any: The JSON-decoded response content.
        """
        result = await self._response.json()
        return result


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
        """
        Sends an HTTP request.

        Args:
            method (str): The HTTP method (e.g., 'GET', 'POST').
            url (str): The target URL.
            headers (Optional[Dict[str, str]]): Optional headers to include in the request.
            params (Optional[Dict[str, str]]): Query parameters to include in the URL.
            data (Optional[Union[Dict[str, Any], bytes]]): Form data or raw bytes to include in the body.
            json (Optional[Dict[str, Any]]): JSON data to include in the body.
            files (Optional[Dict[str, bytes]]): Files to include in the body (currently unused).
            timeout (Optional[int]): Timeout for the request in seconds.
            allow_redirects (bool): Whether to follow redirects (default is True).
            ssl (Optional[bool]): Whether to verify SSL certificates (default is None).

        Returns:
            Response: A wrapper around the aiohttp response object.
        """
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                timeout=timeout,
                allow_redirects=allow_redirects,
                ssl=ssl,
            ) as response:
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
        """
        Sends a GET request.

        Args:
            url (str): The target URL.
            headers (Optional[Dict[str, str]]): Optional headers to include in the request.
            params (Optional[Dict[str, str]]): Query parameters to include in the URL.
            timeout (Optional[int]): Timeout for the request in seconds.
            allow_redirects (bool): Whether to follow redirects (default is True).
            ssl (Optional[bool]): Whether to verify SSL certificates (default is None).

        Returns:
            Response: A wrapper around the aiohttp response object.
        """
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
        """
        Sends a POST request.

        Args:
            url (str): The target URL.
            headers (Optional[Dict[str, str]]): Optional headers to include in the request.
            params (Optional[Dict[str, str]]): Query parameters to include in the URL.
            data (Optional[Union[Dict[str, Any], bytes]]): Form data or raw bytes to include in the body.
            json (Optional[Dict[str, Any]]): JSON data to include in the body.
            files (Optional[Dict[str, bytes]]): Files to include in the body (currently unused).
            timeout (Optional[int]): Timeout for the request in seconds.
            allow_redirects (bool): Whether to follow redirects (default is True).
            ssl (Optional[bool]): Whether to verify SSL certificates (default is None).

        Returns:
            Response: A wrapper around the aiohttp response object.
        """
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
        """
        Sends a PUT request.

        Args:
            url (str): The target URL.
            headers (Optional[Dict[str, str]]): Optional headers to include in the request.
            params (Optional[Dict[str, str]]): Query parameters to include in the URL.
            data (Optional[Union[Dict[str, Any], bytes]]): Form data or raw bytes to include in the body.
            json (Optional[Dict[str, Any]]): JSON data to include in the body.
            timeout (Optional[int]): Timeout for the request in seconds.
            allow_redirects (bool): Whether to follow redirects (default is True).
            ssl (Optional[bool]): Whether to verify SSL certificates (default is None).

        Returns:
            Response: A wrapper around the aiohttp response object.
        """
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
        """
        Sends a DELETE request.

        Args:
            url (str): The target URL.
            headers (Optional[Dict[str, str]]): Optional headers to include in the request.
            params (Optional[Dict[str, str]]): Query parameters to include in the URL.
            data (Optional[Union[Dict[str, Any], bytes]]): Form data or raw bytes to include in the body.
            json (Optional[Dict[str, Any]]): JSON data to include in the body.
            timeout (Optional[int]): Timeout for the request in seconds.
            allow_redirects (bool): Whether to follow redirects (default is True).
            ssl (Optional[bool]): Whether to verify SSL certificates (default is None).

        Returns:
            Response: A wrapper around the aiohttp response object.
        """
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
        )"""


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
        async with httpx.AsyncClient() as client:
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
                verify=ssl,
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