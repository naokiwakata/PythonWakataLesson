# if文って知ってるか？
# プログラムは3つの基本となる処理が組み合わさってできるのだ
# 「順次」「分岐」「繰り返し」の3つのみ
# その中で「分岐」にあたるのが「if」

if True:
    print('True')
else:
    print('確実に条件式がTrueになるから実行されない')

name = "ROLAND"
isRoland = name == "ROLAND"
if isRoland:
    print('おれ')
else: 
    print('おれいがい')    

number = 9
isOdd = number % 2

if isOdd:
    print('奇数')
else:
    print('偶数')

print(type(isOdd)) # boolではなく...