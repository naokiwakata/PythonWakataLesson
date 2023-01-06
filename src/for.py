# みなさんお馴染みのfor文
# 「順次」「分岐」「繰り返し」のうちの「繰り返し」
# Pythonはいろいろなfor文の書き方があるよ

# listに対してfor文を使用する（頻出）
members = ["wakata","takai","fuji","terazawa"]
for member in members:
    print(member)

# range関数、indexでfor文回す。
for i in range(5):# 0,1,2,3,4と i が増えていく
    print(i)

# indexを同時に参照する
for i, member in enumerate(members):
    print(f'{i+1}番目のメンバーは{member}だぜ')

# break：条件に当てはまった場合に繰り返し処理を終わらせる
for member in members:
    print(member)
    if member == "fuji":
        print(f'{member}で終了')
        break

# continue：条件に当てはまった場合にとばす
for member in members:
    if member == "takai":
        continue
    print(member)