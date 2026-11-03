'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student: Leigha Lennon
Description: The ThermostatTestCase class
'''

import unittest 
from thermostat import Thermostat

class ThermostatTestCase(unittest.TestCase): 

    # TODO #1
        # pre-condition: a thermostat set to 75F
        # post-condition: a thermostat (actually) set to 75F 
        def test_thermostat_set_to_75(self):
            thermostat = Thermostat(75)
            self.assertEqual(thermostat.set_point, 75)
    
        # TODO #2
        # pre-condition: a thermostat set to (any) temperature below Thermostat.MIN_SET_POINT
        # post-condition: a thermostat (actually) set to Thermostat.MIN_SET_POINT
        def test_thermostat_set_to_below_min_set_point(self):
            thermostat = Thermostat(Thermostat.MIN_SET_POINT - 1)
            self.assertEqual(thermostat.set_point, Thermostat.MIN_SET_POINT)
    
        # TODO #3
        # pre-condition: a thermostat set to (any) temperature above Thermostat.MAX_SET_POINT
        # post-condition: a thermostat (actually) set to Thermostat.MAX_SET_POINT
        def test_thermostat_set_to_above_max_set_point(self):
            thermostat = Thermostat(Thermostat.MAX_SET_POINT + 1)
            self.assertEqual(thermostat.set_point, Thermostat.MAX_SET_POINT)
    
        # TODO #4
        # pre-conditions: 
        #   * CURRENT_TEMPERATURE set to Thermostat.MIN_SET_POINT + 1
        #   * a thermostat set to Thermostat.MIN_SET_POINT 
        #   * a call to check_temperature
        # post-condition: CURRENT_TEMPERATURE equals to thermostat's set point
        def test_thermostat_temperature_decrease_by_one(self):
            thermostat = Thermostat(Thermostat.MIN_SET_POINT)
            Thermostat.current_temperature = Thermostat.MIN_SET_POINT + 1
            thermostat.check_temperature()
            self.assertEqual(Thermostat.current_temperature, thermostat.set_point)
            thermostat.check_temperature()  # Already at set point: no change.
            self.assertEqual(Thermostat.current_temperature, thermostat.set_point)
    
        # TODO #5
        # pre-conditions: 
        #   * CURRENT_TEMPERATURE set to Thermostat.MAX_SET_POINT - 1
        #   * a thermostat set to Thermostat.MAX_SET_POINT 
        #   * a call to check_temperature
        # post-condition: CURRENT_TEMPERATURE equals to thermostat's set point
        def test_thermostat_temperature_increase_by_one(self):
            thermostat = Thermostat(Thermostat.MAX_SET_POINT)
            Thermostat.current_temperature = Thermostat.MAX_SET_POINT - 1
            thermostat.check_temperature()
            self.assertEqual(Thermostat.current_temperature, thermostat.set_point)
    
        # TODO #6 (+1 bonus)
        # pre-condition: a thermostat set to some (valid) set point value (like 75F) followed by a call to str
        # post-condition: the output from str should be 'Set Point: 75F'
        def test_thermostat_set_to_75_to_check_str(self):
            thermostat = Thermostat(75)
            self.assertEqual(str(thermostat), "Set Point: 75F")
    
if __name__ == '__main__':  # pragma: no cover
    unittest.main()
    