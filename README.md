# koronavirus
[![İndirme Sayısı](https://static.pepy.tech/personalized-badge/koronavirus?period=total&units=international_system&left_color=green&right_color=orange&left_text=%C4%B0ndirme%20Say%C4%B1s%C4%B1)](https://pepy.tech/project/koronavirus)

Koronavirüs (Covid-19) verilerine erişmenizi sağlayan bir Python modülü.<br>
Verilerin kaynağı: [NovelCOVID API](https://disease.sh/)

PyPI: https://pypi.org/project/koronavirus/<br>
GitHub: https://github.com/Dorukyum/koronavirus/

## Kurulum
**İndirmek için:** ```pip install koronavirus```
## Örnek Kullanım
### Senkron
```python
# modülü içeri aktar
from koronavirus import korona

# Türkiye'nin koronavirüs verilerini al
veriler = korona("Turkey") # veya korona("tr")
print(veriler)
```

### Asenkron
```python
# modülü içeri aktar
from koronavirus import async_korona as korona

# Türkiye'nin koronavirüs verilerini al
async def main():
    veriler = await korona("Turkey") # veya korona("tr")
    print(veriler)
```
