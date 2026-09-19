try:
    from heroes.base_hero import BaseHero
except ImportError:
    from base_hero import BaseHero

class GrandMageHero(BaseHero):
    def __init__(self, name="Grand Mage"):
        super().__init__(name=name, role="Grand Mage", hp=80)

    def calculate_attack(self, boss_hp: int, turn: int = 1, boss_shield: int = 0) -> tuple[int, str]:
        # ========================================================
        # TODO: เขียนเงื่อนไข 3 ข้อตรงนี้ด้วย if - elif - else
        # 1. turn % 4 == 0 -> damage = 65, msg = "..."
        # 2. turn % 2 == 0 -> damage = 40, msg = "..."
        # 3. อื่นๆ          -> damage = 15, msg = "..."
        # ========================================================
        if turn % 4 == 0:
            damage = 65
            msg = "Arcane Nova"
        elif turn % 2 == 0:
            damage = 40
            msg = "Meteor Fall"
        else:
            damage = 15
            msg = "Magic Bolt"
        pass
        return damage, msg

if __name__ == "__main__":
    hero = GrandMageHero()
    # รันตรวจผล: python heroes/hero_mage.py
    assert hero.calculate_attack(boss_hp=300, turn=1)[0] == 15, "เทิร์น 1 ต้องได้ดาเมจ 15"
    assert hero.calculate_attack(boss_hp=300, turn=2)[0] == 40, "เทิร์น 2 ต้องได้ดาเมจ 40"
    assert hero.calculate_attack(boss_hp=300, turn=3)[0] == 15, "เทิร์น 3 ต้องได้ดาเมจ 15"
    assert hero.calculate_attack(boss_hp=300, turn=4)[0] == 65, "เทิร์น 4 ต้องได้ดาเมจ 65"
    assert hero.calculate_attack(boss_hp=300, turn=8)[0] == 65, "เทิร์น 8 ต้องได้ดาเมจ 65"
    print("✅ Grand Mage: ยินดีด้วย! โค้ดผ่านการทดสอบทุกข้อแล้ว พร้อมลงสนาม!")