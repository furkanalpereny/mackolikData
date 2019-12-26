from selenium import webdriver
import time

def get_links(link, season_xpath):
    firefox_path = "/home/muschkulpesend/Documents/Projects/mackolikData/geckodriver"
    driver = webdriver.Firefox(executable_path=firefox_path)
    driver.get(link)
    time.sleep(3)
    link_list = []

    driver.find_element_by_xpath("/html/body/div[6]/div[2]/main/div/div[4]/div[1]/div/div/div").click()
    print("sezon listesine tıklandı")
    time.sleep(1)
    driver.find_element_by_xpath(season_xpath).click()
    print("sezona tıklandı")


    for i in range(33):
        links = driver.find_elements_by_class_name("p0c-competition-match-list__match-link")
        for i in links:
            link_list.append(i.get_attribute("href"))
        a = driver.find_elements_by_xpath("/html/body/div[6]/div[2]/main/div/div[2]/div/div/div[1]")
        a[0].click()
        time.sleep(1.5)


    link_list=list(set(link_list))

    with open('maclar.txt', 'w') as f:
        for item in link_list:
            f.write("%s\n" % item)

    driver.close()
    return link_list

