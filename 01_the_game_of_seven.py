# 🟢 挑战 1：逢七过 (The Game of Seven)
# 这个练习将同时测试你的 循环控制、条件判断 以及简单的 数据类型转换。
# 任务要求： 请编写一段 Python 代码，打印从 1 到 50 的所有数字。但是满足以下条件时需要进行特殊处理：

# 如果数字能被 7 整除，打印 "过" (Pass)。
# 如果数字 包含字符 '7' (例如 17, 27, 37)，打印 "敲" (Knock)。
# 如果 同时满足 以上两个条件 (例如 7)，打印 "过敲" (Pass-Knock)。
# 其他情况，直接打印该数字。

# 提示 (Hints)：
# 你需要用到取模运算符 % 来判断整除。
# 你需要将数字转换为字符串 str() 来检查是否包含 '7'。
# 注意 if-elif-else 的顺序，或者思考如何组合条件。
# 请在下方贴出你的代码：

for i in range(1, 51):
    if (i % 7 == 0) and ("7" in str(i)):
        print("Pass-Knock")
    elif i % 7 == 0:
        print("pass")
    elif "7" in str(i):
        print("Knock")
    else:
        print(i)