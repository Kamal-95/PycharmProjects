import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = "http://localhost:9090/job/GUS_Automation_Testing/ws/reports/reports.html"
auth = HTTPBasicAuth('jadmin', 'jpass@8080')
r = requests.get(url, headers=headers, auth=auth)



if r.status_code == 200:
    # print(r.text)
    soup = BeautifulSoup(r.text, "lxml")
    tag = soup
    print(tag)




else:
    print(f"Failed to fetch the HTML content. Status code: {r.status_code}")



