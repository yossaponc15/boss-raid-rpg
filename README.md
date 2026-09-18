# 🐉 Boss Raid RPG: The Bug Hunters Guild

โปรเจกต์เกมตะลุยดันเจี้ยนจำลองในเทอร์มินัล สำหรับฝึกฝน **Git Collaboration (Fork, Feature Branch, Sync Upstream, PR Cross-repo, และ Resolve Merge Conflict)**

---

## 🎯 เรื่องราวของเกม

กิลด์ **The Bug Hunters** ต้องรวมพลังผู้กล้าไปปราบมังกรโบราณ **Ancient Flame Dragon** (HP: 500) ในดันเจี้ยน!  
ผู้กล้าแต่ละคนจะเขียนความสามารถและสกิลของตนเองลงในโฟลเดอร์ `heroes/` จากนั้นนำมารวมพลังใน `guild.py` แล้วรัน `main.py` เพื่อดูผลการต่อสู้และจัดอันดับ MVP ประจำทีม!

---

## 📁 โครงสร้างโปรเจกต์

```text
fork-collab-git/
├── main.py                  # โปรแกรมหลัก: จำลองการต่อสู้ Turn-based และคำนวณผลลัพธ์
├── boss.py                  # คลาส Dragon Boss พร้อมระบบ HP และเกราะ Shield
├── guild.py                 # ศูนย์รวมกิลด์ (ลงทะเบียนฮีโร่ และกำหนดสโลแกนประจำทีม)
├── heroes/
│   ├── base_hero.py         # คลาสแม่ BaseHero
│   └── knight_bot.py        # ตัวอย่างฮีโร่เริ่มต้น
├── HERO_ROLES.md            # คู่มือสเปก 4 อาชีพ และโครงโค้ดตั้งต้นสำหรับนักเรียน
├── STUDENT_MISSIONS.md      # ใบภารกิจการเรียน 5 ด่าน สำหรับนักเรียน
├── TEACHER_GUIDE.md         # คู่มือครูและแผนการสอน 120 นาที
└── teacher_assets/          # เครื่องมือเสริมสำหรับครู (สำหรับปล่อย Event อัปเดต Upstream)
```

---

## 🚀 วิธีรันเกม

เปิด Terminal ในโฟลเดอร์นี้ แล้วพิมพ์:

```bash
python main.py
```
*(หากใช้เครื่อง Mac/Linux แล้วคำสั่ง `python` ไม่ติด ให้ใช้ `python3 main.py` แทน)*

---

## 📖 คู่มือการเรียนรู้

- สำหรับนักเรียน (เลือกอาชีพ): ศึกษาความสามารถของฮีโร่ที่ [HERO_ROLES.md](HERO_ROLES.md)
- สำหรับนักเรียน (ทำภารกิจ): เปิดอ่านใบภารกิจที่ [STUDENT_MISSIONS.md](STUDENT_MISSIONS.md)
- สำหรับผู้สอน: ดูแผนการสอนและเฉลยที่ [TEACHER_GUIDE.md](TEACHER_GUIDE.md)
