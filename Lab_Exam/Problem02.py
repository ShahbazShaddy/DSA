from selenium import webdriver


# Set up the Chrome driver
driver = webdriver.Chrome(executable_path=r'D:/Workspace/3rd Semester/DSA/Pre-Mid/Scrapping/chromedriver-win64/chromedriver.exe')

# Navigate to the URL
driver.get("https://www.coursera.org/learn/cybersecurity-for-everyone")

# Find the elements containing the course name, university name, course rating, and relation using XPath
course_name = driver.find_element_by_xpath('//div[@class="cds-119 cds-Typography-base css-1xy8ceb cds-121"]').text
university_name = driver.find_element_by_xpath('//span[@class="cds-119 cds-Typography-base css-e7lgfl cds-121"]').text
course_rating = driver.find_element_by_xpath('//div[@class="cds-119 cds-Typography-base css-h1jogs cds-121"]').text
relation = driver.find_element_by_xpath('//div[@class="cds-119 cds-Typography-base css-h1jogs cds-121"]').text

# Print the scraped data
print(f"Course Name: {course_name}")
print(f"University Name: {university_name}")
print(f"Course Rating: {course_rating}")
print(f"Relation: {relation}")

# Close the driver
driver.quit()