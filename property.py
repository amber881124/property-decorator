class Game:
    def __init__(self, hp, role):
        self._hp = hp
        self._role = role
    
    # getter method (hp)
    def get_hp(self):
        return self._hp

    #  setter method (hp)
    def set_hp(self, new_hp):
        self._hp  =  new_hp

    # getter method (role)
    def get_role(self):
        return self._role

    #  setter method (role)
    def set_role(self, new_role):
        self._role  =  new_role

game = Game(50, '魔法師')
game1 = Game(100, '魔法師')
game.set_hp(game.get_hp() + game1.get_hp())
game.set_role('回復師')
print(f'角色職位改為{game.get_role()}，生命值改為{game.get_hp()}')
# 角色職位改為回復師，生命值改為150



