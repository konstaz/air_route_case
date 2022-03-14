import os
import time

from app import database_write, get_public_url
from data_model import Airline, AirlineSchema, Route, RouteSchema
from database import Database

PUBLIC_URL = get_public_url()


def main(data_to_delete):
    try:

        Database.initialize()
        removed_data = Database.remove_from_db(data_to_delete['_id'])

    except Exception as err:
        return f"API call failed: {err}"

    return removed_data


if __name__ == "__main__":
    print(main())