from database import Database
from flask import Response


def main(data_to_delete):
    try:

        Database.initialize()
        removed_data = Database.remove_one_from_db(data_to_delete['_id'])
        print(f'DADADADADDADADADADDADA ::::: {removed_data}')

        return Response(f"Deleted object: {str(removed_data)}", status=200)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)


if __name__ == "__main__":
    print(main())