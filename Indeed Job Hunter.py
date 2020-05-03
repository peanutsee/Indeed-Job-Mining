from selenium import webdriver
from bs4 import BeautifulSoup
from MYSQL import Connector
from time import sleep

class Hunter():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=chrome_options)

    def title(self, soup):
        '''
        Extract Title from Result Box
        :return: Title
        '''
        title_elem = soup.find('h2', class_ = 'title')
        title = title_elem.text.strip()
        return title

    def companyName(self, soup):
        '''
        Extract Company Name form Result Box
        :return: Company Name
        '''
        company_name_elem = soup.find(class_="company")
        company_name = company_name_elem.text.strip()
        return company_name

    def location(self, soup):
        '''
        Extract Location form Result Box
        :return: Location
        '''
        location_elem = soup.find(class_="location accessible-contrast-color-location")
        location = location_elem.text.strip()
        return location

    def salary(self, soup):
        '''
        Extract Salary form Result Box
        :return: Salary
        '''
        salary_elem = soup.find(class_="salaryText")
        salary = salary_elem.text.strip()
        return salary

    def summary(self, soup):
        '''
        Extract Summary from Result Box
        :return: Location
        '''
        summary_elem = soup.find(class_="summary")
        summary = summary_elem.text.strip()
        return summary

    def POST(self, title, company, location, salary, summary, description):
        c = Connector()
        c.post(title, company, location, salary, summary, description)

    def getJob(self, url):
        self.driver.get(url)

        job_soup = self.driver.find_element_by_id(id_="resultsCol")

        jobs_elem = job_soup.find_elements_by_class_name('jobsearch-SerpJobCard')

        for job in jobs_elem:
            result_html = job.get_attribute('innerHTML')
            soup = BeautifulSoup(result_html, 'html.parser')

            # Milk Dem Basic Information
            try:
                title = self.title(soup)
            except:
                title = 'None'
                print('No Title')

            try:
                company = self.companyName(soup)
            except:
                company = 'None'
                print('No Company Name')

            try:
                location = self.location(soup)
            except:
                location = 'None'
                print('No Location Provided')

            try:
                salary = self.salary(soup)
            except:
                salary = 'None'
                print('No Salary Provided')

            try:
                summary = self.summary(soup)
            except:
                summary = 'None'
                print('No Summary Provided')

            try:
                # Milk Even More Information
                sum_div = job.find_element_by_class_name('summary')
                sum_div.click()
                sleep(0.5)
                description = self.driver.find_element_by_id('vjs-desc').text.strip()
            except:
                description = 'None'
                print("Can't Milk Shit")

            try:
                self.POST(title,company, location, salary, summary, description)
            except:
                print('CANNOT POST TO DB')
            print('*' * 100)

hunter = Hunter()
for i in range(0, 1000, 10):
    url = 'https://sg.indeed.com/jobs?q=data+scientist&l=Singapore&start=' + str(i)
    hunter.getJob(url)



