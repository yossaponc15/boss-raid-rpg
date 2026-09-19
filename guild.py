# guild.py
"""
Guild Headquarters - ศูนย์รวมปาร์ตี้ของกิลด์
ไฟล์นี้เป็นจุดที่นักเรียนทุกคนจะเข้ามาลงทะเบียน Hero และร่วมกันกำหนดสโลแกนประจำทีม
(หมายเหตุสำหรับครู: จุดนี้คือพื้นที่ควบคุม Controlled Conflict)
"""

# -------------------------------------------------------------
# [CONFLICT_ZONE_SLOGAN]
# แต่ละคน/แต่ละคู่ จะแก้ไขคำขวัญกิลด์ตรงนี้ให้เป็นสไตล์ของตัวเอง
GUILD_NAME = "Hero"
GUILD_SLOGAN = "hello"
# -------------------------------------------------------------


# Import ฮีโร่ของแต่ละคนเข้ามา
from heroes.knight_bot import KnightBot
# [STUDENT_IMPORTS_HERE]
# ตัวอย่าง: from heroes.hero_berserker import BerserkerHero
from heroes.hero_mage import GrandMageHero

# -------------------------------------------------------------
# [CONFLICT_ZONE_PARTY]
# รายชื่อสมาชิกปาร์ตี้ที่จะลงสนามสู้บอส
# นักเรียนเพิ่ม instance ของฮีโร่ตนเองเข้าไปใน List นี้
PARTY_MEMBERS = [
    KnightBot(),
    # [ADD_YOUR_HERO_HERE]
    GrandMageHero(),
]
# -------------------------------------------------------------

def get_party():
    """ดึงรายชื่อสมาชิกปาร์ตี้ที่พร้อมต่อสู้"""
    return [hero for hero in PARTY_MEMBERS if hero.is_alive()]
