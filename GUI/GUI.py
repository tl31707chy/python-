# coding=gbk
import easygui
# easygui.msgbox(msg='�ҽ���ȥ���ذ�ש��',title='ȥ���صĵ�һ��',ok_button='�������ȥ')

#����һ��ѡ��Ϊchoices��ֻ����������ѡ���
# easygui.ccbox(msg='��������',title='�������',choices=('��','����'))

#���ѡ��
# a=easygui.buttonbox(msg='��������',title='�������',choices=('��','����','��'))
# print(a)

# choicebox��ѡ
# a=easygui.choicebox(msg='����ѧϰʲô���ԣ�',title='��������ѡ��',choices=['java','python','C++'])
# print(a)

# multchoicebox��ѡ
# a=easygui.multchoicebox(msg='����ѧϰʲô���ԣ�',title='��������ѡ��',choices=['java','python','C++'])
# print(a)

#�ı������  ���У�default�ؼ��ֶ�������ı���Ĭ��ֵ��strip��ֵΪTrueʱ���Զ������������β�ո�False���෴
# a=easygui.enterbox(msg='�������һ������',title='�ӷ�������',default='63',strip=True)
# print(a)

#ֻ����������
# a=easygui.integerbox(msg='ֻ����������',title='���Ͳ���',default='12',lowerbound=0,upperbound=99)
# print(a)

#����values�������Ĭ��ֵ��feilds����Ҫ��д����Ŀ���ƣ������б���д
# a=easygui.multenterbox(msg='����ϵͳ��¼',title='����ϵͳ',fields=['�û���','����'],values=[0,0])
# print(a)

#passwordbox()������������򣨲���ʾ��
# a=easygui.passwordbox(msg='�����ԡ�***����ʾ',title='����ʾ��������')
# print(a)

#ģ���¼����
a=easygui.multpasswordbox(msg='��¼��ҳ',title='����ϵͳ',fields=['�û���','����'])
print(a)