import requests
import parsel
import csv

for page in range(1, 101):
    print(f'\n--------------page{page}--------------------')

    url = f'https://sz.lianjia.com/ershoufang/pg{page}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    response = requests.get(url=url, headers=headers)
    html_data = response.text

    selector = parsel.Selector(html_data)
    lis = selector.css('.clear.LOGCLICKDATA')

    for li in lis:
        title = li.css('.title a::text').get()
        totalPrice = li.css('.priceInfo .totalPrice span::text').get() + 'W'
        tags = li.css('.tag span::text').getall()
        unitPrice = li.css('.unitPrice  span::text').get()
        star = li.css('.followInfo::text').get()
        introduce = li.css('.houseInfo::text').get()
        address = li.css('.flood a::text').getall()
        address = '- '.join(address)
        tags = '|'.join(tags)

        # print(title,address,introduce,star,totalPrice,unitPrice,sep='\n--------------')

        with open('../lesson/HOUSE.csv', mode='a', encoding='UTF-8', newline='') as file:
            csv_w = csv.writer(file)
            csv_w.writerow([title, address, introduce, star, totalPrice, unitPrice])
