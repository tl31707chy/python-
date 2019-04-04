import logging
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,  # 日志级别设置
        format="%(asctime)s  %(filename)s [line: %(lineno)d] %(levelname)s %(message)s",
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='mylog.log',
        filemode='w'
    )
    logging.debug(u'这是debug级别日志记录')
    logging.info(u'这是信息级别日志记录')
    logging.warning(u'这是警告级别日志记录')