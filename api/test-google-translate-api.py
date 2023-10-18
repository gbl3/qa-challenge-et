import requests


class TestGoogleTranslateApi:
    URL: str = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    HEADERS: dict = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "e75696bd7cmsh2c6aeb979fa9e25p144730jsnf62c4bde84cd",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    def test_valid_post_translate_api_with_single_query(self):
        payload = {
            "q": "Empathy Talent",
            "target": "es",
            "source": "en",
            "model": "nmt"
        }
        expected_translation = 'Talento Empatía'

        response = requests.post(url=self.URL, data=payload, headers=self.HEADERS)
        data = response.json()['data']
        translations = data['translations']

        assert response.status_code == 200
        assert translations[0]['translatedText'] == expected_translation
        assert translations[0]['model'] == payload['model']

    def test_valid_post_translate_api_with_multiple_query(self):
        payload = {
            "q": ["Now I am become Death, the destroyer of worlds", "Quis custodiet ipsos custodes?"],
            "target": "pt-br",
        }
        expected_translations = [
            {'text': 'Agora eu me tornei a Morte, a destruidora de mundos', 'source': 'en'},
            {'text': 'Quem vigia os observadores?', 'source': 'la'},
        ]

        response = requests.post(url=self.URL, data=payload, headers=self.HEADERS)
        data = response.json()['data']
        translations = data['translations']

        assert response.status_code == 200
        for x in range(0, len(translations)):
            assert expected_translations[x]['text'] == translations[x]['translatedText']
            assert expected_translations[x]['source'] == translations[x]['detectedSourceLanguage']

    def test_invalid_post_translate_api_bad_pair(self):
        payload = {
            "q": ["Arrivederci", 'Blue and Green are great colors'],
            "target": "es",
            "source": "es",
        }
        expected_error = 'Bad language pair: es|es'
        expected_code = 400

        response = requests.post(url=self.URL, data=payload, headers=self.HEADERS)
        error = response.json()['error']

        assert response.status_code == expected_code
        assert error['code'] == expected_code
        assert error['message'] == expected_error

    def test_invalid_post_translate_api_no_query(self):
        payload = {
            "target": "en",
        }
        # To be honest, I think the error message and code should be different here. But, since that's what is being
        # returned, I am verifying anyway.
        expected_error = 'The API is unreachable, please contact the API provider'
        expected_code = 502

        response = requests.post(url=self.URL, data=payload, headers=self.HEADERS)
        data = response.json()

        assert response.status_code == expected_code
        assert data['messages'] == expected_error

    def test_no_api_key_post_translate_api(self):
        payload = {
            "target": "en",
        }
        expected_error = 'Invalid API key. Go to https://docs.rapidapi.com/docs/keys for more info.'
        expected_code = 401

        headers: dict = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.post(url=self.URL, data=payload, headers=headers)
        data = response.json()

        assert response.status_code == expected_code
        assert data['message'] == expected_error

    def test_invalid_api_key_post_translate_api(self):
        payload = {
            "target": "en",
        }
        expected_error = 'You are not subscribed to this API.'
        expected_code = 403

        headers: dict = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "invalid_api_key",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.post(url=self.URL, data=payload, headers=headers)
        data = response.json()

        assert response.status_code == expected_code
        assert data['message'] == expected_error

    def test_invalid_target_post_translate_api(self):
        payload = {
            "q": 'El ratón loco',
            "target": "invalid_target"
        }
        expected_error_message = 'Invalid Value'
        expected_error_description = 'Target language: invalid_target'
        expected_field_violation = 'target'
        expected_code = 400

        response = requests.post(url=self.URL, data=payload, headers=self.HEADERS)
        error = response.json()['error']

        assert response.status_code == expected_code
        assert error['code'] == expected_code
        assert error['message'] == expected_error_message
        assert error['details'][0]['fieldViolations'][0]['field'] == expected_field_violation
        assert error['details'][0]['fieldViolations'][0]['description'] == expected_error_description
