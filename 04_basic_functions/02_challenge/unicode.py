def encode(message):
    encoded = []
    for c in message:
        encoded.append(str(ord(c)))
    
    return " ".join(encoded)

def decode(message):
    unicode_list = message.split()
    decoded_list = [chr(int(i)) for i in unicode_list]
    # result = ""
    # for i in unicode_list:
    #     result += chr(int(i))
    return "".join(decoded_list)

print(encode("Hello World"))
print(decode("72 101 108 108 111 32 119 111 114 108 100"))