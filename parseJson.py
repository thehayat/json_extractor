import json
import logging
import traceback


def write_json(jsonData: dict, output_path: str) -> None:
    try:
        with open(output_path, 'w') as fp:
            fp.write(json.dumps(jsonData))
        print("File successfully saved to: ", output_path)
    except Exception as e:
        logging.exception(f"{traceback.format_exc()}")
        raise Exception(str(e))


class ParseJson:
    """
    Class to parse the json and extract the schema.
    required params:
        input_dir: input files directory : str
        output_dir: output files directory : str

    """

    def __init__(self, input_dir, output_dir, *args, **kwargs):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.schema = {}

    @staticmethod
    def read_json(filepath):
        """
        The function reads and returns the json.
        :param filepath: full filepath (str)
        :return: json data (dict)
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as fp:
                json_data = json.loads(fp.read())
        except Exception as e:
            logging.exception(f"{traceback.format_exc()}")
            raise Exception(str(e))
        return json_data

    def schemify_json(self, json_data: dict):
        """
        The function parse the json to find the schema available under a specified json key.
        :param json_data: json data (dict)
        :return: parsed scehema json (dict)
        """
        try:
            dtype = ""
            for key, value in json_data.items():
                if isinstance(value, str):
                    dtype = "STRING"
                elif isinstance(value, int):
                    dtype = "INTEGER"
                elif isinstance(value, bool):
                    dtype = "BOOLEAN"
                elif isinstance(value, dict):
                    dtype = "ARRAY"
                    self.schemify_json(value)
                elif isinstance(value, list):
                    dtype = "ENUM ARRAY"
                    for val in value:
                        if isinstance(val, dict):
                            dtype = "ARRAY"
                            self.schemify_json(val)

                self.schema[key] = {"type": dtype,
                                    "tag": "",
                                    "description": "",
                                    "required": False
                                    }

            return self.schema
        except Exception as e:
            logging.exception(f"{traceback.format_exc()}")
            raise Exception(str(e))
