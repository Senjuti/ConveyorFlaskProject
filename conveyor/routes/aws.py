import logging

from flask_restx import Resource, Namespace
from flask_restx.fields import Raw, String, Boolean

from ..utils.s3_utils import list_buckets, create_bucket, delete_bucket

aws_api = Namespace('aws')

log = logging.getLogger(__name__)

response_t = aws_api.model(
    'response_t',
    {
        'data': Raw,
        'errors': Raw,
        'message': String,
        'success': Boolean,
    },
)


@aws_api.errorhandler
def default_error_handler(error):
    return {'message': f'{error=}', 'success': False}, 500


@aws_api.route('/list', methods=['GET'])
class List(Resource):
    @aws_api.marshal_with(response_t, skip_none=True)
    def get(self):
        log.info('List buckets.')
        try:
            return {'message': list_buckets(), 'success': True}
        except Exception as e:
            return {
                'message': f'Failed to list buckets due to error: {e}',
                'success': False,
            }


@aws_api.route('/create/<string:bucket_name>', methods=['POST'])
class Create(Resource):
    @aws_api.marshal_with(response_t, skip_none=True)
    def post(self, bucket_name):
        log.info(f'Create bucket={bucket_name}.')
        try:
            return {'message': create_bucket(bucket_name), 'success': True}
        except Exception as e:
            return {
                'message': f'Failed to create bucket={bucket_name} due to error: {e}',
                'success': False,
            }


@aws_api.route('/delete/<string:bucket_name>', methods=['DELETE'])
class Delete(Resource):
    @aws_api.marshal_with(response_t, skip_none=True)
    def delete(self, bucket_name):
        log.info(f'Delete bucket={bucket_name}.')
        try:
            return {'message': delete_bucket(bucket_name), 'success': True}
        except Exception as e:
            return {
                'message': f'Failed to delete bucket={bucket_name} due to error: {e}',
                'success': False,
            }
