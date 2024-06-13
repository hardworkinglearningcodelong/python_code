import requests
from bs4 import BeautifulSoup
import pandas as pd
import time,os
ef init_csv():
    """初始化CSV文件，仅在文件不存在时写入列名"""
    if not os.path.exists('tianqi.csv'):
        pd.DataFrame(columns=['ISIN', 'Bond_code', 'Issuer', 'Bond_Type']).to_csv('shuju.csv', index=False)
def get_html(url,data):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers, params=data)
    return response.json()['data']['resultList']

def get_json(json_data):
    for data in json_data:
        ISIN = data['isin']
        Bond_code = data['bondCode']
        Issuer = data['entyFullName']
        Bond_Type = data['bondType']
        df = pd.DataFrame({
            'ISIN': [ISIN],
            'Bond_code': [Bond_code],
            'Issuer': [Issuer],
            'Bond_Type':[Bond_Type]
        })
        df.to_csv('shuju.csv', mode='a', header=False, index=False)
if __name__ == '__main__':
    for a in range(1, 9):
        url = 'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN'
        data = {
            'pageNo': a,
            'pageSize': 15,
            'isin': '',
            'bondCode': '',
            'issueEnty': '',
            'bondType': 100001,
            'couponType': '',
            'issueYear': 2023,
            'rtngShrt': '',
            'bondSpclPrjctVrty': ''
        }
        html = get_html(url, data)
        get_json(html)
        # print(f'正在爬取第{a}页')
