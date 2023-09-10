import json

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import helper

service = "regres"

def post_login_successful(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='login-successful']").click()
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code']").text)
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = helper.api_request(
        service, "post",
        url="/api/login",
        json=payload
    )
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body


def post_login_unsuccessful(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='login-unsuccessful']").click()
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code bad']").text)
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    payload = {
        "email": "peter@klaven"
    }
    response = helper.api_request(
        service, "post",
        url="/api/login",
        json=payload
    )
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body