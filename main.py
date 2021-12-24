from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Opera()
url = "https://www.youtube.com/"


wrds = ["eeeboy", "complicate you", "ui testing"]
driver.get(url)
for i in zip(wrds):
    driver.find_element_by_css_selector("input#search").clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
    driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
    print(driver.current_url)



driver.get("https://www.youtube.com/")
driver.find_element_by_css_selector("tp-yt-paper-button.style-scope.ytd-button-renderer.style-suggestive.size-small").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#identifierId"))).send_keys("mr.kruglik1717@gmail.com")
driver.find_element_by_css_selector("span.VfPpkd-vQzf8d").click()
print(driver.current_url)
driver.quit()