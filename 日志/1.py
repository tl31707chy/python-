import xlrd
data = xlrd.open_workbook('D:\\圈子精选\\login-quit\\用户名密码.xlsx')
sheet = data.sheets()[0]
print(sheet.row_values())





