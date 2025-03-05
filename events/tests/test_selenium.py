import time
import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By



def test_home_page(browser):
    browser.get('http://localhost:8000/')

    header_section = browser.find_element(By.TAG_NAME, 'title')
    header_title = header_section.get_attribute('textContent')
    assert header_title == 'e-tkets Home Page'

    hero_section = browser.find_element(By.CSS_SELECTOR, 'div.hero-text span')
    hero_title = hero_section.get_attribute('textContent')
    assert hero_title == 'Your next great experience is just a click away.'

    hero_section = browser.find_element(By.CSS_SELECTOR, 'div.hero-text h2')
    hero_title = hero_section.get_attribute('textContent').strip()
    assert hero_title == 'Bringing you closer to all the events you love'

    hero_section = browser.find_element(By.CSS_SELECTOR, 'div.hero-text a')
    button_name = hero_section.get_attribute('textContent')
    assert button_name == 'Create events'

    nav_links = browser.find_elements(By.CSS_SELECTOR, 'nav.mainmenu ul li a')
    print('nav links', nav_links)

    expected_links = [
        {"text": "Home", "href": "/"},
        {"text": "About", "href": "#"},
        {"text": "Create", "href": "#"},
        {"text": "Discover events", "href": "#"},
        {"text": "Contacts", "href": "/"}
    ]

    assert len(nav_links) == len(expected_links)

    about_section = browser.find_element(By.CSS_SELECTOR, 'div.ha-text h2')
    about_section_title = about_section.get_attribute('textContent')
    assert about_section_title == 'About e-tkets'

    event_section = browser.find_element(By.CSS_SELECTOR, 'div.section-title h2')
    event_section_title = event_section.get_attribute('textContent')
    assert event_section_title == 'Recent Events'


    # test for title [x]
    # test 'Your next great ...' [x]
    # test_links availabe in the nav [x]
    # create events button [x]
    # test latest events has 3 events
    # test price tickets has 3 block
    # test location title in home page
    # test template used
    # test for hero image
    # test about image




@pytest.mark.django_db
def test_create_event_page(browser):
    browser.get('http://localhost:8000/' + reverse('create_event'))

    header = browser.find_element(By.TAG_NAME, 'title')
    header_title = header.get_attribute('textContent')
    assert header_title == 'e-tkets Create Event', f"Expected title to be 'e-tkets Create Event' but got {header_title}"

    event_name_input = browser.find_element(By.ID, 'id_name')
    event_description_input = browser.find_element(By.ID, 'id_description')
    start_date_input = browser.find_element(By.ID, 'id_start_date')
    end_date_input = browser.find_element(By.ID, 'id_end_date')
    location_input = browser.find_element(By.ID, 'id_location')
    location_tips_input = browser.find_element(By.ID, 'id_location_tips')
    call_for_direction_input = browser.find_element(By.ID, 'id_call_for_direction')
    country_input = browser.find_element(By.ID, 'id_country')
    event_type_input = browser.find_element(By.ID, 'id_event_type')
    is_free_input =  browser.find_element(By.ID, 'id_is_free')
    submit_button = browser.find_element(By.ID, 'submit')


    event_name_input.send_keys('March 2025 event')
    event_description_input.send_keys('... some random descriptions for this event')
    start_date_input.send_keys()
    end_date_input.send_keys()
    location_input.send_keys('Ghana')
    location_tips_input.send_keys('Africa')
    call_for_direction_input.send_keys('123456')
    country_input.send_keys('Ghana')
    event_type_input.send_keys('Business and mentorship')
    if not is_free_input.is_selected():
        is_free_input.click()

    submit_button.click()
    
    # apprantly there's no significantly easy to mock datetime date in selenium
    # when using datetime-local in an inpute field, so I have to sleep the process
    # for 10 seconds so the fields can be manually inputted
        
    time.sleep(10)
    redirect_url = 'http://localhost:8000/account/profile'
    assert browser.current_url == redirect_url, f"Expected to be redirected to {redirect_url} but got redirected here {browser.current_url}"