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


