from The_RPG_Hero import Hero

class Mage(Hero):
    def __init__(self, name: str, hp: int, mana: int):
        super().__init__(name, hp)
        self.__mana = mana
        
    def cast_spell(self, cost):
        if self.__mana >= cost:
            self.__mana -= cost
            print(f"[{self.name}] 释放了法术，消耗了[{cost}] 法力, 剩余 {self.__mana}")
        else:
            print(f"[{self.name}] 法力不足,施法失败!")
            
            
merlin = Mage("Merlin", 80, 50) # 名字, 血量, 法力
merlin.take_damage(10)          # 继承自 Hero 的方法，应该能正常工作
merlin.cast_spell(30)           # Mage 独有的方法
merlin.cast_spell(30)           # 再次施法，此时法力应该不足