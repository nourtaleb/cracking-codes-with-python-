message = input ('enter message: ')

key = int( input('enter key: ').strip())

mode = int(input ('enter  mode, 0 for decrypt, 1 for encrypt: ').strip()) == 0 

SYMBOLS =  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated='' 

for symbol in message: 
    if symbol in SYMBOLS:
        symbolindex = SYMBOLS.find(symbol)
        if mode ==False:
            translatedindex = symbolindex+key
        elif mode ==True:
            translatedindex = symbolindex-key 
    
        if translatedindex>=len(SYMBOLS):
            translatedindex= translatedindex - len(SYMBOLS)
        elif translatedindex<0:
            translatedindex = translatedindex + len(SYMBOLS)

        translated = translated + SYMBOLS [translatedindex]
    else:
        translated = translated + symbol


print(translated)
# pyperclip.copy(translated)

print('im a new change')
