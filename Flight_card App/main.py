#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime,timedelta
from flight_search import FlightSearch
from pprint import pprint

data = DataManager()
data_sheet = data.prices()


if data_sheet[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in data_sheet:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data.data = data_sheet
    data.data_update()

ORIGIN_CITY_IATA = "LON"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in data_sheet:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
