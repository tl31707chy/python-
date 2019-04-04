name1 = "ada lovelace"
print(name1.title())
# title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。这很有用，
# 因为你经常需要将名字视为信息。例如，你可能希望程序将值Ada、ADA和ada视为同一个名字，
# 并将它们都显示为Ada。
print("\n")

name2 = "Ada Lovelace"
print(name2.upper())
print(name2.lower())
# 将字符串改为全部大写或全部小写
print("\n")

first_name = "欢迎"
last_name = "光临"
full_name = first_name + "" + last_name
print(full_name)
print('hello,',full_name)
# 合并字符串
print("\n")

print("Languages:\nPython\nC\nJavaScript")
# 在字符串中添加换行符，可使用字符组合\n：
print("\n")

print("Languages:\n\tPython\n\tC\n\tJavaScript")
# 在同一个字符串中同时包含制表符和换行符。字符串"\n\t"让Python换到下一行，并在
# 下一行开头添加一个制表符。
print("\n")

favorite_language = 'python '
print(favorite_language)#打印出“python ”
print(favorite_language.rstrip())#打印出“python”
# 能够找出字符串开头和末尾多余的空白。可使用方法rstrip()
print("\n")

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)
#永久删除这个字符串中的空白
print("\n")

favorite_language = ' python '
print(favorite_language.rstrip())#末尾
print(favorite_language.lstrip())#开头
print(favorite_language.strip())#两端
# 分别删除末尾、开头和两端的空格

