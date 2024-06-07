import unittest
from city_functions import city_function


class CityCountry(unittest.TestCase):
    def test_city_country(self):
        city_country = city_function("santiago", "chile")
        self.assertEqual(city_country, "Santiago, Chile")


unittest.main()
