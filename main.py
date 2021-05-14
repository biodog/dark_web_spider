import json
from handle_login import session, base_url
from scrapy import Selector


def parse_html(html):
    select = Selector(text=html)
    table = select.css('table.u_ea_a')
    trs = table.xpath('./tr')[1::2][1:-1]
    with open('./result.txt', 'a', encoding='utf8') as f:
        for tr in trs:
            item = {
                "time": tr.xpath('./td[2]/text()').get(),
                "title": tr.xpath('.//a/text()').get(),
                "url": base_url + tr.xpath('.//a/@href').get()
            }
            item['tid'] = item['url'].split('=')[-1]
            f.write(json.dumps(item, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    page_num = 287
    url_list = [base_url + 'ea.php?ea=10001&pagea=%s' % str(i + 1) for i in range(page_num)]
    for url in url_list:
        print(url)
        html = session.get(url).text
        parse_html(html)
