from os import remove


class FilePath:
    def __init__(self, path: str):
        self.path = path

    def delete(self):
        """
        Deletes the file at the specified path.
        """
        try:
            remove(self.path)
        except Exception:
            pass

    def __str__(self):
        return self.path
