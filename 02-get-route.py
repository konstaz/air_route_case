import os
import time

from app import database_write, get_public_url
from data_model import Airline, AirlineSchema, Route, RouteSchema
from database import Database

PUBLIC_URL = get_public_url()


def main(_id: str):
    try:
        Database.initialize()
        retrieved_data = Database.load_from_db(
            {
                "_id": _id
            }
        )

    except Exception as err:
        return f"API call failed: {err}"

    return retrieved_data


if __name__ == "__main__":
    print(main())