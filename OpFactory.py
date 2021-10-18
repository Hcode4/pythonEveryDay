import SpliteColumn
import WriteExcel


def op_factory(filePath):
    opType = input("请输入操作类型: \n 1. 按照某一列数据切割多行\n")
    opType = int(opType)

    if opType == 1:
        a = input("输入需要按某一列分行的列数，从0开始计数\n")

        a = int(a)

        b = input("输入间隔方式，如,等 注意中英文\n")

        tables = SpliteColumn.read_excel(filePath, a, b)
        print('读取成功')

        WriteExcel.writeExcel(tables, filePath, len(tables), len(tables[0]))

        input('回车键退出 ')
        tables = SpliteColumn.read_excel(filePath, a, b)
        print('读取成功')
        WriteExcel.writeExcel(tables, filePath, len(tables), len(tables[0]))
