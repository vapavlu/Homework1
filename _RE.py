import re

def normalize_phone(phone_number):
    # Видалення всіх символів, крім цифр та (+)
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Перевірка, чи номер починається з міжнародного коду
    if cleaned_number.startswith('380'):
        # Додавання (+)
        cleaned_number = '+' + cleaned_number
    else:
        # Додавання  (+38)
        cleaned_number = '+38' + cleaned_number
    
    return cleaned_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11"
]
normalize_phonsanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(normalize_phonsanitized_numbers)