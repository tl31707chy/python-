dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 为元组添加值 会报错
#元组的元素是不可变的，元组的元素的元素是可变的
# 1.可以统计某个元组段在整个元组中出现的次数    count
# # 2.可以查询某个元组段在整个元组中的元组号    index
# # 3.定义元组时候使用小括号"()
print('\n')
for dimension in dimensions:
 print(dimension)
 #遍历元组
 print('\n')

a = (200, 50)
print("Original dimensions:")
for b in a:
     print(b)
a = (400, 100)
print("\nModified dimensions:")
for b in a:
    print(b)
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，
# 可重新定义整个元组,因为给元组变量赋值是合法的：

