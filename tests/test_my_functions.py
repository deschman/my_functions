# -*- coding: utf-8 -*-
"""Test my_functions package."""


# %% Imports
# %%% 3rd Party
import pytest

# %%% User Defined
from my_functions import get_between


# %% Functions
def test_get_between() -> None:
    between_text = get_between(
        "This is some text (between (nested) parenthasis.)")
    assert between_text == "(between (nested) parenthatsis.)"
