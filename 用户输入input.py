
i=0
while i<3:
  i = i + 1
  ask = input('您好，请问您多少人就餐：')
  ask=int(ask)
  if ask%10==0 and ask<=20:#取余，判断输入数字是否未10的整数
     print('来客官请进有空座')
     break
  elif ask%10!=0 and ask<20:
     if i==1:
         print('不好意思，我们的桌子是10人桌和20人桌，我们只针对满座用户服务，请您们凑够人再来')
         print('欢迎再次光临')
     elif i==2:
         print('不好意思，我们的桌子是10人桌和20人桌，我们只针对满座用户服务，请您们凑够人再来')
         print('客官您都来两次了，请您们凑够人再来')
     elif i==3:
         print('都来了'+str(i)+'次了，人还不够，滚')

  elif ask>20:
     print('人太多gun')
     continue

