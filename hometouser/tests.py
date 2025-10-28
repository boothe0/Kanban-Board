from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

# Create your tests here.
# use selenium instead 

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ["user-data.json"]
    # opens browser
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
        Test if the user can log in 
        Given:  username- guest
                password- secret
        Clicks: button with value="Submit"
        Reference the file login.html under this app to see the button and file 
        forms.py to see the fields.
    '''
    def test_login(self):
        self.selenium.get(f"{self.live_server_url}/login/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("guest")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("secret")
        self.selenium.find_element(By.XPATH, '//input[@value="Submit"]').click()