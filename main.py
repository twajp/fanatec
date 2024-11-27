import requests


class ChangeDetector:
    def __init__(self, filename, url):
        html_new = requests.get(url).content

        with open(f'data/{filename}', mode='rb') as f:
            html_old = f.read()

        with open(f'data/{filename}', mode='wb') as f:
            f.write(html_new)

        self.isChanged = html_old != html_new


tokorozawa = ChangeDetector('transportation.html', 'https://fanatec.com/ja-jp/clubsport-pedals-v3-inverted?_gl=1*7z2g83*_gcl_au*ODg5MzkxODUwLjE3MjU4Mzk0NTM.*_ga*MzQ2MTYzNjYuMTcyMzY4ODgyMQ..*_ga_Q6VYC4JPVE*MTczMjcxMjc0Ny40LjAuMTczMjcxMjc0Ny42MC4wLjA.')

print(f'isChanged={tokorozawa.isChanged}')
# print(f'isChanged={any((tokorozawa.isChanged, tokorozawa.isChanged))}')
