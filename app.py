import os
import re
import requests
from PIL import Image
from bs4 import BeautifulSoup

class ImageSpider:
    def __init__(self):
        self.home = os.getcwd()
    
    def grab_all_image_links(self, URL):
        try:
            valid_links = []
            url_protocol = URL.split('/')[0]
            url_html = requests.get(URL).text
            Image_urls = re.findall(r'((http\:|https\:)?\/\/[^"\' ]*?\.(png|jpg))', url_html, flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)
            for image in Image_urls:
                image_url = image[0]
                if not image_url.startswith(url_protocol):
                    image_url = url_protocol+image_url
                    valid_links.append(image_url)
                else:
                    valid_links.append(image_url)
            print('Done')
        except Exception as graberror:
            print('Grab occured while getting links')
            print(graberror)
            return []  
        return valid_links

    @staticmethod
    def extract_image_name(url):
        image_name = str(url).split('/')[-1]
        return image_name

    @staticmethod
    def extract_site_name(url):
        sitename = str(url).split('/')[2]
        return sitename
    
    def saving_images(self,url):
        Image_links = self.grab_all_image_links(url)
        for link in Image_links:
            raw_image = requests.get(link, stream=True).raw
            img = Image.open(raw_image)
            image_name = self.extract_image_name(link)
            img.save(image_name)
    
    def grab_all_links(self, url):
        links = [url]
        link_html = requests.get(url).text
        all_links = BeautifulSoup(link_html, 'html.parser').findAll('a')
        for link in all_links:
            href = link.get('href')
            if href:       
                if href.startswith('http') or href.startswith('https'):
                    links.append(href)
        return links

    def download_images(self):
        url = input('Enter URL with images : ')
        try:
            sitename = self.extract_site_name(url)
            print('Extracting from {} ...'.format(sitename))
            os.mkdir(sitename);os.chdir(sitename)
            print('\nShould we can scan entire site or just home page ?')
            option = int(input('1. Entire site\n2.Just this page\nOption : '))
            if option == 1:
                all_avaialble_links = set(self.grab_all_links(url))
            else:
                all_avaialble_links = [url]
            for link in all_avaialble_links:
                try:                        
                    print(link)
                    self.saving_images(link)
                except:
                    continue

        except Exception as Error:
            print('Error occured while grabing site links')
            print(Error)

        finally:
            print('Scraping finished')
            os.chdir(self.home)


spider = ImageSpider()
spider.download_images()
