import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items

# 2. Добавь товар в чек

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
    
        self.__name_items.append(name)
        self.__number_items += 1

# 3. Удали товар из чека

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

# 4. Посчитай общую стоимость товаров

    def check_amount(self):
        total = 0
        for item in self.__name_items:
            total += self.__item_price[item]
    
        if self.__number_items > 10:
            total *= 0.9
    
        return total

#5. Вычисли НДС для товаров со ставкой 20%

    def twenty_percent_tax_calculation(self):
        total_tax = 0.0
    
        discount = 0.9 if self.__number_items > 10 else 1.0
    
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                total_tax += self.__item_price[item] * discount * 0.2
    
        return total_tax

#6. Вычисли НДС для товаров со ставкой 10%

    def ten_percent_tax_calculation(self):
        discount = 0.9 if self.__number_items > 10 else 1.0
    
        total_tax = 0.0
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                total_tax += self.__item_price[item] * discount * 0.1
    
        return total_tax

#7. Посчитай общую сумму налогов

    def total_tax(self):
       
       return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

#8. Верни номер телефона покупателя

    @staticmethod
    def get_telephone_number(telephone_number):

        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
    
        num_str = str(telephone_number)
    
        if len(num_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
    
        return f"+7{num_str}"
#проверка 8 задания
print(OnlineSalesRegisterCollector.get_telephone_number(1234567890))
try:
    print(OnlineSalesRegisterCollector.get_telephone_number("1234567890"))
except ValueError as e:
    print(e)
try:
    print(OnlineSalesRegisterCollector.get_telephone_number(12345))
except ValueError as e:
    print(e)