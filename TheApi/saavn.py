from ._request import Request


class SaavnAPI:
    """
    A class for interacting with the Saavn API.

    This class provides methods for searching songs, albums, artists, and playlists
    globally on the Saavn platform.
    """

    def __init__(self):
        """
        Initializes the SaavnAPI instance with the base URL for the Saavn API.
        """
        self.base_url = "https://saavn.dev"
        self.req = Request()

    async def search(self, query: str):
        """
        Searches globally for songs, albums, artists, and playlists.

        Args:
            query (str): The search query. This can be a song name, album name,
                         artist name, or playlist name.

        Returns:
            dict: The search results containing information about the songs,
                  albums, artists, and playlists matching the query.

        Example:
            .. code-block:: python

               from TheApi import SaavnAPI

               api = SaavnAPI()

               response = await api.search("Jannat Ve")

               print(response)
        """
        url = f"{self.base_url}/api/search"
        r = await self.req.get(url, params={"query": query})
        return r.json()

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
        r = await self.req.get(
            url, params={"query": query, "page": page, "limit": limit}
        )
        return r.json()

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
        r = await self.req.get(
            url, params={"query": query, "page": page, "limit": limit}
        )
        return r.json()

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
        r = await self.req.get(
            url, params={"query": query, "page": page, "limit": limit}
        )
        return r.json()

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
        r = await self.req.get(
            url, params={"query": query, "page": page, "limit": limit}
        )
        return r.json()

    async def get_song_by_id(self, song_id: str):
        """
        Retrieves a song by its ID.

        Args:
            song_id (str): The ID of the song.

        Returns:
            dict: The song details.
        """
        url = f"{self.base_url}/api/songs/{song_id}"
        r = await self.req.get(url)
        return r.json()

    async def get_song_lyrics(self, song_id: str):
        """
        Retrieves lyrics for a song by its ID.

        Args:
            song_id (str): The ID of the song.

        Returns:
            dict: The song lyrics.
        """
        url = f"{self.base_url}/api/songs/{song_id}/lyrics"
        r = await self.req.get(url)
        return r.json()

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
        r = await self.req.get(url, params={"limit": limit})
        return r.json()

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
        r = await self.req.get(url, params=params)
        return r.json()

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
        r = await self.req.get(url, params=params)
        return r.json()

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
        r = await self.req.get(url, params=params)
        return r.json()

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
        r = await self.req.get(url, params=params)
        return r.json()

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
        r = await self.req.get(url, params=params)
        return r.json()
