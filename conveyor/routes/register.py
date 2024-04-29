import logging

from flask_restx import Namespace, Resource, abort

log = logging.getLogger(__name__)

register_api = Namespace('register')

db = {'2@gmail.com': 'admin', '1@gmail.com': 'password'}


@register_api.route(
    '/login/<string:username>/<string:password>', methods=['POST']
)
class Login(Resource):
    def post(self, username: str, password: str):
        log.info('Login user')
        status = is_logged_in(username, password)
        log.info(f'{status=}')
        if status == 200:
            return {'message': 'Successfully logged in', 'success': True}
        else:
            abort(status, custom='Either password or username is incorrect.')


def is_logged_in(username: str, password: str) -> int:
    if username not in db:
        # 404
        return 404
    if db.get(username) != password:
        # 401
        return 401
    return 200
