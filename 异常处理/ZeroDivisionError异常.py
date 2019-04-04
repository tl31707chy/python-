# print(5/0)
try:#尝试执行  print(5/0)
    print(5/0)
except ZeroDivisionError: # 如果执行 print(5/0) 失败，就执行  print('分母不能为0')
    print('分母不能为0')

# 使用异常避免崩溃
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
  first_number = input("\nFirst number: ")
  if first_number == 'q':
     break
  second_number = input("Second number: ")
  if first_number == 'q':
     break
  try:
     answer = int(first_number) / int(second_number)
  except ZeroDivisionError:
      print("You can't divide by 0!")
  else:
     print(answer)

