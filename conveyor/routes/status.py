from flask_restx import Resource, Namespace

status_api = Namespace('')


@status_api.route('/ready', methods=['GET'])
class Ready(Resource):
    def get(self):
        return {'message': 'ready', 'success': True}
