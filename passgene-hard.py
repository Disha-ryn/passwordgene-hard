import random
letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm', 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' ,  'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
numbers = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
symbols = ['!' , '#' , '$' , '%' , '&' , '*' ,  '+']
print("Welcome to Password Generator!")
ur_letter = int(input("How many letters would u like in your password? "))    
ur_numbers = int(input("How many numbers would u like in your password? "))   
ur_symbols = int(input("How many symbols would u like in your password? "))  
#hard level
password_list = []
for char in range(0 , ur_letter):
    password_list.append(random.choice(letters))
 
for char in range(0 , ur_numbers ):
    password_list.append(random.choice(numbers))

for char in range(0 , ur_symbols ):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)    

password =""
for char in password_list:
    password += char
         

        
print(f"Your Final Password is {password}")
