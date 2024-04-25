# セットアップと実行の手順
ご自身の環境にリポジトリをCloneした後、以下を実行してください。
```bash
python main.py
```

# プロジェクトにおける重要な設計やその設計理由
## 全体
- 1人のユーザーが実際の本棚に格納された本の読書状況を管理するために使用することを想定しています。
- 5つの関数が実行される度に、現在シェルフに登録されている本の一覧が表示されます。これは、各関数の中には、操作対象となる本の情報を参照する必要があるものが含まれるためです。
- また、ユーザーの認知負荷を下げるため、5つの関数が実行される度に、実行する関数と対応する番号の関係も表示されます。
## 本の追加
- ユーザーはリアルな本棚に本を追加した際や電子ブックを購入した際に、このアプリにも本を追加します。
- 同じ本を2冊登録することは想定していないため、登録済みのタイトルと重複したものを追加しようとすると、登録ができない仕様としました。
- また、空文字も登録できません。
## 本の編集
- 追加した本の内容に誤りがあった場合や、未読⇒既読になった際に、本の編集を行います。
- 指定したidの本の、タイトルと既読/未読の状態をそれぞれ編集できるようにしました。idを特定するためには、毎回プロンプトに出力される本の一覧を確認するか、後で述べる検索機能を使います。
- 本の追加と同様に、登録済みのタイトルと重複したものを追加しようとすると、登録ができない仕様となっています。
- ユーザーの入力の手間を軽減する目的で、ユーザーが空文字を入力した際には、元データを変更しないようにしました。これは、タイトルだけ、既読/未読の状態だけを編集するケースが多いことを想定したためです。
- ブックシェルフに対象idの本が存在しない場合には、ユーザーにその旨が伝えられます。処理は行われません。
## 本の検索
- 以下2つの検索が可能です。
    - 本のタイトルに含まれるキーワードで、該当する本の一覧を取得する：
        - 編集したい本のIDを特定するために使用する想定です。タイトルの認識には揺らぎがあることを想定し、キーワードに部分一致するものを出力するようにしました。
    - 既読/未読の条件に合致する本の一覧を取得する：
        - 次の読書対象とする未読の本を見つけたり、削除すべき既読の本を見つけるために使用することを想定しています。
## 本の削除
- 入力ミスや、本棚から処分した本を削除するために使用する想定です。
- 指定したIDの本を削除します。
- 対象IDが存在しない場合には、そのことがユーザーに通知されます。
## 統計情報の表示
- 指定の通りの実装です。
## アプリ終了
- 指定の通りの実装です。

# このツールまたはサービスの使い方の説明 (ユーザー向けの説明)
## これは何か？
- これは勉強家のエンジニアが本の未読/既読の状況を管理するためのサービスです。
- 紙の本、Kindle、楽天Kobo、O'Reillyで買った電子ブック、・・・etc。いろんなプラットフォームで本を買ってしまい大量の積読を抱えて困っているあなたを助けます！
## どうやって使うの？
- 使い方はシンプル（？）。ご自身の環境にリポジトリをCloneした後、まずは以下のコマンドを実行してアプリを起動しましょう！
```bash
python main.py
```
- 基本的にガイドに沿って本の追加や編集をすればOKです！
- アプリを終了すると、登録されている本が消えてしまうから気を付けましょう😢