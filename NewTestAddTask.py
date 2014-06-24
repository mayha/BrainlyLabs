from appium import webdriver
import os
import time
import sys

sys.path.append("/usr/local/share/python")

from xpath import xpath

success 		= True

desired_caps 					= {}
desired_caps['appium-version'] 	= '1.0'
desired_caps['platformName'] 	= 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] 		= 'HMMRSO59Z9WOCUSW'
desired_caps['app'] 			= os.path.abspath('/Users/mariann/Dropbox/releases/debug/android-search-off-registration-new.apk')
desired_caps['appPackage'] 		= 'com.brainly'
desired_caps['appActivity'] 	= 'com.brainly.ui.activities.MainActivity'

wd = webdriver.Remote('http://0.0.0.0:4725/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present():
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

def login():
	# Click on the login button
	print xpath['login-button']
	wd.find_element_by_xpath(xpath['login-button']).click()
	# Input login information
	wd.find_element_by_xpath(xpath['login-form-username']).send_keys('moniczka10983')
	wd.find_element_by_xpath(xpath['login-form-password']).send_keys('test123')
	# Submit login form
	wd.find_element_by_xpath(xpath['login-form-button']).click()

def chooseTaskSubject():
	# Click choose subject button
	wd.find_element_by_xpath(xpath['task-subject']).click()
	# Scroll through the subjects
	for i in range(1, 4):
		wd.find_element_by_xpath(xpath['task-subject-next']).click()
	# Tap 'OK' button to exit the pop-up
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5451172, "x": 310, "y": 625 })

def chooseTaskPoints():
	# Click choose points button
	wd.find_element_by_xpath(xpath['task-points']).click()
	# Tap 'OK' button
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5641016, "x": 282, "y": 622 })

def addTaskPicture():
	# Click add photo button
	wd.find_element_by_xpath(xpath['task-add-photo']).click()
	# Choose take picture option
	wd.find_element_by_xpath(xpath['take-picture']).click()
	# Time to make a cool picture :D
	time.sleep(2)
	# Click shutter button
	wd.find_element_by_name("Shutter button").click()
	# Wait for 2 seconds
	time.sleep(2)
	# Click confirm button
	wd.find_element_by_name("OK").click()

def search():
	# Click on search bar
	wd.find_element_by_xpath(xpath['header-search']).click()
	# Type search terms
	wd.find_element_by_name("Search query").send_keys('Kto to byl Janko Muzykant?')
	# Wait for results
	time.sleep(3)
	# Select first result
	wd.find_element_by_xpath(xpath['search-result-1']).click()
	# Wait on the selected task
	time.sleep(2)
	# Get back to the search results
	wd.find_element_by_xpath(xpath['back']).click()
	# Exit search view
	wd.find_element_by_xpath(xpath['back']).click()


# Cool brainly test

# Wait on the initial screen
time.sleep(3)
# Login into the application
login()
time.sleep(2)
#Enter tutorial
# Add Task
wd.find_element_by_xpath(xpath['tutorial-add-task']).click()
# Type task content
wd.find_element_by_xpath(xpath['task-input']).send_keys('Jak powstaja chmury burzowe?')
# Choose task subject
chooseTaskSubject()
# Select task points
chooseTaskPoints()
# Add picture
addTaskPicture()
# Click add task button
wd.find_element_by_xpath(xpath['add-task-button']).click()
# Select highlighted task
wd.find_element_by_xpath(xpath['stream-highlight']).click()
# Wait on task view
time.sleep(10)
# Return to the main stream
wd.find_element_by_xpath(xpath['back']).click()
# Exit tutorial
wd.find_element_by_xpath(xpath['tutorial-1']).click()
wd.find_element_by_xpath(xpath['tutorial-1']).click()
# Search for tasks
search()
# Stay on stream for some time
time.sleep(5)
# Click home
wd.find_element_by_xpath(xpath['home']).click()
# Click settings
wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.6203516, "x": 113, "y": 955 })
# Log out
wd.find_element_by_xpath(xpath['logout-button']).click()

# Quit webdriver session
wd.quit()
# If succes is false, test failed
if not success:
	raise Exception("Test failed.")