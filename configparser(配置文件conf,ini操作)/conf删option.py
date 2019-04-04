import configparser
#实例化
config = configparser.ConfigParser()
#读取.ini文件
config.read('D:\\TL\\configparser(配置文件conf,ini操作)\\conf.ini')

config.remove_option('type', 'stuno')  # 删除type分组的stuno
o = open('D:\\TL\\configparser(配置文件conf,ini操作)\\conf.ini', 'w')
config.write(o)
o.close()  # 不要忘记关闭