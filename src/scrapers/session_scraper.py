import requests

def scrape_with_session():
    session = requests.Session()

    set_cookie_url = "https://httpbin.org/cookies/set?session=123456"
    session.get(set_cookie_url)

    check_cookie_url = "https://httpbin.org/cookies"
    response = session.get(check_cookie_url)

    print("🍪 Cookies received from server:")
    print(response.json()) 

if __name__ == "__main__":
    scrape_with_session()
