from typing import Any, Dict, Union, Optional

import aiohttp


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
        return_json: bool = True,
        return_text: bool = False,
        return_content: bool = False,
    ) -> Any:
        """
        Make an HTTP request.

        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE).
            url (str): URL to make the request to.
            headers (Optional[Dict[str, str]]): HTTP headers to send with the request.
            params (Optional[Dict[str, str]]): Query string parameters to send with the request.
            data (Optional[Union[Dict[str, Any], bytes]]): Data to send in the body of the request.
            json (Optional[Dict[str, Any]]): JSON serializable object to send in the body of the request.
            files (Optional[Dict[str, bytes]]): Files to send with the request.
            timeout (Optional[int]): Request timeout.
            allow_redirects (bool): Whether to allow redirects.
            ssl (Optional[bool]): SSL configuration.
            return_json (bool): Return the response as JSON.
            return_text (bool): Return the response as text.
            return_content (bool): Return the response as raw bytes.

        Returns:
            Any: The response data.
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
                if return_text:
                    response_data = await response.text()
                elif return_content:
                    response_data = await response.read()
                elif return_json:
                    response_data = await response.json()
                else:
                    response_data = {
                        "status_code": response.status,
                        "headers": response.headers,
                        "text": await response.text(),
                    }
                return response_data

    async def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
        allow_redirects: bool = True,
        ssl: Optional[bool] = None,
        return_json: bool = True,
        return_text: bool = False,
        return_content: bool = False,
    ) -> Any:
        """
        Make a GET request.

        Args:
            url (str): URL to make the request to.
            headers (Optional[Dict[str, str]]): HTTP headers to send with the request.
            params (Optional[Dict[str, str]]): Query string parameters to send with the request.
            timeout (Optional[int]): Request timeout.
            allow_redirects (bool): Whether to allow redirects.
            ssl (Optional[bool]): SSL configuration.
            return_json (bool): Return the response as JSON.
            return_text (bool): Return the response as text.
            return_content (bool): Return the response as raw bytes.

        Returns:
            Any: The response data.
        """
        return await self._request(
            "GET",
            url,
            headers=headers,
            params=params,
            timeout=timeout,
            allow_redirects=allow_redirects,
            ssl=ssl,
            return_json=return_json,
            return_text=return_text,
            return_content=return_content,
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
        return_json: bool = True,
        return_text: bool = False,
        return_content: bool = False,
    ) -> Any:
        """
        Make a POST request.

        Args:
            url (str): URL to make the request to.
            headers (Optional[Dict[str, str]]): HTTP headers to send with the request.
            params (Optional[Dict[str, str]]): Query string parameters to send with the request.
            data (Optional[Union[Dict[str, Any], bytes]]): Data to send in the body of the request.
            json (Optional[Dict[str, Any]]): JSON serializable object to send in the body of the request.
            files (Optional[Dict[str, bytes]]): Files to send with the request.
            timeout (Optional[int]): Request timeout.
            allow_redirects (bool): Whether to allow redirects.
            ssl (Optional[bool]): SSL configuration.
            return_json (bool): Return the response as JSON.
            return_text (bool): Return the response as text.
            return_content (bool): Return the response as raw bytes.

        Returns:
            Any: The response data.
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
            return_json=return_json,
            return_text=return_text,
            return_content=return_content,
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
        return_json: bool = True,
        return_text: bool = False,
        return_content: bool = False,
    ) -> Any:
        """
        Make a PUT request.

        Args:
            url (str): URL to make the request to.
            headers (Optional[Dict[str, str]]): HTTP headers to send with the request.
            params (Optional[Dict[str, str]]): Query string parameters to send with the request.
            data (Optional[Union[Dict[str, Any], bytes]]): Data to send in the body of the request.
            json (Optional[Dict[str, Any]]): JSON serializable object to send in the body of the request.
            timeout (Optional[int]): Request timeout.
            allow_redirects (bool): Whether to allow redirects.
            ssl (Optional[bool]): SSL configuration.
            return_json (bool): Return the response as JSON.
            return_text (bool): Return the response as text.
            return_content (bool): Return the response as raw bytes.

        Returns:
            Any: The response data.
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
            return_json=return_json,
            return_text=return_text,
            return_content=return_content,
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
        return_json: bool = True,
        return_text: bool = False,
        return_content: bool = False,
    ) -> Any:
        """
        Make a DELETE request.

        Args:
            url (str): URL to make the request to.
            headers (Optional[Dict[str, str]]): HTTP headers to send with the request.
            params (Optional[Dict[str, str]]): Query string parameters to send with the request.
            data (Optional[Union[Dict[str, Any], bytes]]): Data to send in the body of the request.
            json (Optional[Dict[str, Any]]): JSON serializable object to send in the body of the request.
            timeout (Optional[int]): Request timeout.
            allow_redirects (bool): Whether to allow redirects.
            ssl (Optional[bool]): SSL configuration.
            return_json (bool): Return the response as JSON.
            return_text (bool): Return the response as text.
            return_content (bool): Return the response as raw bytes.

        Returns:
            Any: The response data.
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
            return_json=return_json,
            return_text=return_text,
            return_content=return_content,
        )
