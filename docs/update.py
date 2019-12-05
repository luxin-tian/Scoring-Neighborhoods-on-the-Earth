text = '''Interactive map saved to ./vis/pp2_Amsterdam_safety.html
Interactive map saved to ./vis/pp2_Atlanta_safety.html
Interactive map saved to ./vis/pp2_Bangkok_safety.html
Interactive map saved to ./vis/pp2_Barcelona_safety.html
Interactive map saved to ./vis/pp2_Belo Horizonte_safety.html
Interactive map saved to ./vis/pp2_Berlin_safety.html
Interactive map saved to ./vis/pp2_Boston_safety.html
Interactive map saved to ./vis/pp2_Bratislava_safety.html
Interactive map saved to ./vis/pp2_Bucharest_safety.html
Interactive map saved to ./vis/pp2_Cape Town_safety.html
Interactive map saved to ./vis/pp2_Chicago_safety.html
Interactive map saved to ./vis/pp2_Copenhagen_safety.html
Interactive map saved to ./vis/pp2_Denver_safety.html
Interactive map saved to ./vis/pp2_Dublin_safety.html
Interactive map saved to ./vis/pp2_Gaborone_safety.html
Interactive map saved to ./vis/pp2_Glasgow_safety.html
Interactive map saved to ./vis/pp2_Guadalajara_safety.html
Interactive map saved to ./vis/pp2_Helsinki_safety.html
Interactive map saved to ./vis/pp2_Hong Kong_safety.html
Interactive map saved to ./vis/pp2_Houston_safety.html
Interactive map saved to ./vis/pp2_Johannesburg_safety.html
Interactive map saved to ./vis/pp2_Kiev_safety.html
Interactive map saved to ./vis/pp2_Kyoto_safety.html
Interactive map saved to ./vis/pp2_Lisbon_safety.html
Interactive map saved to ./vis/pp2_London_safety.html
Interactive map saved to ./vis/pp2_Los Angeles_safety.html
Interactive map saved to ./vis/pp2_Madrid_safety.html
Interactive map saved to ./vis/pp2_Melbourne_safety.html
Interactive map saved to ./vis/pp2_Mexico City_safety.html
Interactive map saved to ./vis/pp2_Milan_safety.html
Interactive map saved to ./vis/pp2_Minneapolis_safety.html
Interactive map saved to ./vis/pp2_Montreal_safety.html
Interactive map saved to ./vis/pp2_Moscow_safety.html
Interactive map saved to ./vis/pp2_Munich_safety.html
Interactive map saved to ./vis/pp2_New York_safety.html
Interactive map saved to ./vis/pp2_Paris_safety.html
Interactive map saved to ./vis/pp2_Philadelphia_safety.html
Interactive map saved to ./vis/pp2_Portland_safety.html
Interactive map saved to ./vis/pp2_Prague_safety.html
Interactive map saved to ./vis/pp2_Rio De Janeiro_safety.html
Interactive map saved to ./vis/pp2_Rome_safety.html
Interactive map saved to ./vis/pp2_San Francisco_safety.html
Interactive map saved to ./vis/pp2_Santiago_safety.html
Interactive map saved to ./vis/pp2_Sao Paulo_safety.html
Interactive map saved to ./vis/pp2_Seattle_safety.html
Interactive map saved to ./vis/pp2_Singapore_safety.html
Interactive map saved to ./vis/pp2_Stockholm_safety.html
Interactive map saved to ./vis/pp2_Sydney_safety.html
Interactive map saved to ./vis/pp2_Taipei_safety.html
Interactive map saved to ./vis/pp2_Tel Aviv_safety.html
Interactive map saved to ./vis/pp2_Tokyo_safety.html
Interactive map saved to ./vis/pp2_Toronto_safety.html
Interactive map saved to ./vis/pp2_Valparaiso_safety.html
Interactive map saved to ./vis/pp2_Warsaw_safety.html
Interactive map saved to ./vis/pp2_Washington DC_safety.html
Interactive map saved to ./vis/pp2_Zagreb_safety.html'''

text = text.split('\nInteractive map saved to ')
for i in text: 
    filename = i.split('/')[-1]
    cityname = filename.split('.')[0].split('_')[1]
    print(f' - [{cityname}](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/safety/{filename})')