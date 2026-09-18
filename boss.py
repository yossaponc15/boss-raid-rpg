# boss.py
"""
Boss Engine - ระบบจัดการมังกรบอส (Dragon Boss)
"""

class DragonBoss:
    def __init__(self, name: str = "Ancient Flame Dragon", max_hp: int = 500, shield: int = 0):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.shield = shield
        self.base_attack = 10

    def take_damage(self, damage: int) -> tuple[int, int]:
        """
        รับดาเมจจากฮีโร่ โดยหักจากเกราะก่อน ถ้าเกราะหมดจึงเข้าเลือดบอส
        :return: (damage_to_hp, absorbed_by_shield)
        """
        if damage <= 0:
            return 0, 0

        absorbed = 0
        damage_left = damage

        if self.shield > 0:
            if damage_left <= self.shield:
                self.shield -= damage_left
                absorbed = damage_left
                damage_left = 0
            else:
                absorbed = self.shield
                damage_left -= self.shield
                self.shield = 0

        actual_hp_damage = min(self.hp, damage_left)
        self.hp -= actual_hp_damage
        return actual_hp_damage, absorbed

    def is_alive(self) -> bool:
        return self.hp > 0

    def render_status(self) -> str:
        """แสดงแถบเลือดและเกราะแบบ ASCII"""
        bar_length = 25
        hp_percent = max(0.0, min(1.0, self.hp / self.max_hp))
        filled = int(bar_length * hp_percent)
        bar = "█" * filled + "░" * (bar_length - filled)

        shield_info = f" | 🛡️ SHIELD: {self.shield}" if self.shield > 0 else ""
        return f"🐉 {self.name}\n   HP: [{bar}] {self.hp}/{self.max_hp} ({int(hp_percent * 100)}%){shield_info}"
