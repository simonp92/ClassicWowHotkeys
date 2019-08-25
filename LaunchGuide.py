from pynput.keyboard import Key, KeyCode, Listener
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
from furl import furl

# Initialize values from configuration
config = ConfigParser()
config.read('settings.ini')

faction = config.get('settings', 'faction')
race = config.get('settings', 'race')
className = config.get('settings', 'class')
section = config.get('settings', 'section')
step = config.get('settings', 'step')

def execute_next():
    print("Detected next hotkey")
    nextBtn.click()
    global step
    #step+=1
    url = driver.current_url
    print(url)
    update_settings()

def execute_prev():
    print("Detected prev hotkey")
    prevBtn.click()
    global step
    #step-=1
    update_settings()

# Create a mapping of keys to function (use frozenset as sets are not hashable - so they can't be used as keys)
combination_to_function = {
    frozenset([Key.shift, KeyCode(char='s')]): execute_next, # No `()` after function_1 because we want to pass the function, not the value of the function
    frozenset([Key.shift, KeyCode(char='S')]): execute_next,
    frozenset([Key.shift, KeyCode(char='a')]): execute_prev,
    frozenset([Key.shift, KeyCode(char='A')]): execute_prev,
}

current_keys = set()

#Start webbrowser
guideUrl = "https://classicwow.live/leveling/"+faction+"/solo/"+race+"/"+className+"?section="+section+"&step="+step
driver = webdriver.Chrome()
driver.get(guideUrl)

try: nextBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/main/section/div/div[2]/div[1]/div/div[1]/div/button[2]"))
    )
except:
    print("Timeout while waiting for presence of next button element")

try: prevBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/main/section/div/div[2]/div[1]/div/div[1]/div/button[1]"))
    )
except:
    print("Timeout while waiting for presence of prev button element")

print(nextBtn.get_attribute("name"))



def on_press(key):
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
    current_keys.remove(key)

def update_settings():
    global step
    global section

    step = get_step_from_url(driver.current_url)
    section = get_section_from_url(driver.current_url)

    settings_file = open('settings.ini','w')
    config.set('settings', 'step', step)
    config.set('settings', 'section', section)
    config.write(settings_file)
    settings_file.close()

def get_step_from_url(url):
    print("Step")
    localStep = furl(url).args['step']
    print(localStep)
    return localStep

def get_section_from_url(url):
    print("Section")
    localSection = furl(url).args['section']
    print(localSection)
    return localSection

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()