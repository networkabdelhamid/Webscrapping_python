# this is a simple projet for web scrapping
# we extract the best prices for products in WWW.jumia.ma
# save the result in excelsheet
# The fisrt test with BeautifulSoupe4 library

from bs4 import BeautifulSoup
from csv import writer
import requests
print(" ")
print(18*"##"+"\t WEBSCRAPP with abdelhamid\t"+18*"##")
print(("\tResult: >>>"))
result = requests.get("https://www.jumia.ma/fashion-mode/")
print(result)
doc = BeautifulSoup(result.text, "html.parser")
product = doc.findAll(class_='itm col')
print(product)

# opennnig csv file
with open("product.csv","w") as file_csv:
    writer_file=writer(file_csv)
    headers=["name","prix","image"]
    for pro in product:
        product_name = pro.find(class_='name').get_text()
        price = pro.find(class_='prc').get_text()
        image_link = pro.find('img')['data-src']
        writer_file.writerow([product_name,price,image_link])













