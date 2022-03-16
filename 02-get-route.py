from flask import Response

from database import Database


def main(query: dict) -> dict:  # showed dict here in order to avoid additional imports
    """
    The function finds one specific route by its ID
    (not really convenient I know that
    and better search by two airports
    but I technically showed in route with one stop 05-retrieve-routes)
    """
    try:
        Database.initialize()
        retrieved_data = Database.load_one_from_db(query)

        return dict(retrieved_data)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)
