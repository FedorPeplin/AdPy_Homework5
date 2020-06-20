import requests
from ast import literal_eval as le

API_KEY = 'trnsl.1.1.20200416T085746Z.896eacde732b4ea4.4be4e3a63a09e1253507d8744142224f3f1687e7'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

params = {
    'key': API_KEY,
    'lang': 'en-ru',
    'reason': 'auto',
    'format': 'text'
    }

def translation_function():
    translation_text=input('Insert english text to translate on russian ')
    data={
        'text': translation_text
    }

    resp = requests.post(
        URL,
        params=params,
        data=data)

    result=resp.text
    result_dict=le(result)
    print (result_dict)
    return result_dict


if __name__ == '__main__':
    translation_function()

