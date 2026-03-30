import tkinter as tk
from PIL import Image, ImageTk

# =========================
# البيانات (كل الدول)
# =========================
places = {
    "saudi arabia": {
        "info_en": "Saudi Arabia has Mecca & Medina.",
        "info_ar": "السعودية بها مكة والمدينة.",
        "flight1": "8:00 AM",
        "flight2": "6:00 PM",
        "duration": "3 hours",
        "arrival": "11:00 AM",
        "price": "5000 EGP"
    },
    "uae": {
        "info_en": "UAE has Dubai and Abu Dhabi.",
        "info_ar": "الإمارات بها دبي وأبوظبي.",
        "flight1": "10:00 AM",
        "flight2": "8:00 PM",
        "duration": "3 hours",
        "arrival": "1:00 PM",
        "price": "4500 EGP"
    },
    "kuwait": {
        "info_en": "Kuwait is a rich Gulf country.",
        "info_ar": "الكويت دولة غنية في الخليج.",
        "flight1": "9:00 AM",
        "flight2": "7:00 PM",
        "duration": "2 hours",
        "arrival": "11:00 AM",
        "price": "4000 EGP"
    },
    "qatar": {
        "info_en": "Qatar is famous for Doha city.",
        "info_ar": "قطر مشهورة بالدوحة.",
        "flight1": "11:00 AM",
        "flight2": "9:00 PM",
        "duration": "3 hours",
        "arrival": "2:00 PM",
        "price": "4200 EGP"
    },
    "jordan": {
        "info_en": "Jordan has Petra and Dead Sea.",
        "info_ar": "الأردن بها البتراء والبحر الميت.",
        "flight1": "7:00 AM",
        "flight2": "5:00 PM",
        "duration": "2 hours",
        "arrival": "9:00 AM",
        "price": "3500 EGP"
    },
    "morocco": {
        "info_en": "Morocco has Marrakech and Casablanca.",
        "info_ar": "المغرب بها مراكش والدار البيضاء.",
        "flight1": "6:00 AM",
        "flight2": "4:00 PM",
        "duration": "5 hours",
        "arrival": "11:00 AM",
        "price": "6000 EGP"
    },
    "algeria": {
        "info_en": "Algeria is the largest country in Africa.",
        "info_ar": "الجزائر أكبر دولة في أفريقيا.",
        "flight1": "9:00 AM",
        "flight2": "6:00 PM",
        "duration": "4 hours",
        "arrival": "1:00 PM",
        "price": "5500 EGP"
    },
    "tunisia": {
        "info_en": "Tunisia has beautiful beaches.",
        "info_ar": "تونس بها شواطئ جميلة.",
        "flight1": "8:00 AM",
        "flight2": "5:00 PM",
        "duration": "4 hours",
        "arrival": "12:00 PM",
        "price": "5000 EGP"
    },
    "egypt": {
        "info_en": "Egypt has pyramids and Nile.",
        "info_ar": "مصر بها الأهرامات والنيل.",
        "flight1": "11:20 AM",
        "flight2": "7:40 PM",
        "duration": "1:40 hours",
        "arrival": "2:30",
        "arrival": "-",
        "price": "1000 EGP"
    },
    
    "السعوديه":{    
        "info_en": "السعوديه has Mecca & Medina.",
        "info_ar": "السعودية بها مكة والمدينة.",
        "flight1": "8:00 AM",
        "flight2": "6:00 PM",
        "duration": "3 hours",
        "arrival": "11:00 AM",
        "price": "5000 EGP"
    },"الامارات": {
        "info_en": "UAE has Dubai and Abu Dhabi.",
        "info_ar": "الإمارات بها دبي وأبوظبي.",
        "flight1": "10:00 AM",
        "flight2": "8:00 PM",
        "duration": "3 hours",
        "arrival": "1:00 PM",
        "price": "4500 EGP"
    }, "مصر": {
        "info_en": "Egypt has pyramids and Nile.",
        "info_ar": "مصر بها الأهرامات والنيل.",
        "flight1": "11:20 AM",
        "flight2": "7:40 PM",
        "duration": "1:40 hours",
        "arrival": "2:30",
        "price": "1000 EGP"
    }
}

# =========================
# إرسال الرسالة
# =========================
def send_message():
    user_input = entry.get().lower().strip()

    if user_input == "":
        return

    chat_box.config(state="normal")
    chat_box.insert(tk.END, f"You: {user_input}\n", "user")

    if user_input in places:
        data = places[user_input]

        chat_box.insert(tk.END, "Bot:\n", "bot")

        # English
        chat_box.insert(tk.END, "----- English -----\n", "en")
        chat_box.insert(tk.END, f"{data['info_en']}\n", "en")
        chat_box.insert(tk.END, f"First Flight: {data['flight1']}\n", "en")
        chat_box.insert(tk.END, f"Second Flight: {data['flight2']}\n", "en")
        chat_box.insert(tk.END, f"Duration: {data['duration']}\n", "en")
        chat_box.insert(tk.END, f"Arrival: {data['arrival']}\n", "en")
        chat_box.insert(tk.END, f"Price: {data['price']}\n\n", "en")

        # Arabic
        chat_box.insert(tk.END, "----- العربية -----\n", "ar")
        chat_box.insert(tk.END, f"{data['info_ar']}\n", "ar")
        chat_box.insert(tk.END, f"✈️ أول طائرة: {data['flight1']}\n", "ar")
        chat_box.insert(tk.END, f"✈️ ثاني طائرة: {data['flight2']}\n", "ar")
        chat_box.insert(tk.END, f"🕒 مدة الرحلة: {data['duration']}\n", "ar")
        chat_box.insert(tk.END, f"⏰ وقت الوصول: {data['arrival']}\n", "ar")
        chat_box.insert(tk.END, f"💰 السعر: {data['price']}\n\n", "ar")

    else:
        chat_box.insert(tk.END, "Bot: Please enter a valid country ❌\n\n", "bot")

    chat_box.config(state="disabled")
    entry.delete(0, tk.END)
    chat_box.yview(tk.END)

# =========================
# النافذة
# =========================
root = tk.Tk()
root.title("Tourism Chatbot")
root.state("zoomed")

# الخلفية
img = Image.open("download.jpg")
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg = ImageTk.PhotoImage(img)

bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# الشات
chat_box = tk.Text(root, bg="#111111", fg="white",
                   font=("Arial", 14), bd=0)
chat_box.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

chat_box.tag_config("user", foreground="#38bdf8")
chat_box.tag_config("bot", foreground="#22c55e")
chat_box.tag_config("en", foreground="#38bdf8")
chat_box.tag_config("ar", foreground="#f3f4f4")
chat_box.tag_config("flight1", foreground="#847f6b")
chat_box.tag_config("flight2", foreground="#897525")


chat_box.insert(tk.END, "Bot: Enter a country in English 🌍\n\n", "bot")
chat_box.config(state="disabled")

# input
entry = tk.Entry(root, font=("Arial", 14))
entry.place(relx=0.1, rely=0.75, relwidth=0.6, height=40)

# زرار
btn = tk.Button(root, text="Send", command=send_message)
btn.place(relx=0.72, rely=0.75, relwidth=0.18, height=40)

root.bind("<Return>", lambda e: send_message())

root.mainloop()