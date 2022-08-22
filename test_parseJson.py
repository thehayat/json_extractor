import unittest
from main import *


class TestParseJson(unittest.TestCase):

    def setUp(self) -> None:
        file = "data_1.json"
        self.parsingJson = ParseJson(INPUT_DIR, OUTPUT_DIR)
        self.filepath = os.path.join(INPUT_DIR, file)
        jsonData = self.parsingJson.read_json(self.filepath)
        self.input_data = jsonData['message']
        self.schema = self.parsingJson.schemify_json(json_data=self.input_data)

    def test_key(self):
        files = os.listdir(INPUT_DIR)
        for file in files:
            json_data = self.parsingJson.read_json(os.path.join(INPUT_DIR, file))
            self.assertTrue("message" in json_data)

    def test_attributes(self):
        for key, value in self.schema.items():
            self.assertTrue(('tag' in value and 'description' in value))

    def test_required_attribute(self):
        for key, value in self.schema.items():
            self.assertEqual(value['required'], False, "Wrong default value")

    def test_datatype(self):
        for key, value in self.schema.items():
            self.assertIn(value['type'], ['STRING', 'INTEGER', 'ENUM ARRAY', 'ARRAY'])


if __name__ == '__main__':
    unittest.main()
