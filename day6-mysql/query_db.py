import pymysql

# 连接数据库配置
config = {
    'host': 'localhost',
    'port': 3307,          # 注意：你安装时配置的是 3307 端口
    'user': 'root',
    'password': '123456',  # 请替换成你设置的 root 密码
    'database': 'test_db',
    'charset': 'utf8mb4'
}

def query_users():
    """查询 test_users 表所有数据并打印"""
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        print("✅ 成功连接到 MySQL 数据库！")
        
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql = "SELECT * FROM test_users"
            cursor.execute(sql)
            
            # 获取所有结果
            results = cursor.fetchall()
            
            # 打印结果
            print("\n📊 test_users 表数据：")
            print("id\tusername\tage\temail")
            print("-" * 50)
            for row in results:
                print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}")
                
        # 关闭连接
        connection.close()
        print("\n✅ 查询完成，连接已关闭。")
        
    except pymysql.MySQLError as e:
        print(f"❌ 连接失败或查询出错: {e}")

if __name__ == "__main__":
    query_users()