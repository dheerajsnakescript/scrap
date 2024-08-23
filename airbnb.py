from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")

driver.get('https://www.airbnb.co.in/india/stays')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
# Wait for the elements to be present
wait = WebDriverWait(driver, 10)

try:
    # Get the window handles before clicking the button
    original_windows = driver.window_handles
    checkIn = driver.find_element(By.XPATH, '//*[@id="site-content"]/section[1]/div/div/div/div/form/div[2]/label[1]/input[2]')
    print("\n One\n")

    checkOut = driver.find_element(By.XPATH, '//*[@id="site-content"]/section[1]/div/div/div/div/form/div[2]/label[2]/input[2]')
    print("\n Two \n")

    checkIndate = datetime(year = 2024, month=7,day=12).strftime("%Y-%m-%d")
    
    checkOutdate = datetime(year = 2024,month=7,day=14).strftime("%Y-%m-%d")
   
    
    driver.execute_script("arguments[0].value = arguments[1];", checkIn, checkIndate)
    # print(checkIn.get_attribute('value'))
    driver.execute_script("arguments[0].value = arguments[1];", checkOut, checkOutdate)

    search = driver.find_element(By.XPATH, '//*[@id="site-content"]/section[1]/div/div/div/div/form/button')
    print("\n Three \n")
    search.click()


    # Get the new window handle
    new_window = [window for window in driver.window_handles if window not in original_windows][0]
    
    # Switch to the new window
    driver.switch_to.window(new_window)

    # Wait for the new page to load
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    ## For verification that new page contains both date values.
    assert checkIndate in driver.page_source
    assert checkOutdate in driver.page_source

    title_clas_id = 'listing-card-title'
    subtitle_class_id = 'listing-card-subtitle'
    data_test_id = "data-testid"
    main_div = (
    "//*[contains(@class, 'g1qv1ctd') and "
    "contains(@class, 'atm_u80d3j_1li1fea') and "
    "contains(@class, 'atm_c8_o7aogt') and "
    "contains(@class, 'atm_g3_8jkm7i') and "
    "contains(@class, 'c1v0rf5q') and "
    "contains(@class, 'atm_9s_11p5wf0') and "
    "contains(@class, 'atm_cx_4wguik') and "
    "contains(@class, 'atm_dz_7esijk') and "
    "contains(@class, 'atm_e0_1lo05zz') and "
    "contains(@class, 'dir') and "
    "contains(@class, 'dir-ltr')]"
    )
    location_name = (
    "//*[contains(@class, 't1jojoys') and "
    "contains(@class, 'atm_g3_1kw7nm4') and "
    "contains(@class, 'atm_ks_15vqwwr') and "
    "contains(@class, 'atm_sq_1l2sidv') and "
    "contains(@class, 'atm_9s_cj1kg8') and "
    "contains(@class, 'atm_6w_1e54zos') and "
    "contains(@class, 'atm_fy_1vgr820') and "
    "contains(@class, 'atm_7l_jt7fhx') and "
    "contains(@class, 'atm_cs_10d11i2') and "
    "contains(@class, 'atm_w4_1eetg7c') and "
    "contains(@class, 'atm_ks_zryt35__1rgatj2') and "
    "contains(@class, 'dir') and "
    "contains(@class, 'dir-ltr')]"
    )
    location_info = (
    ".//*[contains(@class, 't6mzqp7') and "
    "contains(@class, 'atm_g3_1kw7nm4') and "
    "contains(@class, 'atm_ks_15vqwwr') and "
    "contains(@class, 'atm_sq_1l2sidv') and "
    "contains(@class, 'atm_9s_cj1kg8') and "
    "contains(@class, 'atm_6w_1e54zos') and "
    "contains(@class, 'atm_fy_kb7nvz') and "
    "contains(@class, 'atm_7l_1he744i') and "
    "contains(@class, 'atm_am_qk3dho') and "
    "contains(@class, 'atm_ks_zryt35__1rgatj2') and "
    "contains(@class, 'dir') and "
    "contains(@class, 'dir-ltr')]"
    )
    per_night_class = "_11jcbg2"
    ratings = (
    "//*[contains(@class, 'a8jt5op') and "
    "contains(@class, 'atm_3f_idpfg4') and "
    "contains(@class, 'atm_7h_hxbz6r') and "
    "contains(@class, 'atm_7i_ysn8ba') and "
    "contains(@class, 'atm_e2_t94yts') and "
    "contains(@class, 'atm_ks_zryt35') and "
    "contains(@class, 'atm_l8_idpfg4') and "
    "contains(@class, 'atm_vv_1q9ccgz') and "
    "contains(@class, 'atm_vy_t94yts') and "
    "contains(@class, 'au0q88m') and "
    "contains(@class, 'atm_mk_stnw88') and "
    "contains(@class, 'atm_tk_idpfg4') and "
    "contains(@class, 'dir') and "
    "contains(@class, 'dir-ltr')]"
    )
    locations = wait.until(EC.presence_of_all_elements_located((By.XPATH, location_name)))
    print("\n Four \n ")

    location_info = driver.find_elements(By.XPATH, location_info)
    print("\n Five \n")

    per_night_price = driver.find_elements(By.CLASS_NAME,per_night_class)
    print("\n Six \n")
    
    ratings = driver.find_elements(By.XPATH, ratings)
    print("\n seven \n")

    col = ['Location Name','Info','Price','Ratings']

    df = pd.DataFrame(columns=col,index=range(1,len(locations)+1))
    # This is one way of scraping the contents
    for i in range(len(locations)):
        name = locations[i].get_attribute('textContent')
        df.index.name = 'Index'
 
        df.loc[i,'Location Name'] = str(name)
        df.loc[i,'Info'] = location_info[i].get_attribute('textContent')
        df.loc[i,'Price'] = per_night_price[i].get_attribute('textContent')
        df.loc[i,'Ratings'] = ratings[i].get_attribute('textContent')

        # print(f"Card no : {i} : Location name : {name}\n"
        #         f"Info : {location_info[i].get_attribute('textContent')}\n"
        #         f"Price : {per_night_price[i].get_attribute('textContent')} - per night \n"
        #         f"Ratings : {ratings[i].get_attribute('textContent')} \n\n"
        #     )
        
    print(df.iloc[4,2])

    df.to_csv('output.csv',index=True)

    # cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, main_div)))
    # content = [[]]

    # This is another way to scrap 
    # for card,i in zip(cards,range(len(cards))):
    #     child_divs = card.find_elements(By.XPATH, ".//div")
    #     print(f"Content of card {i} : {card.get_attribute('textContent')}\n")


    
    # for i in range(len(set(content))):
    #     lc_info = set(content[i])
    #     for j in range(len(lc_info)):
    #         print(lc_info[j])
            
   

        


    driver.delete_all_cookies()
    # Close the browser
    driver.quit()
except NoSuchElementException as e:
    print("Element not found")

except TimeoutException as e:
    print("Time out exception: %s" % e.msg )
