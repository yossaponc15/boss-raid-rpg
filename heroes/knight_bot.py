# heroes/knight_bot.py
"""
Knight Bot - อัศวินฝึกหัด (ตัวอย่างฮีโร่เริ่มต้นที่ครูเตรียมไว้ให้)
นักเรียนสามารถดูตัวอย่างนี้เพื่อสร้างไฟล์ฮีโร่ของตนเองได้
"""

try:
    from heroes.base_hero import BaseHero
except ImportError:
    from base_hero import BaseHero

class KnightBot(BaseHero):
    def __init__(self):
        super().__init__(name="Knight Bot", role="Trainee Knight", hp=100)

    def calculate_attack(self, boss_hp: int, turn: int = 1, boss_shield: int = 0) -> tuple[int, str]:
        # ท่าโจมตีพื้นฐานง่ายๆ
        if boss_hp < 100:
            damage = 30
            msg = "🗡️ Knight Bot ใช้ดาบเหล็กฟันสุดแรงเกิด!"
        else:
            damage = 15
            msg = "⚔️ Knight Bot ฟันดาบทดสอบพลัง"
        return damage, msg

if __name__ == "__main__":
    bot = KnightBot()
    # Test cases ตรวจสอบความถูกต้อง
    dmg, _ = bot.calculate_attack(boss_hp=200, turn=1)
    assert dmg == 15, f"คาดหวัง 15 แต่ได้ {dmg}"

    dmg, _ = bot.calculate_attack(boss_hp=50, turn=1)
    assert dmg == 30, f"คาดหวัง 30 แต่ได้ {dmg}"

    print("✅ Knight Bot: Self-tests passed!")
