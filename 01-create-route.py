from data_model import Route, RouteSchema
from database import Database
from flask import Response


def main(data_to_store: Route) -> Response:
    try:
        print(f'SAVVVAVAAVVAVAVAVAV::::::: {data_to_store}')
        route_schema = RouteSchema()
        deserialized_data = route_schema.load(data_to_store)
        if deserialized_data:
            Database.initialize()
            saved_data = Database.save_one_to_db(data_to_store)

            return Response(f"Saved object: {str(saved_data)}", status=200)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)


if __name__ == "__main__":
    print(main())