def counter():
    occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]

    # ここにコードを書いてください
    occurrences = {k: fruits.count(k) for k in set(fruits)}
    for (k ,v) in occurrences.items():
        print(k+": "+str(v))

    return occurrences

print(counter())
