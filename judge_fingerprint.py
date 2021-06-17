import nmap


def scan_finger(ipaddr,port):
    """
    nmap -p 31000 -T4 -A -v 114.55.248.124
    """
    port = str(port)
    nm = nmap.PortScanner()
    scan_port_finger_results = nm.scan(ipaddr, port, '-T5 -O -sS -sU')
    # print(scan_port_finger_results)
    #获取端口状态
    port2 = int(port)
    if scan_port_finger_results['scan'] == {}:
        return 'Nmap识别失败！'
    else:
        tcp_status = scan_port_finger_results['scan'][ipaddr]['tcp'][port2]['state']
        tcp_name = scan_port_finger_results['scan'][ipaddr]['tcp'][port2]['name']
        tcp_product = scan_port_finger_results['scan'][ipaddr]['tcp'][port2]['product']
        tcp_version = scan_port_finger_results['scan'][ipaddr]['tcp'][port2]['version']
        tcp_extrainfo = scan_port_finger_results['scan'][ipaddr]['tcp'][port2]['extrainfo']
        udp_status = scan_port_finger_results['scan'][ipaddr]['udp'][port2]['state']
        udp_name = scan_port_finger_results['scan'][ipaddr]['udp'][port2]['name']
        udp_product = scan_port_finger_results['scan'][ipaddr]['udp'][port2]['product']
        udp_version = scan_port_finger_results['scan'][ipaddr]['udp'][port2]['version']
        udp_extrainfo = scan_port_finger_results['scan'][ipaddr]['udp'][port2]['extrainfo']
        #获取主机信息
        os_name = scan_port_finger_results['scan'][ipaddr]['osmatch'][0]['name']
        # print('端口状态：tcp>{},udp>{}，端口名字：tcp>{},udp>{}，端口指纹：tcp>{},udp>{}，端口版本：tcp>{},udp>{}，扩展版本：tcp>{},udp>{}，系统可能版本：{}'
        #       .format(tcp_status,udp_status,tcp_name,udp_name,tcp_product,udp_product,tcp_version,udp_version,tcp_extrainfo,
        #               udp_extrainfo,os_name))
        return_str = '端口状态：tcp>{},udp>{}，端口名字：tcp>{},udp>{}，端口指纹：tcp>{},udp>{}，端口版本：tcp>{},udp>{}，扩展版本：tcp>{},udp>{}，系统可能版本：{}'.format(tcp_status,udp_status,tcp_name,udp_name,tcp_product,udp_product,tcp_version,udp_version,tcp_extrainfo,
                      udp_extrainfo,os_name)
        print('指纹识别结果：{}'.format(return_str))
        return return_str

if __name__ == '__main__':
    scan_finger('127.0.0.1',8188)