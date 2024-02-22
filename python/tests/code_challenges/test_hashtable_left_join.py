import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["wrath", "anger", "delight"],
        ["outfit", "garb", "NONE"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_left_join():
    cinnamons = {"happy": "joyful", "sad": "sorrowful"}
    auntieannes = {"happy": "sad", "angry": "calm"}
    expected = [["happy", "joyful", "sad"], ["sad", "sorrowful", None]]
    assert left_join(cinnamons, auntieannes) == expected

# @pytest.mark.skip("TODO")
def test_key_in_both():
    cinnamons = {"fast": "quick", "slow": "sluggish"}
    auntieannes = {"fast": "slow", "bright": "dim"}
    expected = [["fast", "quick", "slow"], ["slow", "sluggish", None]]
    assert left_join(cinnamons, auntieannes) == expected

# @pytest.mark.skip("TODO")
def test_key_in_first():
    cinnamons = {"light": "bright", "dark": "dim"}
    auntieannes = {"heavy": "light", "shallow": "deep"}
    expected = [["light", "bright", None], ["dark", "dim", None]]
    assert left_join(cinnamons, auntieannes) == expected
