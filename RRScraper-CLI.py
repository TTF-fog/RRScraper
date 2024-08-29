from selenium import webdriver
from tqdm import tqdm
import pypub
from selenium.webdriver.common.by import By
import iridi

browser = webdriver.Chrome()


iridi.presets.wiretap.print("RRScraper")
iridi.presets.wiretap.print("Single URL or List")
iridi.presets.wiretap.print("Royal Road URL (In https:// format) :")
url = input()

browser.get(url)


class Ebook:
    def __init__(self, links: [str]):
        self.name = ""
        self.format = "epub"
        self.chapters = 0
        self.links = links
        self.chapters = links
        self.pages = len(self.links)
        self.format = {}

    def loadText(self):
        Output = pypub.Epub(url[url.rfind("/"):len(url)].replace("-", " ").title().replace("/", ""),publisher="RRScraper",creator="RRScraper")

        for i in tqdm(range(0, len(links))):
            browser.get(links[i])
            
            womper = browser.find_element(By.CLASS_NAME,
                                          "chapter-inner").get_attribute(
                 "innerHTML")

            try:
                my_first_chapter = pypub.create_chapter_from_html(womper.encode("utf-8"),
                                                                  chapters[i]["title"])
                Output.add_chapter(my_first_chapter)
            except Exception as e:
                iridi.presets.wiretap.print(f" Error encountered {e}")

                pass

        Output.create('./' + url[url.rfind("/"):len(url)].replace("-", " ").title())
        iridi.presets.wiretap.print("Saved")


no = 0

# chapter_links=[]
chapters = browser.execute_script("return window.chapters;")
links = []

for i in tqdm(range(0, len(chapters))):
    links.append("https://royalroad.com" + chapters[i]["url"])

iridi.presets.wiretap.print("Chapters found")
iridi.presets.wiretap.print("Setting up book")
t = Ebook(links)

t.loadText()
# for i in textbox:
#     chapter_links.append(i.find_element(By.TAG_NAME,"a").get_attribute("href"))

#
# for i in chapter_links:
#     browser.get(i)
