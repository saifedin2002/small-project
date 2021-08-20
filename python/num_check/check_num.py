"""

"""
import locale
def add_comma(num)  :
    f_num = f"{num:,}"
    to_list = f_num.split(",")
    first_part = " ".join(to_list[:-1])
    first_int = int(first_part)
    return first_int
    #return  f"{first_part:,}_{to_list[-1]}"

print(add_comma(1000000000))    
