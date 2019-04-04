#定义函数
def greet_user():
   """显示简单的问候语"""
   print("Hello!")
greet_user()

# 向函数传递信息
def greet_user(username):
  """显示简单的问候语"""
  print("Hello, " + username.title() + "!")
greet_user('jesse')
# 实参和形参
# 在函数greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信息。
# 在代码greet_user('jesse')中，值'jesse'是一个实参。实参是调用函数时传递给函数的信息。
# 我们调用函数时，将要让函数使用的信息放在括号内。在greet_user('jesse')中，将实参
# 'jesse'传递给了函数greet_user()，这个值被存储在形参username中。
print('\n')

# 调用函数多次
def describe_pet(animal_type, pet_name):
 """显示宠物的信息"""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
print('\n')

# 关键字实参是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆
# 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
def describe_pet(animal_type, pet_name):
 """显示宠物的信息"""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

# 传入默认值
def describe_pet(pet_name, animal_type='dog'):
 """显示宠物的信息"""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 describe_pet(pet_name='willie')
print('\n')

# 让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
     """返回整洁的姓名"""
     full_name = first_name + ' ' + middle_name + ' ' + last_name
     return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
print('\n')

#返回字典
def build_person(first_name, last_name, age=''):
 """返回一个字典，其中包含有关一个人的信息"""
 person = {'first': first_name, 'last': last_name}
 if age:
   person['age'] = age
 return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

