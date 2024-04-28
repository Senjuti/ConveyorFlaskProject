from unittest import mock

import pytest
from botocore.exceptions import ClientError

from conveyor.flask_app import create_app

buckets = ['test-bucket-1']


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


@pytest.fixture
def list_fixture_success():
    with mock.patch('conveyor.routes.aws.list_buckets', return_value=buckets):
        yield


@pytest.fixture
def list_fixture_failure():
    with mock.patch(
        'conveyor.routes.aws.list_buckets',
        side_effect=ClientError(
            {'Error': {'Code': 500, 'Message': 'General'}}, 'list'
        ),
    ):
        yield


def test_ready_route(client):
    response = client.get('/api/v1/ready')
    assert response.json == {'message': 'ready', 'success': True}


def test_list_route_success(client, list_fixture_success):
    response = client.get('/api/v1/aws/list')
    assert response.json == {'message': f'{buckets}', 'success': True}


def test_list_route_failure(client, list_fixture_failure):
    response = client.get('/api/v1/aws/list')
    assert response.json == {
        'message': 'Failed to list buckets due to error: An error occurred (500) when calling the list operation: General',
        'success': False,
    }
