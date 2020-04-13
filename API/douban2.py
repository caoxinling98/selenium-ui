# 林笑天
from selenium import webdriver

class Text:

    def BookName(self,num):
        self.driver = webdriver.Chrome("../../chromedriver.exe")
        self.driver.get("https://book.douban.com/")
        self.driver.find_element_by_link_text("豆瓣书店").click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        i=1
        for i in range(num+1):
            self.elements=self.driver.find_elements_by_css_selector('.book-list li.book-item a div.panel-detail div.book-brief h3')
            for j in self.elements:
                print(j.text)
            i=i+1
            self.driver.find_element_by_link_text(str(i)).click()
            self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()

b=Text()
b.BookName(5)