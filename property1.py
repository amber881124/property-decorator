class Game:
    def __init__(self, hp, role):
        self.hp  = hp
        self.role = role

    # hp的getter
    @property
    def hp(self):
        print('get hp')
        return self._hp

    # hp的setter
    @hp.setter
    def hp(self, new_hp):
        if new_hp > 100:
            self._hp = 100
        else:
            self._hp = new_hp

    # role的getter
    @property
    def role(self):
        print('get role')
        return self._role

    # role的setter
    @role.setter
    def role(self, new_role):
        if new_role == '劍士':
            self._role = '無敵' + new_role
        else:
            self._role = '霹靂' + new_role

g = Game(40, '魔法師')
g.hp = 150
g.role = '射擊者'
print(g.hp)
print(g.role)
# get hp
# 100
# get role
# 霹靂射擊者


