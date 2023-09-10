import json

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import helper

service = "regres"

def get_list_resources(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='unknown']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code']").text)
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    response = helper.api_request(service, "get", url="/api/unknown")
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body


def get_single_resource(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='unknown-single']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code']").text)
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    response = helper.api_request(service, "get", url="/api/unknown/2")
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body


def get_single_resource_not_found(app):
    driver = app.wd
    section = driver.find_element(By.XPATH, "//section[@id='console']")
    while not section.is_displayed():
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.find_element(By.XPATH, "//li[@data-id='unknown-single-not-found']").click()
    actual_status_code = int(driver.find_element(By.XPATH, "//span[@class='response-code bad']").text)
    driver.find_element(By.XPATH, "//pre[@data-key='output-response']").click()
    actual_element_content = driver.find_element(By.XPATH, "//pre[@data-key='output-response']").text
    actual_response_body = json.loads(actual_element_content)
    response = helper.api_request(service, "get", url="/api/unknown/23")
    expected_status_code = response.status_code
    expected_response_body = response.json()
    assert actual_status_code == expected_status_code
    assert actual_response_body == expected_response_body