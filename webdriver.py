from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

__browser_url = r'D:\360Chrome\360Chrome\Chrome\Application\360chrome.exe'  ##浏览器的地址  
chrome_options = Options()  
# chrome_options.add_argument('--headless')
chrome_options.binary_location = __browser_url 
browser  = webdriver.Chrome(chrome_options=chrome_options) 