    if pressGoButton:
        goButton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div')))
        goButton.click()