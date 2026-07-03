from src.energy_lakehouse.clients import OpenMeteo
from src.energy_lakehouse.writers import RawJsonWriter


def run() -> None:
    client = OpenMeteo()
    writer = RawJsonWriter(base_path="data/bronze")

    prices = client.fetch_hourly_temperature()
    writer.write(
        dataset="weather_hourly",
        data=prices
    )


if __name__ == "__main__":
    run()