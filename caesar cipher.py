import pyperclip

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

key=13

mode= 'decrypt' #set to either encrypt' or 'decrypt'.

SYMBOLS =  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated='' 

for symbol in message: 
    if symbol in SYMBOLS:
        symbolindex = SYMBOLS.find(symbol)
        if mode =='encrypt':
            translatedindex = symbolindex+key
        elif mode =='decrypt':
            translatedindex = symbolindex-key 
    
        if translatedindex>=len(SYMBOLS):
            translatedindex= translatedindex - len(SYMBOLS)
        elif translatedindex<0:
            translatedindex = translatedindex + len(SYMBOLS)

        translated = translated + SYMBOLS [translatedindex]
    else:
        translated = translated + symbol


print(translated)
pyperclip.copy(translated)
            