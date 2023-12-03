from flask_restx import Namespace, Resource, abort

api = Namespace('User', description='Endpoint de ejemplo')

parser = api.parser()
parser.add_argument('id', type=int, help='ID', required=True)


@api.route('/')
class User(Resource):
    @api.expect(parser)
    @api.response(200, 'Success')
    @api.response(404, 'User not found')
    def get(self):
        args = parser.parse_args()
        id = args['id']

        if id == 1:
            return {'id': id, 'name': 'Manolo'}, 200
        if id == 2:
            return {'id': id, 'name': 'Pepe'}, 200

        return abort(404, 'User not found', id=id)
