import os
import time

from app import database_write, get_public_url
from data_model import Airline, AirlineSchema, Route, RouteSchema
from database import Database

PUBLIC_URL = get_public_url()


def main(data_to_store):
    try:

        route_schema = RouteSchema()
        deserialized_data = route_schema.load(data_to_store)
        Database.initialize()
        saved_data = Database.save_to_db(deserialized_data)

    except Exception as err:
        return f"API call failed: {err}"

    return saved_data


if __name__ == "__main__":
    print(main())