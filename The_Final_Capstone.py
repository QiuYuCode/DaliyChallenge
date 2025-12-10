"""
### 🏆 最终阶段：综合实战挑战 (The Final Capstone)

现在，我们将进入最后一步。这个挑战将不再是单一知识点的练习，而是要求你像架构师一样，将之前学到的所有积木组合在一起，构建一个完整的微型系统。

**挑战主题：简易银行账本系统 (The Simple Banking System)**

**目标：**
编写一个模拟银行账户的程序，它必须包含以下三个组件，并无缝协作。

#### 组件 1：装饰器 `@audit_log`
编写一个装饰器，用于包装账户的操作方法。
* 它需要在函数执行**前**打印：`"正在处理交易..."`
* 它需要在函数执行**后**打印：`"交易结束"`
* *(注意：你需要使用 `*args` 和 `**kwargs` 来确保它能兼容任何参数)*

#### 组件 2：核心类 `BankAccount`
定义一个类，包含：
1.  **`__init__`**：接收 `owner` (户主名) 和 `balance` (初始余额)。同时初始化一个空列表 `self.history` 用来存记录。
2.  **`deposit(amount)`**：存款。加上余额，把字符串 `"存入 [amount]"` 存进 `history` 列表。**必须应用 `@audit_log` 装饰器**。
3.  **`withdraw(amount)`**：取款。
    * 如果余额不足，**抛出 `ValueError` 异常**（这是 Python 内置异常，无需自定义）。
    * 如果余额足够，扣除余额，把字符串 `"取出 [amount]"` 存进 `history` 列表。**必须应用 `@audit_log` 装饰器**。
4.  **`review_history()`**：这是一个**生成器 (Generator)** 方法。
    * 使用 `yield` 逐条返回 `self.history` 中的记录。

#### 组件 3：主程序逻辑 (Main)
在主代码块中：
1.  实例化一个账户。
2.  进行一次存款。
3.  尝试进行一次**合法的**取款。
4.  尝试进行一次**非法的**取款（金额超过余额），并使用 `try...except` 块捕获这个错误，打印 `"错误：余额不足！"`。
5.  最后，调用 `review_history()` 生成器，遍历并打印所有交易记录。

---

这将测试你对 Python 知识框架的综合掌控能力。
"""

from functools import wraps


def audit_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("正在处理交易...")
        result = func(*args, **kwargs)
        print("交易结束")
        return result
    return wrapper


class BankAccount:
    
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    @audit_log
    def deposit(self, amount: float):
        """存钱操作

        :param float amount: 金额
        """
        self.balance += amount
        self.history.append(f"存入 [{amount}]")
    
    @audit_log
    def withdraw(self, amount: float):
        """取钱操作

        :param float amount: 金额
        :raises ValueError: 余额不足抛出异常
        """
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"取出 [{amount}]")
        else:
            raise ValueError
        
    def review_history(self):
        yield from self.history


def main():
    bank_account = BankAccount("Bob", 1000.0)
    bank_account.deposit(200)
    bank_account.withdraw(50)
    
    try:
        bank_account.withdraw(20000)
    except ValueError:
        print("错误! 取款发生失败")
        
    for each_operation in bank_account.review_history():
        print(each_operation)
    


if __name__ == "__main__":
    main()