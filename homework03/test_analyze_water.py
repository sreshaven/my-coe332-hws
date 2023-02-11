from analyze_water import calc_turbidity, calc_min_time
import math
import pytest

def test_calc_turbidity():
    assert calc_turbidity(1.022, 1.137) == 1.022 * 1.137
    assert calc_turbidity(1.047, -1.115) == 1.047 * -1.115

def test_calc_min_time():
    assert calc_min_time(0.25) == 0
    assert calc_min_time(1.1992) == 8.99
