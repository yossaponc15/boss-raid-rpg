# main.py
"""
Boss Raid Simulator - ระบบจำลองการต่อสู้ตะลุยดันเจี้ยน
รันไฟล์นี้เพื่อดูการต่อสู้ระหว่างกิลด์ผู้กล้ากับมังกรยักษ์!
คำสั่ง: python main.py
"""

import time
import sys
from boss import DragonBoss
import guild

def print_divider(char="=", length=62):
    print(char * length)

def run_raid(sleep_delay=0.6):
    print_divider("=")
    print(f"🏰 GUILD: {guild.GUILD_NAME}")
    print(f"📢 SLOGAN: \"{guild.GUILD_SLOGAN}\"")
    print_divider("=")

    party = guild.get_party()
    if not party:
        print("❌ ไม่มีฮีโร่ในปาร์ตี้! กรุณาเพิ่มฮีโร่ใน guild.py ก่อน")
        return

    print("👥 สมาชิกปาร์ตี้ที่เข้าร่วมศึก:")
    for idx, hero in enumerate(party, 1):
        print(f"   [{idx}] {hero.name} ({hero.role}) - HP: {hero.current_hp}/{hero.max_hp}")
    print_divider("-")

    # กำหนดค่าเริ่มต้นของบอส
    boss = DragonBoss(name="Ancient Flame Dragon", max_hp=500, shield=0)
    print(boss.render_status())
    print_divider("=")
    print("⚔️ ศึกเริ่มต้นขึ้นแล้ว! ทุกลมหายใจคือการต่อสู้!\n")
    time.sleep(sleep_delay)

    turn = 1
    damage_scoreboard = {hero.name: 0 for hero in party}

    while boss.is_alive() and turn <= 15:
        print(f"--- [ TURN {turn} ] ---")
        
        for hero in party:
            if not boss.is_alive():
                break

            # แต่ละฮีโร่คำนวณการโจมตีตาม logic สกิลของตนเอง
            damage, msg = hero.calculate_attack(boss_hp=boss.hp, turn=turn, boss_shield=boss.shield)
            actual_dmg, absorbed = boss.take_damage(damage)
            damage_scoreboard[hero.name] += (actual_dmg + absorbed)

            absorb_text = f" (🛡️ ซับเกราะไป {absorbed})" if absorbed > 0 else ""
            print(f"👤 {hero.name}: {msg} -> ทำดาเมจ {damage}{absorb_text}!")
            time.sleep(sleep_delay)

        print()
        print(boss.render_status())
        print()
        time.sleep(sleep_delay)

        if not boss.is_alive():
            break
        turn += 1

    print_divider("=")
    if not boss.is_alive():
        print(f"🏆 VICTORY! กิลด์ {guild.GUILD_NAME} พิชิตบอสได้สำเร็จใน {turn} เทิร์น!")
        print_divider("-")
        print("📊 สรุปผลงานดาเมจของผู้กล้า (Scoreboard):")
        
        # จัดอันดับตามดาเมจรวม
        sorted_scores = sorted(damage_scoreboard.items(), key=lambda x: x[1], reverse=True)
        medals = ["🥇 MVP", "🥈 Runner-up", "🥉 3rd Place", "🎖️ Contributor"]
        
        for idx, (name, total_dmg) in enumerate(sorted_scores):
            badge = medals[idx] if idx < len(medals) else "⚔️ Fighter"
            print(f"   {badge:<14} : {name:<22} รวมทำดาเมจ {total_dmg:>4} หน่วย")
        print_divider("=")
    else:
        print("💀 บอสยังไม่ตายใน 15 เทิร์น! กิลด์ต้องรวมพลังพัฒนาสกิลให้แกร่งขึ้น!")
        print_divider("=")

if __name__ == "__main__":
    # ถ้าระบุ argument --fast จะรันโดยไม่หน่วงเวลา (เหมาะสำหรับ unit test)
    delay = 0.0 if "--fast" in sys.argv else 0.5
    run_raid(sleep_delay=delay)
