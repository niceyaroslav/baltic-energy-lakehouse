import datetime
import openmeteo_requests
import requests_cache
from retry_requests import retry


class OpenMeteo:

    def __init__(self, timeout=3600):
        self.session = requests_cache.CachedSession('.cache', expire_after=timeout)
        self.retry_session = retry(self.session, retries=5, backoff_factor=0.2)
        self.client = openmeteo_requests.Client(session=self.retry_session)
        self.base_url = 'https://api.open-meteo.com/v1/forecast'
        self.country_coordinates = {
            'ee': (59.43696, 24.75353),
            'lv': (56.946, 25.2798),
            'lt': (54.68916, 25.279652),
            'fi': (60.16952, 24.93545)
        }

    @staticmethod
    def prepare_dates_for_past_day_request() -> tuple:
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=1)

        start_date = datetime.datetime.strftime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strftime(end, '%Y-%m-%d')

        return start_date, end_date

    @staticmethod
    def convert_open_meteo_object_to_raw_dict(response, variables) -> dict:
        hourly = response.Hourly()

        start = hourly.Time()
        step = hourly.Interval()

        value_count = hourly.Variables(0).ValuesLength()
        timestamps = [start + j * step for j in range(value_count)]

        flattened_hourly_data = {
            ts: {
                    variable: hourly.Variables(i).Values(j) for i,variable in enumerate(variables)
            } for j,ts in enumerate(timestamps)
        }
        return flattened_hourly_data



    def fetch_hourly_temperature(
            self,
            start_date: str = None,
            end_date: str = None,
            future_forecast: bool = False
    ) -> dict:
        params = {
            'latitude': [v[0] for k, v in self.country_coordinates.items()],
            'longitude': [v[1] for k, v in self.country_coordinates.items()],
            'hourly': 'temperature_2m',
            'timezone': 'UTC',
        }

        if not future_forecast and not (start_date and end_date):
            start_date, end_date = self.prepare_dates_for_past_day_request()
            params.update({
                'start_date': start_date,
                'end_date': end_date
            })

        responses = self.client.weather_api(self.base_url, params = params)

        variables = params['hourly']
        if isinstance(params['hourly'], str):
            variables = [params['hourly']]

        flattened_responses = [
            self.convert_open_meteo_object_to_raw_dict(response, variables) for response in responses
        ]
        data = dict(zip(self.country_coordinates.keys(), flattened_responses))

        return {
            "metadata": {
                "source": "open-meteo",
                "request_params": params,
            },
            "payload": data
        }
