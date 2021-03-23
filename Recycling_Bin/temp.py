from selenium import webdriver
import time
import random

templist = ["98.1","98.2","98.3","98.4","98.5","98.6","98.7","98.8"]

upl = ["USERNAME","PASSWORD"]

for i in range(0,int(upl.len()/2)):

    driver = webdriver.Chrome()

    driver.get("https://www.wabash.edu/covidpass/%22)

    element = driver.find_element_by_id("i0116")

    print("INPUTTING USER")
    element.send_keys(upl[2i])

    nextbutt = driver.find_element_by_id("idSIButton9")

    nextbutt.click()
    time.sleep(2)
    password = driver.find_element_by_id("i0118")
    password.send_keys(upl[(2i)+1])

    time.sleep(2)
    try:
        signin = driver.find_element_by_id("idSIButton9")
        signin.click()
        time.sleep(2)
        nobutt = driver.find_element_by_id("idBtn_Back");
        nobutt.click()
        time.sleep(2)

        no = driver.find_element_by_xpath("//div[1]/div/div[2]/label")
        no.click()

        temp = driver.find_element_by_id("temperature_input")
        random.seed(time.time())
        randtemp = random.randint(0,7)
        temp.send_keys(templist[randtemp])

        nosymp = driver.find_element_by_xpath("//div[3]/div[10]/div/div/label")
        nosymp.click()

        submitbttn = driver.find_element_by_xpath("//div[4]/div[2]/p[2]/button")
        submitbttn.click()
        driver.close()
    except:
        print("invalid")
        driver.close()