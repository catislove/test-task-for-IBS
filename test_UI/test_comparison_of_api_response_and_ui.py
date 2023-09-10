import pytest

from pages.reqres_login import post_login_successful, post_login_unsuccessful
from pages.reqres_register import post_register_successful, post_register_unsuccessful
from pages.reqres_resource import get_list_resources, get_single_resource, get_single_resource_not_found
from pages.reqres_users import get_list_users, get_single_user, get_single_user_not_found, post_create_user, \
    put_update_user, patch_update_user, delete_user


def test_comparison_of_api_response_and_ui_for_users(app):
    get_list_users(app)
    get_single_user(app)
    get_single_user_not_found(app)
    post_create_user(app)
    put_update_user(app)
    patch_update_user(app)
    delete_user(app)


def test_comparison_of_api_response_and_ui_for_resources(app):
    get_list_resources(app)
    get_single_resource(app)
    get_single_resource_not_found(app)


def test_comparison_of_api_response_and_ui_for_register(app):
    post_register_successful(app)
    post_register_unsuccessful(app)

def test_comparison_of_api_response_and_ui_for_login(app):
    post_login_successful(app)
    post_login_unsuccessful(app)