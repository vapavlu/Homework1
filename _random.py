import random 

def get_numbers_ticket (min_num,max_num,quantity):
    if min_num < 1 or max_num + 1> 1000 or quantity < 1 or quantity > (max_num - min_num + 1):#параметри
        return [] 
    lottery_numbers = random.sample(range(min_num, max_num,),quantity)
    return sorted(lottery_numbers) # 
print ("Ваші номери",get_numbers_ticket(1,49,5)) #підставляємо числа з задачі
print ("Ваші номери ",get_numbers_ticket(0,20,21))