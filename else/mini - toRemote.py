#!/usr/bin/python
import sys
import time
# import json
from py4j.java_gateway import GatewayParameters, JavaGateway, java_import
J = JavaGateway(gateway_parameters = GatewayParameters(address="app.vietthuan.com",port=33333))
JJ = J.entry_point

java_import(J.jvm,'java.json.*')  
java_import(J.jvm,'java.lang.*')
java_import(J.jvm,'java.util.*')
java_import(J.jvm,'java.io.*')
# java_import(J.jvm,'java.sql.*')
java_import(J.jvm,'java.Math.*')

print("E",J.jvm.Math.E)
print("PI",J.jvm.java.lang.Math.PI)
print("ATEN",J.jvm.Math.atan(J.jvm.Math.PI))
# ====================================
print("max",J.jvm.Math.max(543.234,34242.764))
print("min",J.jvm.java.lang.Math.min(543.234,34242.764)) #完整路徑
# ====================================

# print(type(J.jvm.System.getProperties())) #用key/value方法取值

# print(J.jvm.java.util.ArrayList()) #完整路徑
# jList2 = J.jvm.ArrayList()
# jMap = J.jvm.HashMap()

# jArr = J.jvm.ArrayList()
# jArr.add(1234)
# jArr.add(5678)

# print("呼叫時間的靜態方法",J.jvm.System.currentTimeMillis())
# print(J.jvm.java.lang.String("a"))
# print(J.jvm.java.lang.Integer(99))
# print(J.jvm.String("a"))
# print(J.jvm.Integer(5))
# str = J.jvm.String("This is a book .00000000000000000000000000000000..")
# print(len(str)) #這是python叫的

# for x in jArr:
# 	print(x)

# python 呼叫MySQL
db = "db01"
table = "food"
connUrl = "jdbc:mysql://app.vietthuan.com:3306/"+ db +"?useSSL=false"
conn = J.jvm.java.sql.DriverManager.getConnection(connUrl,"root","#OoXx@748#")
sql = "SELECT * FROM "+ table
stmt = conn.createStatement()
# python 呼叫MySQL & 傳值給java解析
data = JJ.objToList(stmt,sql)
print(data)
# rs = stmt.executeQuery(sql)
# print(" rs : %s \n type(rs) : %s \n J.jvm.rs : %s \n" % (rs,type(rs),J.jvm.rs))

print("==================================")

# 呼叫java端的mysql jdbc
# sql = "select * from department"
# rs = JJ.connMysql(sql,"jdbc")
# print(rs)

# print(J.jvm.rs.getString(1))
# data = JJ.objToList(J.jvm.rs)
# data = JJ.objToList(rs)
# print(data)

# #print到java的console
J.jvm.System.out.println("START !!! msg from python ..")

if __name__ == "__main__":
	print(">>Finsh<<")
