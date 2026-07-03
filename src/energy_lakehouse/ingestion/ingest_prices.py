from energy_lakehouse.clients import NordPoolPrices
from energy_lakehouse.writers import RawJsonWriter

def run() -> None:
    client = NordPoolPrices()
    writer = RawJsonWriter(base_path="data/bronze")

    prices = client.fetch_hourly_prices()
    writer.write(
        dataset="prices_hourly",
        data=prices
    )


if __name__ == "__main__":
    run()