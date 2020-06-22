import requests
from bs4 import BeautifulSoup
import csv

res = requests.get("https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup = BeautifulSoup(res.text, 'html.parser')

brands = soup.select("._3wU53n")
prices = soup.select("._2rQ-NK")
others = soup.select(".vFw0gD")

def write_to_csv(mobile):
    for mob in mobile:
        mobile_name = mob['mobile_name']
        price = mob['price']
        ram = mob['ram']
        battery = mob['battery']
        with open("database.csv", mode='a', encoding="utf-8", newline='') as database:
            csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([mobile_name,price,ram,battery])

def custom_mobile_list(brands, prices, others):
    mobile = []
    for idx, brand in enumerate(brands):
        name = brand.getText()
        price = str(prices[idx].getText().replace('₹', ''))
        other = others[idx]
        children = other.findChildren("li", recursive=False)
        ram = children[0].getText()
        battery = children[3].getText()

        mobile.append({"mobile_name":name, "price":price, "ram":ram, "battery":battery})

    return write_to_csv(mobile)    

custom_mobile_list(brands, prices, others)



