import os
import logging
from parseJson import ParseJson, write_json

INPUT_DIR = "./data"
OUTPUT_DIR = "./schema"

LOG_FILEPATH = "Logs/json_parse.log"
if not os.path.exists(LOG_FILEPATH):
    os.makedirs(os.path.basename(LOG_FILEPATH), exist_ok=True)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(os.path.basename(OUTPUT_DIR), exist_ok=True)
logging.basicConfig(filename=LOG_FILEPATH, level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def main(files):
    for file in files:
        parsingJson = ParseJson(input_dir=INPUT_DIR,
                                output_dir=OUTPUT_DIR)
        filepath = os.path.join(INPUT_DIR, file)
        jsonData = parsingJson.read_json(filepath)

        try:
            input_data = jsonData['message']
        except KeyError:
            raise Exception("Unstructured Json: No 'message' key found.")

        schema = parsingJson.schemify_json(json_data=input_data)

        # saving the results.
        output_path = os.path.join(OUTPUT_DIR, f"{file.split('.')[0]}_schema.json")
        write_json(jsonData=schema, output_path=output_path)
    return True


if __name__ == '__main__':
    files = [file for file in os.listdir(INPUT_DIR) if file.endswith('.json')]
    print("Total files found: ", len(files))
    logging.info(f"Total files found: {len(files)}")

    if main(files):
        logging.info(f"Parsing completed for files:  {', '.join(files)}")
        logging.info("-" * 30)
