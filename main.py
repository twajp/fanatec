import requests


class ChangeDetector:
    def __init__(self, filename, url):
        html_new = requests.get(url).content

        with open(f'data/{filename}', mode='rb') as f:
            html_old = f.read()

        with open(f'data/{filename}', mode='wb') as f:
            f.write(html_new)

        self.isChanged = html_old != html_new


tokorozawa = ChangeDetector('transportation.html', 'https://www.waseda.jp/fhum/hum/facility/bus-parking/')
fanatec = ChangeDetector('fanatec.html', 'https://fanatec.com/ja-jp/black-friday/')

print(f'isChanged={any((tokorozawa.isChanged, fanatec.isChanged))}')
