# 関数って知ってる？

def twice(number):
  number = number *2
  return number

age = 20
age = twice(age)
print(age)

def greet(name):
    text = f'みんなおはよう! おれは{name} だ！　今日はゼミだけど資料何もできてないぜ！'
    return text

greeting = greet("ふじい")
print(greeting)

# 関数を使う目的は、処理の共通化や可読性の向上かなあ
# 何回も同じ処理書いていることがあれば関数にすると読みやすくなるで、あとメンテも楽