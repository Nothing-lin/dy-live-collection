import logging
import threading
import config
from douyin import Douyin

if __name__ == '__main__':

    # 获取直播间地址
    urls = config.content['urls']  # 假设这里是一个包含多个URL的列表
    # 初始化日志
    logging.basicConfig(level=config.content['log']['level'], format=config.content['log']['format'])
    #初始化Douyin.gift_values的值
    Douyin.gift_values = Douyin.load_gift_values()

    threads = []
    for url in urls:
        thread = threading.Thread(target=Douyin.start_douyin_stream, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()  # 等待所有线程完成

