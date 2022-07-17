from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\ichig\Documents\chromedriver_win32\chromedriver.exe')
youtube_url='https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
driver.get(youtube_url)