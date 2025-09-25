while True:

    print(" \n1. Convert into Uppercase  \n2. Convert into Lowercase  \n3. Find length  \n4. Replace  \n5. Exit ")
    choice = int(input("Please enter your choice : "))
    match choice:
        case 1:
            string=input("Pelase enter string that want to convert in upper")
            print(f"Converted string is {string.upper()}")
        case 2: 
            string=input("Pelase enter string that want to convert in lower")
            print(f"Converted string is {string.lower()}")
        case 3:
            string=input("Pelase enter string , find length ")
            print(f"Converted string is {len(string)}")
        case 4:
            string=input("Pelase enter string ")
            old_str=input("Pelase enter string that you want to replace ")
            new_str=input("Please enter new string that you want to replace ")
            print(f"After replace {string.replace(old_str,new_str)}")
        case 5:
            break
        case _:
            print("Enter valid choice ")