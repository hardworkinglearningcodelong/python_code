import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
response = requests.get(url, headers={'User-Agent':
                                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

# 检查HTML内容中是否存在表格
tables = soup.find_all('table',{'class','san-sheet-alternating'})
if tables:
    # 尝试使用pandas读取找到的表格
    df = pd.read_html(str(tables[0]))[0]
    print(df)
else:
    print("No tables .")

# 过滤条件:债券类型为国债,发行年份为2023
mask = (tables['Bond Type'] == 'Treasury Bond') & (tables['Issue Year'] == 2023)
table = tables[mask]
# 选择需要的列
cols = ['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating']
table = table[cols]
# 因为有多余列,重新设置列顺序和列名
table = table[['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating']]
# 保存为CSV文件
table.to_csv('chinamoney_bonds_2023.csv', index=False)