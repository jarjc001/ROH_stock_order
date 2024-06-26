from playwright.sync_api import Playwright

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .login_info import *
from .file_dates import *


def run(playwright: Playwright, filelocation: str) -> None:
    """
    downloads the csv of the wine order list, can do today or tomorrow
    :param playwright:
    :param filelocation:
    :return:
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.goto("https://resdiary.com/")
    page.goto("https://resdiary.com/?region=GB")
    page.locator("#hs_cos_wrapper_Navbar_with_Menu").get_by_role("link", name="Login").click()
    page.get_by_placeholder("you@domain.com").fill(USERNAME)
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_role("button", name="Log In").click()

    #
    #
    # page.locator("#datepicker-txt").click()
    # page.locator("#datepicker-txt").fill("Wednesday, 7 March 2024")
    # page.locator("#datepicker-txt").press("Enter")

    if for_tomorrow:
        page.wait_for_load_state("networkidle")
        page.wait_for_load_state("networkidle")
        page.get_by_role("link", name="Tomorrow").click()


    with page.expect_download() as download_info:
        page.get_by_role("link", name="Export as CSV").click()
    download = download_info.value

    download.save_as(filelocation + "/" + file_name)

    # ---------------------
    context.close()
    browser.close()


# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.python.org")
# print(driver.title)
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()
