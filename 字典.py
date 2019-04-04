alien_0 = {'color': 'green', 'points': 5}
#color和points为键，points和5为值，color-green键值对
#字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之
# 相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
# 上述代码首先定义了一个字典，然后从这个字典中获取与键'points'相关联的值
# 并将这个值存储在变量new_points中。接下来，将这个整数转换为字符串，并打印一条消息


print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 添加键—值对

a={}
a['name']='张三'
a['age']=24
a['sex']='男'
print(a)
#创建字典

a['name']='李四'
print(a)
#修改字典中的值

del a['sex']
print(a)
#删除键值对

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
   print("\nKey: " + key)
   print("Value: " + value)
# 遍历所有的键—值对
print('\n')

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
    'apl':'dfgdgfd'
 }
for name in favorite_languages.keys():
   print(name.title())#此处title将首写字母大写
# 遍历字典中的所有键（无序）
print('\n')

for name in sorted(favorite_languages.keys()):
    print(name.title())
# 遍历字典中的所有键（按字母排序）
print('\n')

for language in favorite_languages.values():
  print(language.title())
# 遍历字典中的所有值(有重复）
print('\n')

for language in set(favorite_languages.values()):
 print(language.title())
 ## 遍历字典中的所有值(去重复）

 alien_0 = {'color': 'green', 'points': 5}
 alien_1 = {'color': 'yellow', 'points': 10}
 alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
   print(alien)
print('\n')

# 更符合现实的情形是，外星人不止三个，且每个外星人都是使用代码自动生成的。在下面的
# 示例中，我们使用range()生成了30个外星人：

# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
   aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
  print(alien)
  print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
print('\n')

# 在什么情况下需要处理成群结队的外星人呢？想象一下，可能随着游戏的进行，有些外星人
# 会变色且移动速度会加快。必要时，我们可以使用for循环和if语句来修改某些外星人的颜色。
# 例如，要将前三个外星人修改为黄色的、速度为中等且值10个点，可以这样做：
for alien in aliens[0:3]:
 if alien['color'] == 'green':
   alien['color'] = 'yellow'
   alien['speed'] = 'medium'
for alien in aliens[:5]:
  print(alien)
  print("...")


