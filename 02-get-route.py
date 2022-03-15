from flask import Response

from database import Database


def main(query: dict) -> dict:
    try:
        Database.initialize()
        retrieved_data = Database.load_one_from_db(query)
        print(f' HEHEHEHEHHEHEHEHEHHEH   :::::::: {list(retrieved_data)}')

        return dict(retrieved_data)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)


if __name__ == "__main__":
    print(main())