
#coding: utf-8
import socket
import socks
import time
import requests

from stem.control import Controller
from stem import Signal

proxies = {
    'http':'127.0.0.1:9050'
}

controller = Controller.from_port(port=9051)

def proxy_init():
    global controller
    controller.authenticate()
    socks.setdefaultproxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket


def renew_ip():
    controller.authenticate()
    controller.signal(Signal.NEWNYM)
    controller.close()

def get_self_ip():
    #socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    #socket.socket = socks.socksocket
    #renew_ip()
    pass



proxy_init()
renew_ip()
print(requests.get('http://icanhazip.com', proxies).text)


