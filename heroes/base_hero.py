# heroes/base_hero.py
"""
Base Hero Class - คลาสแม่สำหรับฮีโร่ทุกคนในเกม Boss Raid
นักเรียนจะสืบทอด (Inherit) คลาสนี้ไปสร้างฮีโร่ของตนเอง
"""

class BaseHero:
    def __init__(self, name: str, role: str, hp: int = 100):
        self.name = name
        self.role = role
        self.max_hp = hp
        self.current_hp = hp

    def calculate_attack(self, boss_hp: int, turn: int = 1, boss_shield: int = 0) -> tuple[int, str]:
        """
        คำนวณพลังโจมตีและข้อความการใช้สกิล
        :param boss_hp: เลือดปัจจุบันของบอส
        :param turn: เทิร์นปัจจุบันของการต่อสู้
        :param boss_shield: เกราะปัจจุบันของบอส (อาจอัปเดตเข้ามากลางเกม)
        :return: tuple ของ (damage: int, action_message: str)
        """
        raise NotImplementedError("ฮีโร่ทุกคนต้องเขียนฟังก์ชัน calculate_attack ของตนเอง!")

    def take_damage(self, damage: int):
        self.current_hp = max(0, self.current_hp - damage)

    def is_alive(self) -> bool:
        return self.current_hp > 0

    def __str__(self):
        return f"{self.name} ({self.role}) [HP: {self.current_hp}/{self.max_hp}]"
