import requests
from datetime import datetime


def check_json_response(data: dict, response, expected_name: str, expected_region: str) -> None:
    expected_location_info: list = ['name', 'region', 'country', 'lat', 'lon', 'tz_id', 'localtime_epoch',
                                    'localtime']
    expected_current_info: list = ['last_updated_epoch', 'last_updated', 'temp_c', 'temp_f', 'is_day', 'condition',
                                   'wind_mph', 'wind_kph', 'wind_degree', 'wind_dir', 'pressure_mb', 'pressure_in',
                                   'precip_mm', 'precip_in', 'humidity', 'cloud', 'feelslike_c', 'feelslike_f',
                                   'vis_km', 'vis_miles', 'uv', 'gust_mph', 'gust_kph']
    expected_country = 'Brazil'
    expected_status = 200
    location_keys: list = data['location'].keys()
    current_keys: list = data['current'].keys()
    today: str = datetime.now().strftime('%Y-%m-%d')

    assert response.status_code == expected_status
    assert all(loc_info in expected_location_info for loc_info in location_keys)
    assert all(cur_info in expected_current_info for cur_info in current_keys)
    assert today in data['location']['localtime']
    assert data['location']['name'] == expected_name
    assert data['location']['region'] == expected_region
    assert data['location']['country'] == expected_country


class TestWeatherApi:
    URL: str = "https://weatherapi-com.p.rapidapi.com/current.json"
    HEADERS: dict = {
        "X-RapidAPI-Key": 'e75696bd7cmsh2c6aeb979fa9e25p144730jsnf62c4bde84cd',
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    def test_valid_lat_lon_get_realtime_weather_api(self):
        querystring: dict = {"q": "-8.063200,-34.871113"}

        response = requests.get(url=self.URL, headers=self.HEADERS, params=querystring)

        check_json_response(
            data=response.json(),
            response=response,
            expected_name='Recife',
            expected_region='Pernambuco',
        )

    def test_valid_city_get_realtime_weather_api(self):
        querystring: dict = {"q": "Sao Paulo"}
        response = requests.get(url=self.URL, headers=self.HEADERS, params=querystring)

        check_json_response(
            data=response.json(),
            response=response,
            expected_name='Sao Paulo',
            expected_region='Sao Paulo',
        )

    def test_valid_airport_get_realtime_weather_api(self):
        querystring: dict = {"q": "CWB"}
        response = requests.get(url=self.URL, headers=self.HEADERS, params=querystring)

        check_json_response(
            data=response.json(),
            response=response,
            expected_name='Curitiba Airport',
            expected_region='Curitiba',
        )

    def test_no_valid_parameter_get_realtime_weather_api(self):
        querystring: dict = {"wrong_param": True}
        response = requests.get(url=self.URL, headers=self.HEADERS, params=querystring)
        data: dict = response.json()

        assert response.status_code == 400
        assert data['error']['code'] == 1003
        assert data['error']['message'] == 'Parameter q is missing.'

    def test_no_location_parameter_get_realtime_weather_api(self):
        querystring: dict = {"q": 123456}
        response = requests.get(url=self.URL, headers=self.HEADERS, params=querystring)
        data: dict = response.json()
        assert response.status_code == 400
        assert data['error']['code'] == 1006
        assert data['error']['message'] == 'No matching location found.'

    def test_no_auth_get_realtime_weather_api(self):
        querystring: dict = {"q": 123456}

        headers: dict = {
            "X-RapidAPI-Key": 'invalid_key',
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url=self.URL, headers=headers, params=querystring)
        data: dict = response.json()
        assert response.status_code == 403
        assert data['message'] == 'You are not subscribed to this API.'
