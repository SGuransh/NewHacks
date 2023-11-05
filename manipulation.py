from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=OvgMS57yMcU")

# Specify the class name you want to target
class_name = "question-hyperlink"

# Use JavaScript to find and print all elements with the specified class
elements = driver.execute_script(f'return document.getElementsByClassName("{class_name}");')

for element in elements:
    print(element.text)
