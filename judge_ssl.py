import requests
from urllib3 import disable_warnings
disable_warnings()

def scan_ssl(url):
    status_value = []
    try:
        req_http = requests.get(url='http://' + url)
        res_http = req_http.status_code
        status_value.append(80)
    except Exception as e:
        # print(e)
        pass
    try:
        req_https = requests.get(url='https://' + url,verify=False)
        res_https = req_https.status_code
        status_value.append(443)
    except Exception as e:
        # print(e)
        pass
    if len(status_value) == 0:
        # print('{}非HTTP协议'.format(url))
        return None
    else:
        # print('{}'.format(status_value))
        return status_value

if __name__ == '__main__':
    scan_ssl('ip:6060')