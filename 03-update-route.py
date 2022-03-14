import os
import time

from app import database_write, get_public_url
from data_model import Airline, AirlineSchema, Route, RouteSchema
from database import Database

PUBLIC_URL = get_public_url()


def main(data_to_update):
    try:

        Database.initialize()
        updated_data = Database.update_to_db(data_to_update.pop('_id'), data_to_update)

    except Exception as err:
        return f"API call failed: {err}"

    return updated_data


if __name__ == "__main__":
    print(main())