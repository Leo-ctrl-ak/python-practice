users = [
    {"name": "张三", "age": 25, "email": "zhangsan@test.com"},
    {"name": "李四", "age": 30, "email": "lisi@test.com"},
    {"name": "王五", "age": 28, "email": "wangwu@test.com"},
]

def add_user(name, age, email):
    users.append({"name": name, "age": age, "email": email})
    print(f"用户 {name} 已添加")

def find_user(name):
    for user in users:
        if user["name"] == name:
            print(f"找到：{user}")
            return user
    print(f"未找到：{name}")
    return None

def list_all():
    print(f"\n共 {len(users)} 个用户：")
    for i, user in enumerate(users, 1):
        print(f"  {i}. {user['name']}，{user['age']}岁，{user['email']}")

list_all()
add_user("赵六", 22, "zhaoliu@test.com")
list_all()
find_user("李四")