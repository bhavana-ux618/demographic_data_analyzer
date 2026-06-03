import unittest
from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTestCase(unittest.TestCase):

    def test_race_count(self):
        actual = calculate_demographic_data()
        self.assertEqual(actual['race_count']['White'], 27816)
