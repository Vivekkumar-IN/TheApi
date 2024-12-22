import aiohttp

class Request:
    async def _request(
      self, 
      method, 
      url, 
      headers=None, 
      params=None, 
      data=None, 
      json=None, 
      files=None, 
      timeout=None, 
      allow_redirects=True, 
      ssl=None, 
      return_json=True, 
      return_text=False, 
      return_content=False
    ):
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
                ssl=ssl
            ) as response:
                if return_json:
                    response_data = await response.json()
                elif return_text:
                    response_data = await response.text()
                elif return_content:
                    response_data = await response.read()
                else:
                    response_data = {
                        'status_code': response.status,
                        'headers': response.headers,
                        'text': await response.text()
                    }
                return response_data

    async def get(self, url, headers=None, params=None, timeout=None, allow_redirects=True, ssl=None, return_json=True, return_text=False, return_content=False):
        return await self._request('GET', url, headers=headers, params=params, timeout=timeout, allow_redirects=allow_redirects, ssl=ssl, return_json=return_json, return_text=return_text, return_content=return_content)

    async def post(self, url, headers=None, params=None, data=None, json=None, files=None, timeout=None, allow_redirects=True, ssl=None, return_json=True, return_text=False, return_content=False):
        return await self._request('POST', url, headers=headers, params=params, data=data, json=json, files=files, timeout=timeout, allow_redirects=allow_redirects, ssl=ssl, return_json=return_json, return_text=return_text, return_content=return_content)

    async def put(self, url, headers=None, params=None, data=None, json=None, timeout=None, allow_redirects=True, ssl=None, return_json=True, return_text=False, return_content=False):
        return await self._request('PUT', url, headers=headers, params=params, data=data, json=json,  timeout=timeout, allow_redirects=allow_redirects, ssl=ssl, return_json=return_json, return_text=return_text, return_content=return_content)

    async def delete(self, url, headers=None, params=None, data=None, json=None, timeout=None, allow_redirects=True, ssl=None, return_json=True, return_text=False, return_content=False):
        return await self._request('DELETE', url, headers=headers, params=params, data=data, json=json, timeout=timeout, allow_redirects=allow_redirects, ssl=ssl, return_json=return_json, return_text=return_text, return_content=return_content)
