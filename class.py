#!/usr/bin/python
# _*_ coding: UTF-8 _*_

# 类 demo
class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount


    def displayEmployee(self):
        print "Name:",self.name,",Salary:",self.salary


emp1 = Employee("Zara",1000)
emp2 = Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
print "Total Employeeddd %d" % Employee.empCount


