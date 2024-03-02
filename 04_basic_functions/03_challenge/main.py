def unique_substrings(input_string):
    # 「pass」を削除して、ここにコードを書いてください
    result_list = []
    for i in range(len(input_string)):
        for j in range(i+1, len(input_string)+1):
            if input_string[i:j] in result_list:
                pass
            else:
                result_list.append(input_string[i:j])
    return result_list

input_string = "banana"
print(unique_substrings(input_string))
