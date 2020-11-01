from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
import re
import time

chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


class GetImg():

    def __init__(self):
        self.url = 'http://cmd-sp.teddymobile.cn/#/login?redirect_url='
        self.browser = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.browser, 100)
        self.browser.get(self.url)

    def get_code_name(self):
        doc = pq(self.browser.page_source)
        getCodeID = doc('#checkcode').attr('src')
        pattern = re.compile('.*id=(.*)', re.S)
        result = re.match(pattern, getCodeID)
        return result[1]

    def mult_get_code_img(self, idx):
        checkcode_tap = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loginimg')))
        save_path = r'imgs\\{}.png'.format(idx)

        # 截图
        ele = self.browser.find_element_by_class_name('loginimg')
        ele.screenshot(save_path)

        checkcode_tap.click()
        time.sleep(1)


if __name__ == '__main__':
    getImg = GetImg()
    for item in range(20):
        getImg.mult_get_code_img(item)
