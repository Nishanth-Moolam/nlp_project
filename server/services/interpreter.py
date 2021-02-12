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
    '''
    refer to expertai_full_data.json for test output (in static)
    '''
    headers = config.expertai_headers
    url = config.expertai_full_url
    data = '{ "document": { "text" : "'+text+'" } }'

    response = requests.post(url, headers=headers, data=data)

    return json.loads(response.text)

def expertai_full_config(response_dict):

    entities = []
    lemmas = []
    phrases = []
    topics = []

    for entity in response_dict['data']['entities']:
        entities.append(entity['lemma'])

    for lemma in response_dict['data']['mainLemmas']:
        lemmas.append(lemma['value'])

    for phrase in response_dict['data']['mainPhrases']:
        phrases.append(phrase['value'])

    for topic in response_dict['data']['topics']:
        topics.append(topic['label'])

    return {
            'entities' : entities, 
            'lemmas': lemmas, 
            'phrases': phrases, 
            'topics': topics
            }

def expertai_full(text):
    response_dict = expertai_full_analyze(text)
    output_dict = expertai_full_config(response_dict)

    return output_dict