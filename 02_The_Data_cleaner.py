
# 挑战 2：数据清洗器 (The Data Cleaner)
# 背景： 你从一个乱七八糟的数据库里拿到了一组用户名字。有些名字太短（无效），有些名字大小写混乱。我们需要清洗这些数据。
# 任务要求： 请编写一行代码（必须使用列表推导式），生成一个新的列表 clean_names。 规则如下：
# 过滤：去掉长度小于 2 的名字（比如 "c", "e", "g" 都要去掉）。
# 转换：将剩下的名字格式化为首字母大写，其余小写（Title Case）。例如 "ALICE" 应变为 "Alice"，"bob" 变为 "Bob"。

names = ["bob", "ALICE", "c", "dave", "e", "Frank", "g"]

clean_names = [new_name.capitalize() for new_name in names if len(new_name) > 2]
print(clean_names)