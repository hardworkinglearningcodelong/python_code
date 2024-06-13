import re
from datetime import datetime

def reg_search(text, regex_list):
    results = []
    for regex_dict in regex_list:
        item = {}
        for key, pattern in regex_dict.items():
            if key == '标的证券':
                # 匹配股票代码
                match = re.search(r'股票代码：(\S+)', text)
                if match:
                    item[key] = match.group(1)
            elif key == '换股期限':
                # 匹配日期范围
                match = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日)', text)
                if match:
                    dates = [datetime.strptime(m, '%Y年%m月%d日') for m in match.groups()]
                    # 将日期转换为YYYY-MM-DD格式
                    item[key] = [date.strftime('%Y-%m-%d') for date in dates]
        results.append(item)
    return results

text = '''
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束之日满12个月后的第一个交易日起至可交换债券到期日止，即2023年6月2日至2027年6月1日止。
'''

regex_list = [{
    '标的证券': '*自定义*',
    '换股期限': '*自定义*'
}]

print(reg_search(text, regex_list))
