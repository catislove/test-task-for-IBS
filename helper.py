import json
import os
from requests import sessions



def read_json_schema(name: str):
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', name)
    return schema_path


def response_schema(file_path):
    with open(file_path, encoding='utf8') as file:
        schema = json.loads(file.read())
    return schema


def api_request(service, method, url, **kwargs):
    base_url = {"regres": "https://reqres.in"}
    new_url = base_url[service] + url
    with sessions.Session() as session:
        response = session.request(method=method, url=new_url, **kwargs)
    return response
