import os
import json
from uuid import uuid4


def generate_config(config_name, **params):
    file_path = "{}_{}.json".format(uuid4().hex, config_name)
    with open(file_path, "w+") as f:
        json.dump(params, f)
    return file_path
