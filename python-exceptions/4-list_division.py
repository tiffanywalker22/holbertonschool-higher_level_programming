#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            num1 = my_list[i] if i < len(new_list1) else 0
            num2 = my_list[i] if i < len(new_list2) else 0

            if not isinstance(num1, (int, float)) or not isinstance(num2, (int,float)):
                raise TypeError("wrong type")
            
            if num2 == 0:
                raise ZeroDivisionError("divide by 0")
            division_result = num1 / num2
            result.append (division_result)
