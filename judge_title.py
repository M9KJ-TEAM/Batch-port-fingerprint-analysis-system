import re
from urllib import request

def scan_title(addr):
    try:
        title_pattern = '<title>(.+)</title>'
        page = request.urlopen(addr)
        html = page.read().decode('utf-8')
        match = re.search(title_pattern,html)
        if match != None:
            # print(match.group().replace('<title>','').replace('</title>',''))
            return match.group().replace('<title>','').replace('</title>','')
        else:
            return None
    except UnicodeEncodeError as e:
        # print('>>Unicode 返回包编码识别错误错误：{}'.format(e))
        return None
    except Exception as e:
        # print('>>综合捕获器 ：{}'.format(e))
        return None

if __name__ == '__main__':
    scan_title('https://www.cnblogs.com/gqhwk/p/5364566.html')