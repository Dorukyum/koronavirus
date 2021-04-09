# koronavirus
Koronavirüs (Covid-19) verilerine erişmenizi sağlayan bir Python modülü.

## Örnek Kullanım
```python
# modülü içeri aktar
from koronavirus import *

# Türkiye'nin koronavirüs verilerini al
veriler =  korona("Turkey") # veya korona()
print(veriler)

# async hâli
veriler = async_korona("Turkey") # veya async_korona()
print(veriler)
```