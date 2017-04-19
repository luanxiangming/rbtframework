import re
import sys
from robot.api import logger
from robot.libraries import BuiltIn

# a= "[(123, 123, '-89--91---9--9--12312--09-')]"
# # a=sys.argv[1]
# print eval(a)
# logger.info("A is :" + a)
# b = eval(a)[0]
# print b
# # b = a.split(",")
# # b = ''.join(a)
# # print isinstance(a,)
# for e in b:
#     if str(e).find("--")!=-1:
#             b = (e.replace("--",",").replace("-","")).split(",")
#             # print (b[0]).split(",")
#             c =  [int(b) for b in b if b]
#             c.sort()
#             print c

path1 = '0,1'
path2 = 'all,1'
path3 = 'all,all'
data = [('xF00000', 'aaa'), ('xF11111', 'bbb')]
if ~True:
    print 1
pathlist = path1.split(",")
if pathlist[0] == 'all':
    print data[0][0]
    print data[1][1]



# if __name__ == "__main__":
#     a = "-9--8-"
#     run = BuiltIn
#     run._Converter.convert_to_number(1.25,1)
