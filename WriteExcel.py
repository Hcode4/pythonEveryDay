import xlwt


def writeExcel(table, localPath, numberCount, numberRange):
    workbook = xlwt.Workbook(localPath)

    # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
    worksheet = workbook.add_sheet("deal")

    for columnIndex in range(numberCount):
        for rangeIndex in range(numberRange):
            worksheet.write(columnIndex, rangeIndex, table[columnIndex][rangeIndex])

    workbook.save(localPath)
    print("写入成功")
