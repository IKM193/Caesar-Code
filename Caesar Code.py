#暗号化したい文章
message = "暗号化したい文章"

key = 1  #どれだけずらすか

mode = "encrypt"  #暗号化->encrypt 復号->decrypt

SYMBOLS = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

translated = ""

for symbol in message: #一文字ずつ暗号化
    if symbol in SYMBOLS:
        symbolIndex=SYMBOLS.find(symbol) #symbolの中身がSYMBOLSの何番目のインデックスにあるか調べる
        if mode == "encrypt":
            translatedIndex = symbolIndex + key
        elif mode =="decrypt":
            translatedIndex = symbolIndex - key
        if translatedIndex >= len(SYMBOLS): #持っているインデックスより大きい場合
            translatedIndex = translatedIndex - len(SYMBOLS)     
        elif translatedIndex < 0:#持っているインデックスより小さい場合
            translatedIndex = translatedIndex + len(SYMBOLS) 
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated =translated + symbol

print(translated)