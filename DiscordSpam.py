import requests
import time

url = ""
#url = "Sohbet URL'si"


mesaj = {'content': ":confused: "}
#mesaj = {'content': ":confused: Girilecek MEsaj "}


token = {'authorization': ''}
#token = {'authorization': 'Discord Token'}


while True:
    requests.post(url, headers=token, data=mesaj)
    time.sleep(0.5)