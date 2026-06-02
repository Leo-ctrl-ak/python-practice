import random

# 生成 1-100 的随机数
target = random.randint(1, 100)
guess = 0
attempts = 0

print("猜数字游戏：1-100 之间的整数")

while guess != target:
    guess = int(input("请输入你的猜测："))
    attempts += 1
    if guess > target:
        print("太大了，再试一次")
    elif guess < target:
        print("太小了，再试一次")
    else:
        print(f"恭喜！你猜对了，共用了 {attempts} 次")