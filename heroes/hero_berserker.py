try:
    from heroes.base_hero import BaseHero
except ImportError:
    from base_hero import BaseHero

class BerserkerHero(BaseHero):
    def __init__(self, name="Berserker"):
        super().__init__(name=name, role="Berserker Warrior", hp=120)

    def calculate_attack(self, boss_hp: int, turn: int = 1, boss_shield: int = 0) -> tuple[int, str]:
        if boss_hp < 80:
            damage = 70
            msg = "Overkill Crash"
        elif boss_hp < 150:
            damage = 45
            msg = "Execute Strike"
        else:
            damage = 20
            msg = "ฟันดาบปกติ"

        # ========================================================
        # TODO: เขียนเงื่อนไข 3 ข้อตรงนี้ด้วย if - elif - else
        # 1. boss_hp < 80  -> damage = 70, msg = "..."
        # 2. boss_hp < 150 -> damage = 45, msg = "..."
        # 3. อื่นๆ          -> damage = 20, msg = "..."
        # ========================================================
        return damage, msg

if __name__ == "__main__":
    hero = BerserkerHero()
    # รันตรวจผล: python heroes/hero_berserker.py
    assert hero.calculate_attack(boss_hp=200)[0] == 20, "เคสเลือด 200 ต้องได้ดาเมจ 20"
    assert hero.calculate_attack(boss_hp=150)[0] == 20, "เคสเลือด 150 ต้องได้ดาเมจ 20"
    assert hero.calculate_attack(boss_hp=149)[0] == 45, "เคสเลือด 149 ต้องได้ดาเมจ 45"
    assert hero.calculate_attack(boss_hp=80)[0] == 45, "เคสเลือด 80 ต้องได้ดาเมจ 45"
    assert hero.calculate_attack(boss_hp=79)[0] == 70, "เคสเลือด 79 ต้องได้ดาเมจ 70"
    print("✅ Berserker: ยินดีด้วย! โค้ดผ่านการทดสอบทุกข้อแล้ว พร้อมลงสนาม!")