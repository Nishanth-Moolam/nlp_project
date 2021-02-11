import requests
import json

import config

'''
note all text must be a SINGLE PARAGRAPH. the api will return an error otherwise
'''


def expertai_entities_analyze(text):
    headers = config.expertai_headers
    url = config.expertai_entities_url
    data = '{ "document": { "text" : "'+text+'" } }'

    response = requests.post(url, headers=headers, data=data)

    return json.loads(response.text)


def expertai_full_analyze(text):
    headers = config.expertai_headers
    url = config.expertai_full_url
    data = '{ "document": { "text" : "'+text+'" } }'

    response = requests.post(url, headers=headers, data=data)

    return json.loads(response.text)

def expertai_full_config(response_dict):
    pass