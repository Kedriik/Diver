from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import tldextract

# =============================================================================
# http://www.google.com/search?
#   start=0
#   &num=10
#   &q=red+sox
#   &cr=countryCA
#   &lr=lang_fr
#   &client=google-csbe
#   &output=xml_no_dtd
#   &cx=00255077836266642015:u-scht7a-8i
# =============================================================================
# =============================================================================
# driver.get("http://www.google.com")
# elem  = driver.find_element_by_name('q')
# elem.send_keys(starting_key)
# time.sleep(1);
# elem.send_keys(Keys.RETURN)
# =============================================================================
current_debug_links = []
links_to_exclude = []
links_to_exclude.append("google")
links_to_exclude.append("register")
links_to_exclude.append("login")
class Page:
    def __init__(self, links, link, text):
        self.links = links
        self.link  = link
        self.text = text
        self.score = 0
        self.sorted_links = {}
        self.domain = ""
        print("Pages links count:")
        print(len(self.links))
        
        
            
    def trim_links(self):
        temp_links = []
        for link in self.links:
            if Page.findKeywords(link,links_to_exclude) == False and len(link) > 0:                
                temp_links.append(link)
        
        self.links = temp_links

        
    
    def sort_links(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(firefox_options=options)
        for link in self.links:
            print("scoring link:"+link)
            driver.get(link)
            score = len(driver.find_elements_by_xpath("//a[@href]"))
            print("score:"+str(score))
            self.sorted_links[link] = score
        driver.close()            
        self.sorted_links = sorted(self.sorted_links)
        
        
    def findKeywords(link,keywords):
        for i in range(len(keywords)):
            if link.find(keywords[i]) != -1:
                return True
        return False
    
    def set_domain(self):
        ext = tldextract.extract(self.link)
        self.domain = ext.domain

            
class Link:
    def __init__(self, url, visited):
        self.url = url
        self.visited  = visited          
            
            
        
class Diver:
    def __init__(self):
        self.driver = webdriver.Firefox()    
        self.starting_key = "Chmiel"
        self.visited_pages = []    
        self.depth = 10
        self.clickable_elements = []
        
    def page_has_loaded(self):
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = self.driver.execute_script('return document.readyState')
        print(page_state)
        return page_state
    
    def start_diving(self):
        self.start()
        time.sleep(4)
        self.create_current_page()
        current_depth = 0
        
        
        while(current_depth<=self.depth):
            self.step()
            self.create_current_page()
            current_depth=current_depth + 1
            time.sleep(2)
        self.close()
            
    def start(self):
        self.driver.get("http://www.google.com")
        elem  = self.driver.find_element_by_name('q')
        elem.send_keys(self.starting_key)
        elem.send_keys(Keys.RETURN)
    
    def step(self):
        current_window = self.driver.current_window_handle   
        self.driver.get(self.get_link())
        
    def peek(self):
        current_window = self.driver.current_window_handle        
        self.clickable_elements[0].click()
        self.driver.switch_to_window(current_window)
        #(IWebElement) self.clickable_elements[0].
        
        
        
       # self.driver.switch_to_window(self, new WindowHandle(link))
        #peek_data = 
        
        
    
    def get_link(self):
        #url = self.visited_pages[len(sel)]
        #print(self.visited_pages[len(self.visited_pages)-1].links[0])
# =============================================================================
#         index = -1
#         if(self.visited_pages[len(self.visited_pages)-1].links != 0):
#             index = int(random.random()*1000000)%len(self.visited_pages[len(self.visited_pages)-1].links)
#         else:
#             self.visited_pages[len(self.visited_pages)-1].links.append(self.visited_pages[len(self.visited_pages)-2].link)
#             index = int(random.random()*1000000)%len(self.visited_pages[len(self.visited_pages)-1].links)
#         print("random index:"+str(index))
# =============================================================================
        
        
        link_scores = []
        
        self.visited_pages
            
        
            
        return self.visited_pages[len(self.visited_pages)-1].sorted_links[0]
        
    def close(self):
        self.driver.close()
        
    def create_current_page(self):
        cont = True
        while(cont == True):
            time.sleep(2)
            print("creating page :" + self.driver.current_url)
            try:
                currentText = self.driver.page_source
            except:
                print("Wzial na klate exceptiona")
            else:
                cont = False
            
        self.clickable_elements = self.driver.find_elements_by_xpath("//a[@href]")
        links = []
        for element in self.clickable_elements:
            link =""
            try:
                link = element.get_attribute("href")
            except:
                print("Exception1")
            else:
                links.append(link)
                
                
        page = Page(links, self.driver.current_url, currentText)
        page.trim_links()
        page.sort_links()
        page.set_domain()
        
        
        self.visited_pages.append(page);
        
        

    
    
        
    
#print(len(driver.find_elements_by_tag_name('a')))
# =============================================================================
# all_links = driver.find_elements_by_class('a')
# link = all_links[0]
# =============================================================================

diver =  Diver()
diver.start_diving()
# =============================================================================
# driverHelper.start() #root czyli google
# driverHelper.create_current_page() #tworzac strone dodajemy ja do historii
# driverHelper.step() #pierwszy link z poprzedniej
# driverHelper.create_current_page() #tworzac strone dodajemy ja do historii
# =============================================================================

#print(driverHelper.visited_pages)

# =============================================================================
# count=0
# 
# 
# firstPage = Page(links, currentText)
# firstPage.trim_links()
# print (firstPage.links)
# 
# 
#     
# #root = new Page(elemens)
#     
# #link.Click()
# #print(driver.page_source)
# driver.close()
# =============================================================================
# =============================================================================
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
# =============================================================================

        
        
