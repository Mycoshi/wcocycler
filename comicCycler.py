import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

from ast import Break
import pyautogui
import time

#Globals
loc = ''
pyautogui.size()  # current screen resolution width and height
(3840, 2160)
page_number = ''
url = ''


class Function:
    def scrape_center_image(self, url):
        """
        Scrapes a website for an image assumed to be in the center of the page.

        This function makes several assumptions that may not hold for all websites.
        It relies on common HTML structures and CSS patterns.

        Args:
            url (str): The URL of the website to scrape.

        Returns:
            Image.Image or None: A PIL Image object if an image is found, otherwise None.
        """
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) #added user-agent to avoid common blocking
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            soup = BeautifulSoup(response.content, "html.parser")

            # Common patterns to find "center" images
            # 1. Look for img tags within a div with class "center", "main", or similar.
            center_divs = soup.find_all("div", class_=["center", "main", "middle", "content"])
            for div in center_divs:
                img = div.find("img")
                if img:
                    return self.download_image(img.get("src"), url) # return if image is found within center div

            # 2. Look for img tags directly within a body or main tag.
            body_img = soup.body.find("img")
            if body_img:
                return self.download_image(body_img.get("src"), url)

            main_tag = soup.find("main")
            if main_tag:
                main_img = main_tag.find("img")
                if main_img:
                    return self.download_image(main_img.get("src"), url)

            # 3. Look for images with specific CSS styles (e.g., margin: auto). This is less reliable.
            # This implementation does not include this method, as its too unreliable.

            # 4. Look for the largest image on the page. this is not necessarily the center image, but can be useful.
            images = soup.find_all("img")
            if images:
                largest_image = None
                largest_image_size = 0
                for img in images:
                    src = img.get("src")
                    if src:
                        try:
                            img_data = requests.get(src, stream=True, headers={"User-Agent": "Mozilla/5.0"})
                            img_data.raise_for_status()
                            img_bytes = img_data.content
                            img_pil = Image.open(BytesIO(img_bytes))
                            width, height = img_pil.size
                            size = width * height
                            if size > largest_image_size:
                                largest_image_size = size
                                largest_image = img
                        except requests.exceptions.RequestException as e:
                            print(f"Error downloading image: {e}")
                        except Exception as e:
                            print(f"Error processing image: {e}")

                if largest_image:
                    return self.download_image(largest_image.get("src"), url)

            return None  # No image found
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def download_image(self, src, base_url):
       if src.startswith("//"): #handles protocol relative urls
            src = "https:" + src
       elif src.startswith("/"): #Handles relative paths
            src = base_url.rstrip("/") + src

       try:
            img_data = requests.get(src, stream=True, headers={"User-Agent": "Mozilla/5.0"})
            img_data.raise_for_status()
            img_pil = Image.open(BytesIO(img_data.content))
            return img_pil
       except requests.exceptions.RequestException as e:
            print(f"Error downloading image: {e}")
            return None
       except Exception as e:
            print(f"Error processing image: {e}")
            return None


    def loop(self):
            
            page_number =  input('Number of pages')
            page_number = int(page_number)
            countset =  input('where did we leave off?')
            countset = int(countset)
            uselessvar = input('press enter when cursor is over browser in taskbar')
            run.cursloc()

            count = countset
            page_number = int(page_number)
            for i in range(page_number):
                if count <= page_number: 
                    self.scrape_center_image(url)
                    count = count + 1 
                
start = input('Begin? (y/n): ')
inputurl = input('please copypaste url: ')
url= inputurl
if start == 'y':
    run = Function()
    run.loop()
else:
    print(pyautogui.position())