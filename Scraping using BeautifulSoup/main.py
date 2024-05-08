import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bookswagon.com/promo/fiction-books/9D7S5K6U3M"
try:
    source = requests.get(url)
    # source.raise_for_status()
    soup = BeautifulSoup(source.text,'html.parser')
    titles = []
    authors = []
    costs = []
    offers = []
    results = soup.find_all("div",class_="col-6 col-sm-4 col-lg-2 text-right p-2 pat8block outerboxborder")
    for result in results:
        title = result.find("span",class_="booktitle font-weight-bold text-center")
        titles.append(title.text if title else "")
        author_span = result.find("span",class_="author authortextcolor d-block text-center mb-2")
        author = author_span.find("span")
        authors.append(author.text if author else "")
        cost_div = result.find_all("div",class_="text-center")
        cost = cost_div[1].find("span",class_="actualprice")
        costs.append(cost.text if cost else "")
        offer = result.find("div",class_="offer")
        offers.append(offer.text if offer else "")
        # print(cost)
        # print(len(cost_div))

    data = {
        'Book Title': titles,
        'Author': authors,
        'Price': costs,
        'Offer': offers
    }
    df =pd.DataFrame(data=data)
    df.to_csv('Books.csv',index=False)
    # print(result.prettify())
except Exception as e:
    print(e)
