import time
import os

# from PIL import Image, ImageGrab
# from PIL import ImageChops

import imgcompare
import pyscreenshot as ImageGrab
import pytest
from pyvirtualdisplay import Display


@pytest.fixture
def setup_page(selenium):
    selenium.get("localhost:8201")
    selenium.find_element_by_css_selector(".container").click()
    time.sleep(5)
    base_img = ImageGrab.grab()
    base_img.save("./images/base_screenshot.jpg")
    return base_img


@pytest.mark.nondestructive
def test_basic_notification(base_url, selenium, setup_page):
    el = selenium.find_element_by_css_selector(
        ".container > p:nth-child(5) > button:nth-child(1)"
    )
    el.click()
    # click allow notification
    with selenium.context(selenium.CONTEXT_CHROME):
        button = selenium.find_element_by_css_selector(
            "button.popup-notification-button:nth-child(4)"
        )
        button.click()
    img = ImageGrab.grab()
    img.save("./images/screenshot.jpg")
    # compare images
    diff = imgcompare.image_diff_percent(setup_page, img)
    assert diff > 0.02


@pytest.mark.nondestructive
def test_basic_notification_with_altered_title(base_url, selenium, setup_page):
    title_box = selenium.find_element_by_css_selector("#msg_txt")
    title_box.send_keys(" testing titles")
    selenium.find_element_by_css_selector(".container").click()
    base_img = ImageGrab.grab()
    base_img.save("./images/base_screenshot_with_altered_title.jpg")
    el = selenium.find_element_by_css_selector(
        ".container > p:nth-child(5) > button:nth-child(1)"
    )
    el.click()
    # click allow notification
    with selenium.context(selenium.CONTEXT_CHROME):
        button = selenium.find_element_by_css_selector(
            "button.popup-notification-button:nth-child(4)"
        )
        button.click()
    selenium.find_element_by_css_selector(".container").click()
    img = ImageGrab.grab()
    img.save("./images/screenshot_with_altered_title.jpg")
    # compare images
    diff = imgcompare.image_diff_percent(base_img, img)
    assert diff > 0.02


@pytest.mark.nondestructive
def test_basic_notification_with_altered_body(base_url, selenium, setup_page):
    body_box = selenium.find_element_by_css_selector("#body_txt")
    body_box.send_keys(" testing body text")
    base_img = ImageGrab.grab()
    el = selenium.find_element_by_css_selector(
        ".container > p:nth-child(5) > button:nth-child(1)"
    )
    el.click()
    # click allow notification
    with selenium.context(selenium.CONTEXT_CHROME):
        button = selenium.find_element_by_css_selector(
            "button.popup-notification-button:nth-child(4)"
        )
        button.click()
    base_img.save("./images/base_screenshot_with_altered_body.jpg")
    img = ImageGrab.grab()
    img.save("./images/screenshot_with_altered_body.jpg")
    diff = imgcompare.image_diff_percent(base_img, img)
    assert diff > 0.02


@pytest.mark.nondestructive
def test_basic_notification_close(base_url, selenium, setup_page):
    el = selenium.find_element_by_css_selector(
        ".container > p:nth-child(5) > button:nth-child(1)"
    )
    el.click()
    # click allow notification
    with selenium.context(selenium.CONTEXT_CHROME):
        button = selenium.find_element_by_css_selector(
            "button.popup-notification-button:nth-child(4)"
        )
        button.click()
    img = ImageGrab.grab()
    img.save("./images/screenshot.jpg")
    # compare images
    diff = imgcompare.image_diff_percent(setup_page, img)
    assert diff > 0.02
    selenium.find_element_by_css_selector(".container > p:nth-child(6) > button:nth-child(1)").click()
    closed_notification_img = ImageGrab.grab()
    closed_notification_img.save("./images/screenshot_close.jpg")
    diff = imgcompare.image_diff_percent(setup_page, closed_notification_img)
    assert round(diff, 2) <= 0.3
