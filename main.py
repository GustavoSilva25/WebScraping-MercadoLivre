from bs4 import BeautifulSoup
from openpyxl import Workbook, worksheet
import requests
import os
from datetime import datetime


def search_product(product_name):
    url = f'https://lista.mercadolivre.com.br/{product_name}'
    

    response = requests.get(url)  
    print('estatus da resposta: ', response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    items = soup.find_all('div',class_='ui-search-result__wrapper')
    
    print(f'Quantidade de produtos encontrado: {len(items)}')
    for item in items:
        title = item.find('h2',class_='ui-search-item__title')
        price = item.find('span', class_='andes-money-amount__fraction')
        link = item.find('a', class_='ui-search-link')
        
        if title and price and link:
            products.append({
                'title' : title.text.strip(),
                'price' : price.text.strip(),
                'link' : link['href']
            })
        else:
            print('Elementos não encontrados: ',
                  'Nome' if  not title else '',
                  'Preço' if not price else '',
                  'Link' if not link else '')
            
    print(f'Produtos processados: {len(products)}')
    return products

def salve_in_excel(products, product_name):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Resultado da busca'
    
    #cabeçalho
    ws.append(['nome','preço','link'])
    
    for p in products:
        ws.append([
            p['title'],
            p['price'],
            p['link']
        ])
    date = datetime.now().strftime('%d%m%Y_%H%M%S')
    product_name = product_name.replace(' ','_')
    file = f'{product_name}_{date}.xlsx'
    wb.save(file)
    print(f'Resultado salvo em: {file}')
    
    
    
    

if __name__ == '__main__':
    print('Digite o nome do produto: ')
    product_name = input('>>') 
    
    products = search_product(product_name)
    salve_in_excel(products, product_name)
