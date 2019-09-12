from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "xxx" # put username here
password = "xxx" # put password here

in_or_out = raw_input("in or out?: ")
if (in_or_out == "i"):
    print("clocking in")
    action = "entered"
else:
    print("clocking out")
    action = "exited"

#grabbing url for the login page for workday
driver = webdriver.Chrome()
driver.get("https://wd5.myworkday.com/uchicago/login.flex")
assert "Web Login Service" in driver.title

#fill in username, password, and submit values
user = driver.find_element(By.NAME, "j_username")
user.clear()
user.send_keys(username)

password = driver.find_element(By.NAME, "j_password")
password.clear()
password.send_keys(password)

submit = driver.find_element(By.NAME, "_eventId_proceed")
submit.send_keys(Keys.RETURN)

#checking that login was successful
assert "Workday" in driver.title

wait = WebDriverWait(driver, 30)

#click on time module
time = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#wd-home-applets > li:nth-child(1) > div")))
time.send_keys(Keys.RETURN)

if (in_or_out == "i"):
    #click on check in button
    enter_time = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wd-DropDownCommandButton-56$234380"]/button[1]')))
    # enter_time.send_keys(Keys.RETURN)

elif (in_or_out == "o"):
    #click on check out button
    exit_time = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wd-DropDownCommandButton-56$234381"]/button[1]')))
    # exit_time.send_keys(Keys.RETURN)

#waiting for popup to be present
popup_accept = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div/div')))

#click on ok
if (popup_accept):
    if (in_or_out == "o"):
        out_option = driver.find_element(By.XPATH, '//*[@id="gwt-uid-6"]')
        out_option.click()
        out_option.send_keys(Keys.RETURN)
    accept_enter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wd-EditPage-6$50468"]/footer/div/div[2]/div/div[1]/div[1]/button[1]')))
    #accept_enter.send_keys(Keys.RETURN)
    
    print("time successfully", action)

