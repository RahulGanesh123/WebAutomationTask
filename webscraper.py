from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ'
browser = webdriver.Chrome('/Users/rahulganesh/Desktop/Projects/webscraper/chromedriver')
browser.get(url)
browser.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-shelf-renderer/div[1]/div[2]/yt-horizontal-list-renderer/div[2]/div/ytd-grid-video-renderer[1]/div[1]/ytd-thumbnail/a').click()