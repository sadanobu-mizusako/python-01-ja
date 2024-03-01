import os


def ls_command(directory):
    # ユーザー入力が「sample」の場合、ディレクトリは「sample」になります
    # 無効なディレクトリパスについて考える必要はありません

    # 「pass」を削除して、ここにコードを書いてください
    files = os.listdir(directory)
    extensions = [os.path.splitext(f)[1] for f in files if os.path.splitext(f)[1]!=""]
    dict_extension = {k: extensions.count(k) for k in set(extensions)}
    extension_sorted = sorted(dict_extension.items(), key=lambda x:x[0])


    print("Summary in alphabetical order:")
    for k, v in extension_sorted:
        if v==1:
            print(k+":"+str(v)+" file")
        else:
            print(k+":"+str(v)+" files")

if __name__ == "__main__":
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
