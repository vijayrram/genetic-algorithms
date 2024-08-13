"""Script with the definition of the DNA class."""

from typing import Any


class DNA:
    """Class used to define the properties of the DNA."""

    def __init__(self, **kwargs: Any) -> None:
        if not kwargs:
            raise TypeError(f"{self.__class__} requires at least one keyword argument.")

        self.kwargs: dict[str, Any] = kwargs
