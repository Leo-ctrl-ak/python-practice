import pymysql
import sys
import io

# 修复 Windows 终端 GBK 编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123.com',
        database='test_db',
        port=3307,
        charset='utf8mb4'
    )
    print("✅ 成功连接到 MySQL!")
except pymysql.MySQLError as e:
    print(f"❌ 数据库连接失败: {e}")
    exit(1)

cursor = conn.cursor()

# INNER JOIN
print("=" * 50)
print("INNER JOIN——订单对应客户：")
cursor.execute("""
    SELECT orders.id, test_users.username, orders.product, orders.amount
    FROM orders
    INNER JOIN test_users ON orders.user_id = test_users.id
""")
for row in cursor.fetchall():
    print(f"  订单{row[0]}：{row[1]} 购买 {row[2]}，元{row[3]}")

# LEFT JOIN
print("\nLEFT JOIN——所有用户及订单（含无订单用户）：")
cursor.execute("""
    SELECT test_users.username, orders.product, orders.amount
    FROM test_users
    LEFT JOIN orders ON test_users.id = orders.user_id
""")
for row in cursor.fetchall():
    if row[1]:
        print(f"  {row[0]}：{row[1]} 元{row[2]}")
    else:
        print(f"  {row[0]}：无订单")

# 子查询
print("\n有订单的用户：")
cursor.execute("""
    SELECT username FROM test_users
    WHERE id IN (SELECT DISTINCT user_id FROM orders)
""")
for row in cursor.fetchall():
    print(f"  {row[0]}")

cursor.close()
conn.close()