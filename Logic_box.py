print("Welcome! Time to explore numbers and shapes.")
while True:
    print("\nSelect your mode: ") 
    print("1. Generating your pattern: ")
    print("2. Decoding your number range: ")
    print("3. Exit: ") 
    w = int(input("Enter your choice: ")) 
    match w:
        case 1:
            n = int(input("\nPattern height (in rows): "))
            if n<0:
                print("Keep it moving forward—positive numbers only.")
            for i in range(1,n+1):
                for j in range(1,i+1):
                    print("*",end="")
                print()   
        case 2:
            x = int(input("\nEnter the start point: "))
            y = int(input("Enter the end point: "))
            if x<0 or y<0:
                print("Keep it moving forward—positive numbers only.") 
                continue 
            sum = 0
            for i in range(x,y+1):
                sum+=i
                if i%2==0:
                    print(f"{i} is even number") 
                else:
                    print(f"{i} is odd number.") 
            print(f"Sum of all numbers between {x} and {y} = {sum}")    
        case 3: 
            print("Session closed. GoodBye.")
            break  
        case _: 
            print("Data mismatch detected. Re-enter valid input.")        