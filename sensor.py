import requests


class Sensor:
    def __init__(self, device_id, api_key):
        self.device_id = device_id
        self.api_key = api_key

    def request(self, data):
        r = requests.post("http://api.heclouds.com/devices/%d/datapoints" % self.device_id,
                          headers={"api-key": self.api_key}, json=data)
        return r.json()

    def report(self, data_type, value):
        data = {"datastreams": [{"id": data_type, "datapoints": [{"value": value}]}]}
        return self.request(data)

    def report_home_temp(self):
        self.report(data_type="home_temp", value=1)

    def report_home_hum(self):
        self.report(data_type="home_hum", value=1)

    def report_cpu_temp(self):
        self.report(data_type="cpu_temp", value=1)

Sensor(device_id=8833946, api_key="wbl4eo1NkQQsoyHldxn=OUdm1eE=").report_home_hum()