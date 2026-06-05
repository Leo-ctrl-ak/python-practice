def analyze_numbers(numbers):
    if not numbers:
        print("列表为空")
        return
    print(f"列表：{numbers}")
    print(f"最大值：{max(numbers)}")
    print(f"最小值：{min(numbers)}")
    print(f"平均值：{sum(numbers)/len(numbers):.2f}")

scores = [85, 92, 78, 90, 88, 76, 95]
analyze_numbers(scores)