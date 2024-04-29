from datetime import datetime

def get_days_from_today(date):
    # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
    past_date = datetime.strptime(date, '%Y-%m-%d')
    
    today_date = datetime.today()
    
    difference = today_date - past_date
    
    
    return difference.days

# Приклад 
date = '2023-04-16'
print(get_days_from_today(date)) 