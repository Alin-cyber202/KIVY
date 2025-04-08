def test_links():
    driver = webdriver.Chrome()
    driver.get("https://kivy.org/doc/stable/gettingstarted/intro.html")
    
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        url = link.get_attribute("href")
        if url:
            driver.get(url)
            assert driver.title is not None
    
    driver.quit()
