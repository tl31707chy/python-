print(3+2)
print(3-2)
print(3*2)
print(4/2)
print(3**2)#平方
print(3**3)#立方
# 空格不影响Python计算表达式的方式，它们的存在旨在让你阅读代码时，能
# 迅速确定先执行哪些运算
print("\n")

print(3+0.1)
print(3-0.1)
print(3*0.1)
print(3/0.1)
print("\n")

age = 23
message = "Happy " + str(age) + "rd Birthday!"
#message = "Happy " + age + "rd Birthday!"  这样会报错  因为age=23里  age未标注字符类型   默认为字符串  所以是str（age）
print(message)
