from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login_link = browser.find_element_by_xpath("//a[text()='Log in']")
login_link.click()

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("<your username>")
password_input.send_keys("<your password>")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(5)

browser.close()
def test_login_page(browser):
    browser.get('https://www.instagram.com/accounts/login/')
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys("<your username>")
    password_input.send_keys("<your password>")
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0
from time import sleep

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        self.browser.find_element_by_xpath("//a[text()='Log in']").click()
        sleep(2)
        return LoginPage(self.browser)
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("<your username>", "<your password>")

browser.close()
def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("<your username>", "<your password>")

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0
from instapy import InstaPy

session = InstaPy(username="<your_username>", password="<your_password>")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session = InstaPy(username='test', password='test', headless_browser=True)
session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
session.clarifai_check_img_for(['nsfw'])
session.set_relationship_bounds(enabled=True, max_followers=8500)