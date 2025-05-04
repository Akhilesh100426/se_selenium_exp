from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
service = Service(executable_path="chromedriver.exe")

user = ["agongadi@gitam.in", "akhilesh@gitam.in", "vamsi@gimail.com"]
passw = ["123456", "123456", "123321"]
height_v = ["173", "180", "160"]
weight_v = ["63", "70", "50"]
age_v = ["20", "21", "1"]




def login(driver, test_count):
    driver.get("https://mnbvcxzlkhj.github.io/SELENIUM/log.html")
    username = driver.find_element(By.ID, "username")
    username.send_keys(user[test_count])
    password = driver.find_element(By.ID, "password")
    password.send_keys(passw[test_count])
    login_button = driver.find_element(By.XPATH, "//button[@type='button']")
    login_button.click()


    time.sleep(2)
    try:
        alert = driver.switch_to.alert
        print(f"Alert Message: {alert.text}") 
        alert.accept()
    except:
        print("No alert detected")

    
    time.sleep(8)

    except_url="https://mnbvcxzlkhj.github.io/SELENIUM/cal.html"
    current_url=driver.current_url
    if current_url == except_url:
        print(f"Login Success for test {test_count}")
        time.sleep(5)
        bmi_test(driver, test_count)
    else:
        print(f"Login failed for test {test_count}")
def bmi_test(driver, test_count):
    driver.get("https://mnbvcxzlkhj.github.io/SELENIUM/cal.html")
    age = driver.find_element(By.ID, "age")
    age.send_keys(age_v[test_count])
    height = driver.find_element(By.ID, "height")
    height.send_keys(height_v[test_count])
    weight = driver.find_element(By.ID, "weight")
    weight.send_keys(weight_v[test_count])
    btn = driver.find_element(By.ID,"btn")
    btn.click()

    time.sleep(5)
    
    result = driver.find_element(By.ID, "output").text
    print(result)
    if "Your BMI is:" in result:
        print(f"BMI Calculation Test success {test_count}")
    else:
        print(f"BMI Calculation Test failed {test_count}")
        print("invalid inputs for BMI calculation")


if __name__ == "__main__":
    for  i in range(len(user)):
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        print("----------------------------------------------------------------------------------------")
        print("Test case: " + str(i))
        try:
            login(driver, i)
        finally:
            driver.quit()






