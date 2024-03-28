def main():
    """
    メイン処理を定義した関数。プログラム起動時にこの関数が呼び出される
    """
    # 本のデータを含むリストの初期化
    book_list = []
    # book idの初期化。本が追加される毎に加算される。これまでに追加された本の冊数合計に合致するように更新される
    count_added = 0

    # 起動時の表示
    print("===============================================")
    print("Welcome to your personal books digital library!")
    print("===============================================")
    while True:
        # コマンドのガイドを毎回表示する
        show_guid()

        command = input()
        if command=='1':
            book_list, count_added = add_book(book_list, count_added)
        elif command=='2':
            book_list = edit_book(book_list)
        elif command=='3':
            search_book(book_list)
        elif command=='4':
            book_list = delete_book(book_list)
        elif command=='5':
            show_stats(book_list)
        elif command=='6':
            print("Exit app")
            return
        else:
            print("Invalid input!")
        
        # 現在のブックシェルフの状態を毎処理実行後に必ず表示する
        show_all_books(book_list)

def show_guid():
    """
    コマンドに対応する数字を表示する関数
    """
    print("")
    print("1: Add a Book")
    print("2: Edit a Book")
    print("3: Search for Books")
    print("4: Delete a Book")
    print("5: View Library Stats")
    print("6: Exit app")
    print("Please select from 1 to 6")
    return

def add_book(book_list, count_added):
    """
    book_listに新しい本を追加する関数。処理が成功した場合、book_idに1加算して更新する
    """
    # タイトルの入力処理
    while True:
        title = input("追加する本のタイトルを入力してください。")
        if title=="":
            print("１文字以上のタイトルを入力してください。")
        elif title in [book["title"] for book in book_list]: #既に追加されているタイトルとの重複を確認
            print("このタイトルは既に登録されています。登録されていないタイトルを追加してください。")
        else:
            break
    
    # read_statusの入力処理（True：既読、False：未読）
    while True:
        read_status = input("既読・未読の状態を1 or 2で入力してください（1: 既読、2: 未読）。")
        if read_status == "1":
            read_status = True
            break
        elif read_status == "2":
            read_status = False
            break
        else:
            print("Invalid input! 1か2を入力してください。")

    # book_listの更新
    added_book = {"id":count_added, "title": title, "read_status": read_status} 
    book_list.append(added_book)
    print("以下の本が追加されました。")
    print(added_book)
    return book_list, count_added+1

def edit_book(book_list):
    """
    ユーザーが指定したidのbook_listを更新する関数
    """
    target_id = input("編集する本のIDを入力してください。")

    for i in range(len(book_list)):
        if str(book_list[i]["id"])==target_id:
            print("これから以下の本の編集を行います。")
            print(book_list[i])
            # タイトルの編集
            while True:
                title = input("タイトルを編集してください。変更しない場合、Enterを押してください。")
                if title=="":
                    title = book_list[i]["title"]
                    break
                elif title in [book["title"] for book in book_list if book["id"]!=i]: #既に追加されているタイトルとの重複を確認
                    print("このタイトルは既に登録されています。登録されていないタイトルを追加してください。")
                else:
                    break
            
            # 既読/未読状態の編集
            while True:
                read_status = input("既読・未読の状態を編集してください（1: 既読、2: 未読）。変更しない場合、Enterを押してください。")
                if read_status=="":
                    read_status = book_list[i]["read_status"]
                    break
                elif read_status == "1":
                    read_status = True
                    break
                elif read_status == "2":
                    read_status = False
                    break
                else:
                    print("Invalid input! 1か2を入力してください。")

            # book_listを更新して処理終了
            edited_book = {"id": book_list[i]["id"], "title": title, "read_status": read_status}
            print("以下の編集を行います。")
            print("編集前：", book_list[i])
            print("編集後：", edited_book)
            book_list[i] = edited_book
            return book_list

    print("指定されたidは存在しません。")
    return book_list

def search_book(book_list):
    """
    book_listから検索条件に合致する本を抽出し、表示する関数。タイトルに検索文字列が含まれる本の一覧を表示する
    """
    # 検索方法
    while True:
        print("検索方法を選択してください。")
        print("1: キーワード検索")
        print("2: 既読/未読による検索")
        search_option = input("")
        if (search_option!="1")and(search_option!="2"):
            print("入力エラーです。1 または 2を入力してください。")
        else:
            break
        
    if search_option=="1":
        # 検索キーワードの入力処理
        while True:
            key_word = input("検索キーワードを入力してください。")
            if key_word=="":
                print("１文字以上の検索キーワードを入力してください。")
            else:
                break
        # 検索の実行
        search_result = [] #検索結果の初期化
        for book in book_list:
            if key_word in book["title"]:
                search_result.append(book)
    elif search_option=="2":
        # 既読/未読の入力処理
        print("既読の本を検索するか、未読の本を検索する選択してください。")
        print("1: 既読")
        print("2: 未読")
        while True:
            key_word = input("")
            if key_word != "1" and key_word != "2":
                print("入力エラーです。1 または 2を入力してください。")
            else:
                break
        # 検索の実行
        search_result = [] #検索結果の初期化
        read_status = (key_word == "1")
        for book in book_list:
            if read_status == book["read_status"]:
                search_result.append(book)
    
    # 検索結果の表示
    print("検索条件に該当する本は%i冊でした。" %(len(search_result)))
    if len(search_result)>0:
        print(search_result)

    return

def delete_book(book_list):
    """
    book_listから指定されたidの本を削除する関数
    """
    target_id = input("削除する本のIDを入力してください。")
    for i in range(len(book_list)):
        if str(book_list[i]["id"])==target_id:
            deleted_book = book_list.pop(i)
            print("以下の本を削除しました。")
            print(deleted_book)
            return book_list

    print("指定されたidは存在しません。")
    return book_list

def show_stats(book_list):
    """
    book_listの統計情報（本の総数、既読の本の数、未読の本の数）を表示する関数
    """
    total_books = len(book_list)
    # 既読の冊数を求める
    count_read = 0 #既読冊数の初期化
    for book in book_list:
        if book["read_status"]:
            count_read+=1

    print("登録されている本の総数は%i冊。うち既読は%i冊、未読は%i冊です。"%(total_books,count_read,total_books-count_read))
    return 

def show_all_books(book_list):
    """
    登録されているすべての本の状態を表示する関数
    """
    print("現在のブックシェルフの状態です。")
    for book in book_list:
        print(book)
    return

main()