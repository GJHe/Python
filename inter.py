#_*_coding:utf-8_*_
#Author：ymxowgk

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

"""单行注释需要在注释所在行前面加 # """

#多行注释采用
#        '''需要注释的内容'''
#        或者
#        """需要注释的内容"""

info = '''
    ----info of %s ----
    Name:%s
    Age:%s
    Job:%s
    Salary:%s
'''%(name,name,age,job,salary)

info1 = '''
    ----info of {_name}----
    Name = {_name}
    Age = {_age}
    Job = {_job}
    Salary = {_salary}
'''.format(_name = name,
        _age = age,
        _job = job,
        _salary = salary)

info2 = """
        ---- info of {0} ----
        Name:{0}
        Age:{1}
        Job:{2}
        Salary:{3}
""".format(name,age,job,salary)
#print(info)
#print(info1)
print(info2)