import requests
import json

import config

# to prevent unneccesary calls to the api (I only have a certain amount in the free tier)
# I'm saving the response ad s a json file, and using that as a reference. (found in static)
def ms_ocr_read(picture_url):
    url = config.ms_computer_vision_ocr_url
    querystring = config.ms_computer_vision_ocr_query_string
    headers = config.ms_computer_vision_headers

    payload = str({"url": picture_url})

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    response_dict = json.loads(response.text)

    return response_dict


def ms_ocr_config(response_dict):
    '''
    returns a list of all words.
    '''
    words = []
    for box in response_dict:
        for line in box['lines']:
            for word in line['words']:
                words.append(word['text'])
    
    return words

def ms_ocr_serialize(words):
    words_string = ''
    for i in words:
        words_string += i+' '
    return words_string

def ms_ocr(picture_url):
    '''
    returns a single string of all words read concatenated together
    '''
    response_dict = ms_ocr_read(picture_url)
    words = ms_ocr_config(response_dict)
    words_string = ms_ocr_serialize(words)

    return words_string
