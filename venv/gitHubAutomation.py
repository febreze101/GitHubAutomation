import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Open the broswer
PATH = "C:\Program Files (x86)\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_argument('headless') # run without opening browser
driver = webdriver.Chrome(PATH, options=option)

# Create new folder for project
directory = input("Where do you want the new directory: ")
parent_dir = "C:/Users/Fabrice B/MyProjects"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
os.chdir(path)

# initialize git
os.system("git init")

# Scrape github.com to create remote repository
driver.get('https://github.com/login')
driver.implicitly_wait(10)
logIn = driver.find_element_by_id('login_field')
logIn.send_keys('fkbokovi@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('Mus32Ate')

signIn = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')
signIn.click()

newRepo = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
newRepo.click()

repoName = driver.find_element_by_id('repository_name')
repoName.send_keys(directory)

createRepo = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')
driver.implicitly_wait(5)
createRepo.submit()
driver.implicitly_wait(5)
remote = driver.find_element_by_xpath('//*[@id="empty-setup-push-repo-echo"]/span[1]').text

# Create README file and push git
os.system(remote)
file = open("README.md", 'w')
os.system('git add .')
os.system('git commit -m "Initial commit"')
os.system('git push -u origin master')

driver.quit()