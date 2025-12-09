# 挑战 4：RPG 角色生成器 (The RPG Hero)
# 任务要求： 请定义一个名为 Hero 的类（Class）。

# 这个类需要具备以下功能：
#   属性：在创建时（__init__），接受 name（名字）和 hp（血量）两个参数，并把它们存到 self 里。
#   方法：定义一个名为 take_damage 的函数。
#   它接受一个参数 damage（伤害值）。
#   调用时，从当前的 hp 中减去这个 damage。
#   打印一句话："[名字] 受到了 [伤害] 点伤害，剩余血量：[剩余HP]"。


class Hero(object):
    
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        
    def take_damage(self, damage: int):
        self.hp -= damage
        print(f"[{self.name}] 受到了 [{damage}] 点伤害，剩余血量：{self.hp}")

player = Hero("Arthur", 100)
player.take_damage(20)