import datetime 

data_waktu = datetime.datetime.now()
print(f"Datetime Now : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ['i','d', 'a', 'f', 'o', 'a', 'f', 'c', 'a']
data_count = Counter(data)
print(f"Data Count: {data_count}")
print(f"Jumlah  a : {data_count['a']}")

import io 

file = io.open("file_text.txt","r")
print(file.read())

