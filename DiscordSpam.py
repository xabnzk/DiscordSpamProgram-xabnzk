import requests
import time

sure = float(input("Süre =>"))
url2 = input("Sohbet URL'si =>")
token2 = input("Discord Token =>")
mesaj2 = input("Gönderilecek Mesaj =>")

#url = "Sohbet URL'si"


mesaj = {'content': mesaj2}
#mesaj = {'content': ":confused: Girilecek MEsaj "}


token = {'authorization': token2}
#token = {'authorization': 'Discord Token'}


while True:
    requests.post(url2, headers=token, data=mesaj)
    time.sleep(sure)