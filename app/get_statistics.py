from selenium import webdriver
import time

firefox_path = "/home/muschkulpesend/Documents/Projects/mackolikData/geckodriver"
driver = webdriver.Firefox(executable_path=firefox_path)



def get_data(cat_count, loop_count, match_details):
    driver.find_element_by_xpath("/html/body/div[6]/div[2]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/div/ul/li["+str(cat_count)+"]/a").click()
    time.sleep(0.5)
    #ev sahibi genel
    xpath = "/html/body/div[6]/div[2]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/ul/li["+str(cat_count)+"]/div/table/tbody/tr[degisken]/td[1]"
    for j in range(1, loop_count+1):
        j = j * 2
        a = driver.find_element_by_xpath(xpath.replace("degisken",str(j))).text
        match_details.append(a)

    #deplasman sahibi genel
    xpath = "/html/body/div[6]/div[2]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/ul/li["+str(cat_count)+"]/div/table/tbody/tr[degisken]/td[3]"
    for j in range(1, loop_count+1):
        j = j * 2
        a = driver.find_element_by_xpath(xpath.replace("degisken",str(j))).text
        match_details.append(a)

def get_stat(link):
    match_details = []
    driver.get(link)
    time.sleep(5)
    #takım isimleri
    xpath = "/html/body/div[6]/div[1]/div[1]/div/div[1]/a[degisken]"
    for i in range(2):
        a = driver.find_element_by_xpath(xpath.replace("degisken",str(i+1))).text
        match_details.append(a)

    #takım skorları
    xpath = "/html/body/div[6]/div[1]/div[1]/div/div[2]/div[2]/div[1]/span[degisken]"
    for i in range(2):
        a = driver.find_element_by_xpath(xpath.replace("degisken",str(i+1))).text
        match_details.append(a)
    
    flag = True
    while(flag):
        try:
            flag = False
            for i in range(1,6):
                if i == 1:
                    get_data(1,6,match_details)
                if i == 2:
                    get_data(2,6,match_details)
                if i == 3:
                    get_data(3,7,match_details)
                if i == 4:
                    get_data(4,3,match_details)
                if i == 5:
                    get_data(5,3,match_details)
        except:
            flag=True
        
    if match_details[2]>match_details[3]:
        match_details.append(1)
    elif match_details[2]<match_details[3]:
        match_details.append(2)
    else:
        match_details.append(0)

    return match_details

