while True:
    answer = input("Choose between encryption mode and decryption mode (encrypt/decrypt/exit): ")
    if answer == "encrypt":

        print("TO USE: Insert text you wish to encrypt in the space following \"Encrypt:\", and type in the shift value you want and the characters in the encrypt input's text will be shifted accordingly.")

        encryptee = input("Encrypt: ")
        while True:
            caesar = input("Shift: ")
            if not caesar.isdigit():
                print("Invalid shift value.")
            else: break

        cryptvalue = int(caesar)
        cipher_text = " "

        for aaa in encryptee:
            if aaa.isalpha():
                if aaa.isupper():
                    start = int(ord('A'))
                    end = int(ord('Z'))
                else:
                    start = int(ord('a'))
                    end = int(ord('z'))
                asciizd = ord(aaa)
                alg = asciizd + cryptvalue
                if alg > end:
                    alg = start + (alg - end - 1)
                encrypted = chr(alg)
                cipher_text += encrypted
            else:
                cipher_text += aaa
        print(f"Encrypted message: {cipher_text}")
        
    elif answer == "decrypt":
        encryptee = input("Decrypt: ")
        while True:
            caesar = input("Shift: ")
            if not caesar.isdigit():
                print("Invalid shift value.")
            else: break

        cryptvalue = int(caesar)
        cipher_text = " "

        for aaa in encryptee:
            if aaa.isalpha():
                if aaa.isupper():
                    start = int(ord('A'))
                    end = int(ord('Z'))
                else:
                    start = int(ord('a'))
                    end = int(ord('z'))
                asciizd = ord(aaa)
                alg = asciizd - cryptvalue
                if alg < start:
                    alg = end + 1 - (start - alg)
                encrypted = chr(alg)
                cipher_text += encrypted
            else:
                cipher_text += aaa
        print(f"Decoded message: {cipher_text}")
    elif answer == "exit": break
    else:
        print("Invalid Response")