from enum import Enum
from json import dumps


class FilePath(str):
    """
    A wrapper around a file path string that provides an additional delete method.

    Attributes:
        path (str): The file path to the media file.

    Methods:
        delete(): Attempts to delete the file at the specified path.
                  If deletion fails, it handles the exception gracefully.
    """

    def delete(self):
        """Deletes the file at the specified path, handling exceptions if deletion fails."""
        try:
            os.remove(self)
        except Exception:
            pass


class Result:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def default(obj: "Result"):
        if isinstance(obj, bytes):
            return repr(obj)

        if isinstance(obj, Enum):
            return str(obj)

        filtered_attributes = {
            attr: ("*" * 9 if attr == "phone_number" else getattr(obj, attr))
            for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
            if getattr(obj, attr) is not None
        }

        return {"_": obj.__class__.__name__, **filtered_attributes}

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Result.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(f'{attr}={repr(getattr(self, attr))}' for attr in filter(lambda x: not x.startswith('_'), self.__dict__) if getattr(self, attr) is not None)})"

    def __eq__(self, other: "Result") -> bool:
        for attr in self.__dict__:
            if attr.startswith("_"):
                continue
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def __getstate__(self):
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        self.__dict__ = state

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __delitem__(self, key):
        if hasattr(self, key):
            delattr(self, key)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def keys(self):
        return [key for key in self.__dict__ if not key.startswith("_")]

    def values(self):
        return [getattr(self, key) for key in self.keys()]

    def items(self):
        return [(key, getattr(self, key)) for key in self.keys()]

    def update(self, **kwargs):
        self.__dict__.update(kwargs)

    def pop(self, key, default=None):
        if key in self.__dict__:
            value = getattr(self, key)
            delattr(self, key)
            return value
        return default
