import requests
import time

headers = {
    'authority': 'voting-vote-producer.r7.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'origin': 'https://afazenda.r7.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://afazenda.r7.com/a-fazenda-12/votacao',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga=GA1.2.752519377.1608122021; _gid=GA1.2.163209966.1608122021; __gads=ID=a3ef5ca3420a7cca:T=1608122022:S=ALNI_MbNeZcqPxODf4zcbpX-5NZCHKVteA; bm_sz=2B2CAE0ABE5D1CAA7FBACA52B2B4AF4C~YAAQjQWWyHFKZ6B1AQAApUXPawoQGDSmmbudHfM+GA0CR93TBz8GbRaB/UEOZC3FDQ2e1/MEqnkssXuLbx9M0Q/+qBkaek1c7O3Edh63rulbpdhFzbk5ikHI6l8esss8WWT2J7KZTZu3nYnnXj6zK8ZzkzVyUWxM2PvP9NybE0WYFNjEtdZ/wtTi11fz5ra+w0eTbmmpRzz9VuFVjnB1QKYTq4L5HQXdMmUotec8wr/sY2bKQZOIlKBwuA==; ak_bmsc=5C6C2D95AEC98908736F1FC677B0D1D5C8960587A31000009526DA5FB9B0DF01~pl6Gh5U7HuuR1IW5AdCvmbNE4ULG2+rxzGZUfycDvRlMeBZoutamrhiEcVQ9aYRAeugGhcHQFO/OIWnMUdXptbjc88EFNvZH3oRgopE0AmNG0Hiw0VLwFKCtY577prUOV/CvrzlyJMBbkgtBUnvSaFoFDwZJ9qgScDyNp/o4ajFYj1ATl46rzeaZOaV5PPbWSN+PxcizVmKxS5cLJbS/vVuzoNv/R+GmXpRLJq1IisX6w=; _gat=1; _dc_gtm_UA-10631407-5=1; bm_sv=FE14E4027D2400E5B907DDE78CE67C3E~sTiOd5bCNcDqbgZ5dJ4mig08fePDdGh7O3C3iKGw/I32xlOLJkOEtN7+wX54+xM6T+eUaAbl+DP0CfqO9sdw/qobdUXwigJUdnQ5ejYMn84PYmODei9xpLiNNjM2fP8JuBocKh3Ts8NK3LTBZ+laXQ==; _abck=BA6CEA0565FDBA3D41E93F4874F7F71B~-1~YAAQhwWWyAF6L+51AQAAc8ZWbAVyS6ITZqWDfcS2jCswyZPj60PExmpDk/BsC15HXVMhNkJN1DPXK7n5+MtE/WP7nR7ICCDGc5KozR4SpRY9hlTXSwVLihtxDxpVd0IoEqD5AiUqtPQBz6b+Pr0hb4rdTJJU+7HNAzHeEwe2l9BMpna6xV5iEhmGN3jPtqmo8ZAyxw9vwRQP/6dEYX37pCNmKkV+0vM2f253ZhAQp0p3gVpxf1amZmj5xSZhWD7u9gqeFXpCeIEXGQRrTp+PTUt6nGti0LJFYMgcn43obRWvWWXc9fY1iEdHYgOuhS7Uq09X~0~1-sQkSDwWxeS-10000-10-1000-1^|^|^|^|~-1',
}


participante = {
    'biel': '758',
    'jojo': '759',
    'lipe': '760',
    'stefany': '761'
}

url = 'https://voting-vote-producer.r7.com/vote'

nome =(input('Insira o nome do participante, sem acentos: ')).lower()
data = {
'voting_id': '302',
'alternative_id': participante[nome]
}
while True:
    r = requests.post(url, headers=headers, data=data)
    if int(r.status_code) == 200:
        print('Voto computado')
        time.sleep(0.5)
    else:
        print('Erro ao votar')
        time.sleep(30)
    