
import requests
from bs4 import BeautifulSoup
# https://movie.douban.com/subject/30444960/comments?                  sort=new_score&status=F
# https://movie.douban.com/subject/30444960/comments?start=20&limit=20&sort=new_score&status=F
# https://movie.douban.com/subject/30444960/comments?start=40&limit=20&sort=new_score&status=F

list_comment = []


def main():

    link1 = 'https://movie.douban.com/subject/30444960/comments?'
    link2 = 'sort=new_score&status=F'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

    for start in range(0, 30):

        if start == 0:
            link = link1 + link2
        else:
            link = link1 + 'start=' + \
                str(20 * start) + '&limit=' + str(start * 20) + '&' + link2

        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.findAll('div', class_='comment')
        for div in div_list:
            comment = div.p.span.text.strip()
            list_comment.append(comment)

    print('listcount:' + str(len(list_comment)))


main()
with open('result.txt', 'w+' ,encoding='utf-8') as f:
    for comment in list_comment:
        f.write(comment + '\n')
