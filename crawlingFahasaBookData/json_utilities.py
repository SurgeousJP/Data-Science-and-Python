import json
import os


def get_dict_data_from_attributes(attributes):
    data = {}
    for key, value in attributes:
        if value == "":
            return {}
        data[key] = value
    return data


def append_one_to_json_collection(new_data, filename, collection_name):
    try:
        if os.path.exists(filename):
            # If the file exists, read the existing JSON content
            with open(filename, 'r', encoding="utf-8") as file:
                data = json.load(file)
        else:
            # If the file doesn't exist, initialize an empty data dictionary
            data = {collection_name: []}

        data[collection_name].append(new_data)

        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

        print("JSON documents appended successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


def append_many_to_json_collection(new_data_list, filename, collection_name):
    try:
        if os.path.exists(filename):
            # If the file exists, read the existing JSON content
            with open(filename, 'r', encoding="utf-8") as file:
                data = json.load(file)
        else:
            # If the file doesn't exist, initialize an empty data dictionary
            data = {collection_name: []}

        for new_data in new_data_list:
            data[collection_name].append(new_data)

        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

        print("JSON documents appended successfully.")
    except Exception as e:
        print("An error occurred:", str(e))
