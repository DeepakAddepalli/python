import xlwt,xlrd

#xlrd.open_workbook("C:/Users/Administrator/Desktop/marks.csv").get_sheet(0).cell(0,0)
f=open("C:/Users/Administrator/Desktop/marks.csv","r")
wb= xlwt.Workbook()
ws = wb.add_sheet("boa")
for row,line in enumerate(f):
    for column,lin in enumerate(line.rstrip().split(",")):
       ws.write(row,column,lin)
wb.save("boa.xls")

for x in range(xlrd.open_workbook("boa.xls").sheet_by_name("boa").nrows):
    for y in range(xlrd.open_workbook("boa.xls").sheet_by_name("boa").ncols):
        print(xlrd.open_workbook("boa.xls").sheet_by_name("boa").cell(x,y))