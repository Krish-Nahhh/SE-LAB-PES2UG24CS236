
import pytest

from photo_print_order import (
    extra_print_charge,
    order_valid,
    dispatch_status,
)


def test_included_prints():
    assert extra_print_charge("4x6", 15, "matte", False) == 0


def test_unknown_size():
    with pytest.raises(ValueError, match="unknown print size"):
        extra_print_charge("A4", 10, "matte", False)


def test_negative_copies():
    with pytest.raises(ValueError, match="invalid copies"):
        extra_print_charge("4x6", -1, "matte", False)


def test_member_included_prints():
    assert extra_print_charge("4x6", 25, "matte", True) == 0


def test_member_8x10():
    assert extra_print_charge("8x10", 10, "matte", True) == 0


def test_matte_charge():
    assert extra_print_charge("4x6", 21, "matte", False) == 4


def test_glossy_charge():
    assert extra_print_charge("4x6", 21, "glossy", False) == 7


def test_bulk_glossy_charge():
    assert extra_print_charge("4x6", 71, "glossy", False) == 459


def test_bulk_canvas_charge():
    assert extra_print_charge("4x6", 71, "canvas", False) == 714


def test_rush_valid():
    assert order_valid(100, 50, True) is True


def test_rush_invalid():
    assert order_valid(10, 51, True) is False


def test_file_too_large():
    assert order_valid(26, 100, False) is False


def test_regular_order_valid():
    assert order_valid(25, 500, False) is True


def test_too_many_regular_copies():
    assert order_valid(10, 501, False) is False


def test_dispatch_on_time():
    assert dispatch_status(12, False, False) == "on_time"


def test_dispatch_tight():
    assert dispatch_status(6, False, False) == "tight"


def test_dispatch_missed():
    assert dispatch_status(5, False, False) == "missed"


def test_framed_international_on_time():
    assert dispatch_status(48, True, True) == "on_time"


def test_international_tight():
    assert dispatch_status(30, False, True) == "tight"


def test_framed_missed():
    assert dispatch_status(17, True, False) == "missed"
