import unittest
from city_functions import city_function


class CityCountry(unittest.TestCase):
    def test_city_country(self):
        city_country = city_function("santiago", "chile")
        self.assertEqual(city_country, "Santiago, Chile")

    def test_city_country_population(self):
        city_country_pop = city_function("santiago", "chile", 500000)
        self.assertEqual(city_country_pop, "Santiago, Chile - population 500000")


unittest.main()
