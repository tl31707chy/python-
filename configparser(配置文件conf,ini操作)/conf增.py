import configparser
#实例化
config = configparser.ConfigParser()
#读取.ini文件
config.read('D:\\TL\\configparser(配置文件conf,ini操作)\\conf.ini')

list = []
list= config.sections()  # 获取到配置文件中所有分组名称
if 'type' not in list:  # 如果分组type不存在则插入type分组
    config.add_section('type')
    config.set('type', 'stuno', '10211201')  # 给type分组设置值
# config.set('type', 'stuno', '10211201')  # 给type分组设置值

o = open('D:\\TL\\configparser(配置文件conf,ini操作)\\conf.ini', 'w')
config.write(o)
o.close()  # 不要忘记关闭
