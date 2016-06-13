from nose.tools import assert_raises

from totoro.totoro import jump_in_rain


def test_jump_height_is_positive():
    assert_raises(ValueError, lambda: jump_in_rain(-1))


def test_jump_returns_positive_number():
    assert jump_in_rain(1) >= 0
