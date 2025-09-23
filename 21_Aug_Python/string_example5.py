name=input("Enter name ")
total_len = len(name)
half_len = total_len//2
print(half_len)
first_part = name[:half_len]
last_part = name[half_len:]
print(f" First Part {first_part} Last {last_part} ")
final_str = last_part+first_part
print(f"Final Result {final_str} ")
