import json
import requests
from flask_babel import lazy_gettext as _l
from flask import current_app


def translate(content, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _l('Error: the translation service is not configured.')
    # MS translator v3.0 requires JSON array (not dict) POST
    request_body = [{'Text': content}]
    headers = {'Content-Type': 'application/json'}  # explicit, redundant with requests package default
    print(current_app.config['MS_TRANSLATOR_KEY'])
    auth = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    urlparams = {'api-version': '3.0', 'from': source_language, 'to': dest_language}
    r = requests.post('https://api.cognitive.microsofttranslator.com'
                      '/translate', json=request_body, params=urlparams, headers={**auth, **headers})
    response = json.loads(r.content.decode('utf-8-sig'))
    if r.status_code != 200:
        return response['error']['message']+' Blame Microsoft, sorry!'  # _l('Error: the translation service failed you.')
    return response[0]['translations'][0]['text']
