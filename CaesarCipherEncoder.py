print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

while True:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = list(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))
    shift = shift%26

    if direction == "encode":
        for i in text:
            z = alphabet.find(i)
            new = z+shift
            text[text.index(i)] = alphabet[new]
    else:
        for i in text:
            z = alphabet.find(i)
            new = z-shift
            text[text.index(i)] = alphabet[new]
    print(f"Encoded result --> {''.join(text)}")
    dec = input("Wanna Continue (Yes/No) : ").lower
    if dec == "no":
        break