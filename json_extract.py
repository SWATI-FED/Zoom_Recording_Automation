# Selenium 
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Date and time
import time
from datetime import date
from datetime import timedelta

# Captcha Solver
import captcha_solve

# List Parser
import list_parser

# Get the current date
today = date.today()
options = selenium.webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3')
driver = selenium.webdriver.Chrome('chromedriver.exe', options=options)
GLA = 'https://glauniversity.in:8085/'
duty_details = 'https://glauniversity.in:8085/MyAccount/DutyDetails'


"""

Json Extraction

"""

def extract_json(days_ago):
    driver.get(GLA)

    # Find the Sign In button
    dropdown = find_element('ed-micon', 'class')
    dropdown.click()

    sign_in_button = find_element('/html/body/section[1]/div/div/div[2]/div/div/ul/li[1]/a', 'xpath')
    time.sleep(1)
    sign_in_button.click()
    time.sleep(1)
    
    # User Input ROLL_NO
    ROLL_NO = input("Enter your ROLL_NO: ")

    # User Input PASSWORD
    PASSWORD = input("Enter your PASSWORD: ")
    
    # Finds University Roll Number Input Box
    roll = find_element('username')
    roll.send_keys(ROLL_NO)

    # Finds Password Input Box
    password = find_element('userpass')
    password.send_keys(PASSWORD)

    while True:
        # Find the Captcha image, and save it
        img = find_element('LImgCaptcha')
        img.screenshot('CaptchaImage.png')

        # Finds Captcha Input Box
        captcha = find_element('LCaptcha')

        # Find the Alert Box OK Button, to click if the Captcha is Wrong
        captcha.send_keys(captcha_solve.solve_captcha('CaptchaImage.png'))

        # Clicks the 'Login' button
        login = find_element('//*[@id="modal1"]/div/div[2]/form/div[5]/div/a', 'xpath')
        login.click()
        time.sleep(2)

        try:
            alert_button = driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/button')
            alert_button.click()
        # If the button can not be clicked [Possibly Logged In]
        except selenium.common.exceptions.ElementClickInterceptedException:
            print(f"No Element")
            break
        # If the button is not found
        except selenium.common.exceptions.NoSuchElementException:
            print(f"Probably Logged in Now")
            break

    time.sleep(5)

    for i in range(1, days_ago+1):
        if (today-timedelta(days=i)).strftime('%A') == 'Saturday' or (today-timedelta(days=i)).strftime('%A') == 'Sunday':
            continue
        else:
            date = {'text': str(today-timedelta(days=i))}  # Today's Date
            class_details = driver.execute_script(f'return ($.post("{duty_details}", {date}))')
            # print(class_details)

            if class_details[0]['JoinUrl'] == None:
                continue
            else:
                if class_details:
                    list_parser.write_class(class_details, date['text'])
                    print(f"Written Classes for {date['text']}")
    
    driver.quit()


def find_element(element_id, element_type='ID'):
    dct = {'ID': By.ID, 'link': By.LINK_TEXT, 'class': By.CLASS_NAME, 'xpath': By.XPATH}
    by = dct[element_type]
    try:
        # Waits for 10 seconds until the given element id is found
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, element_id))
        )
        return element

    except selenium.common.exceptions.TimeoutException:
        # In case its not found, the browser quits and the program exits
        print(f"Could not find Online Class element, exiting..")
        driver.quit()
