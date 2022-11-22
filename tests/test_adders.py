from adders_test import adders


def test_add_one():
    assert adders.add_one(2) == 3


def test_add_two():
    assert adders.add_two(2) == 4
