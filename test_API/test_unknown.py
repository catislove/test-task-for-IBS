import jsonschema
import pytest
import helper

service = "regres"


@pytest.mark.parametrize('per_page', (1, 2, 3))
def test_get_list_resources(per_page):
    schema = helper.response_schema(helper.read_json_schema('get_list_resources.json'))
    response = helper.api_request(
        service, "get",
        url="/api/unknown",
        params={"per_page": per_page}
    )

    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.status_code == 200
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page


@pytest.mark.parametrize('resource_id', (1, 5, 7))
def test_get_single_resource(resource_id):
    schema = helper.response_schema(helper.read_json_schema('get_single_resource.json'))
    response = helper.api_request(
        service, "get",
        url=f"/api/unknown/{resource_id}"
    )

    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.status_code == 200

@pytest.mark.parametrize('resource_id', (23, 90))
def test_get_single_resource_not_found(resource_id):
    response = helper.api_request(
        service, "get",
        url=f"/api/users/{resource_id}"
    )

    assert response.status_code == 404