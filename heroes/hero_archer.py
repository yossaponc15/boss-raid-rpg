try:
    from heroes.base_hero import BaseHero
except ImportError:
    from base_hero import BaseHero

class SniperArcherHero(BaseHero):
    def __init__(self, name="Sniper Archer"):
        super().__init__(name=name, role="Sniper Archer", hp=90)

    def calculate_attack(self, boss_hp: int, turn: int = 1, boss_shield: int = 0) -> tuple[int, str]:
        # ========================================================
        # TODO: เขียนเงื่อนไข 3 ข้อตรงนี้ด้วย if - elif - else
        if boss_shield >= 50:
            damage = 55
            msg = "55 Damage Dealt"
        elif boss_shield > 0:
            damage = 30
            msg = "30 Damage Dealt"
        elif boss_shield == 0:
            damage = 40
            msg = "40 Damage Dealt"
        # 1. boss_shield >= 50 -> damage = 55, msg = "..."
        # 2. boss_shield > 0   -> damage = 30, msg = "..."
        # 3. อื่นๆ (shield == 0)-> damage = 40, msg = "..."
        # ========================================================
        pass
        return damage, msg

if __name__ == "__main__":
    hero = SniperArcherHero()
    # รันตรวจผล: python heroes/hero_archer.py
    assert hero.calculate_attack(boss_hp=300, boss_shield=60)[0] == 55, "เกราะ 60 ต้องได้ดาเมจ 55"
    assert hero.calculate_attack(boss_hp=300, boss_shield=50)[0] == 55, "เกราะ 50 ต้องได้ดาเมจ 55"
    assert hero.calculate_attack(boss_hp=300, boss_shield=49)[0] == 30, "เกราะ 49 ต้องได้ดาเมจ 30"
    assert hero.calculate_attack(boss_hp=300, boss_shield=1)[0] == 30, "เกราะ 1 ต้องได้ดาเมจ 30"
    assert hero.calculate_attack(boss_hp=300, boss_shield=0)[0] == 40, "เกราะ 0 ต้องได้ดาเมจ 40"
    print("✅ Sniper Archer: ยินดีด้วย! โค้ดผ่านการทดสอบทุกข้อแล้ว พร้อมลงสนาม!")
