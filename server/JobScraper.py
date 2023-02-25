from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

op = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=op, executable_path="/usr/local/bin/chromedriver")
wait = WebDriverWait(driver, 2)
actions = ActionChains(driver)
driver.get("https://www.jobstreet.com.sg/")

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="searchKeywordsField"]')))

# Pass the CAPTCHA manually
search_box = driver.find_element(By.XPATH, '//*[@id="searchKeywordsField"]')
search_box.send_keys("software engineer")
search_box.send_keys(Keys.ENTER)


wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="jobList"]/div[2]/div[1]/div[1]/div/span')))

# Find all elements with data-automation="job-card-logo"
job_elements = driver.find_elements(By.CSS_SELECTOR, '.sx2jih0.zcydq84u.es8sxo0.es8sxo3.es8sxo21.es8sxoi')

# Loop through each logo element and extract information
for job in job_elements:
    # Extract all information
    job_link = job.find_element(By.CLASS_NAME, "_1hr6tkx5._1hr6tkx7._1hr6tkxa.sx2jih0.sx2jihf.zcydq8h")
    print(job_link.text)
