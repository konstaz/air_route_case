from marshmallow import Schema, fields, post_load


class Airline:

    def __init__(
            self,
            _id: str,
            name: str,
            alias: str,
            iata: str
    ):
        self.id = _id
        self.name = name
        self.alias = alias
        self.iata = iata


class Route:

    def __init__(
            self,
            _id: str,
            airline: dict,
            src_airport: str,
            dst_airport: str,
            codeshare: str,
            stops: str,
            airplane: str
    ):
        self._id = _id
        self.airline = airline
        self.src_airport = src_airport
        self.dst_airport = dst_airport
        self.codeshare = codeshare
        self.stops = stops
        self.airplane = airplane


class AirlineSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    alias = fields.Str()
    iata = fields.Str()

    @post_load
    def make_airline(self, data, **kwargs):
        return Airline(**data)


class RouteSchema(Schema):
    _id = fields.Str()
    airline = fields.Dict()
    src_airport = fields.Str()
    dst_airport = fields.Str()
    codeshare = fields.Str()
    stops = fields.Str()
    airplane = fields.Str()

    @post_load
    def make_route(self, data, **kwargs):
        return Route(**data)




# {
#     "_id": {
#         "$oid": "56e9b39b732b6122f8781620"
#     },
#     "airline": {
#         "id": {
#             "$numberInt": "214"
#         },
#         "name": "Air Berlin",
#         "alias": "AB",
#         "iata": "BER"
#     },
#     "src_airport": "DUS",
#     "dst_airport": "CAG",
#     "codeshare": "",
#     "stops": {
#         "$numberInt": "0"
#     },
#     "airplane": {
#         "$numberInt": "738"
#     }
# }
