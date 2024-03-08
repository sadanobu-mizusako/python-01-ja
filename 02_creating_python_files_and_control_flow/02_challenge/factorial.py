def compute_factorial():
    # ここにコードを書いてください
    # number変数を編集し、ユーザー入力として正の整数を受け取ります。整数に変換することを忘れないでください
    number = input("正の整数をインプットしてください: ")
    number = int(number)

    # result変数を編集し、最終的な計算結果を保存します
    result = 1
    for i in range(number):
        result *= (i + 1)

    return result


compute_factorial()
