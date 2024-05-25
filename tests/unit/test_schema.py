import unittest
import api.schema as schema

class SchemaTest(unittest.TestCase):

	def test_validate_input_json_with_missing_input(self):
		input_json = {"test":"Test"}
		status, response = schema.validate_input_json(input_json)
		expected_result = {
			"lat": "Missing data for required field.",
			"lon": "Missing data for required field."
		}
		self.assertEqual(set(response.keys()), set(expected_result.keys()))


	def test_validate_input_json_with_all_input(self):
		input_json = {"lat": 26.529796, "lon": 84.910852}
		status, response = schema.validate_input_json(input_json)
		expected_result = {"lat": 26.529796, "lon": 84.910852}
		self.assertEqual(set(response.keys()), set(expected_result.keys()))
