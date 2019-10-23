from selenium import webdriver
import re
import time
#https://movie.douban.com/subject/30444960/comments?                  sort=new_score&status=F
#https://movie.douban.com/subject/30444960/comments?start=20&limit=20&sort=new_score&status=F

dic = dict()
start = 0
limit = 20
pages = 0

movie_id = 26426056
fileName = 'ChenShuiMoZhou.txt'

status = 'P'

link1 = 'https://movie.douban.com/subject/' + str(movie_id) + '/comments?'
link2 = 'sort=new_score&status=' + status

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(link1 + link2)

total = driver.find_element_by_tag_name('li.is-active')
total = re.search(r'(\d+)', total.text)
total = int(total.group(0))

if total % limit == 0:
    pages = total // limit
else:
    pages = total // limit + 1

with open(fileName, 'w+', encoding='utf-8') as f:
    for page in range(0 , pages):
        if page == 0:
            link = link1 + link2
        else:
            link = link1 + 'start=' + str(page * limit) + '&limit=' + str(limit) + '&' + link2

        driver.get(link)
        comments = driver.find_elements_by_tag_name('div.comment')
        for comment in comments:
            span = comment.find_element_by_tag_name('span.comment-info')
            a = span.find_element_by_tag_name('a')
            span = comment.find_element_by_tag_name('span.short')
            dic[a.text] = span.text
        time.sleep(10)

    for key, value in dic.items():
        f.write(key + ' : ' + value + '\n\n')
        f.flush()

    dic.clear()

driver.quit()

