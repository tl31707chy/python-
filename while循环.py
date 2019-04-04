a= 1
while  a<= 5:
 print(a)
 a=a+1

while a!='否':
    print('------开始数字游戏-------')
    A=input('请输入数字A：')
    A=int(A)
    B=input('请输入数字B: ')
    B =int(B)
    C=A+B
    C =int(C)
    D=input('请输入两数之后：')
    D =int(D)
    if C==D:
        print('恭喜您回答正确')
        a=input('是否继续：')
    else:
        print('回答错误')
        a = input('是否继续：')


