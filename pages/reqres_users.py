import json

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import helper

service = "regres"


def get_list_users(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='users']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@data-key='response-code']").text)
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    response = helper.api_request(service, "get", url="/api/users?page=2")
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body


def get_single_user(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='users-single']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@data-key='response-code']").text)
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    response = helper.api_request(service, "get", url="/api/users/2")
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body


def get_single_user_not_found(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='users-single-not-found']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code bad']").text)
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    response = helper.api_request(service, "get", url="/api/users/23")
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body

def post_create_user(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='post']").click()
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code']").text)
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = helper.api_request(
        service, "post",
        url="/api/users",
        json=payload
    )
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body['name'] == expected_response_body['name']
    assert actual_response_body['job'] == expected_response_body['job']


def put_update_user(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='put']").click()
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code']").text)
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = helper.api_request(
        service, "put",
        url="/api/users/2",
        json=payload
    )
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body['name'] == expected_response_body['name']
    assert actual_response_body['job'] == expected_response_body['job']


def patch_update_user(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='patch']").click()
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code']").text)
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = helper.api_request(
        service, "put",
        url="/api/users/2",
        json=payload
    )
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body['name'] == expected_response_body['name']
    assert actual_response_body['job'] == expected_response_body['job']


def delete_user(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='delete']").click()
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code bad']").text)
    response = helper.api_request(service, "delete", url="/api/users/2")
    expected_status_code = response.status_code
    assert actual_status_code == expected_status_code
