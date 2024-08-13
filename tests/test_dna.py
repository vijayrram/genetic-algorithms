"""Test suite for the objects in gene.py"""

import pytest

from dna import DNA


def test_dna_class_cannot_be_instantiated_without_arguments() -> None:
    """Test to ensure that the DNA class cannot be instantiated without arguments."""

    with pytest.raises(TypeError):
        _: DNA = DNA()
