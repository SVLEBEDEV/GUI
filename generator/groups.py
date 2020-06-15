from comtypes.client import CreateObject
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '\\groups.xlsx'
xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.open(project_dir)
i = 1
list_group = []
while xl.Range["A%s" % i].Value() is not None:
    list_group.append(xl.Range["A%s" % i].Value())
    i += 1
print(list_group)
xl.Quit()




#project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#xl = CreateObject("Excel.Application")
#xl.Visible = 1
#wb = xl.Workbooks.Add()
#for i in range(10):
#    xl.Range["A%s" % (i+1)].Value[()] = "group %s" % (i+1)
#wb.SaveAs(os.path.join(project_dir, 'groups.xlsx'))
#xl.Quit()