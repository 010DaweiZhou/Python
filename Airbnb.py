from selenium import webdriver
import time

# div class="_gig1e7"   house
# div class="_1ixtnfc"  price

houseDic = dict()
link = r'https://www.airbnb.cn/s/北京/homes?parent_city_place_id=ChIJuSwU55ZS8DURiqkPryBWYrk&place_id=ChIJuSwU55ZS8DURiqkPryBWYrk&query=北京&refinement_paths%5B%5D=%2Fhomes&checkin=&checkout='
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(link)

houses = driver.find_elements_by_css_selector('div._gig1e7')

for house in houses:
    price = house.find_element_by_css_selector('div._1ixtnfc')
    name = house.find_element_by_css_selector('div._qhtkbey')
    houseDic[name.text.strip()] = price.text[4:].strip()


for key, value in houseDic.items():
    print('%s : %4s' % (key ,value))


driver.quit()
