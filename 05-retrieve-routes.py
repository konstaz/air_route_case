import json

from database import Database
from flask import Response


def main(query: dict) -> dict:  # showed dict here in order to avoid additional imports
    """
    The function resposible for retrieving and representing
    flights with one stop when choosing between airports"""
    try:

        Database.initialize()
        retrieved_data = Database.load_routes_from_db(
            {
                "src_airport": query['src_airport'],
                "dst_airport": query['dst_airport'],
                "stops": "1"
            }
        )
        routes_with_one_stop = [
            {
                "src_airport": airports['src_airport'],
                "dst_airport": airports['dst_airport'],
                "stop_airport": airports['airline']['iata']  # <- I understand that this is not a transit airport but
                                                             # I've decided to consider as a transit airport due to the lack of
                                                             # data in case if it was available I'd get the right one
            } for airports in retrieved_data
        ]
        return json.dumps(routes_with_one_stop)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)
