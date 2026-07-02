import datetime
import requests


class NordPoolPrices:

    def __init__(self, timeout=30):
        self.timeout = timeout
        self.base_url = 'https://nordapi.ee'

    def fetch_hourly_prices(
            self,
            start_date: str = None,
            end_date: str = None
    ) -> dict:
        url_extension = '/api/v1/elering/prices'
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=1)

        url_path  = self.base_url + url_extension
        if not start_date:
            start_date = datetime.datetime.strftime(start, '%Y-%m-%d')
        if not end_date:
            end_date = datetime.datetime.strftime(end, '%Y-%m-%d')

        response = requests.get(url_path, params={'start': start_date, 'end': end_date})
        data = response.json()
        if data.get('success'):
            return data.get('data')
        return {}



if __name__ == "__main__":
    nordpool_prices = NordPoolPrices()
    res = nordpool_prices.fetch_hourly_prices()