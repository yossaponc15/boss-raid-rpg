# 📜 คู่มือเลือกอาชีพและสเปกสกิลผู้กล้า (Hero Class & Skill Codex)

ยินดีต้อนรับสู่หอเกียรติยศกิลด์ The Bug Hunters!  
ให้นักเรียนอ่านความสามารถและสกิลของแต่ละอาชีพด้านล่างนี้ จากนั้น **เลือก 1 อาชีพที่อยากเล่น (ไม่ซ้ำกับเพื่อนในทีม)** แล้วนำโครงโค้ดตั้งต้นไปเขียนเงื่อนไข `if-elif-else` ด้วยตนเอง

---

## 🧭 สรุป 4 อาชีพในกิลด์

| สัญลักษณ์ | อาชีพ | สไตล์การเล่น | จุดเด่นของสกิล |
|:---:|---|---|---|
| 🗡️ | **Berserker Warrior** | สายบ้าคลั่ง เลือดนักสู้ | ยิ่งบอสเลือดเหลือน้อย ดาเมจจะยิ่งพุ่งสูงขึ้นเป็นทวีคูณ |
| 🔮 | **Grand Mage** | จอมเวทคำนวณจังหวะ | ร่ายเวทตามรอบเทิร์น และปล่อยมหาเวทใหญ่ทุกๆ 4 เทิร์น |
| 🏹 | **Sniper Archer** | สไนเปอร์เจาะเกราะ | เก่งเรื่องยิงทะลวงเกราะบอส และยิงเบิ้ลเมื่อบอสไร้เกราะ |
| 🛡️ | **Holy Paladin** | อัศวินผู้พิทักษ์ | เปิดฉากด้วยทัณฑ์ศักดิ์สิทธิ์ และฮึดสู้แสงแห่งรุ่งอรุณเมื่อวิกฤต |

---

## 🗡️ อาชีพที่ 1: นักรบเบอร์เซิร์กเกอร์ (Berserker Warrior)

- **ไฟล์ที่ต้องสร้าง:** `heroes/hero_berserker.py`
- **คำอธิบายสกิล:** เมื่อบอสยังมีพลังเยอะ นักรบจะฟันดาบหยั่งเชิง แต่เมื่อเห็นบอสเริ่มบาดเจ็บจะพุ่งปิดฉาก และถ้าบอสเลือดวิกฤตจะปลดปล่อยพลังคลั่งขั้นสุด!
- **กติกาคำนวณดาเมจ (`calculate_attack`):**
  1. **วิกฤต:** ถ้าบอสเลือดน้อยกว่า 80 (`boss_hp < 80`) -> ใช้ท่า *"Overkill Crash"* ดาเมจ **`70`**
  2. **บาดเจ็บ:** ถ้าบอสเลือดต่ำกว่า 150 (`boss_hp < 150`) -> ใช้ท่า *"Execute Strike"* ดาเมจ **`45`**
  3. **ปกติ:** บอสเลือดตั้งแต่ 150 ขึ้นไป -> ฟันดาบปกติ ดาเมจ **`20`**

### โครงโค้ดตั้งต้น (นำไปใส่ในไฟล์ แล้วเขียนส่วน TODO):
```python
try:
    from heroes.base_hero import BaseHero
except ImportError:
    from base_hero import BaseHero

class BerserkerHero(BaseHero):
    def __init__(self, name="Berserker"):
        super().__init__(name=name, role="Berserker Warrior", hp=120)

    def calculate_attack(self, boss_hp: int, turn: int = 1, boss_shield: int = 0) -> tuple[int, str]:
        # ========================================================
        # TODO: เขียนเงื่อนไข 3 ข้อตรงนี้ด้วย if - elif - else
        # 1. boss_hp < 80  -> damage = 70, msg = "..."
        # 2. boss_hp < 150 -> damage = 45, msg = "..."
        # 3. อื่นๆ          -> damage = 20, msg = "..."
        # ========================================================
        pass
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
```

---

## 🔮 อาชีพที่ 2: มหาจอมเวท (Grand Mage)

- **ไฟล์ที่ต้องสร้าง:** `heroes/hero_mage.py`
- **คำอธิบายสกิล:** ใช้การคำนวณจังหวะรอบเทิร์น เทิร์นคี่ร่ายกระสุนเวท เทิร์นคู่ร่ายอุกกาบาต และทุก 4 เทิร์นจะระเบิดมหาเวทสูงสุด!
- **กติกาคำนวณดาเมจ (`calculate_attack`):**
  1. **มหาเวท:** เทิร์นที่หารด้วย 4 ลงตัว (`turn % 4 == 0`) -> ร่ายมหาเวท *"Arcane Nova"* ดาเมจ **`65`**
  2. **เวทใหญ่:** เทิร์นที่เป็นเลขคู่ทั่วไป (`turn % 2 == 0`) -> ร่ายเวท *"Meteor Fall"* ดาเมจ **`40`**
  3. **เวทปกติ:** เทิร์นที่เป็นเลขคี่ -> ยิงกระสุนเวท *"Magic Bolt"* ดาเมจ **`15`**

### โครงโค้ดตั้งต้น:
```python
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
```

---

## 🏹 อาชีพที่ 3: สไนเปอร์นักธนู (Sniper Archer)

- **ไฟล์ที่ต้องสร้าง:** `heroes/hero_archer.py`
- **คำอธิบายสกิล:** เชี่ยวชาญการสังเกตเกราะของบอส ถ้าเกราะหนาจะใช้ลูกศรยักษ์เจาะเกราะ ถ้าเกราะเริ่มบางจะยิงธรรมดา และถ้าบอสไม่มีเกราะจะยิงเบิ้ลเข้าจุดตาย!
- **กติกาคำนวณดาเมจ (`calculate_attack`):**
  1. **เจาะเกราะหนัก:** ถ้าบอสเกราะหนาตั้งแต่ 50 ขึ้นไป (`boss_shield >= 50`) -> ใช้ *"Heavy Piercing"* ดาเมจ **`55`**
  2. **เจาะเกราะปกติ:** ถ้าบอสมีเกราะบางส่วน (`boss_shield > 0` แต่น้อยกว่า 50) -> ใช้ *"Piercing Arrow"* ดาเมจ **`30`**
  3. **ยิงเบิ้ล:** ถ้าบอสไม่มีเกราะเลย (`boss_shield == 0`) -> ยิงเบิ้ล 2 ดอก *"Double Snipe"* ดาเมจ **`40`**

### โครงโค้ดตั้งต้น:
```python
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
```

---

## 🛡️ อาชีพที่ 4: พาลาดินศักดิ์สิทธิ์ (Holy Paladin)

- **ไฟล์ที่ต้องสร้าง:** `heroes/hero_paladin.py`
- **คำอธิบายสกิล:** เมื่อเปิดศึกจะใช้พลังศักดิ์สิทธิ์ลงทัณฑ์บอส ระหว่างการต่อสู้จะคอยเอาโล่กระแทก และเมื่อบอสเลือดวิกฤตจะรวบรวมแสงกู้โลกฮึดสู้อีกครั้ง!
- **กติกาคำนวณดาเมจ (`calculate_attack`):**
  1. **ทัณฑ์สวรรค์:** ช่วงเปิดฉากบอสเลือดเต็ม (`boss_hp >= 250`) -> ใช้ *"Holy Judgement"* ดาเมจ **`45`**
  2. **แสงกู้โลก:** ช่วงบอสเลือดวิกฤตใกล้ตาย (`boss_hp < 80`) -> ใช้ *"Light of Dawn"* ดาเมจ **`50`**
  3. **กระแทกโล่:** ช่วงเลือดปานกลาง (80 ถึง 249) -> ฟันดาบกระแทกโล่ *"Shield Bash"* ดาเมจ **`25`**

### โครงโค้ดตั้งต้น:
```python
try:
    from heroes.base_hero import BaseHero
except ImportError:
    from base_hero import BaseHero

class HolyPaladinHero(BaseHero):
    def __init__(self, name="Holy Paladin"):
        super().__init__(name=name, role="Holy Paladin", hp=140)

    def calculate_attack(self, boss_hp: int, turn: int = 1, boss_shield: int = 0) -> tuple[int, str]:
        # ========================================================
        # TODO: เขียนเงื่อนไข 3 ข้อตรงนี้ด้วย if - elif - else
        # 1. boss_hp >= 250 -> damage = 45, msg = "..."
        # 2. boss_hp < 80   -> damage = 50, msg = "..."
        # 3. อื่นๆ           -> damage = 25, msg = "..."
        # ========================================================
        pass
        return damage, msg

if __name__ == "__main__":
    hero = HolyPaladinHero()
    # รันตรวจผล: python heroes/hero_paladin.py
    assert hero.calculate_attack(boss_hp=300)[0] == 45, "เลือด 300 ต้องได้ดาเมจ 45"
    assert hero.calculate_attack(boss_hp=250)[0] == 45, "เลือด 250 ต้องได้ดาเมจ 45"
    assert hero.calculate_attack(boss_hp=249)[0] == 25, "เลือด 249 ต้องได้ดาเมจ 25"
    assert hero.calculate_attack(boss_hp=80)[0] == 25, "เลือด 80 ต้องได้ดาเมจ 25"
    assert hero.calculate_attack(boss_hp=79)[0] == 50, "เลือด 79 ต้องได้ดาเมจ 50"
    print("✅ Holy Paladin: ยินดีด้วย! โค้ดผ่านการทดสอบทุกข้อแล้ว พร้อมลงสนาม!")
```
