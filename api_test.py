import json
import requests
import api_endpoint

def call_api(endpoint):
    """
    API呼び出し、GET/POSTの区別やURLはapi_endpointに定数として設定
    """
    if endpoint['request'] == 'GET':
        response = requests.get(endpoint['url'], headers={'Authorization':'Bearer '+config['token']})
    elif endpoint['request'] == 'POST':
        response = requests.post(endpoint['url'], headers={'Authorization':'Bearer '+config['token']})
    if response.status_code == 200:
        return response.text
    else:
        raise

def get_sensor_values():
    """
    センサーで測った現在の値を取得
    """
    devices = json.loads(call_api(api_endpoint.GET_DEVICES))

    for device in devices:
        print(device["name"])
        print("温度：" + str(device["newest_events"]["te"]))
        print("湿度：" + str(device["newest_events"]["hu"]))
        print("照度：" + str(device["newest_events"]["il"]))
        print("movement：" + str(device["newest_events"]["mo"]))

with open("./config.json") as config_file:
    config = json.load(config_file)

get_sensor_values()
