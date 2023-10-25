ilk= kelime[0].lower()

if ilk== "a" or ilk== "e" or ilk== "ı" or ilk=="i" or ilk=="u" or ilk=="ü" or ilk=="o" or ilk=="ö":
    print("yeni kelime şu= ", kelime+"way" )
else:
    print("Yeni kelime şu= ", kelime[1:-1].lower()+ilk+"ay")