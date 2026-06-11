# Python + MySQL 常用代码片段

## 1. 连接数据库
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='xxx', database='test_db', port=3307, charset='utf8mb4')
cursor = conn.cursor()

## 2. 查询并打印
cursor.execute("SELECT * FROM test_users")
for row in cursor.fetchall():
    print(row)

## 3. JOIN 查询
SELECT a.字段, b.字段 FROM 表A a INNER JOIN 表B b ON a.id = b.外键

## 4. 分组统计
SELECT 字段, COUNT(*) FROM 表 GROUP BY 字段 HAVING COUNT(*) > 1

## 5. 子查询
SELECT 字段 FROM 表 WHERE 字段 IN (SELECT 字段 FROM 另一张表)

## 6. 关闭连接
cursor.close()
conn.close()