import time

from selenium import webdriver

chrome_driver_path = 'D:\\python_projects\\selenium prijects\\chromedriver.exe'
app_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
def launch_browser():
    chromeDriver = webdriver.Chrome(executable_path=chrome_driver_path)
    chromeDriver.get(app_url)
    chromeDriver.maximize_window()
    time.sleep(2)
    return chromeDriver
chromeDriver = launch_browser()

def login_finctionality():
    username_element = chromeDriver.find_element_by_name('username')
    password_element = chromeDriver.find_element_by_name('password')
    login_btn = chromeDriver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

    username_element.send_keys('Admin')
    password_element.send_keys('admin123')
    login_btn.click()
    time.sleep(2)
login_finctionality()

def click_on_Admin():
    admin_element = chromeDriver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
    admin_element.click()
click_on_Admin()