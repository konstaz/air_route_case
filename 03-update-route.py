from flask import Response

from data_model import RouteSchema
from database import Database


def main(data_to_update):
    try:
        route_schema = RouteSchema()
        deserialized_data = route_schema.load(data_to_update)
        if deserialized_data:
            Database.initialize()
            updated_data = Database.update_one_to_db(data_to_update.pop('_id'), data_to_update)

            return Response(f"Updated object: {str(updated_data)}", status=200)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)


if __name__ == "__main__":
    print(main())