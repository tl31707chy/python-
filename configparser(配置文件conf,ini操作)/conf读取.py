import configparser
#实例化
config = configparser.ConfigParser()
#读取.ini文件
config.read('D:\\TL\\configparser(配置文件conf,ini操作)\\conf.ini')

# -sections得到所有的section，并以列表的形式返回
print('sections:',config.sections())


# -options(section)得到该section的所有option(config为配置文件里的【】中的值，获取的结果为=号左侧的所有值)
print('options:' , config.options('test'))

# -items（section）得到该section的所有键值对
print('items:' ,config.items('Letter'))

# -get(section,option)得到section中option的值，返回为string类型
print('get:', config.get('test', 'hand'))


# -getint(section,option)得到section中的option的值，返回为int类型
print('getint:' ,config.getint('Letter', 'id'))
print('getfloat:' , config.getfloat('Letter', 'weight'))
print('getboolean:', config.getboolean('Letter', 'isChoice'))

#遍历出每个值
for sections in config.sections():
    for items in config.items(sections):
        print(items)



