# -*- coding: utf-8 -*-
import xlrd
import copy


def read_excel(excelPath, splitCols, splitePattern):
    tables = []
    # 打开文件
    workbook = xlrd.open_workbook(excelPath)
    # sheet索引从0开始
    sheet = workbook.sheet_by_index(0)

    for rown in range(sheet.nrows):
        array = [""] * sheet.ncols
        for ncol in range(sheet.ncols):
            array[ncol] = sheet.cell_value(rown, ncol)

        if splitCols != -1 and splitCols < sheet.ncols and array[splitCols].find(splitePattern) > 0:

            arraySplit = array[splitCols].split(",")
            for spliteIndex in range(len(arraySplit)):
                arrayCopy = copy.copy(array)
                arrayCopy[splitCols] = arraySplit[spliteIndex]
                tables.append(arrayCopy)

        else:
            tables.append(array)

    return tables
