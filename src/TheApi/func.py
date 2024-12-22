from os import remove
from os.path import exists


class FilePath:
    def __init__(self, path: str):
        self.path = path
        if not exists(self.path):
            raise FileNotFoundError(f"File does not exist: {self.path}")

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
