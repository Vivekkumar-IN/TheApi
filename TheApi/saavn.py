import aiohttp


class SaavnAPI:
    def __init__(self):
        """
        Initializes the JioSaavnAPI with a base URL.

        Args:
            base_url (str): The base URL for the JioSaavn API.
        """
        self.base_url = base_url

    async def _make_request(self, url: str, params: dict = None):
        """
        Makes an HTTP GET request to the specified URL with optional parameters.

        Args:
            url (str): The URL to make the request to.
            params (dict, optional): The parameters to include in the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            aiohttp.ClientError: If the request fails.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                return await response.json()

    async def search(self, query: str):
        """
        Searches globally for songs, albums, artists, and playlists.

        Args:
            query (str): The search query.

        Returns:
            dict: The search results.
        """
        url = f"{self.base_url}/api/search"
        return await self._make_request(url, params={"query": query})

    async def search_songs(self, query: str, page: int = 0, limit: int = 10):
        """
        Searches for songs.

        Args:
            query (str): The search query.
            page (int, optional): The page number to retrieve. Defaults to 0.
            limit (int, optional): The number of results per page. Defaults to 10.

        Returns:
            dict: The search results for songs.
        """
        url = f"{self.base_url}/api/search/songs"
        return await self._make_request(
            url, params={"query": query, "page": page, "limit": limit}
        )

    async def search_albums(self, query: str, page: int = 0, limit: int = 10):
        """
        Searches for albums.

        Args:
            query (str): The search query.
            page (int, optional): The page number to retrieve. Defaults to 0.
            limit (int, optional): The number of results per page. Defaults to 10.

        Returns:
            dict: The search results for albums.
        """
        url = f"{self.base_url}/api/search/albums"
        return await self._make_request(
            url, params={"query": query, "page": page, "limit": limit}
        )

    async def search_artists(self, query: str, page: int = 0, limit: int = 10):
        """
        Searches for artists.

        Args:
            query (str): The search query.
            page (int, optional): The page number to retrieve. Defaults to 0.
            limit (int, optional): The number of results per page. Defaults to 10.

        Returns:
            dict: The search results for artists.
        """
        url = f"{self.base_url}/api/search/artists"
        return await self._make_request(
            url, params={"query": query, "page": page, "limit": limit}
        )

    async def search_playlists(self, query: str, page: int = 0, limit: int = 10):
        """
        Searches for playlists.

        Args:
            query (str): The search query.
            page (int, optional): The page number to retrieve. Defaults to 0.
            limit (int, optional): The number of results per page. Defaults to 10.

        Returns:
            dict: The search results for playlists.
        """
        url = f"{self.base_url}/api/search/playlists"
        return await self._make_request(
            url, params={"query": query, "page": page, "limit": limit}
        )

    async def get_song_by_id(self, song_id: str):
        """
        Retrieves a song by its ID.

        Args:
            song_id (str): The ID of the song.

        Returns:
            dict: The song details.
        """
        url = f"{self.base_url}/api/songs/{song_id}"
        return await self._make_request(url)

    async def get_song_lyrics(self, song_id: str):
        """
        Retrieves lyrics for a song by its ID.

        Args:
            song_id (str): The ID of the song.

        Returns:
            dict: The song lyrics.
        """
        url = f"{self.base_url}/api/songs/{song_id}/lyrics"
        return await self._make_request(url)

    async def get_song_suggestions(self, song_id: str, limit: int = 10):
        """
        Retrieves song suggestions based on the given song ID.

        Args:
            song_id (str): The ID of the song.
            limit (int, optional): The number of suggestions to retrieve. Defaults to 10.

        Returns:
            dict: The song suggestions.
        """
        url = f"{self.base_url}/api/songs/{song_id}/suggestions"
        return await self._make_request(url, params={"limit": limit})

    async def get_album(self, album_id: str = None, album_link: str = None):
        """
        Retrieves an album by its ID or link.

        Args:
            album_id (str, optional): The ID of the album.
            album_link (str, optional): The link to the album.

        Returns:
            dict: The album details.
        """
        url = f"{self.base_url}/api/albums"
        params = {}
        if album_id:
            params["id"] = album_id
        if album_link:
            params["link"] = album_link
        return await self._make_request(url, params=params)

    async def get_playlist(
        self,
        playlist_id: str = None,
        playlist_link: str = None,
        page: int = 0,
        limit: int = 10,
    ):
        """
        Retrieves a playlist by its ID or link.

        Args:
            playlist_id (str, optional): The ID of the playlist.
            playlist_link (str, optional): The link to the playlist.
            page (int, optional): The page number to retrieve. Defaults to 0.
            limit (int, optional): The number of results per page. Defaults to 10.

        Returns:
            dict: The playlist details.
        """
        url = f"{self.base_url}/api/playlists"
        params = {"page": page, "limit": limit}
        if playlist_id:
            params["id"] = playlist_id
        if playlist_link:
            params["link"] = playlist_link
        return await self._make_request(url, params=params)

    async def get_artist(
        self,
        artist_id: str,
        page: int = 0,
        song_count: int = 10,
        album_count: int = 10,
        sort_by: str = "popularity",
        sort_order: str = "desc",
    ):
        """
        Retrieves an artist by their ID.

        Args:
            artist_id (str): The ID of the artist.
            page (int, optional): The page number to retrieve. Defaults to 0.
            song_count (int, optional): The number of songs to retrieve. Defaults to 10.
            album_count (int, optional): The number of albums to retrieve. Defaults to 10.
            sort_by (str, optional): The sorting criteria. Defaults to "popularity".
            sort_order (str, optional): The sorting order. Defaults to "desc".

        Returns:
            dict: The artist details.
        """
        url = f"{self.base_url}/api/artists/{artist_id}"
        params = {
            "page": page,
            "songCount": song_count,
            "albumCount": album_count,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }
        return await self._make_request(url, params=params)

    async def get_artist_albums(
        self,
        artist_id: str,
        page: int = 0,
        sort_by: str = "popularity",
        sort_order: str = "desc",
    ):
        """
        Retrieves a list of albums for a given artist by their ID.

        Args:
            artist_id (str): The ID of the artist.
            page (int, optional): The page number to retrieve. Defaults to 0.
            sort_by (str, optional): The sorting criteria. Defaults to "popularity".
            sort_order (str, optional): The sorting order. Defaults to "desc".

        Returns:
            dict: The list of albums for the artist.
        """
        url = f"{self.base_url}/api/artists/{artist_id}/albums"
        params = {"page": page, "sortBy": sort_by, "sortOrder": sort_order}
        return await self._make_request(url, params=params)

    async def get_artist_songs(
        self,
        artist_id: str,
        page: int = 0,
        sort_by: str = "popularity",
        sort_order: str = "desc",
    ):
        """
        Retrieves a list of songs for a given artist by their ID.

        Args:
            artist_id (str): The ID of the artist.
            page (int, optional): The page number to retrieve. Defaults to 0.
            sort_by (str, optional): The sorting criteria. Defaults to "popularity".
            sort_order (str, optional): The sorting order. Defaults to "desc".

        Returns:
            dict: The list of songs for the artist.
        """
        url = f"{self.base_url}/api/artists/{artist_id}/songs"
        params = {"page": page, "sortBy": sort_by, "sortOrder": sort_order}
        return await self._make_request(url, params=params)