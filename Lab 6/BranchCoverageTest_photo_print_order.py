
import pytest

from photo_print_order import (
    extra_print_charge,
    order_valid,
    dispatch_status,
)


@pytest.mark.parametrize(
    "size,copies,finish,member,expected",
    [
        ("4x6", 20, "matte", False, 0),
        ("4x6", 21, "matte", False, 4),
        ("4x6", 21, "glossy", False, 7),
        ("4x6", 70, "glossy", False, 350),
        ("4x6", 71, "glossy", False, 459),
        ("4x6", 71, "canvas", False, 714),
        ("4x6", 25, "matte", True, 0),
        ("4x6", 26, "matte", True, 4),
        ("8x10", 10, "matte", True, 0),
        ("8x10", 11, "glossy", True, 7),
        ("5x7", 15, "matte", False, 0),
    ],
)
def test_extra_print_charge_branches(
    size, copies, finish, member, expected
):
    assert extra_print_charge(size, copies, finish, member) == expected


@pytest.mark.parametrize(
    "size,copies,finish,member,error",
    [
        ("A4", 10, "matte", False, "unknown print size"),
        ("4x6", -1, "matte", False, "invalid copies"),
    ],
)
def test_extra_print_charge_errors(
    size, copies, finish, member, error
):
    with pytest.raises(ValueError, match=error):
        extra_print_charge(size, copies, finish, member)


@pytest.mark.parametrize(
    "file_mb,copies,is_rush,expected",
    [
        (100, 50, True, True),
        (100, 51, True, False),
        (26, 100, False, False),
        (25, 500, False, True),
        (25, 501, False, False),
        (10, 100, False, True),
    ],
)
def test_order_valid_branches(file_mb, copies, is_rush, expected):
    assert order_valid(file_mb, copies, is_rush) is expected


@pytest.mark.parametrize(
    "hours,framed,international,expected",
    [
        (12, False, False, "on_time"),
        (6, False, False, "tight"),
        (5, False, False, "missed"),
        (24, True, False, "on_time"),
        (18, True, False, "tight"),
        (17, True, False, "missed"),
        (36, False, True, "on_time"),
        (30, False, True, "tight"),
        (29, False, True, "missed"),
        (48, True, True, "on_time"),
        (42, True, True, "tight"),
        (41, True, True, "missed"),
    ],
)
def test_dispatch_status_branches(
    hours, framed, international, expected
):
    assert dispatch_status(
        hours, framed, international
    ) == expected

