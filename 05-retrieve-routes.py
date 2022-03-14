import os
import time
import json
from typing import List

from app import database_write, get_public_url
from data_model import Airline, AirlineSchema, Route, RouteSchema
from database import Database

PUBLIC_URL = get_public_url()


def main(src_airport: str, dest_airport: str):
    try:
        Database.initialize()
        retrieved_data = Database.load_from_db(
            {
                "src_airport": src_airport,
                "dest_airport": dest_airport,
                "stops": 1
            }
        )
        routes_with_one_stop = [
            {
                "src_airport": airports['src_airport'],
                "dst_airport": airports['dst_airport'],
                "stop_airport": airports['airline']['iata']
            } for airports in retrieved_data
        ]

    except Exception as err:
        return f"API call failed: {err}"

    return json.dumps(routes_with_one_stop)


if __name__ == "__main__":
    print(main())