from judge_port import scan_port
# need -> ipaddr,port
from judge_ssl import scan_ssl
# need -> url for example blog.aq-sec.com
from judge_title import scan_title
# need -> addr for example http://blog.aq-sec.com
from judge_fingerprint import scan_finger
# need -> ipaddr,port
import time,gevent

#公共变量
nowtime = time.strftime('%Y-%m-%d %H:%M:%S')

def pythonAnyScan(ip,port):
    with gevent.Timeout(70, False) as timeout:
        print('[√] 开始判断 ~')
        if scan_port(ip,port) == True:
            portstatus = 'open'
            fingerResult = scan_finger(ip,port)
            fingerstatus = fingerResult
            sslscan = scan_ssl('{}:{}'.format(ip,str(port)))
            if sslscan != None:
                if 443 in sslscan:
                    httpstatus = 'HTTPS'
                    target_URl = 'https://' + '{}:{}'.format(ip,str(port))
                    title = scan_title(target_URl)
                    if title !=None:
                        httptitle = title
                    else:
                        httptitle = title
                elif 80 in sslscan:
                    httpstatus = 'HTTP'
                    target_URl = 'https://' + '{}:{}'.format(ip,str(port))
                    title = scan_title(target_URl)
                    if title !=None:
                        httptitle = title
                    else:
                        httptitle = title
                else:
                    httptitle = 'NULL'
            else:
                httpstatus =  'TCP'
                httptitle = 'NULL'
        else:
            portstatus = 'close'
            httpstatus = 'NULL'
            fingerstatus = 'NULL'
            httptitle = 'NULL'
        print('[√] 判断完毕 ~')
        with open('result_自动化指纹识别系统.csv','a+',encoding='UTF-8') as f:
            f.write('{}，{}，{}，{}，{}，{}，{}'.format(ip,port,nowtime,portstatus,httpstatus,
            fingerstatus,httptitle))
            f.write('\n')
            f.close()
if __name__ == '__main__':
    pythonAnyScan('127.0.0.1',8188)