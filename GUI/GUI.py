# coding=gbk
import easygui
# easygui.msgbox(msg='我今天去工地搬砖了',title='去工地的第一天',ok_button='明天继续去')

#多了一个选项为choices（只能容纳两个选项！）
# easygui.ccbox(msg='工地热吗',title='工地情况',choices=('热','不热'))

#多个选项
# a=easygui.buttonbox(msg='工地热吗',title='工地情况',choices=('热','不热','冷'))
# print(a)

# choicebox单选
# a=easygui.choicebox(msg='可以学习什么语言？',title='开发语言选择',choices=['java','python','C++'])
# print(a)

# multchoicebox多选
# a=easygui.multchoicebox(msg='可以学习什么语言？',title='开发语言选择',choices=['java','python','C++'])
# print(a)

#文本输入框  其中，default关键字定义的是文本框默认值，strip的值为True时会自动忽略输入的首尾空格，False则相反
# a=easygui.enterbox(msg='请输入第一个数：',title='加法运算题',default='63',strip=True)
# print(a)

#只能输入整型
# a=easygui.integerbox(msg='只能输入整型',title='整型测试',default='12',lowerbound=0,upperbound=99)
# print(a)

#其中values是输入的默认值、feilds是需要填写的条目名称，均用列表填写
# a=easygui.multenterbox(msg='测试系统登录',title='测试系统',fields=['用户名','密码'],values=[0,0])
# print(a)

#passwordbox()——密码输入框（不显示）
# a=easygui.passwordbox(msg='密码以“***”显示',title='不显示明文密码')
# print(a)

#模拟登录界面
a=easygui.multpasswordbox(msg='登录首页',title='测试系统',fields=['用户名','密码'])
print(a)