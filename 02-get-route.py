from flask import Response

from database import Database


def main(query: dict) -> dict:  # showed dict here in order to avoid additional imports
    try:
        Database.initialize()
        retrieved_data = Database.load_one_from_db(query)

        return dict(retrieved_data)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)
