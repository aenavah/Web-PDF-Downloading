from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import wget

chrome_options = Options()

driver = webdriver.Chrome(executable_path = "./chromedriver", options = chrome_options )

folder_path = "/Users/alexandranava/Desktop/CODE/World Banking Project"

basepage = "http://www.ccb.com/cn/investor/reportv3/annual_report_1.html"

class1 = "list" #class of where to find anchor tags in first page
type1 = "ul"
list1 = "list1"

class2 ="section clearfix"
type2 = "div"
num_pages = 2
next_button = "下一页"

#--------------------------------------- #initialize
driver.get(basepage)
counter = 0
soup = BeautifulSoup(driver.page_source,"html.parser")  #beautiful soup object of second page html

#--------------------------------------- #fcns
def download_pdfs(pdf_path, download_file):
    wget.download(pdf_path, download_file)

#--------------------------------------- #scrolls through pages of basepage
page = 1
list1 = []

while page <= num_pages :
    soup = BeautifulSoup(driver.page_source,"html.parser")
    anchor_list = soup(type,{"class": class1})[0]("a")
    for anchor in anchor_list:
        list1.append(anchor)
    if page < num_pages:
        driver.find_element_by_partial_link_text(next_button).click()
    #else:
        #driver.get(basepage)
    page += 1
#--------------------------------------- goes through list of anchor tags and extracts hyperlink text, then clicks text and gets anchors
counter_link = 0 #index for saved anchor tags
driver.close()
driver.quit()
for link in list1[17:18]:
    front = "http://www.ccb.com"
    full_link = front + link['href']
    driver2 = webdriver.Chrome(executable_path = "./chromedriver", options = chrome_options )
    driver2.get(full_link)

    list2 = []
    soup2 = BeautifulSoup(driver2.page_source,"html.parser")
    anchor_list2 = soup2("div",{"class": "content f14"})[0]("a")
    for anchor in anchor_list2: #for each anchor of pdfs
        link_text2 = str(anchor.getText())
        link_text2 = link_text2.split("title")
        link_text2 = link_text2[0].replace("• ","").strip() #now link text is just text on hyperlink
        print("downloading: " + link_text2)
        href2 = anchor.get('href')
        download_pdfs(href2, link_text2)
    driver2.close()
    driver2.quit()
print("DONE")




#
