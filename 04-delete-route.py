from database import Database
from flask import Response


def main(data_to_delete: dict) -> Response:
    try:

        Database.initialize()
        removed_data = Database.remove_one_from_db(data_to_delete['_id'])

        return Response(f"Deleted object: {str(removed_data)}", status=200)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)
