import time

from selenium.webdriver.common.by import By


from conftest import browser


class Checkpage:

    def __init__(self, browser):
        self.browser = browser

    def checktitle_moreinfo(self, title):
        time.sleep(2)
        moreinfo_title = self.browser.find_element(By.XPATH, '//h2[text()="Форматы сотрудничества"]')
        assert moreinfo_title.text == title

    def checktitle_leavereq(self, title):
        leavereq_title = self.browser.find_element(By.XPATH, '//h2[text()="Свяжитесь с нами"]')
        time.sleep(2)
        assert leavereq_title.text == title

    def checktitle_vacancy(self, title):
        vacancy_title = self.browser.find_element(By.XPATH, '//a[text()="Вакансии"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", vacancy_title)
        assert vacancy_title.text == title

    def checktitle_review(self, title):
        review_title = self.browser.find_element(By.XPATH, '//a[text()="Отзывы"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", review_title)
        assert review_title.text == title

    def checktitle_aboutus(self, title):
        aboutus_title = self.browser.find_element(By.XPATH, '//a[text()="О нас"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", aboutus_title)
        assert aboutus_title.text == title

    def checktitle_contact(self, title):
        contact_title = self.browser.find_element(By.XPATH, '//a[text()="Контакты"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", contact_title)
        assert contact_title.text == title

    def checktitle_outstaff(self, title):
        outstaff_title = self.browser.find_element(By.XPATH, '//a[text()="Аутстафф"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", outstaff_title)
        assert outstaff_title.text == title

    def checktitle_employment(self, title):
        employment_title = self.browser.find_element(By.XPATH, '//a[text()="Трудоустройство"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", employment_title)
        assert employment_title.text == title

    def checktitle_consultation(self, title):
        consultation_title = self.browser.find_element(By.XPATH, '//a[text()="Консультация"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", consultation_title)
        assert consultation_title.text == title

    def checktitle_policy(self, title):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        policy_title = self.browser.find_element(By.XPATH, '//a[text()="Политика конфиденциальности"]')
        self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", policy_title)
        assert policy_title.text == title

    def checktitle_termofuse(self, title):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        termofuse_title = self.browser.find_element(By.XPATH, '//a[text()="Условия использования"]')
        self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", termofuse_title)
        assert termofuse_title.text == title

    def checktitle_actvacancies(self, title):
        actvacancies_title = self.browser.find_element(By.XPATH, '//a[text()="Актуальные вакансии"]')
        assert actvacancies_title.text == title

    def checktitle_captcha(self):
        captcha_title = self.browser.find_element(By.XPATH, '//h2[text()="Свяжитесь с нами"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", captcha_title)