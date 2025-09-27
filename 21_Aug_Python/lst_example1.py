lst_numbers=[12,34,56,78]

print(f"Original list {lst_numbers}")
lst_numbers.append(900)
print(f"After append {lst_numbers}")
lst_numbers.append(450)
print(f"After append {lst_numbers}")
lst1_number=[900,78,345]
lst_numbers.append(lst1_number)
print(f"After append {lst_numbers}")
print(lst_numbers[6])

# append and extends

lst=['Ahemdabad',"Baroda"]
lst1=['Udaipur','Jaipur']
#lst.append(lst1)
lst.extend(lst1)
print(lst)
