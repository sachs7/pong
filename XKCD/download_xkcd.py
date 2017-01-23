import bs4
import logging
import requests
import datetime

URL = 'https://xkcd.com'


def get_site(site_url):
    return requests.get(site_url)


''' In function scrape_comic, the parameter COMIC is actually RESPONSE from above. '''


def scrape_comic(comic):
    soup = bs4.BeautifulSoup(comic, 'html.parser')
    comic_element = soup.select('#comic img')
    comic_url = 'http:' + comic_element[0].get('src')
    print('Downloading {}'.format(comic_url))
    res = get_site(comic_url)
    res.raise_for_status()
    return res, comic_url


def save_comic(downl_comic_response):
    with open(str(datetime.date.today()) + '.png', 'wb') as f:
        for chunk in downl_comic_response.iter_content(100000):
            f.write(chunk)


def main():
    response = get_site(URL)
    response.raise_for_status()
    downloaded_comic_response, img_url = scrape_comic(response.text)
    save_comic(downloaded_comic_response)


main()

Sample Output: 

- Downloading http://imgs.xkcd.com/comics/voice_commands.png
