import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    return data
f=open('randomuser_data.json').read()
data=json.loads(f)
print(get_data(data))