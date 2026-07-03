import datetime
import requests


class NordPoolPrices:

    def __init__(self, timeout=30):
        self.timeout = timeout
        self.base_url = 'https://nordapi.ee/api/v1/elering'

    def fetch_hourly_prices(
            self,
            start_date: str = None,
            end_date: str = None
    ) -> dict:
        url_extension = '/prices'
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=1)

        url_path  = self.base_url + url_extension
        if not start_date:
            start_date = datetime.datetime.strftime(start, '%Y-%m-%d')
        if not end_date:
            end_date = datetime.datetime.strftime(end, '%Y-%m-%d')
        params = {'start': start_date, 'end': end_date}

        response = requests.get(url_path, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        result = {
            "metadata": {
                "source": "nordapi",
                "request_params": params,
                "success": data.get("success", False),
            },
            "payload": data
        }
        return result



if __name__ == "__main__":
    nordpool_prices = NordPoolPrices()
    res = nordpool_prices.fetch_hourly_prices()