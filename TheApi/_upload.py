from io import BytesIO
from typing import Union

import aiofiles


class UploadMedia:

    async def _get_bytes(self, file_input):
        data, err = None, None
        try:
            if isinstance(file_input, bytes):
                data = file_input
            elif isinstance(file_input, BytesIO):
                data = file_input.getvalue()
            else:
                async with aiofiles.open(file_input, "rb") as f:
                    data = await f.read()
        except Exception as err:
            return err, data
        if not data:
            err = "Invalid input type"
        return err, data

    async def upload_image(self, file_path: Union[str, bytes, BytesIO]) -> dict:
        return await self.upload_to_envsh(file_path)

    async def upload_to_envsh(self, file_path: Union[str, bytes, BytesIO]) -> dict:
        """Uploads an image to `Envs.sh <https://envs.sh>`_.

        Args:
            file_path (Union[str, bytes, BytesIO]): The media file to upload. Can be one of:

                - str: Local file path (e.g., "image.png").
                - bytes: Raw binary data of the file.
                - BytesIO: File-like object containing binary data.

        Returns:
            dict: A dictionary containing the upload result:
                - On success: {"success": true, "url": "<file_url>", "retention": "<days> days"}
                - On failure: {"success": false, "error": "<error_message>"}
                Retention period is calculated based on file size, ranging from 30 to 90 days.

        Examples:

            .. code-block:: python
               :caption: Upload an image from a file path

                x = await api.upload_image("image.png")
                print(x)
                if x["success"]:
                    print(f"Your uploaded file link is {x["url"]} and this will be deleted in {x["retention"]}")


            .. code-block:: json

                {
                    "success": true,
                    "url": "https://envs.sh/abc.png",
                    "retention": "85 days"
                }

            .. code-block:: text

                Your uploaded file link is https://envs.sh/abc.png and this will be deleted in 85 days.


            .. code-block:: python
               :caption: Upload an image from binary data

                with open("image.png", "rb") as f:
                    x = await api.upload_image(f.read())
                print(x)
                # Output: {"success": true, "url": "https://envs.sh/def.png", "retention": "78 days"}

            .. code-block:: python
               :caption: Upload an image from BytesIO

                from io import BytesIO
                x = await api.upload_image(BytesIO(b"image binary data"))
                print(x)
                # Output: {"success": true, "url": "https://envs.sh/ghi.png", "retention": "82 days"}

            .. code-block:: python
               :caption: Invalid input example

                x = await api.upload_image(12345)
                print(x)
                # Output: {"success": false, "error": "Invalid input type"}

            .. code-block:: python
               :caption: File not found error

                x = await api.upload_image("non_existent_file.png")
                print(x)
                # Output: {"success": false, "error": "File not found: 'non_existent_file.png'"}
        """
        err, image_bytes = await self._get_bytes(file_path)
        if err:
            return {"success": False, "error": err}

        file_size = len(image_bytes)
        max_size, min_age, max_age = 512 * 1024 * 1024, 30, 90
        retention = min_age + (-max_age + min_age) * pow((file_size / max_size - 1), 3)
        retention = max(min_age, min(max_age, retention))

        url = "https://envs.sh"
        files = {"file": image_bytes}

        try:
            response = await self.request.post(url=url, files=files)
            return {
                "success": True,
                "url": response.text.strip(),
                "retention": f"{round(retention)} days",
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def upload_to_catbox(self, file_path: Union[str, bytes, BytesIO]):
        """
        Uploads a file to `Catbox.moe <https://catbox.moe>`_ and Get the uploaded file URL.

        Args:
            file_path (Union[str, bytes, BytesIO]): The media file to upload. Can be one of:

                - str: Local file path (e.g., "image.png").
                - bytes: Raw binary data of the file.
                - BytesIO: File-like object containing binary data.

        Returns:
            dict: A dictionary containing:
                - "success" (bool): True if the upload was successful, False otherwise.
                - "url" (str, optional): The URL of the uploaded file if successful.
                - "error" (Exception, optional): The error message if the upload fails.

        Example:

            .. code-block:: python
               :caption: Successful upload

                >>> result = await api.upload_to_catbox("example.jpg")
                >>> print(result)
                # {'success': True, 'url': 'https://files.catbox.moe/abcd1234.jpg'}

            .. code-block:: python
               :caption: Failed upload (e.g., file not found)

                >>> result = await api.upload_to_catbox("invalid.jpg")
                >>> print(result)
                # {'success': False, 'error': FileNotFoundError("File not found")}
        """
        err, raw = await self._get_bytes(file_path)
        if err:
            return {"success": False, "error": err}

        files = {"fileToUpload": raw}
        data = {"reqtype": "fileupload", "userhash": ""}
        try:
            response = await self.request.post(
                "https://catbox.moe/user/api.php", data=data, files=files
            )
        except Exception as e:
            return {"success": False, "error": e}

        return {"success": True, "url": response.text}

    async def upload_to_pomf(self, file_path: Union[str, bytes, BytesIO]):
        """
        Uploads a file to `Catbox.moe <https://catbox.moe>`_ and Get the uploaded file URL.

        Args:
            file_path (Union[str, bytes, BytesIO]): The media file to upload. Can be one of:

                - str: Local file path (e.g., "image.png").
                - bytes: Raw binary data of the file.
                - BytesIO: File-like object containing binary data.

        Returns:
            dict: A dictionary containing:
                - "success" (bool): True if the upload was successful, False otherwise.
                - "url" (str, optional): The URL of the uploaded file if successful.
                - "error" (Exception, optional): The error message if the upload fails.

        Example:

            .. code-block:: python
               :caption: Successful upload

                >>> result = await api.upload_to_pomf("example.jpg")
                >>> print(result)
                # {'success': True, 'url': 'https://pomf2.lain.la/f/abcd.jpg'}

            .. code-block:: python
               :caption: Failed upload (e.g., file not found)

                >>> result = await api.upload_to_pomf("invalid.jpg")
                >>> print(result)
                # {'success': False, 'error': FileNotFoundError("File not found")}
        """

        err, raw = await self._get_bytes(file_path)
        if err:
            return {"success": False, "error": err}

        files = {"files[]": raw}
        try:
            response = await self.request.post(
                "https://pomf.lain.la/upload.php", files=files
            )
        except Exception as e:
            return {"success": False, "error": e}

        return {"success": True, "url": response.json()["files"][0]["url"]}

    async def upload_to_0x0(
        self,
        file_path: Union[str, bytes, BytesIO],
        secret: bool = False,
        expires: int = None,
    ) -> dict:
        """
        Uploads a file to 0x0.st and returns the uploaded file URL along with retention details.

        Args:
            file_path (Union[str, bytes, BytesIO]): The media file to uploaded.
            secret (bool, optional): If True, generates a longer, hard-to-guess URL (default: False).
            expires (int, optional): Sets the maximum file lifetime in hours or the expiration time in
                                     milliseconds since the UNIX epoch (default: None).

        Returns:
            dict: A dictionary containing:
                - "success" (bool): True if the upload was successful, False otherwise.
                - "url" (str, optional): The URL of the uploaded file if successful.
                - "retention" (str, optional): The estimated retention period of the file.
                - "error" (str, optional): The error message if the upload fails.

        Example:
            Successful upload:
                >>> result = await api.upload_to_0x0("example.jpg")
                >>> print(result)
                {'success': True, 'url': 'https://0x0.st/abcd', 'retention': '30 days'}

            Successful upload with expiration:
                >>> result = await api.upload_to_0x0("example.jpg", expires=48)
                >>> print(result)
                {'success': True, 'url': 'https://0x0.st/abcd', 'retention': '48 hours'}

            Failed upload (e.g., file not found):
                >>> result = await api.upload_to_0x0("invalid.jpg")
                >>> print(result)
                {'success': False, 'error': 'File not found'}
        """
        url = "https://0x0.st"
        files = {"file": file_bytes}
        data = {}

        if secret:
            data["secret"] = ""
        if expires is not None:
            data["expires"] = str(expires)
        err, file_bytes = await self._get_bytes(file_path)
        if err:
            return {"success": False, "error": err}

        file_size_mb = len(file_bytes) / (1024 * 1024)
        min_age, max_age, max_size = 30, 365, 512.0

        if expires is not None:
            retention_days = (
                f"{expires} hours"
                if expires <= 8760
                else f"{round(expires / 24, 2)} days"
            )
        else:
            if file_size_mb >= max_size:
                retention_days = f"{min_age} days"
            else:
                retention = min_age + (min_age - max_age) * (
                    (file_size_mb / max_size - 1) ** 3
                )
                retention_days = f"{max(min_age, round(retention, 2))} days"

        try:
            response = self.request.post(url, files=files, data=data)
            response.raise_for_status()
            return {
                "success": True,
                "url": response.text.strip(),
                "retention": retention_days,
            }

        except Exception as e:
            return {"success": False, "error": str(e)}
