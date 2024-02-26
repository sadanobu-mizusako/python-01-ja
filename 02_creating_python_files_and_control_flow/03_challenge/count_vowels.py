# ここにコードを書いてください
input_string = input("Enter a string: ")

cnt = 0
for c in input_string:
    if c in "aiueo":
        cnt += 1

print("Number of vowels:" + str(cnt))