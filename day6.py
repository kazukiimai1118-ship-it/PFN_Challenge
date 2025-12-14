# リスト（List） - 箱が並んでいるイメージ
skills = ["Python", "Git"]
print(skills[0]) # -> Python （0から始まること注意！）

required_skills = ["Python", "Git", "Streamlit"]
print(required_skills[1])
required_skills.append("LLM")
print(required_skills)

# 辞書 (Dictionaly) - ラベルが付いた箱のイメージ
user = {"name": "Taro", "level": 5}
print(user["name"]) # -> Taro

mentor_profile = {"name": "PFN Mentor", "role": "Educator", "age": 30}
print(f"私の役割は{mentor_profile['role']}")
mentor_profile["company"] = "Preferred Networks"

# 現場でよく見る形（JSON構造）
data = [
    {"id": 1, "text": "Hello"},
    {"id": 2, "text": "World"}
]
#　これをループで回すのがWebアプリの基本です
for item in data:
    print(item["text"])

employees = [
    {"name": "PFN Mentor", "role": "Educator", "age": 30},
    {"name": "Bob", "role": "Student", "age": 25},
    {"name": "Alex", "role": "President", "age": 60}
]

for employee in employees:
    print(employee["name"])