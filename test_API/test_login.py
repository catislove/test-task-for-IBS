import jsonschema
import pytest
import helper

service = "regres"


@pytest.mark.parametrize('payload', (
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        },
        {
            "email": "eve.holt@reqres.in",
            "password": "pistol_another"
        }))
def test_post_login_successful(payload):
    schema = helper.response_schema(helper.read_json_schema('post_login_successful.json'))

    response = helper.api_request(
        service, "post",
        url="/api/login",
        json=payload
    )
    assert response.status_code == 200
    jsonschema.validators.validate(instance=response.json(), schema=schema)

@pytest.mark.parametrize('payload', (
        {
            "email": "sydney@fife"
        },
        {
            "email": "sydney@six"
        }))
def test_post_login_unsuccessful(payload):
    schema = helper.response_schema(helper.read_json_schema('post_login_unsuccessful.json'))

    response = helper.api_request(
        service, "post",
        url="/api/login",
        json=payload
    )
    assert response.status_code == 400
    jsonschema.validators.validate(instance=response.json(), schema=schema)