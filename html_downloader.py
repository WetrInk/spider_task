import requests

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            response.encoding = 'gb2312'
            return response.text

        except:
            return None

