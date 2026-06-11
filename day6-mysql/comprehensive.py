import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password=u'123.com',  
    database='test_db',
    port=3307,
    charset='utf8mb4'
)

cursor = conn.cursor()

# 1. 每个用户的订单总金额
print("=" * 50)
print("用户订单总额：")
cursor.execute("""
    SELECT test_users.username, SUM(orders.amount) AS total
    FROM test_users
    LEFT JOIN orders ON test_users.id = orders.user_id
    GROUP BY test_users.username
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    total = row[1] if row[1] else 0
    print(f"  {row[0]}：¥{total}")

# 2. 无订单用户
print("\n无订单用户：")
cursor.execute("""
    SELECT username FROM test_users
    WHERE id NOT IN (SELECT DISTINCT user_id FROM orders)
""")
for row in cursor.fetchall():
    print(f"  {row[0]}")

# 3. 高消费用户（>500元）
print("\n高消费用户（>500元）：")
cursor.execute("""
    SELECT DISTINCT test_users.username, orders.product, orders.amount
    FROM test_users
    INNER JOIN orders ON test_users.id = orders.user_id
    WHERE orders.amount > 500
""")
for row in cursor.fetchall():
    print(f"  {row[0]}：{row[1]} ¥{row[2]}")

cursor.close()
conn.close()