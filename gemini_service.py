import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# คำที่เกี่ยวกับ D&D ทั้งหมด (อัปเดตเพิ่มให้ครอบคลุม)
DD_KEYWORDS = [
    # ชื่อหลัก
    "d&d", "dungeons & dragons", "ดันเจี้ยน", "ดราก้อน",

    # ตัวละครและคลาส
    "คลาส", "class", "wizard", "fighter", "rogue", "paladin", "bard", "sorcerer", "monk",
    "barbarian", "cleric", "druid", "warlock", "artificer",

    # เวทมนตร์ / กฎ
    "เวทมนตร์", "spell", "cantrip", "magic missile", "counterspell", "casting time",
    "ระดับเวท", "ritual", "spell slot", "spellcasting",

    # กฎพื้นฐาน / การเล่น
    "กฎ", "rule", "basic rules", "dnd rules", "stat block", "ability score", "skill check",
    "saving throw", "proficiency", "advantage", "disadvantage", "initiative", "movement",
    "reaction", "bonus action", "long rest", "short rest", "combat", "armor class", "hit point",
    "attack roll", "damage roll", "d20", "d6", "d8", "d10", "d12", "d4",

    # ค่าพลัง/ค่าสถานะ (Stats)
    "strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma",
    "str", "dex", "con", "int", "wis", "cha",
    "ค่าพลัง", "ค่าสถานะ", "ความแข็งแรง", "ความว่องไว", "พลังชีวิต", "เชาวน์", "ปัญญา", "เสน่ห์",

    # Alignment และทัศนคติ
    "alignment", "chaotic good", "chaotic neutral", "chaotic evil",
    "neutral good", "true neutral", "neutral evil",
    "lawful good", "lawful neutral", "lawful evil",
    "จารีตดี", "จารีตกลาง", "จารีตร้าย", "เป็นกลางดี", "เป็นกลางแท้", "เป็นกลางร้าย", "โกลาหลดี", "โกลาหลกลาง", "โกลาหลร้าย",

    # มอนสเตอร์ / ศัตรู
    "monster", "beholder", "lich", "goblin", "dragon", "mind flayer", "tarrasque",
    "bugbear", "kobold", "orc", "giant", "undead", "zombie", "skeleton", "มอนสเตอร์", "ปีศาจ", "ศัตรู",

    # โลก / เรื่องราว / Campaign
    "faerun", "forgotten realms", "campaign", "adventure", "quest", "story arc",
    "npc", "dm", "dungeon master", "session", "worldbuilding", "lore", "ดันเจียนมาสเตอร์", "โลกแฟนตาซี",

    # ภาษาไทยเฉพาะ
    "พ่อมด", "นักรบ", "นักฆ่า", "นักรบศักดิ์สิทธิ์", "นักดนตรี", "นักเวท", "ดันเจียน", "มอนสเตอร์", "นักบวช", "คนเถื่อน", "นักประดิษฐ์"
]


def is_dd_related(prompt):
    return any(keyword.lower() in prompt.lower() for keyword in DD_KEYWORDS)

def generate_text(prompt):
    if not is_dd_related(prompt):
        return "This question is not related to Dungeons & Dragons (D&D)."
    
    instruction = (
        "You are a Dungeons & Dragons (D&D) expert."
        "Please answer this question in detail but do not discuss any topics outside of D&D."
    )
    full_prompt = instruction + "\n\nคำถาม: " + prompt
    response = model.generate_content(full_prompt)
    return response.text.strip()
