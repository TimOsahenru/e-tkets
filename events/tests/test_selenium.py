import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By


@pytest.mark.django_db
def test_create_event_page(browser):
    browser.get('http://localhost:8000/' + reverse('create_event'))

    header = browser.find_element(By.TAG_NAME, 'title')
    header_title = header.get_attribute('textContent')
    assert header_title == 'e-tkets Create Event', f"Expected title to be 'Create Event' but got {header_title}"


    event_name_input = browser.find_element(By.NAME, 'name')
    event_description_input = browser.find_element(By.NAME, 'description')
    start_date_input = browser.find_element(By.NAME, 'start_date')
    end_date_input = browser.find_element(By.NAME, 'end_date')
    location_input = browser.find_element(By.NAME, 'location')
    location_tips_input = browser.find_element(By.NAME, 'location_tips')
    call_for_direction_input = browser.find_element(By.NAME, 'call_for_direction')
    country_input = browser.find_element(By.NAME, 'country')
    event_type_input = browser.find_element(By.NAME, 'event_type')
    is_free_input =  browser.find_element(By.NAME, 'is_free')

    submit_button = browser.find_element(By.NAME, 'submit')

    event_name_input.send_keys('March 2025 event')
    event_description_input.send_keys('... some random descriptions for this event')
    start_date_input.send_keys('2023-10-01 12:00:00')
    end_date_input.send_keys('2023-10-01 14:00:00')
    location_input.send_keys('Ghana')
    location_tips_input.send_keys('Africa')
    call_for_direction_input.send_keys('123456')
    country_input.send_keys('Ghana')
    event_type_input.send_keys('Business and mentorship')
    is_free_input.send_keys('True')
    submit_button.click()


    redirect_url = 'http://localhost:8000/account/profile'
    assert browser.current_url == redirect_url, f"Expected to be redirected to {redirect_url} but got redirected here {browser.current_url}"