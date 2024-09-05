# Given Input name, middle name, and surname of a person and print only the initials.

def initial_letter(first_name, middle_name, last_name):
    return first_name[0].upper() + middle_name[0].upper() + last_name[0].upper()


first_name = "kinjal"
middle_name = "I"
last_name = "patel"

name = initial_letter(first_name, middle_name, last_name)
print(name)
