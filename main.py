import requests
from bs4 import BeautifulSoup
import csv
from model import Product

def pars(url:str,max_item:int):
    create_csv()
    page = 1
    count_it = 0
    while max_item > count_it:
        list_product = []
        res = requests.get(f"{url};{page}")
        soup = BeautifulSoup(res.text, "lxml")
        products = soup.find_all("div", class_="l-GwW js-productad")



        for product in products:
            if count_it >= max_item:
                break
            count_it += 1
            title = product.find("span",class_="_3Trjq htldP _7NHpZ h97_n").text
            print(title)
            price = product.find("span",class_="yzKb6").text
            print(price)
            list_product.append(Product(title=title,
                                        price=price))
    write_csv(list_product)



def create_csv():
    with open("glavsnab.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "price"])

def write_csv(products: list[Product]):
    with open("glavsnab.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([product.title, product.price])


if __name__ == "__main__":
    pars(url="https://prom.ua/ua/Sportivnye-kepki",max_item=50)
