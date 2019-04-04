import re
# re.match函数
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# re.search方法
# re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配



a='14885ssdsdabc46545abcerwerabcsdfsd'
b='abc14885ssdsdabc46545abcerwerabsdfdsf'
c=re.findall(r'abc',a)
print(c)
#返回所有abc字符

d=re.findall(r'^abc',a)
e=re.findall(r'^abc',b)
print(d)
print(e)
# 判断字符串是否以abi开始的

f=re.findall(r'fsd$',a)
g=re.findall(r'xxx',b)
print(f)
print(g)
# 判断字符串是否以fsd结尾的

h='qawaeswdeasratf'
o=re.findall(r'[qwrt]a',h)
print(o)
# [...]的意思匹配括号内q和a，或者w和a，或者r和a,或者t和a的值返回列表

p='1we11r8dg4ert5we3ry2we65er'
q=re.findall(r'\d',p)
print(q)
# '\d'是正则语法规则用来匹配0到9之间的数返回列表,需要注意的是11会当成字符串'1'和'1'返回而不是返回'11'这个字符串

r='123asdww456wewqe14eqwe85'
s=re.findall(r'\d\d\d',r)
t=re.findall(r'\d\d',r)
print(s)
print(t)
# \d\d表示所去位数，一个\d表示一位

u=re.findall(r'\D',r)
print(u)
print('\n')
# 匹配除数字以外的数字

x='qwe984896sdww4445QW81EEFGTG'
y=re.findall(r'\w',x)
print(y)
# '\w'匹配从小写a到z，大写A到Z，数字0到9(将所有字母、数字匹配出来。备注：不是按顺序匹配)

aa='Q1a!@15weg7494TEF#$%^#.,/'
bb=re.findall(r'\W',aa)
print(bb)
# '\W'匹配除字母和数字以外的字符

cc='<div>hello<div><div>hello<div>'
dd=re.findall(r'<div>(.*)<div>',cc)
print(dd)
# 表示匹配括号内里面的内容，这里.*是正则贪婪匹配语法，就是最大范围的匹配准则

ee='<div>hello<div><div>hello<div>'
ff=re.findall(r'<div>(.*?)<div>',ee)
print(ff)
# 非贪婪模式


aaa='<div>hello<div>'
bbb=re.findall(r'<div>(HElLO)<div>',aaa)
ccc=re.findall(r'<div>(HElLO)<div>',aaa,re.I)
print(bbb)
print(ccc)
# re.I(大写的i)表示匹配时不区分大小写

xx='<div>hello\nHELLO<div>'
yy=re.findall(r'<div>(.*)<div>',xx,re.I)
zz=re.findall(r'<div>(.*)<div>',xx,re.I|re.S)
print(yy)
print(zz)
# re.S(大写)这样代表比匹配包括换行符在内的所有字符





