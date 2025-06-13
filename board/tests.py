from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
# Create your tests here.

class MySeleniumTestsBoard(StaticLiveServerTestCase):
    # get the guest user that is not "really" in my database just for testing purposes
    fixtures = ["user-data.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
    # closes it
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    

    '''
        Test if the guest can log in, successfully auth and make a task
        Given: nothing
        Inputs: name- Clean
                description- Find wipes
                due_date- 2025-10-24
                user_on_task- Mary
        Made a Tasks.json file to show the developmental database so far incase
        I wish to reference it in later tests
    '''

    def test_task(self):
        # same as the test login so far might seem repetitive but I need to 
        # know if the task foreign key authenticates with a user
        self.selenium.get(f"{self.live_server_url}/login/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("guest")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("secret")
        self.selenium.find_element(By.XPATH, '//input[@value="Submit"]').click()
        # new testing starts here
        select_element = self.selenium.find_element(By.ID, "views")
        select_element.click()
        # getting the actual text here instead of an ID or Name because it is a dropdown/I didnt want to add an id to it
        board_option = self.selenium.find_element(By.XPATH, '//a[text()="Board"]')  # or another selector
        board_option.click()
        create_task = self.selenium.find_element(By.ID, "createtask")
        create_task.click()
        name_input = self.selenium.find_element(By.NAME, "name")
        name_input.send_keys("Clean")
        description_input = self.selenium.find_element(By.NAME, "description")
        description_input.send_keys("Find wipes")
        due_date_input = self.selenium.find_element(By.NAME, "due_date")
        due_date_input.send_keys("2025-10-24")
        user_on_task_input = self.selenium.find_element(By.NAME, "user_on_task")
        user_on_task_input.send_keys("Mary")
        # same as login logic here it triggers the view and submits the data can tell by 
        # warning message in terminal when submitting the date
        self.selenium.find_element(By.XPATH, '//input[@value="Submit"]').click()