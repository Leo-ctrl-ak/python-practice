import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123.com',  # 这里已经改成了你刚才设置的密码
    database='test_db',
    port=3307,
    charset='utf8mb4'
)

cursor = conn.cursor()

# 1. 模糊查询
print("=" * 40)
print("用户名包含'张'的用户：")
cursor.execute("SELECT * FROM test_users WHERE username LIKE '%张%'")
for row in cursor.fetchall():
    print(f"  {row[1]}，{row[2]}岁")

# 2. 排序查询
print("\n按年龄降序排列：")
cursor.execute("SELECT username, age FROM test_users ORDER BY age DESC")
for row in cursor.fetchall():
    print(f"  {row[0]}：{row[1]}岁")

# 3. 分组统计
print("\n各年龄段人数：")
cursor.execute("SELECT age, COUNT(*) AS count FROM test_users GROUP BY age")
for row in cursor.fetchall():
    print(f"  {row[0]}岁：{row[1]}人")

# 4. 聚合统计
cursor.execute("SELECT MAX(age), MIN(age), AVG(age) FROM test_users")
max_age, min_age, avg_age = cursor.fetchone()
print(f"\n最大年龄：{max_age}，最小年龄：{min_age}，平均年龄：{avg_age:.1f}")

cursor.close()
conn.close()