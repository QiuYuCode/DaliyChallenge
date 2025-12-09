# 挑战 3：字典推导式 (Dictionary Comprehensions)
# 既然你已经掌握了列表推导式，我们现在将难度提升一点点，进入**字典（Dictionary）**的世界。
# 
# 在 Python 中，字典推导式和列表推导式非常像，区别在于：
# 
# 使用的是大括号 {}。
# 
# 你需要同时定义 键 (Key) 和 值 (Value)，中间用冒号 : 分隔。
names = ['Bob', 'Alice', 'Dave', 'Frank']

my_dict = {x: len(x) for x in names if x.lower().startswith("f") or x.lower().startswith("a")}

print(my_dict)

