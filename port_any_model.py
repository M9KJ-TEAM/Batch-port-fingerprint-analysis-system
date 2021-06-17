from judge_port import scan_port
# need -> ipaddr,port
from judge_ssl import scan_ssl
# need -> url for example blog.aq-sec.com
from judge_title import scan_title
# need -> addr for example http://blog.aq-sec.com
from judge_fingerprint import scan_finger
# need -> ipaddr,port
import time

#公共变量
nowtime = time.strftime('%Y-%m-%d %H:%M:%S')

def pythonAnyScan(ip,port):
    print('[√] 开始判断 ~')
    if scan_port(ip,port) == True:
        portstatus = '[0]√！ 端口开启'
        fingerResult = scan_finger(ip,port)
        fingerstatus = '[GET]:指纹获取结果->{}'.format(fingerResult)
        sslscan = scan_ssl('{}:{}'.format(ip,str(port)))
        if sslscan != None:
            httpstatus = '[1]√！ 是HTTP资产'
            if 443 in sslscan:
                target_URl = 'https://' + '{}:{}'.format(ip,str(port))
                title = scan_title(target_URl)
                if title !=None:
                    httptitle = '[GET]:标题获取结果->{}'.format(title)
                else:
                    httptitle = '[2]×！ 标题识别失败'.format(title)
            elif 80 in sslscan:
                target_URl = 'https://' + '{}:{}'.format(ip,str(port))
                title = scan_title(target_URl)
                if title !=None:
                    httptitle = '[GET]:标题获取结果->{}'.format(title)
                else:
                    httptitle = '[2]×！ 标题识别失败'.format(title)
            else:
                httptitle = 'NULL'
        else:
            httpstatus =  '[1]×！ 非HTTP资产'
            httptitle = 'NULL'
    else:
        portstatus = '[0]×！ 端口关闭'
        httpstatus = 'NULL'
        fingerstatus = 'NULL'
        httptitle = 'NULL'
    print('[√] 判断完毕 ~')
    with open('result_自动化指纹识别系统.csv','a+') as f:
        f.write('{}，{}，{}，{}，{}'.format(nowtime,portstatus,httpstatus,
        fingerstatus,httptitle))
        f.write('\n')
        f.close()
if __name__ == '__main__':
    pythonAnyScan('127.0.0.1',8188)