import requests


class ChangeDetector:
    def __init__(self, filename, url):
        html_new = requests.get(url).content

        with open(f'data/{filename}', mode='rb') as f:
            html_old = f.read()

        with open(f'data/{filename}', mode='wb') as f:
            f.write(html_new)

        self.isChanged = html_old != html_new


tokorozawa = ChangeDetector('clubsport-pedals-v3-inverted.html', 'https://fanatec.com/ja-jp/clubsport-pedals-v3-inverted')

print(f'isChanged={tokorozawa.isChanged}')
# print(f'isChanged={any((tokorozawa.isChanged, tokorozawa.isChanged))}')
