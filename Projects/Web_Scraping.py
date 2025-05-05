# The code is designed to scrape (collect) information
# about books from a website, store this data in a database,
# and then use machine learning to predict book prices
# based on certain features like page count and weight.


# This project was written around 2018.
# I apologize if, as a beginner student at the time,
# I didn't follow many programming principles and
# the code isn't very clean :)


import requests
from bs4 import BeautifulSoup
import re
from sklearn import tree
import mysql.connector

my_price = list()
my_name = list()
my_weight = list()
my_cover = list()
my_page = list()
print("Procesing...")
rep = requests.get("https://www.30book.com/Home/Search/8/0/%D9%BE%D8%B1%D9%81%D8%B1%D9%88%D8%B4%20%D9%87%D8%A7?checkQ=true&pageSize=100&sort=1&sortType=1&adName=&adWriter=&adInterpreter=&adPublisher=&adTs=&adTa=&adTf=&adC1=&adC2=&adPubY1=&adPubY2=&propT=")
soup = BeautifulSoup(rep.text, "html.parser")
p = soup.find_all("p", attrs={"class": "card-text price-discount font-13"})
n = soup.find_all("p", attrs={"class": "card-text font-12 box-name-h"})
inf = soup.find_all("a", attrs={"target": "_blank"})
for i in range(len(inf)):
    if (i > 5) and (i < 106):
        repElemID = inf[i].get('href')
        repElemID = "https://www.30book.com"+repElemID
        rep1 = requests.get(repElemID)
        soup1 = BeautifulSoup(rep1.text, "html.parser")
        info = soup1.find_all("table", attrs={"class": "table table-striped"})
        for x in range(len(info)):
            mybook = (re.sub(r"\s+", " ", info[x].text).strip()).split(" ")
            if x == 1:
                count1 = mybook.index("وزن")
                count2 = mybook.index("صفحه")
                count3 = mybook.index("جلد")
                safe = mybook[count2+1]
                if safe == "0":
                    continue
                else:
                    my_page.append(safe)
                    my-weight.append(mybook[count1+1])
                    my_cover.append(mybook[count3+2])
                    my_name.append(re.sub(r"\s+", " ", n[i-6].text).strip())
                    rial = re.sub(r"\s+", " ", p[i-6].text).strip()
                    count4 = rial.index(" ")
                    rial = rial[:count4]
                    rial1 = rial.replace(",", "")
                    my_price.append(rial1)

x1 = []
y1 = []
cnx = mysql.connector.connect(user='root', password='salehi82@I',
                              host='127.0.0.1',
                              database='book')
cursor = cnx.cursor()
cursor.execute("DELETE FROM mybook")
query = "SELECT * FROM mybook;"
for y in range(len(my_name)):
    cursor.execute("INSERT INTO mybook VALUES (\"%s\" , \"%s\" , \"%s\" , \"%s\" , \"%s\")" % (
        my_name[y], my_price[y], my_page[y], my-weight[y], my_cover[y]))
cursor.execute(query)
for g in cursor:
    kol = list(g)
    x1.append(kol[2:4])
    y1.append(kol[1])
clf = tree.DecisionTreeClassifier()
clf.fit(x1, y1)
x2 = int(input("NumPage: "))
x3 = int(input("Weight: "))
newdata = [[x2, x3]]
answer = clf.predict(newdata)
print(answer[0] + " Rial")
cnx.commit()
cnx.close()
