from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from csvwriter import write_to_csv
from bs4 import BeautifulSoup
from tqdm import tqdm

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_2"
driver.get(url)
driver.implicitly_wait(5)


soup = BeautifulSoup(driver.page_source, 'html.parser')
#print(soup)

res = soup.find_all(attrs={"data-asin": True})
data = []
links = []
names = []
prices = []
data = []
for i in tqdm(res, desc="Loading..."):
    asin = i["data-asin"]
    if asin:
        link = i.find_all(attrs={"href": True})
        name = i.find_all(attrs={"class": "a-size-medium a-color-base a-text-normal"})
        price = i.find_all(attrs={"class": "a-price-whole"})
        norev = i.find_all(attrs={"class": "a-size-base s-underline-text"})
        rating = i.find_all(attrs={"class": "a-section a-spacing-none a-spacing-top-micro"})
        for j in rating:
            k = j.find('span', attrs={"class": "a-size-base"})
            if link and name and price and norev and k:

                data.append({"asin":asin,
                             "name":name[0].text,
                             "link": ("amazon.in" + link[0]["href"]),
                             "price" : price[0].text,
                             "no_of_rating" : norev[0].text,
                             "rating" : k.text
                             })
print(data)
print(len(data))
res = write_to_csv(data)
print(res)
if res[0]:
    print("data added to csv file named: {}".format(res[1]))
else:
    print("some error occured, couldnt add to file")


