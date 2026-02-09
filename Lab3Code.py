
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont

# Определение продукционных правил
rules = [
    [1, {
        "Время суток": "Ночь",
        "Люди в доме": "Нет",
        "Сезон": "Зима",
        "Погода": "Холодно"
    }, "Снизить температуру отопления до 16°С и отключить несущественное освещение"],

    [2, {
        "Время суток": "День",
        "Люди в доме": "Нет",
        "Сезон": "Лето",
        "Погода": "Солнечно"
    }, "Закрыть жалюзи для затемнения, отключить кондиционер и использовать естественное освещение"],

    [3, {
        "Время суток": "Вечер",
        "Люди в доме": "Есть",
        "Сезон": "Осень",
        "Погода": "Пасмурно"
    }, "Включить энергосберегающее освещение с датчиками движения и установить температуру 20°С"],

    [4, {
        "Время суток": "День",
        "Люди в доме": "Есть",
        "Сезон": "Весна",
        "Погода": "Солнечно"
    }, "Открыть жалюзи для естественного освещения и отключить искусственное освещение в освещённых комнатах"],

    [5, {
        "Время суток": "Утро",
        "Люди в доме": "Нет",
        "Сезон": "Зима",
        "Погода": "Холодно"
    }, "Перевести систему в режим «Отсутствие»: отопление 15°С, отключить все розетки кроме холодильника"],

    [6, {
        "Время суток": "Вечер",
        "Люди в доме": "Есть",
        "Сезон": "Лето",
        "Погода": "Дождь"
    },
     "Включить кондиционер на энергоэффективный режим (24°С) и активировать локальное освещение только в используемых зонах"]
]

# Создание основного окна
root = tk.Tk()
root.title("Умный дом: Оптимизация энергопотребления")
root.geometry("800x650")
root.resizable(False, False)
root.configure(bg="#f5f7fa")

# Стилизация
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#f5f7fa", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11, "bold"), padding=10)
style.configure("TCombobox", font=("Arial", 11), padding=5)
style.configure("Header.TLabel", font=("Arial", 16, "bold"), foreground="#2c3e50", background="#f5f7fa")
style.configure("Result.TFrame", background="white", relief="solid", borderwidth=1)

# Заголовок
header_frame = tk.Frame(root, bg="#3498db", height=80)
header_frame.pack(fill="x")
tk.Label(header_frame, text="СИСТЕМА ОПТИМИЗАЦИИ ЭНЕРГОПОТРЕБЛЕНИЯ",
         font=("Arial", 18, "bold"), bg="#3498db", fg="white").pack(pady=20)

# Основной контейнер
main_frame = tk.Frame(root, bg="#f5f7fa", padx=30, pady=20)
main_frame.pack(fill="both", expand=True)

# Поля ввода параметров
input_frame = tk.Frame(main_frame, bg="#f5f7fa")
input_frame.pack(fill="x", pady=(0, 25))

# Время суток
tk.Label(input_frame, text="Время суток:", font=("Arial", 12, "bold"), bg="#f5f7fa", anchor="w").grid(row=0, column=0,
                                                                                                      sticky="w",
                                                                                                      pady=8)
time_var = tk.StringVar(value="День")
time_combo = ttk.Combobox(input_frame, textvariable=time_var, state="readonly", width=25, font=("Arial", 11))
time_combo["values"] = ["Утро", "День", "Вечер", "Ночь"]
time_combo.grid(row=0, column=1, padx=20, pady=8, sticky="w")

# Наличие людей
tk.Label(input_frame, text="Люди в доме:", font=("Arial", 12, "bold"), bg="#f5f7fa", anchor="w").grid(row=1, column=0,
                                                                                                      sticky="w",
                                                                                                      pady=8)
people_var = tk.StringVar(value="Есть")
people_combo = ttk.Combobox(input_frame, textvariable=people_var, state="readonly", width=25, font=("Arial", 11))
people_combo["values"] = ["Есть", "Нет"]
people_combo.grid(row=1, column=1, padx=20, pady=8, sticky="w")

# Сезон
tk.Label(input_frame, text="Сезон года:", font=("Arial", 12, "bold"), bg="#f5f7fa", anchor="w").grid(row=2, column=0,
                                                                                                     sticky="w", pady=8)
season_var = tk.StringVar(value="Лето")
season_combo = ttk.Combobox(input_frame, textvariable=season_var, state="readonly", width=25, font=("Arial", 11))
season_combo["values"] = ["Зима", "Весна", "Лето", "Осень"]
season_combo.grid(row=2, column=1, padx=20, pady=8, sticky="w")

# Погода
tk.Label(input_frame, text="Погодные условия:", font=("Arial", 12, "bold"), bg="#f5f7fa", anchor="w").grid(row=3,
                                                                                                           column=0,
                                                                                                           sticky="w",
                                                                                                           pady=8)
weather_var = tk.StringVar(value="Солнечно")
weather_combo = ttk.Combobox(input_frame, textvariable=weather_var, state="readonly", width=25, font=("Arial", 11))
weather_combo["values"] = ["Солнечно", "Пасмурно", "Дождь", "Холодно"]
weather_combo.grid(row=3, column=1, padx=20, pady=8, sticky="w")

# Кнопка анализа
analyze_btn = ttk.Button(main_frame, text="Анализировать энергопотребление",
                         command=lambda: analyze_energy(), style="TButton")
analyze_btn.pack(pady=15, ipadx=20)

# Рамка для результата
result_frame = tk.Frame(main_frame, bg="white", relief="solid", borderwidth=1, padx=25, pady=20)
result_frame.pack(fill="both", expand=True)

result_title = tk.Label(result_frame, text="Результат анализа",
                        font=("Arial", 14, "bold"), bg="white", fg="#2c3e50")
result_title.pack(anchor="w", pady=(0, 15))

result_text = tk.Text(result_frame, wrap="word", font=("Arial", 11), bg="white",
                      relief="flat", height=12, padx=10, pady=10)
result_text.pack(fill="both", expand=True)
result_text.configure(state="disabled")

status_label = tk.Label(root, text="Готово к анализу",
                        font=("Arial", 10), bg="#ecf0f1", fg="#7f8c8d", anchor="w", padx=20, pady=8)
status_label.pack(fill="x", side="bottom")


# Функция анализа
def analyze_energy():
    # Сбор фактов
    facts = {
        "Время суток": time_var.get(),
        "Люди в доме": people_var.get(),
        "Сезон": season_var.get(),
        "Погода": weather_var.get()
    }

    # Поиск совпадений
    matched_rules = []
    for rule_id, conditions, recommendation in rules:
        matches = sum(1 for key, value in conditions.items() if facts.get(key) == value)
        total_conditions = len(conditions)
        matched_rules.append((rule_id, recommendation, matches, total_conditions))

    # Сортировка по совпадениям
    matched_rules.sort(key=lambda x: x[2], reverse=True)
    best_rule = matched_rules[0]

    # Формирование результата
    result_text.configure(state="normal")
    result_text.delete("1.0", "end")

    # Цветовая индикация фона результата
    if best_rule[2] == 4:
        result_frame.configure(bg="#d4edda")
        result_title.configure(bg="#d4edda", fg="#155724")
        status_label.configure(text="✓ Точное совпадение найдено", bg="#d4edda", fg="#155724")
        result_text.insert("end", "✅ ТОЧНОЕ СОВПАДЕНИЕ\n\n", "exact")
        result_text.insert("end", f"Правило №{best_rule[0]}\n\n", "rule_num")
        result_text.insert("end", "РЕКОМЕНДАЦИЯ:\n", "header")
        result_text.insert("end", best_rule[1], "recommendation")
        result_text.tag_configure("exact", font=("Arial", 12, "bold"), foreground="#155724")
        result_text.tag_configure("rule_num", font=("Arial", 11, "bold"), foreground="#2c3e50")
        result_text.tag_configure("header", font=("Arial", 11, "bold"), foreground="#27ae60")
        result_text.tag_configure("recommendation", font=("Arial", 11), foreground="#2c3e50", lmargin1=10, lmargin2=20)
    elif best_rule[2] >= 2:
        result_frame.configure(bg="#fff3cd")
        result_title.configure(bg="#fff3cd", fg="#856404")
        status_label.configure(text="⚠ Частичное совпадение", bg="#fff3cd", fg="#856404")
        result_text.insert("end", "⚠ ЧАСТИЧНОЕ СОВПАДЕНИЕ\n\n", "partial")
        result_text.insert("end", f"Правило №{best_rule[0]} (совпадений: {best_rule[2]}/4)\n\n", "rule_num")
        result_text.insert("end", "ОСНОВНАЯ РЕКОМЕНДАЦИЯ:\n", "header")
        result_text.insert("end", best_rule[1] + "\n\n", "recommendation")
        result_text.insert("end", "ДОПОЛНИТЕЛЬНЫЕ СОВЕТЫ:\n", "header2")

        # Дополнительные рекомендации на основе времени суток и сезона
        tips = []
        if facts["Время суток"] == "Ночь":
            tips.extend(["• Отключить все неиспользуемые электроприборы",
                         "• Установить минимальную температуру в спальных зонах"])
        elif facts["Время суток"] == "День" and facts["Погода"] == "Солнечно":
            tips.extend(["• Максимально использовать естественное освещение",
                         "• Открыть шторы/жалюзи для прогрева помещения (зимой)"])
        elif facts["Сезон"] == "Зима":
            tips.extend(["• Поддерживать базовую температуру не ниже 18°С",
                         "• Проверить работу терморегуляторов на радиаторах"])
        elif facts["Сезон"] == "Лето":
            tips.extend(["• Использовать вентиляцию в утренние и вечерние часы",
                         "• Ограничить работу тепловыделяющих приборов в дневное время"])

        for tip in tips:
            result_text.insert("end", tip + "\n", "tip")

        result_text.tag_configure("partial", font=("Arial", 12, "bold"), foreground="#856404")
        result_text.tag_configure("rule_num", font=("Arial", 11), foreground="#856404")
        result_text.tag_configure("header", font=("Arial", 11, "bold"), foreground="#d35400")
        result_text.tag_configure("header2", font=("Arial", 11, "bold"), foreground="#e67e22", lmargin1=0, lmargin2=0)
        result_text.tag_configure("recommendation", font=("Arial", 11), foreground="#2c3e50", lmargin1=10, lmargin2=20)
        result_text.tag_configure("tip", font=("Arial", 11), foreground="#7f8c8d", lmargin1=15, lmargin2=25)
    else:
        result_frame.configure(bg="#e2e8f0")
        result_title.configure(bg="#e2e8f0", fg="#4a5568")
        status_label.configure(text="ℹ Рекомендация на основе времени суток и сезона", bg="#e2e8f0", fg="#4a5568")
        result_text.insert("end", "ℹ БАЗОВАЯ РЕКОМЕНДАЦИЯ\n\n", "basic")
        result_text.insert("end", f"Для времени суток «{facts['Время суток']}» в сезон «{facts['Сезон']}»:\n\n",
                           "context")

        # Дефолтные рекомендации
        if facts["Время суток"] == "Ночь":
            result_text.insert("end", "• Снизить общее освещение до минимума\n", "tip")
            result_text.insert("end",
                               "• Установить температуру отопления/кондиционирования на экономичный ночной режим\n",
                               "tip")
        elif facts["Время суток"] == "День":
            result_text.insert("end", "• Использовать естественное освещение\n", "tip")
            result_text.insert("end", "• Отключить свет в неиспользуемых помещениях\n", "tip")
        elif facts["Время суток"] == "Вечер":
            result_text.insert("end", "• Включить освещение только в активных зонах\n", "tip")
            result_text.insert("end", "• Настроить таймеры для автоматического отключения приборов\n", "tip")

        if facts["Сезон"] == "Зима":
            result_text.insert("end", "\n• Оптимизировать работу отопления: 18-20°С в жилых зонах\n", "tip")
        elif facts["Сезон"] == "Лето":
            result_text.insert("end", "\n• Использовать кондиционер с установкой температуры не ниже 24°С\n", "tip")

        result_text.tag_configure("basic", font=("Arial", 12, "bold"), foreground="#4a5568")
        result_text.tag_configure("context", font=("Arial", 11, "italic"), foreground="#2c3e50")
        result_text.tag_configure("tip", font=("Arial", 11), foreground="#4a5568", lmargin1=15, lmargin2=25)

    result_text.configure(state="disabled")


# Горячая клавиша для анализа (Enter)
root.bind('<Return>', lambda event: analyze_energy())

# Запуск приложения
root.mainloop()