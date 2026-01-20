from flask import Flask, render_template
import random  # Tasodifiy maslahat tanlash uchun

app = Flask(__name__)

# Foydali maslahatlar ro'yxati
tips = [
    "Bugun 10 daqiqa sport qiling",
    "Telefoningizni 1 soat dam olish uchun o‘chirib qo‘ying",
    "Kunlik prioritetlarni yozing",
    "Suv ichishni unutmang",
    "Kitob o‘qing",
    "Har kuni minnatdorlik qiladigan narsani yozing",
    "Kechqurun ertangi ishlarni rejalashtiring",
    "Do‘stlaringizga minnatdorlik bildirgan xabar yozing",
    "Ishni kichik bosqichlarga bo‘ling",
    "5 daqiqa meditatsiya qiling",
    "Kun oxirida o‘zingizni maqtang"
    # Shu yerga yana 20-30 yoki 50 maslahat qo‘shish mumkin
]

@app.route('/')
def home():
    tip = random.choice(tips)  # Tasodifiy maslahat tanlanadi
    return render_template('index.html', tip=tip)

if __name__ == '__main__':
    app.run(debug=True)
