"""Script with the definition of the DNA class."""

from typing import Any


class DNA:
    """Class used to define the properties of the DNA."""

    def __init__(self, **kwargs: Any) -> None:
        if not kwargs:
            raise TypeError(f"{self.__class__} requires at least one keyword argument.")

        self.kwargs: dict[str, Any] = kwargs

    def __getitem__(self, key: str) -> Any:
        """Method to get the value for the passed key.

        Args:
            key (str): Key whose value should be retrieved.

        Returns:
            Any: Retrieved value.
        """

        return self.kwargs[key]
