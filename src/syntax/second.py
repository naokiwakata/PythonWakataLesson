# クラスって知ってる？

class Human:
    # コンストラクタを定義
    def __init__(self, name, year):

        # メンバ
        self.name = name
        self.year = year
    
naoki = Human('WAKATA NAOKI',20)
print(naoki.name)
print(type(naoki))