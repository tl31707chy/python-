cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
   print(car.upper())
  else:
    print(car.title())
# 这个示例中的循环首先检查当前的汽车名是否是'bmw'。如果是，就以全大写的方式
# 打印它；否则就以首字母大写的方式打印：
print('\n')

# if-elif-else
# 在现实世界中，很多情况下需要考虑的情形都超过两个。例如，来看一个根据年龄段收费的游乐场：
#  4岁以下免费；
#  4~18岁收费5美元；
#  18岁（含）以上收费10美元。
age = 20
if age < 4:
  print("Your admission cost is $0.")
elif age < 18:
  print("Your admission cost is $5.")
else:
  print("Your admission cost is $10.")
print('\n')

# 使用多个 elif
# 例如，假设前述游乐场要给老年人打折，可再添加
# 一个条件测试，判断顾客是否符合打折条件。下面假设对于65岁（含）以上的老人，可以半价（即5美元）购买门票：
age = 12
if age < 4:
   price = 0
   print(price)
elif age < 18:
   price = 5
   print(price)
elif age < 65:
   price = 10
   print(price)
else:
   price = 5
   print(price)

print('\n')


# 省略 else 代码块
# Python并不要求if-elif结构后面必须有else代码块。在有些情况下，else代码块很有用；而
# 在其他一些情况下，使用一条elif语句来处理特定的情形更清晰
age = 80
if age < 4:
   price = 0
   print(price)
elif age < 18:
   price = 5
   print(price)
elif age < 65:
   price = 10
   print(price)
elif age>65:
   price = 5
   print(price)

print('\n')