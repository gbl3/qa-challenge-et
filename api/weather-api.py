import requests
from datetime import datetime


def test_valid_lat_lon_get_realtime_weather_api():
    url: str = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring: dict = {"q": "-8.063200,-34.871113"}

    headers: dict = {
        "X-RapidAPI-Key": 'e75696bd7cmsh2c6aeb979fa9e25p144730jsnf62c4bde84cd',
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data: dict = response.json()
    today: str = datetime.now().strftime('%Y-%m-%d')

    expected_location_info: list = ['name', 'region', 'country', 'lat', 'lon', 'tz_id', 'localtime_epoch', 'localtime']
    expected_current_info: list = ['last_updated_epoch', 'last_updated', 'temp_c', 'temp_f', 'is_day', 'condition',
                                   'wind_mph', 'wind_kph', 'wind_degree', 'wind_dir', 'pressure_mb', 'pressure_in',
                                   'precip_mm', 'precip_in', 'humidity', 'cloud', 'feelslike_c', 'feelslike_f',
                                   'vis_km', 'vis_miles', 'uv', 'gust_mph', 'gust_kph']

    assert response.status_code == 200
    assert all(loc_info in expected_location_info for loc_info in data['location'].keys())
    assert all(cur_info in expected_current_info for cur_info in data['current'].keys())
    assert data['location']['name'] == 'Recife'
    assert data['location']['region'] == 'Pernambuco'
    assert data['location']['country'] == 'Brazil'
    assert today in data['location']['localtime']


def test_valid_city_get_realtime_weather_api():
    url: str = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring: dict = {"q": "Sao Paulo"}

    headers: dict = {
        "X-RapidAPI-Key": 'e75696bd7cmsh2c6aeb979fa9e25p144730jsnf62c4bde84cd',
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data: dict = response.json()
    today: str = datetime.now().strftime('%Y-%m-%d')

    expected_location_info: list = ['name', 'region', 'country', 'lat', 'lon', 'tz_id', 'localtime_epoch', 'localtime']
    expected_current_info: list = ['last_updated_epoch', 'last_updated', 'temp_c', 'temp_f', 'is_day', 'condition',
                                   'wind_mph', 'wind_kph', 'wind_degree', 'wind_dir', 'pressure_mb', 'pressure_in',
                                   'precip_mm', 'precip_in', 'humidity', 'cloud', 'feelslike_c', 'feelslike_f',
                                   'vis_km', 'vis_miles', 'uv', 'gust_mph', 'gust_kph']

    assert response.status_code == 200
    assert all(loc_info in expected_location_info for loc_info in data['location'].keys())
    assert all(cur_info in expected_current_info for cur_info in data['current'].keys())
    assert data['location']['name'] == 'Sao Paulo'
    assert data['location']['region'] == 'Sao Paulo'
    assert data['location']['country'] == 'Brazil'
    assert today in data['location']['localtime']


def test_valid_airport_get_realtime_weather_api():
    url: str = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring: dict = {"q": "CWB"}

    headers: dict = {
        "X-RapidAPI-Key": 'e75696bd7cmsh2c6aeb979fa9e25p144730jsnf62c4bde84cd',
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data: dict = response.json()
    today: str = datetime.now().strftime('%Y-%m-%d')

    expected_location_info: list = ['name', 'region', 'country', 'lat', 'lon', 'tz_id', 'localtime_epoch', 'localtime']
    expected_current_info: list = ['last_updated_epoch', 'last_updated', 'temp_c', 'temp_f', 'is_day', 'condition',
                                   'wind_mph', 'wind_kph', 'wind_degree', 'wind_dir', 'pressure_mb', 'pressure_in',
                                   'precip_mm', 'precip_in', 'humidity', 'cloud', 'feelslike_c', 'feelslike_f',
                                   'vis_km', 'vis_miles', 'uv', 'gust_mph', 'gust_kph']

    assert response.status_code == 200
    assert all(loc_info in expected_location_info for loc_info in data['location'].keys())
    assert all(cur_info in expected_current_info for cur_info in data['current'].keys())
    assert data['location']['name'] == 'Curitiba Airport'
    assert data['location']['region'] == 'Curitiba'
    assert data['location']['country'] == 'Brazil'
    assert today in data['location']['localtime']


def test_no_valid_parameter_get_realtime_weather_api():
    url: str = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring: dict = {"wrong_param": True}

    headers: dict = {
        "X-RapidAPI-Key": 'e75696bd7cmsh2c6aeb979fa9e25p144730jsnf62c4bde84cd',
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data: dict = response.json()

    assert response.status_code == 400
    assert data['error']['code'] == 1003
    assert data['error']['message'] == 'Parameter q is missing.'


def test_no_location_parameter_get_realtime_weather_api():
    url: str = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring: dict = {"q": 123456}

    headers: dict = {
        "X-RapidAPI-Key": 'e75696bd7cmsh2c6aeb979fa9e25p144730jsnf62c4bde84cd',
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data: dict = response.json()
    assert response.status_code == 400
    assert data['error']['code'] == 1006
    assert data['error']['message'] == 'No matching location found.'


def test_no_auth_get_realtime_weather_api():
    url: str = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring: dict = {"q": 123456}

    headers: dict = {
        "X-RapidAPI-Key": 'invalid_key',
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data: dict = response.json()
    assert response.status_code == 403
    assert data['message'] == 'You are not subscribed to this API.'
