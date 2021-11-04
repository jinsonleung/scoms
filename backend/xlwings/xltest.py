import time
import xlwings as xws
import random

'''
写入数据
'''
def xw_write():
    # 应用方法 创建应用-工作簿-工作表-范围
    # add_book属性表示操作excel时是否新增一个excel文件，默认为ture表示添加
    # 创建应用 visible操作过程是否显示
    app = xws.App(visible=False, add_book=False)
    # 工作簿
    wb = app.books.add()
    # 工作表(不能使用中文命名)
    sht = wb.sheets["sheet1"]
    # 范围（插入数据）options(transpose=True)竖着插入
    sht.range("a1").options(transpose=True) .value = ["xlwings", "hello", "world", "beauteful", "friend"]
    sht.range("b1").value = [[1, 2], [3, 4], [5, 6], [7, 8]]
    # 关闭excel 保存excel
    wb.save(r"d:\temp\demo01.xlsx")
    wb.close()
    app.quit()


'''
读取数据
'''
def xw_read():
    # 创建应用
    app = xws.App(visible=False, add_book=False)
    # 打开demo01数据表读取sheet1的数据
    wb = app.books.open(r"d:\temp\demo01.xlsx")
    sht = wb.sheets["sheet1"]
    # 读取A1到C5的数据
    print(sht.range("a1:c5").value)
    # 打开了就要关闭
    wb.close()
    app.quit()

'''
体温数据写入示例
'''

temperature_min = 36.4
temperature_max = 37.0
month = "8月"
day_min = 14
day_max = 30
# 可以写成具体的电脑路径（默认为py程序的目录生成）
file_name = r"d:\temp\demo2.xlsx"

'''
体温数据写入示例
'''
def sheet1():
    app = xws.App(visible=True, add_book=False)
    wb = app.books.add()
    sht = wb.sheets["sheet1"]
    sht.range("a1").value = ["日期", "早", "中", "晚"]
    lst = []
    for it in range(day_min, day_max):
        temp = month + str(it) + "日"
        lst.append(temp)
    sht.range("a2").options(transpose=True).value = lst

    lst.clear()
    for it in range(day_min, day_max):
        temp = random.uniform(temperature_min, temperature_max)
        lst.append(round(temp, 1))
    sht.range("b2").options(transpose=True).value = lst

    lst.clear()
    for it in range(day_min, day_max):
        temp = random.uniform(temperature_min, temperature_max)
        lst.append(round(temp, 1))
    sht.range("c2").options(transpose=True).value = lst

    lst.clear()
    for it in range(day_min, day_max):
        temp = random.uniform(temperature_min, temperature_max)
        lst.append(round(temp, 1))
    sht.range("d2").options(transpose=True).value = lst

    wb.save(file_name)
    wb.close()
    app.quit()



