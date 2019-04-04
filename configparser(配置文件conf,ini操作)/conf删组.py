import configparser
#实例化
config = configparser.ConfigParser()
#读取.ini文件
config.read('D:\\TL\\configparser(配置文件conf,ini操作)\\conf.ini')

config.remove_section('type') # 删除配置文件中type分组
o = open('D:\\TL\\configparser(配置文件conf,ini操作)\\conf.ini', 'w')
config.write(o)
o.close()  # 不要忘记关闭