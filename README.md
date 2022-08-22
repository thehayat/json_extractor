# Objective

### Write a generic program that:

- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file
- Dumps the output in (./schema/)

#### Few extra conditions to check while implementing

- Padding: All attributes in the JSON schema should be padded with "tag" and "description" keys.
- The schema output must capture ONLY the attributes within the "message" key of the input JSON source data (see line 8
  in the input JSON files). All attributes withn the key "attributes" should be excluded.
- The JSON schema should set all properties "required": false.
- For data types of the JSON schema: STRING: program should identify what is a string and map accordingly in JSON schema
  output INTEGER: program should identify what is an integer and map accordingly in JSON schema output ENUM: When the
  value in an array is a string, the program should map the data type as an ENUM ARRAY: When the value in an array is
  another JSON object, the program should map the data type as an ARRAY

<!-- GETTING STARTED -->

## Getting Started

This is a project to read the json data and extract the schema from it.

### Prerequisites

`python 3.5` and above

## Usage

__Run__

```python
python main.py
```

__Tests__

```python
python test_parseJson.py
```

The default output location is: `./schema`

__Output data format__

```json
{
  "key_one": {
    "type": "string",
    "tag": "",
    "description": "",
    "required": false
  },
  "key_two": {
    "type": "string",
    "tag": "",
    "description": "",
    "required": false
  }
}
```

<!-- LICENSE -->

## License

Distributed under the MIT License.

<!-- CONTACT -->

## Contact

- [StackOverflow](https://stackoverflow.com/users/8868699/hayat)
- [LinkedIn](https://www.linkedin.com/in/sarwarhayat/)
- [Project Link](https://github.com/thehayat/json_extractor)
<p align="right">(<a href="https://github.com/thehayat/json_extractor#objective">back to top</a>)</p>