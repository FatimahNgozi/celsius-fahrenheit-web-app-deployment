import unittest

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion"""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)

    def test_edge_cases(self):
        """Test edge cases"""
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, places=2)

if __name__ == '__main__':
    unittest.main()
