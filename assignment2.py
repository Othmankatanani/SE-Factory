
# def reverse_and_concatenate(string, integer): # 1
#     if integer == 0:
#         return ""
    
#     reversed_s = string[::-1]  
#     concatenated_string = reversed_s * integer  
#     return concatenated_string


# user_string = input("Enter a string: ")
# user_integer = int(input("Enter an integer: "))


# result = reverse_and_concatenate(user_string, user_integer)


# print("Result:", result)


#*******************************************************



# def upper_lowercase(s): #2
#     upper_case = ''.join(ch for ch in s if ch.isupper())
#     lower_case = ''.join(ch for ch in s if ch.islower())
#     return upper_case + lower_case


# user_string = input("Enter a string: ")


# result = upper_lowercase(user_string)


# print("Result:", result)



#**********************************************************



# def same_string(string1, string2): #3
#     sorted_string1 = sorted(string1)
#     sorted_string2 = sorted(string2)
#     return sorted_string1 == sorted_string2


# user_string1 = input("Enter the first string: ")
# user_string2 = input("Enter the second string: ")


# result = same_string(user_string1, user_string2)


# print("Result:", result)


#************************************************************


# def max_min_equation(lst):  #4
#     if not lst:
#         return ""

#     max_num = lst[0]
#     min_num = lst[0]
#     max_index = 0
#     min_index = 0

#     for i in range(1, len(lst)):
#         if lst[i] > max_num:
#             max_num = lst[i]
#             max_index = i
#         elif lst[i] < min_num:
#             min_num = lst[i]
#             min_index = i

#     return max_num, max_index, min_num, min_index


# user_numbers = input("Enter a numbers with sapce between it : ")
# user_list = [int(num) for num in user_numbers.split()]


# max_number, max_index, min_number, min_index = max_min_equation(user_list)


# print("MAX number:", max_number)
# print("Index of MAX number:", max_index)
# print("MIN number:", min_number)
# print("Index of MIN number:", min_index)


#***************************************************************


# def count_lenght(n): #5
#     if n == 0:
#         return 1
#     elif n < 0:
#         n = -n
    
#     if n < 10:
#         return 1
#     else:
#         return 1 + count_lenght(n // 10)


# user_integer = input("Enter an integer: ")
# user_number = int(user_integer)


# result = count_lenght(user_number)


# print("Number of lenght:", result)


#**************************************************


# def list_jumps(jumps):
#     n = len(jumps)
#     index = 0
#     visited = set()

#     while index >= 0 and index < n:
#         if index in visited:
#             return "cycle"
#         visited.add(index)
#         index += jumps[index]

#     return "out-of-bounds"


# print(list_jumps([2, -1, 3, 0, 2]))   
# print(list_jumps([3, 2, -1, 1, 4]))   




#***************************************************************




# def generate_receipt(items): #POS System
#     total_amount = 0
#     print("Receipt:")
#     for item in items:
#         barcode, item_name, quantity, unit_price = item
#         item_total = total_cost(quantity, unit_price)
#         print(f"{item_name} x {quantity} = {item_total:.2f}")
#         total_amount += item_total
#     print("Total: {:.2f}".format(total_amount))
#     print()


# def total_cost(quantity, unit_price): 
#     return quantity * unit_price



# def pos_system():
#     while True:
#         start_receipt = input("Start a new receipt? (yes/no): ").lower()
#         if start_receipt == "no":
#             break
#         elif start_receipt == "yes":
#             items = []
#             while True:
#                 barcode = input("Enter the item barcode (or 'no' to finish the receipt): ")
#                 if barcode.lower() == "no":
#                     break
#                 item_name = input("Enter the item name: ")
#                 quantity = int(input("Enter the quantity purchased: "))
#                 unit_price = float(input("Enter the unit price: "))
#                 items.append((barcode, item_name, quantity, unit_price))

#             generate_receipt(items)


# pos_system()

