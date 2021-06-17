import gevent
from gevent import monkey,pool
monkey.patch_all()
from port_any_model import pythonAnyScan
#ip port:int

def go():
    gthread_pool = pool.Pool(10)
    threads = []
    assets_lsit = []
    for assets in open('target.txt','r'):
        assets_lsit.append(assets.strip())
    for id,asset in enumerate(assets_lsit):
        print('[*]scan_process: {:.0%}'.format(id / len(assets_lsit)),end='\r',flush=True)
        print('>>开始加载资产：{}'.format(asset))
        ip = asset.split(',')[0]
        port = asset.split(',')[1]
        g = gthread_pool.spawn(pythonAnyScan,ip,int(port))
        threads.append(g)
    gevent.joinall(threads)
if __name__ == '__main__':
    go()