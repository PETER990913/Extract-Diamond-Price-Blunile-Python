from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd
import time
import re
df1 = pd.read_csv("url.csv")
url = df1.url
driver = uc.Chrome()
driver.maximize_window()
diamond_list = []
shp = []
pri = []
crt = []
cutg = []
clr = []
clrt = []
Dat = []
for j in range(0, len(url)):
    if j==4 or j==6 or j==8:
        # j==0 ----- Round
        # j==1 ----- Princess
        # j==2 ----- Cushion
        # j==3 ----- Oval
        # j==4 ----- Emarald
        # j==5 ----- Pear
        # j==6 ----- Asscher
        # j==7 ----- Heart
        # j==8 ----- Radiant
        # j==9 ----- Marquise
        driver.get(url[j])
        #### Carat Option ####
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div[1]/main/div/div/div/section/div/div[2]/div[4]/div[2]/div[3]/div[2]/div[2]/div/fieldset/div/div[2]/input')))
        a = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/section/div/div[2]/div[4]/div[2]/div[3]/div[2]/div[2]/div/fieldset/div/div[2]/input')
        action = ActionChains(driver)
        action.double_click(a)
        action.send_keys('5.99')
        action.send_keys(Keys.ENTER)
        action.perform()


        #### Color Option ####
        color_min = driver.find_element(By.XPATH, '//*[@id="color-filter-container-accordion"]/div/div[2]/div[9]')
        color_max = driver.find_element(By.XPATH, '//*[@id="color-filter-container-accordion"]/div/div[2]/div[10]')
        b = driver.find_element(By.XPATH, '//*[@id="color-filter-container-accordion"]/div/div[2]/div[1]')
        driver.execute_script(
            "arguments[0].setAttribute('style','width: calc(87.5% + 2px); left: 12.5%;')", b)
        driver.execute_script(
            "arguments[0].setAttribute('style','right: 87.5%;')", color_min)
        driver.execute_script(
            "arguments[0].setAttribute('class','left handle ')", color_min)
        driver.execute_script(
            "arguments[0].setAttribute('aria-valuenow','J')", color_min)
        driver.execute_script(
            "arguments[0].setAttribute('aria-valuetext','J')", color_min)
        driver.execute_script(
            "arguments[0].setAttribute('aria-valuemin','J')", color_max)
        action.send_keys(Keys.ENTER)
        action.perform()
        driver.find_element(By.XPATH, '//*[@id="color-filter-container-accordion"]/div/div[2]/div[9]').click()


        #### CutGrade Option ####
        if j==0:
            carat_min = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[5]')
            carat_max = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[6]')
            c = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[1]')
            driver.execute_script(
                "arguments[0].setAttribute('style','width: calc(25% + 2px); left: 25%;')", c)
            driver.execute_script(
                "arguments[0].setAttribute('style','right: 75%;')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('class','left handle ')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuenow','Very Good')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuetext','Very Good')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuemin','Very Good')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('style','left: 50%;')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuenow','Very Good')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuetext','Very Good')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuemax','Very Good')", carat_min)
            action.send_keys(Keys.ENTER)
            action.perform()
            driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[5]').click()
            driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[6]').click()
        if j==1 or j==2 or j==3 or j==7 or j==8:
            carat_min = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[4]')
            carat_max = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[5]')
            c = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[1]')
            driver.execute_script(
                "arguments[0].setAttribute('style','width: calc(33.3333% + 2px); left: 33.3333%;')", c)
            driver.execute_script(
                "arguments[0].setAttribute('style','right: 66.6667%;')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('class','left handle ')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuenow','Very Good')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuetext','Very Good')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuemin','Very Good')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('style','left: 66.6667%;')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuenow','Very Good')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuetext','Very Good')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuemax','Very Good')", carat_min)
            action.send_keys(Keys.ENTER)
            action.perform()
            carat_min = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[4]').click()
            carat_max = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[5]').click()
        if j==4 or j==5 or j==6 or j==9:
            carat_min = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[3]')
            carat_max = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[4]')
            c = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[1]')
            driver.execute_script(
                "arguments[0].setAttribute('style','width: calc(50% + 2px); left: 50%;')", c)
            driver.execute_script(
                "arguments[0].setAttribute('style','right: 50%;')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('class','left handle ')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuenow','Very Good')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuetext','Very Good')", carat_min)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuemin','Very Good')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('style','left: 100%;')", carat_max)
            driver.execute_script(
                "arguments[0].setAttribute('aria-valuemax','Very Good')", carat_min)
            action.send_keys(Keys.ENTER)
            action.perform()
            carat_min = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[3]').click()
            carat_max = driver.find_element(By.XPATH, '//*[@id="cut-filter-container-accordion"]/div/div[2]/div[4]').click()

        #### Click More Filter ####
        driver.find_element(By.XPATH, '//*[@id="react-app"]/div/div/section/div/div[2]/div[4]/div[3]/button[1]').click()
        time.sleep(3)


        #### Florescence Option ####
        florescence_min = driver.find_element(By.XPATH, '//*[@id="fluorescence-filter-container-accordion"]/div/div[2]/div[6]')
        florescence_max = driver.find_element(By.XPATH, '//*[@id="fluorescence-filter-container-accordion"]/div/div[2]/div[7]')
        d = driver.find_element(By.XPATH, '//*[@id="fluorescence-filter-container-accordion"]/div/div[2]/div[1]')
        driver.execute_script(
            "arguments[0].setAttribute('style','width: calc(40% + 2px); left: 60%;')", d)
        driver.execute_script(
            "arguments[0].setAttribute('style','right: 40%;')", florescence_min)
        driver.execute_script(
            "arguments[0].setAttribute('class','left handle ')", florescence_min)
        driver.execute_script(
            "arguments[0].setAttribute('aria-valuenow','Faint')", florescence_min)
        driver.execute_script(
            "arguments[0].setAttribute('aria-valuetext','Faint')", florescence_min)
        driver.execute_script(
            "arguments[0].setAttribute('aria-valuemin','Faint')", florescence_max)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="fluorescence-filter-container-accordion"]/div/div[2]/div[6]')))
        driver.find_element(By.XPATH, '//*[@id="fluorescence-filter-container-accordion"]/div/div[2]/div[6]').click()  
        action.perform()
        time.sleep(5)


        #### Scroll down to Bottom ####
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        #### Waiting for page loading ####
        time.sleep(30)

        #### Move on to the Top ####
        driver.find_element(By.XPATH, '//*[@id="back-to-top-button"]').click()

        #### Finding the Rows and scraping ####
        tables = driver.find_elements(By.XPATH, '//*[@id="diamond-result"]/div[2]/div/div[2]/div')
        print(len(tables))
        for i in range(0, len(tables)):
            row = tables[i].find_elements(By.CLASS_NAME, "row-cell")    
            new_data = {}
            Shape = row[0].text
            shp.append(Shape)
            new_data["Shape"] = Shape

            Price = row[1].text
            pri.append(Price)
            new_data["Price"] = Price

            Carat = row[2].text
            crt.append(Carat)
            new_data["Carat"] = Carat

            CutGrade = row[3].text
            cutg.append(CutGrade)
            new_data["CutGrade"] = CutGrade

            Color = row[4].text
            clr.append(Color)
            new_data["Color"] = Color

            Clarity = row[5].text
            clrt.append(Clarity)
            new_data["Clarity"] = Clarity

            Delivery_date = row[15].text
            Dat.append(Delivery_date)
            new_data["Delivery_date"] = Delivery_date

            diamond_list.append(new_data)

            dict = {'Shape': shp, 'Price': pri, 'Carat': crt, 'CutGrade': cutg,
                    'Color': clr, 'Clarity': clrt, 'Delivery_date': Dat}

            df = pd.DataFrame(dict)

            df.to_csv('Result_diamond.csv')

print(diamond_list)
while True:
    pass
