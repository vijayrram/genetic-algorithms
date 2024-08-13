"""Test suite for the objects in gene.py"""

import pytest

from dna import DNA


def test_dna_class_cannot_be_instantiated_without_arguments() -> None:
    """Test to ensure that the DNA class cannot be instantiated without arguments."""

    with pytest.raises(TypeError):
        _: DNA = DNA()


def test_dna_class_cannot_be_instantiated_with_positional_arguments() -> None:
    """Test to ensure that the DNA class cannot be instantiated with positional arguments."""

    with pytest.raises(TypeError):
        _: DNA = DNA(1)  # type: ignore = Pylance.reportCallIssue


def test_dna_class_can_be_instantiated_with_keyword_arguments() -> None:
    """Test to ensure that the DNA class can be instantiated with keyword arguments."""

    dna: DNA = DNA(value=1)

    assert isinstance(dna, DNA)
    assert dna.kwargs == {"value": 1}
