import logging
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,  # 日志级别设置
        format="%(asctime)s  %(filename)s [line: %(lineno)d] %(levelname)s %(message)s",
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='mylog.log',
        filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.debug(u"这是debug日志记录")
    logging.info(u'这是info日志记录')
    logging.warning(u'这是warning日志记录')
#将日志信息打印在控制台
