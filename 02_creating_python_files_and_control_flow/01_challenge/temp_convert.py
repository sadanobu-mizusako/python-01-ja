def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    temp = float(input("温度を入力してください: "))
    unit = input("温度の単位（c or f）を入力してください: ") # c or f

    if (unit == "f"):
        "f to c"
        temp = (temp-32.0)*5.0/9.0
    else:
        "c to f"
        temp = (temp * 9.0/5.0)+32.0

    return temp


convert()
