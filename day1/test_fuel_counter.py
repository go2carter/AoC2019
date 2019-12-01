import pytest

from fuel_counter_upper import fuel_for_module, compute_total_fuel


class TestFuelCounter:
    def test_fuel_counter_upper(self):
        assert fuel_for_module(12) == 2
        assert fuel_for_module(14) == 2
        assert fuel_for_module(1969) == 654
        assert fuel_for_module(100756) == 33583

        assert fuel_for_module(12, True) == 2
        assert fuel_for_module(14, True) == 2
        assert fuel_for_module(1969, True) == 966
        assert fuel_for_module(100756, True) == 50346

    def test_input(self):
        assert compute_total_fuel('input.txt') == 3271994
        
        assert compute_total_fuel('input.txt', True) == 4905116
