from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse

def first_page(request):
    response = requests.get('<https://quotes.toscrape.com/>')
    soup = BeautifulSoup(response.text, 'html.parser')
    quote = soup.find('span', class_ = 'text')
    return HttpResponse(quote.text)