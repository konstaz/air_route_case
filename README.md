There are 2 ways to launch the app:
- python app.py
- via docker-compose

.env :
MONGO_NAME = 'sample'
MONGO_COLLECTION = 'routes'
MONGO_URI = 'mongodb://172.17.0.1:27017/'

python app.py:

- clone repository
- python3 -m venv env
- source env/bin/activate
- python app.py

docker-compose:
- Dockerfile is already on the server
- docker build -t < name > .
- docker-compose up -d
json example:
    {
    "_id": "65e9b39b732b6122f8781621",
    "airline": {
        "id": "212",
        "name": "Air Berlin",
        "alias": "AB",
        "iata": "BER"
    },
    "src_airport": "DUS",
    "dst_airport": "CAG",
    "codeshare": "",
    "stops": "0",
    "airplane": "738"
    }
    
postman requests examples:
http://<ip>:5000/01-create-route   (json example above)
http://<ip>:5000/02-get-route?_id=< id >
http://<ip>:5000/03-update-route   (json example above)
http://<ip>:5000/04-delete-route   (json with _id)
http://<ip>:5000/05-retrieve-routes?src_airport=<example>&dst_airport=<example>