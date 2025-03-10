import pytest
from app import app

def test_request():
    TestResponse = app.test_client().get('/')
    response_status_code = TestResponse.status_code
    response_data = TestResponse.data
    assert response_status_code == 200, 'Response invalid !'
    assert response_data == b'<h1 style = "color:green;">Hello world !</h1>'