import json

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import helper

service = "regres"

def post_register_successful(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='register-successful']").click()
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code']").text)
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = helper.api_request(
        service, "post",
        url="/api/register",
        json=payload
    )
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body


def post_register_unsuccessful(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='register-unsuccessful']").click()
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code bad']").text)
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    payload = {
        "email": "sydney@fife"
    }
    response = helper.api_request(
        service, "post",
        url="/api/register",
        json=payload
    )
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body