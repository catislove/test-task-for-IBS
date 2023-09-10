import jsonschema
import pytest
import helper

service = "regres"


@pytest.mark.parametrize('per_page', (1, 2, 3))
def test_get_list_users_with_per_page(per_page):
    schema = helper.response_schema(helper.read_json_schema('get_list_users.json'))
    response = helper.api_request(
        service, "get",
        url="/api/users",
        params={"per_page": per_page}
    )

    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.status_code == 200
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page


@pytest.mark.parametrize('user_id', (1, 5, 12))
def test_get_single_user(user_id):
    schema = helper.response_schema(helper.read_json_schema('get_single_user.json'))
    response = helper.api_request(
        service, "get",
        url=f"/api/users/{user_id}"
    )

    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@pytest.mark.parametrize('user_id', (24, 234))
def test_get_single_user_not_found(user_id):
    response = helper.api_request(
        service, "get",
        url=f"/api/users/{user_id}"
    )

    assert response.status_code == 404


@pytest.mark.parametrize('payload', (
        {
            "name": "morpheus",
            "job": "leader"
        },
        {
            "name": "another morpheus",
            "job": "another leader"
        }))
def test_post_create_user(payload):
    schema = helper.response_schema(helper.read_json_schema('post_create_user.json'))

    response = helper.api_request(
        service, "post",
        url="/api/users",
        json=payload
    )
    assert response.status_code == 201
    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']


@pytest.mark.parametrize('payload, user_id',
                         [({
                               "name": "morpheus",
                               "job": "zion resident"
                           }, 2),
                             ({
                                  "name": "another morpheus",
                                  "job": "another zion resident"
                              }, 3)])
def test_put_update_user(payload, user_id):
    schema = helper.response_schema(helper.read_json_schema('put_update_user.json'))

    response = helper.api_request(
        service, "put",
        url=f"/api/users/{user_id}",
        json=payload
    )
    assert response.status_code == 200
    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']


@pytest.mark.parametrize('payload, user_id',
                         [({
                               "name": "morpheus",
                               "job": "zion resident"
                           }, 4),
                             ({
                                  "name": "another morpheus",
                                  "job": "another zion resident"
                              }, 5)])
def test_patch_update_user(payload, user_id):
    schema = helper.response_schema(helper.read_json_schema('patch_update_user.json'))

    response = helper.api_request(
        service, "patch",
        url=f"/api/users/{user_id}",
        json=payload
    )
    assert response.status_code == 200
    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']


@pytest.mark.parametrize('user_id', (1, 2, 3))
def test_delete_user(user_id):
    response = helper.api_request(
        service, "delete",
        url=f"/api/users/{user_id}"
    )
    assert response.status_code == 204


