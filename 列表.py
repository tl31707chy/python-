bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[-1])
print(bicycles[-2])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print('\n')

motorcycles1 = ['honda', 'yamaha', 'suzuki']
print(motorcycles1)
motorcycles1[0] = 'ducati'
print(motorcycles1)
# 修改列表中的值
print('\n')

motorcycles2 = ['honda', 'yamaha', 'suzuki']
motorcycles2.append('ducati')
print(motorcycles2)
# 在末尾增加列表中的值
print('\n')

motorcycles3 = ['honda', 'yamaha', 'suzuki']
motorcycles3.insert(0, 'ducati')#0是索引  插入到开头
print(motorcycles3)
# 任意插入
print('\n')

motorcycles4 = ['honda', 'yamaha', 'suzuki']
print(motorcycles4)
del motorcycles4[0]
print(motorcycles4)
# 删除列表中的值
print('\n')

motorcycles5 = ['honda', 'yamaha', 'suzuki']
print(motorcycles5)
popped_motorcycle = motorcycles5.pop()
print(motorcycles5)
print(popped_motorcycle)
# 方法pop()可删除列表末尾的元素，并让你能够接着使用它。
print('\n')

motorcycles6 = ['honda', 'yamaha', 'suzuki']
print(motorcycles6)
popped_motorcycle1 = motorcycles6.pop(1)
print(motorcycles6)
print(popped_motorcycle1)
# 方法pop()可删除列表任意元素，并让你能够接着使用它。
print('\n')

motorcycles10 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles10)
motorcycles10.remove('suzuki')
print(motorcycles10)
# 不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()。
print('\n')

motorcycles11 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles11)
too_expensive = 'ducati'
motorcycles11.remove(too_expensive)
print(motorcycles11)
print("\nA " + too_expensive.title() + " is too expensive for me.")
# 使用remove()从列表中删除元素时，也可接着使用它的值。
print('\n')

cars1 = ['bmw', 'audi', 'toyota', 'subaru']
cars1.sort()
print(cars1)
#列表里的值按字母顺序正向排序,无法恢复到原来的排列顺序：

cars2 = ['bmw', 'audi', 'toyota', 'subaru']
cars2.sort(reverse=True)
print(cars2)
#列表里的值按字母顺序反向排序,无法恢复到原来的排列顺序：
print('\n')

cars3 = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars3)
print("\nHere is the sorted list:")
print(sorted(cars3))
print("\nHere is the original list again:")
print(cars3)
# 可以恢复到原来的排列顺序：
print('\n')

cars4 = ['bmw', 'audi', 'toyota', 'subaru']
print(cars4)
cars4.reverse()
print(cars4)
#倒序打印列表
print('\n')

cars5 = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars5))
# 确认列表里有几个值

magicians1 = ['alice', 'david', 'carolina']
for magician in magicians1:
    print(magician)
# 遍历数据一个一个的取出来
print('\n')

magicians2 = ['alice', 'david', 'carolina']
for magician in magicians2:
   print(magician.title() + ", that was a great trick!")
print('\n')

for value in range(1,5):
   print(value)
print('\n')

numbers = list(range(1,6))
print(numbers)
#创建列表
print('\n')

even_numbers = list(range(2,11,2))
print(even_numbers)
#函数range()从2开始数，然后不断地加2，直到达到或超过终值（11）
print('\n')

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
# 对数字列表执行简单的统计计算
print('\n')

squares = [value**2 for value in range(1,11)]
print(squares)
#使用列表解析创建你在前面看到的平方数列表
print('\n')

players1 = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players1[0:3])
#打印该列表的一个切片，其中只包含三名队员。输出也是一个列表，其中包含前三名队员
players2 = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players2[1:4])
##打印该列表的一个切片，打印出2-4
players3 = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players3[:4])
#没有指定第一个索引，Python将自动从列表开头开始

players4 = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players4[2:])
#提取从第3个元素到列表末尾的所有元素，可将起始索引指定为2

players4 = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players4[-3:])
# 将返回从第3个元素到列表末尾的所有元素
print('\n')

players10 = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players10[:3]:
    print(player.title())
# 遍历切片
print('\n')


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#复制列表
print('\n')

my_foods1 = ['pizza', 'falafel', 'carrot cake']
friend_foods1 = my_foods[:]
friend_foods1.append('ice cream')
print(my_foods)
print(friend_foods)


# 1.可以增加列表内容     append
# 2.可以统计某个列表段在整个列表中出现的次数 count
# 3.可以插入一个字符串，并把整个字符串的每个字母拆分当作一个列表段追加到列表当中 extedn
# 4.可以查询某个列表段在整个列表的位置 index
# 5.可以在指定位置插入一个列表段 insert
# 6.可以删除列表的最后一个列表段 pop
# 7.可以删除指定列表中的某个列表段 remove
# 8.可以正向反向排序 reverse
# 9.可以按字母或数字排序 sort
# 10.定义列表时候使用中括号"[]"