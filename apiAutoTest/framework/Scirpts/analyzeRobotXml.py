# from robot.output import TestSuite
#
# def walk_testcase(suite):
# for test in suite.tests:
# yield test
# for sub_suite in suite.suites:
# for test in walk_testcase(sub_suite):
# yield test
# suite = TestSuite('output.xml')
# for test in walk_testcase(suite):
# print test.status, test.name
path1 = '0,1'
path2 = 'all,1'
path3 = 'all,all'
data = [('xF00000', 'aaa'), ('xF11111', 'bbb')]

pathlist = path1.split(",")
if pathlist[0] == 'all':
    print data[0][0]
    print data[1][1]
