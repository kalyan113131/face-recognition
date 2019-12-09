""" filename: script.py """
import os
from parsel import Selector
# imports
from selenium import webdriver
import parameters
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd
import time
import clipboard
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait    

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.select import Select
import sys

'''
def skip_linkedin_profile(profile_count,profile_index,result_count,profile_page_count,driver,copy_linkedin_urls_list=[]):
    for j in range(profile_index,result_count):
        print("proile count",profile_count,profile_index,result_count,profile_page_count,copy_linkedin_urls_list)
        #print("kalyan7",results.text,profile_count)
        #string_view='(//a[@class="result-lockup__view-profile-link ember-view"])'+'['+str(profile_count)+']'
        #string_profile_click="(//li-icon[@type='ellipsis-horizontal-icon'])"+"["+str(profile_count)+"]"
        profile_view_css="section#results>div>ol>li:nth-of-type("+str(profile_count)+")>div:nth-of-type(2)>div>div>div>article>section>div>figure>a>div>img"
        #print("proile count1",profile_count,profile_index,result_count,profile_page_count,copy_linkedin_urls_list)
        #profile_pic_string='(//img[contains(@class,"lazy-image max-width")])'+'['+str(profile_count)+']'
        print("profile pic string",profile_view_css)
        try:
            L1=driver.find_element_by_css_selector(profile_view_css)
            #actionChains=ActionChains(driver)
            #actionChains.context_click(L1).perform()
            #actionChains.move_to_element(L1).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            #actionChains.context_click(L1).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            ActionChains(driver).context_click(L1).key_down(Keys.CONTROL).click(L1).perform()
            print("link of profile urls",L1.get_attribute('href'),driver.current_url)
            #L1.click().send_keys(Keys.CONTROL + 't')
            #driver.find_element_by_css_selector(profile_view_css).send_keys(Keys.CONTROL + 't')
        except:
                #time.sleep(2)
                profile_count=1
                profile_page_count+=1
                profile_page_click="section#results>div:nth-of-type(2)>nav>ol>li:nth-of-type("+str(profile_page_count)+")>button"
                driver.find_element_by_css_selector(profile_page_click).click()
                time.sleep(3)
                profile_view_css="section#results>div>ol>li:nth-of-type("+str(profile_count)+")>div:nth-of-type(2)>div>div>div>article>section>div>figure>a>div>img"
                #driver.findElement(By.cssSelector(profile_view_css)).sendKeys(Keys.CONTROL +"t");
                #driver.find_element_by_css_selector(profile_view_css).click()
                driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL +"t");
                driver.find_element_by_css_selector(profile_view_css).sendKeys(Keys.CONTROL +"t")
                
                

                      
        #driver.find_element_by_xpath(string_profile_click).click()
        #driver.find_element_by_xpath(string_view).click()
        time.sleep(2)
        profile_count+=1
        profile_index+=1
        for element11 in driver.find_elements_by_xpath('.//artdeco-dropdown-trigger[@class = "button-round-tertiary-medium-muted block ml1 ember-view"]'):
            print("checking the menu tag")
            element11.click()
            print("proile count..2",profile_count,profile_index,result_count,profile_page_count,driver,copy_linkedin_urls_list)

            time.sleep(2)
            for e11 in driver.find_elements_by_xpath('//artdeco-dropdown-item[@class="inverse-link-on-a-light-background ember-view"]'):
                print("text checking....",e11.text)
                time.sleep(1)
                print("copying checking..")
                print("proile count..3",profile_count,profile_index,result_count,profile_page_count,copy_linkedin_urls_list)

                if(e11.text=="Copy LinkedIn.com URL"):
                    #print("proile count..4",profile_count,profile_index,result_count,profile_page_count,copy_linkedin_urls_list)

                    e11.click()
                    time.sleep(1)
                    if(len(copy_linkedin_urls_list)!=0):
                        if(copy_linkedin_urls_list[-1]==clipboard.paste()):
                            profile_index=profile_index-1
                            profile_count=profile_count-1
                            print("proile count..5",profile_count,profile_index,result_count,profile_page_count,copy_linkedin_urls_list)

                            driver.execute_script("window.history.go(-1)")
                            time.sleep(6)
                            skip_linkedin_profile(profile_count,profile_index,result_count,profile_page_count,copy_linkedin_urls_list)
                    copy_linkedin_urls_list.append(clipboard.paste())
                    print("copy Linkedin URL",clipboard.paste())
                    #print("proile count..6",profile_count,profile_index,result_count,profile_page_count,copy_linkedin_urls_list)

        driver.execute_script("window.history.go(-1)")
        time.sleep(7)
        print("proile count..7",profile_count,profile_index,result_count,profile_page_count,copy_linkedin_urls_list)

        #scroll_down(driver)
        #driver.execute_script("window.scrollTo(0,100);")
        #html = driver.find_element_by_tag_name('html')
        #html.send_keys(Keys.END)
        print("profile pic string",profile_count)
    return copy_linkedin_urls_list
'''
'''
def scroll_down(driver):
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
'''
    


def csv_file_urls(linkedin_details=[],linkedin_urls=[]):
    
    linkedin_length=len(linkedin_urls)
    final_csv_details=[]
    for details_in in linkedin_details:
        print("details in .....",details_in)
        if(str(details_in)=="nan"):
            print("details in .....",details_in)
            details_in=""
        final_csv_details.append(details_in)
    #for details_urls_in in linkedin_urls:
    #    final_csv_details.append(details_urls_in)
    for loop_url_index in range(0,linkedin_length):
        if(loop_url_index>0):
            #final_csv_details=['_','_','_']
            final_csv_details.append(linkedin_urls[loop_url_index])
        else:
            final_csv_details.append(linkedin_urls[loop_url_index])
        print("csv file writing ...1")
        with open(r'test1.csv', 'a',newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(final_csv_details)
            del final_csv_details[-1]
            print("csv file writing loop")
        print("csv file writing ...2")
        csvFile.close()

# defining new variable passing two parameters
#writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
#writer.writerow(['Name'.encode(), 'Job Title'.encode(), 'Company'.encode(), 'College'.encode(), 'Location'.encode(), 'URL'.encode()])

# specifies the path to the chromedriver.exe
def Linkedin_profile_url(start_index,linkedin_credentials=[]):
    #driver = webdriver.Firefox('C:\Users\admin\Anaconda3\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
    #driver = webdriver.Firefox(executable_path=r'C:\Users\admin\Anaconda3\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
    #option = webdriver.ChromeOptions()
    #option.add_argument("headless")
    driver = webdriver.Chrome('F:\sales_force\chromedriver')
    #driver = webdriver.phantomjs ('F:\sales_force\phantomjs')
     
    #base_path = "./"
    #driver = webdriver.Firefox(executable_path=os.path.join(base_path, "geckodriver"), **config)
    #credentials_count=0
    linkedin_credentials_list=linkedin_credentials[0]
    del linkedin_credentials[0]
    del_linkedin_credentilas=linkedin_credentials
    # driver.get method() will navigate to a page given by the URL address
    driver.get('https://www.linkedin.com/')
    
    time.sleep(10)
    #driver.maximize_window() #//For maximizing window
    #driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds
    # locate email form by_class_name
    '''
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        element.send_keys(parameters.linkedin_username)
        element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        element.send_keys(parameters.linkedin_password)
    except:
        pass
    '''

    username = driver.find_element_by_name('session_key')


     # send_keys() to simulate key strokes
    username.send_keys(linkedin_credentials_list[0])

    # sleep for 0.5 seconds
    #time.sleep(5)

    # locate password form by_class_name
    password = driver.find_element_by_name('session_password')

    # send_keys() to simulate key strokes
    password.send_keys(linkedin_credentials_list[-1])
    time.sleep(5)

    # locate submit button by_xpath
    log_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn') 

    # .click() to mimic button click
    log_in_button.click()

    #credentials_count+=1 

    time.sleep(5)
    '''
    driver.get('https://www.linkedin.com/in/patricktoland')
    time.sleep(3)

    #log_in_button1 = driver.find_element_by_class_name("artdeco-button__text")
    #log_in_button1.click()

    #wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='View in sales Navigator']"))).click()


    #from selenium import webdriver
    #browser = webdriver.Firefox()
    #browser.get("http://www.google.com")
    for elem in driver.find_elements_by_xpath('.//span[@class = "artdeco-button__text"]'):
        #print("element in span",elem.get_attribute('href'))
        if(elem.text=="View in Sales Navigator"):
            #print("element url",elem.url)
            e1=elem.click()
            print("navigation",e1)
            #time.sleep(5)        
            #driver.get("https://www.linkedin.com/sales/people/ACoAAAAAXvMBs9Aifc9Lt3HoThJXHWVj3s6Et48,name,xcUQ")
            break
    time.sleep(5)
    #driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND + 't')
    driver.switch_to.window(driver.window_handles[1])
    #driver.get("https://www.linkedin.com/sales/people/ACoAAAAAXvMBs9Aifc9Lt3HoThJXHWVj3s6Et48,name,xcUQ")
    #select = Select(driver.find_element_by_id('ember34'))
    for element in driver.find_elements_by_xpath('.//artdeco-dropdown-trigger[@class = "button-round-tertiary-medium-muted block ml1 ember-view"]'):
        element.click()
        time.sleep(3)
        for element1 in driver.find_elements_by_xpath('.//artdeco-dropdown-item[@class ="inverse-link-on-a-light-background ember-view"]'):
            if(element1.text=="Copy LinkedIn.com URL"):
                e3=element1.click()
                print("copy Linkedin URL",clipboard.paste())
                break
            
                
                for element2 in driver.find_elements_by_xpath('.//artdeco-dropdown-trigger[@class = "advanced-search-dropdown__trigger color-blue9 Sans-14px-black-90%-bold ember-view"]'):
                    print("kalyan",element2.text)
                    element2.click()
                    ARROW_DOWN = u'\ue015'
     
                        element2.send_keys(ARROW_DOWN).click()
                        #element2.click()
                    #driver.find_element_by_xpath("//select[@class='inverse-link-on-a-light-background ember-view']/option[@value='Copy LinkedIn.com URL']").click()
    '''
    project_data = pd.read_excel(r'F:\sales_force\01_CA_Santa_Barbara_Santa_Barbara_19_09_30.xlsx',usecols = ['PROPERTY ADDRESS','OWNER 1 FIRST NAME','MAIL ZIP CODE','OWNER 1 LAST NAME'],sheet_name='ListReport')

    loop_count_csv=0

    for csv_index in range(start_index,len(project_data)):            
        driver.get('https://www.linkedin.com/sales/search/people?viewAllFilters=true')
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class,'m11')]/[@class='artdeco-icon']"))).click()
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view' and @id='ember130']"))).click()

        '''
        for elem6 in driver.find_elements_by_xpath('.//label[@class = "  t-14 t-black t-bold cursor-inherit m0"]'):
            print(elem6)
            if(elem6.text=="Geography"):
                elem6.click()
                break

        '''

        #//input[contains(@class,'text-input--no-border mh1')]
        #//input[@data-artdeco-is-focused='true']
        #div#artdeco-modal-outlet>div>div>div:nth-of-type(2)>div>div>section>ul>li:nth-of-type(8)>div>div>div:nth-of-type(2)>input

        #//button[@data-artdeco-is-focused='true']
        #//button[@data-ember-action-822='822']
        #div#artdeco-modal-outlet>div>div>div:nth-of-type(2)>div>div>section>ul>li:nth-of-type(8)>div>div>div>div>button



        #first_name=driver.find_element_by_xpath("//label[@class='advanced-search-filter__label  t-14 t-black t-bold cursor-inherit m0' and @for='ember187-input']").click()
        copy_linkedin_urls_list=[]
        print("lengths of first name and last name",len(str(project_data['OWNER 1 FIRST NAME'][csv_index])),len(str(project_data['OWNER 1 LAST NAME'][csv_index])))
        
        if(str(project_data['OWNER 1 FIRST NAME'][csv_index])!='nan' and str(project_data['OWNER 1 FIRST NAME'][csv_index])!='nan'):
            for FL_name in driver.find_elements_by_xpath("//button[@class='advanced-search-filter__placeholder-button t-14 t-black--light button--unstyled full-width flex']"):
                if(FL_name.text=="Add a first name"):
                    FL_name.click()
                    time.sleep(3)
                    first_name=driver.find_element_by_xpath("//input[@class='text-input--no-border mh1 ember-text-field ember-view']")
                    first_name.send_keys(str(project_data['OWNER 1 FIRST NAME'][csv_index]))
                    first_name.send_keys(u'\ue007')
                elif(FL_name.text=="Add a last name"):
                    FL_name.click()
                    time.sleep(3)
                    last_name=driver.find_element_by_xpath("//input[@class='text-input--no-border mh1 ember-text-field ember-view']")
                    last_name.send_keys(str(project_data['OWNER 1 LAST NAME'][csv_index]))
                    last_name.send_keys(u'\ue007')
            '''
            first_name.send_keys(parameters.Firstname)
            first_name.send_keys(u'\ue007')
            #last_name=driver.find_element_by_xpath("//label[@class='advanced-search-filter__label  t-14 t-black t-bold cursor-inherit m0' and @for='ember192-input']").click()
            las  t_name=driver.find_element_by_xpath("//button[contains(@class,'advanced-search-filter__placeholder-button t-14 t-black--light button--unstyled full-width flex')][contains(@data-ember-action,'194']").click()
            last_name.send_keys(parameters.Lastname)
            last_name.send_keys(u'\ue007')
            '''

            for elem7 in driver.find_elements_by_xpath('.//artdeco-dropdown-trigger[@class="flex align-items-flex-end Sans-12px-black-75% ember-view"]'):
                print("k1...",elem7.text)
                if(elem7.text=='Region'):
                    elem7.click()
                    time.sleep(1)


            for elem8 in driver.find_elements_by_xpath('.//artdeco-dropdown-item[@class="search-filter-context-menu__item a11y-artdeco-dropdown font-weight-400 ember-view"]'):
                print("k2....",elem8.text)
                #elem8.click()
                if(elem8.text=="Postal code"):
                    elem8.click()
            #driver.find_element_by_xpath("//select[@aria-label='Specify radius']/option[text()='Within: 100 mi (160 km)']").click()

            time.sleep(2)         
            print("checking the zip code length",len(str(project_data['MAIL ZIP CODE'][csv_index])),project_data['MAIL ZIP CODE'][csv_index])
            zip_code =driver.find_element_by_xpath('.//input[@class="text-input--no-border mt2 mh1 ember-text-field ember-view"]')
            zip_code_exception=str(project_data['MAIL ZIP CODE'][csv_index])
            if(len(str(project_data['MAIL ZIP CODE'][csv_index]))!=5):
                print("checking the length.......................x")
                if(len(zip_code_exception)==7):
                    zip_code_exception=zip_code_exception[0:5]
                elif(len(zip_code_exception)==4):
                    zip_code_exception="0"+zip_code_exception
            print("before sending the zip value",zip_code_exception)
            zip_code.send_keys(zip_code_exception)
            
            #driver.find_element_by_xpath("//select[@aria-label='Specify radius']/option[text()='Within: 75 mi (120 km)']").click()
            #driver.find_element_by_class_name('button-primary-small').click()
            #driver.find_element_by_css_selector('div#artdeco-modal-outlet>div>div>div:nth-of-type(2)>div>div>section>ul>li:nth-of-type(4)>div>div>div>ul>li:nth-of-type(2)>button>li-icon').click
            #time.sleep(3)
            #result_checking=driver.find_element_by_xpath('//span[@class="ph2 t-black"]//b[1]')
            #print("checking for condition",result_checking.text)
            selected_distance_list=["//select[@aria-label='Specify radius']/option[text()='Within: 10 mi (15 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 25 mi (40 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 35 mi (55 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 50 mi (80 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 75 mi (120 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 100 mi (160 km)']"]
            #selected_distance_list=["//select[@aria-label='Specify radius']/option[text()='Within: 25 mi (40 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 35 mi (55 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 50 mi (80 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 75 mi (120 km)']","//select[@aria-label='Specify radius']/option[text()='Within: 100 mi (160 km)']"]
            #if(int(result_checking.text)==0):
            results=0
            index_results=0
            print("csv_index",csv_index)
            #result_checking=driver.find_element_by_xpath('//span[@class="ph2 t-black"]//b[1]')
            #result_checking='1940'
            #results=int(result_checking)
            
            while(results==0):    
                #driver.find_element_by_xpath('//li[@title="Display 0 more Geography filter values"]').click()
                driver.find_element_by_xpath(selected_distance_list[index_results]).click()
                driver.find_element_by_class_name('button-primary-small').click()
                print("outside block for try....3")
                time.sleep(2)
                print("outside block for try5")
                try:
                    print("try  block inside")
                    result_checking=driver.find_element_by_xpath('//span[@class="ph2 t-black"]//b[1]')
                except:
                    print("except  block inside")
                    time.sleep(3)
                    print("except  block inside...1")
                    driver.close()
                    if(len(del_linkedin_credentilas)==0):
                        sys.exit()
                    Linkedin_profile_url(csv_index,del_linkedin_credentilas)
                    
                
                results=int(result_checking.text)
                print("checking the loop of distance selection",results)
                driver.find_element_by_xpath('//li[@title="Display 0 more Geography filter values"]').click()
                print("checking the loop of distance selection...1",results)
                index_results+=1
                if(index_results==6):
                    break
             
            



            #driver.find_element_by_xpath('//li[@title="Display 0 more Geography filter values"]').click()
            #driver.find_element_by_xpath('//li[@title="Display 0 more First name filter values"]').click()
            #driver.find_element_by_xpath('//li[@title="Display 0 more Last name filter values"]').click()

            #driver.find_element_by_xpath('(//path[@d="M14.71,4L12,1.29a1,1,0,0,0-1.41,0L3,8.85,1,15l6.15-2,7.55-7.55A1,1,0,0,0,15,4.71,1,1,0,0,0,14.71,4Zm-8.84,7.6-1.5-1.5L9.42,5.07l1.5,1.5Zm5.72-5.72-1.5-1.5,1.17-1.17,1.5,1.5Z"]').click()
            #driver.find_element_by_xpath('//div[img/@src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"]').click()
            #i=0
            #for results in driver.find_elements_by_xpath("//div[@class='display-flex align-items-center fr mr6']/span"):
            #driver.find_element_by_xpath('.//div[contains(@class,"display-flex align-items-center")]//button[1]').click()
            #time.sleep(5)
            #results=driver.find_element_by_id('search-spotlight-tab-ALL')
            #results=driver.find_element_by_xpath("//artdeco-spotlight-tab[@class='search-spotlights__tab active ember-view']/span[@class='artdeco-tab-primary-text']")
            #results=driver.find_element_by_xpath("//artdeco-spotlight-tab[@id='search-spotlight-tab-ALL']//span[1]")
            print("loop checking ......................")
            #copy_linkedin_urls_list=[]
            
            if(results!=0 and results<=10):
                driver.find_element_by_xpath('.//div[contains(@class,"display-flex align-items-center")]//button[1]').click()
                time.sleep(4)
                results=driver.find_element_by_xpath("//artdeco-spotlight-tab[@id='search-spotlight-tab-ALL']//span[1]")
                print("loop checking1 ......................")
                profile_count=1
                profile_index=0
                profile_page_count=1
                #for k in driver.find_element_by_xpath("//span[)
                #results='1949'
                results=int(results.text)            #for j in range(0,int(results)):
                #result_count=int(results.text)
                #copy_linkedin_urls_list=skip_linkedin_profile(profile_count,profile_index,result_count,profile_page_count,driver,copy_linkedin_urls_list)
                
                for j in range(0,results):
                    #print("kalyan7",results.text,profile_count)
                    #string_view='(//a[@class="result-lockup__view-profile-link ember-view"])'+'['+str(profile_count)+']'
                    #string_profile_click="(//li-icon[@type='ellipsis-horizontal-icon'])"+"["+str(profile_count)+"]"
                    profile_view_css="section#results>div>ol>li:nth-of-type("+str(profile_count)+")>div:nth-of-type(2)>div>div>div>article>section>div>figure>a>div>img"
                    #profile_pic_string='(//img[contains(@class,"lazy-image max-width")])'+'['+str(profile_count)+']'
                    profile_view_element="section#results>div>ol>li:nth-of-type("+str(profile_count)+")>div:nth-of-type(2)>div>div>div>article>section>div:nth-of-type(2)>ul>li>div>div:nth-of-type(2)>button>li-icon"
                    print("profile pic string",profile_view_css)
                    try:
                        L1=driver.find_element_by_css_selector(profile_view_css)
                        #driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
                        #z1=ActionChains(driver).move_to_element(L1).context_click(L1).key_down(Keys.CONTROL).click(L1).perform()
                        z1=ActionChains(driver).key_down(Keys.CONTROL).click(L1).send_keys("k").key_up(Keys.CONTROL).perform()
                        #z1=ActionChains(driver).context_click(L1).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).build().perform()
                        #z1=ActionChains(driver).context_click(L1).send_keys(Keys.DOWN + Keys.ENTER)
                        time.sleep(2)
                        #z1=ActionChains(driver).context_click(L1).key_down(Keys.CONTROL).perform()
                        
                        #//div[contains(@class,'display-flex flex-column')]
                        #(//main[contains(@class,'content-main people')]//div)[1]
                        #driver.find_elements_by_xpath(".//main[contains(@class,'content-main people')]").click()
                        #sendKeys(Keys.CONTROL + "t")
                        #z1.remove()
                        #ActionChains(driver).move_to_element(L1).context_click(L1).perform()
                        #ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
                        #ActionChains(driver).send_keys(Keys.ENTER).perform()
                        #time.sleep(1)
                        #driver.find_element_by_css_selector(profile_view_element).click()
                        #driver.execute_script("window.scrollTo(0,200);")
                        #time.sleep(1)
                        driver.switch_to.window(driver.window_handles[1])
                    except:
                        #time.sleep(2)
                        print("profile page exception handling",profile_view_css)
                        profile_count=1
                        profile_page_count+=1
                        profile_page_click="section#results>div:nth-of-type(2)>nav>ol>li:nth-of-type("+str(profile_page_count)+")>button"
                        driver.find_element_by_css_selector(profile_page_click).click()
                        time.sleep(3)
                        profile_view_css="section#results>div>ol>li:nth-of-type("+str(profile_count)+")>div:nth-of-type(2)>div>div>div>article>section>div>figure>a>div>img"
                        L1=driver.find_element_by_css_selector(profile_view_css)
                        z1=ActionChains(driver).key_down(Keys.CONTROL).click(L1).send_keys("k").key_up(Keys.CONTROL).perform()
                        time.sleep(2)
                        driver.switch_to.window(driver.window_handles[1])
                        
                            
                            

                                  
                    #driver.find_element_by_xpath(string_profile_click).click()
                    #driver.find_element_by_xpath(string_view).click()
                    time.sleep(2)
                    print("checking the missed one",profile_count)
                    for element11 in driver.find_elements_by_xpath('.//artdeco-dropdown-trigger[@class = "button-round-tertiary-medium-muted block ml1 ember-view"]'):
                        print("checking the menu tag")
                        element11.click()
                        time.sleep(1)
                        for e11 in driver.find_elements_by_xpath('//artdeco-dropdown-item[@class="inverse-link-on-a-light-background ember-view"]'):
                            print("text checking....",e11.text)
                            #time.sleep(1)
                            print("copying checking..")
                            if(e11.text=="Copy LinkedIn.com URL"):
                                e11.click()
                                time.sleep(1)
                                copy_linkedin_urls_list.append(clipboard.paste())
                                print("copy Linkedin URL",clipboard.paste())
                    #driver.execute_script("window.history.go(-1)")
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(4)
                    #scroll_down(driver)
                    #driver.execute_script("window.scrollTo(0,100);")
                    #html = driver.find_element_by_tag_name('html')
                    #html.send_keys(Keys.END)
                    print("profile pic string",profile_count)
                    #if(profile_count==results):
                    #    driver.find_element_by_css_selector(profile_view_css).click()
                        
                    profile_count+=1
                    #if(profile_count>20):
                     #   break
                    #if(profile_count==3):
                     #   break
            else:
                if(results!=0):
                    copy_linkedin_urls_list.append('bulk amount of profiles')
                    print("checking the none values..1",results)
                else:
                    print("no urls found")
                    print("checking the none values",results)
                    copy_linkedin_urls_list.append('None')
           
        if(len(copy_linkedin_urls_list)==0):
           copy_linkedin_urls_list.append('None')
        linkedin_details_list=[project_data['PROPERTY ADDRESS'][csv_index],project_data['OWNER 1 LAST NAME'][csv_index],project_data['OWNER 1 FIRST NAME'][csv_index],project_data['MAIL ZIP CODE'][csv_index]]
        print("final csv values",linkedin_details_list,copy_linkedin_urls_list)
        csv_file_urls(linkedin_details_list,copy_linkedin_urls_list)
        loop_count_csv+=1
        #if(loop_count_csv>3):
         #   break

linkedin_arguments=parameters.config_linkedin_credentials
index=0
Linkedin_profile_url(index,linkedin_arguments)


'''
for results in driver.find_elements_by_xpath("//span[@class='ph2 t-black']//b[1]"):    
    print("results checking....",results.text)
    if(results.text=="0 results"):
        print("kalyan......",results.text)
'''
  

#//span[@class='ph2 t-black']//b[1]
    #if(i<1):
    #driver.find_element_by_xpath("//select[@aria-label='Specify radius']/option[text()='Within: 100 mi (160 km)']").click()

    #print(results.get_attribute('b'))




'''
search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
time.sleep(5)

search_query.send_keys(Keys.RETURN)
time.sleep(5)


linkedin_urls = driver.find_elements_by_xpath('//*[@href]')
#linkedin_urls = [url.text for url in linkedin_urls]
linkedin_pages=driver.find_elements_by_xpath('//*[@aria-label]')
#print(linkedin_pages)
final_linkedin_urls=[]
final_linkedin_pages=[]
for linkedin_page in linkedin_pages:
    str_linkedin_page=linkedin_page.get_attribute('aria-label')
    final_linkedin_pages.append(str_linkedin_page)

print("linkind in pages",final_linkedin_pages)
       
for linkedin_url in linkedin_urls:
    str_linkedin_url=linkedin_url.get_attribute('href')
    #str_linkedin_url=str(linkedin_url)
    #print(str_linkedin_url)
    if(str_linkedin_url[0:26]=="https://in.linkedin.com/in"):
        final_linkedin_urls.append(str_linkedin_url)
print("linked in urls",final_linkedin_urls)
#sel1= Selector(text=driver.page_source)
#url =sel1.find_element_xpath("//a").get_attribute("href")
#url =sel1.xpath("//a").extract_first("dat-href")
#print(url)
time.sleep(5)



#driver.quit()

#linkedin_urls = [url for url in linkedin_urls]
#time.sleep(5)




# For loop to iterate over each URL in the list
name_location_details=[]



for view_linkedin_url in final_linkedin_urls:
   
   # get the profile URL
   #print("url for getting",linkedin_url)
   driver.get(view_linkedin_url)
   sel=Selector(text=driver.page_source)
   name =sel.xpath('//*[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()
   location=sel.xpath('//*[starts-with(@class,"t-16 t-black t-normal inline-block")]/text()').extract_first()
   #print(name)
   #print(location)
   name_location_details.append(name)
   name_location_details.append(location)
   time.sleep(3)

print(name_location_details)
'''

#..................................

'''
   # add a 5 second pause loading each URL
   linkedin_urls1=[url for url in linkedin_urls]
   for linkedin_url1 in linkedin_urls1:
       driver.get(linkedin_url1)
       sel = Selector(text=driver.page_source
       )
        


driver.quit()
'''

#driver.get("https://www.linkedin.com/in/connor-mclaughlin-191095/")
#find_url1=Selector(text=driver.page_source)
#name = sel.xpath('//h1/text()').extract_first()
#print(name)
#name = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first()
#print(name)
#linkedin_urls = driver.find_elements_by_class_name('iUh30')
#inline t-24 t-black t-normal break-words

