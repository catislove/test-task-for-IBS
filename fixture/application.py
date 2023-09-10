from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class Application:

    def __init__(self, base_url):
        options = Options()
        self.wd = webdriver.Chrome(chrome_options=options)
        self.wd.implicitly_wait(5)
        self.base_url = base_url

    def open_site(self):
        wd = self.wd
        wd.get(self.base_url)
        wd.maximize_window()

    def destroy(self):
        self.wd.save_screenshot("final.png")
        self.wd.quit()