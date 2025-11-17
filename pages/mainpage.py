import time

from selenium.webdriver.common.by import By

from conftest import browser


class Mainpage:

    def __init__(self, browser):
        self.browser = browser



    def open(self):
        self.browser.get('https://www.effective-mobile.ru/')
        self.browser.implicitly_wait(5)

    def click_moreinfo(self):
        moreinfo = self.browser.find_element(By.XPATH, '//button[text()="Узнать больше"]')
        time.sleep(2)
        moreinfo.click()

    def click_leavereq(self):
        leavereq = self.browser.find_element(By.XPATH, '//button[text()="Оставить заявку"]')
        time.sleep(2)
        leavereq.click()

    def click_vacancy(self):
        vacancy = self.browser.find_element(By.XPATH, '//a[text()="Вакансии"]')
        time.sleep(2)
        vacancy.click()

    def click_review(self):
        review = self.browser.find_element(By.XPATH, '//a[text()="Отзывы"]')
        time.sleep(2)
        review.click()

    def click_aboutus(self):
        aboutus = self.browser.find_element(By.XPATH, '//a[text()="О нас"]')
        time.sleep(2)
        aboutus.click()

    def click_contact(self):
        contact = self.browser.find_element(By.XPATH, '//a[text()="Контакты"]')
        time.sleep(2)
        contact.click()

    def click_outstaff(self):
        outstaff = self.browser.find_element(By.XPATH, '//a[text()="Аутстафф"]')
        time.sleep(2)
        outstaff.click()

    def click_employment(self):
        employment = self.browser.find_element(By.XPATH, '//a[text()="Трудоустройство"]')
        time.sleep(2)
        employment.click()

    def click_consultation(self):
        consultation = self.browser.find_element(By.XPATH, '//a[text()="Консультация"]')
        time.sleep(2)
        consultation.click()

    def click_policy(self):
        policy = self.browser.find_element(By.XPATH, '//a[text()="Политика конфиденциальности"]')
        time.sleep(2)
        policy.click()

    def click_termofuse(self):
        termofuse = self.browser.find_element(By.XPATH, '//a[text()="Условия использования"]')
        time.sleep(2)
        termofuse.click()

    def click_actvacancies(self):
        actvacancies = self.browser.find_element(By.XPATH, '//a[text()="Актуальные вакансии"]')
        time.sleep(2)
        actvacancies.click()

    def is_captcha_present(self):

        captcha_selectors = [
            '//*[contains(@class, "captcha")]',
            '//*[contains(@id, "captcha")]',
            '//*[contains(@name, "captcha")]',
            '//iframe[contains(@src, "captcha")]',
            '//img[contains(@src, "captcha")]',
            '//*[contains(text(), "капч")]',
            '//*[contains(text(), "Captcha")]',
            '//*[contains(text(), "CAPTCHA")]',
            '//*[contains(text(), "робот")]',
            '//*[contains(text(), "robot")]'
        ]

        for selector in captcha_selectors:
            try:
                elements = self.browser.find_elements(By.XPATH, selector)
                if elements:
                    print(f"Найдена капча по селектору: {selector}")
                    print(f"Количество элементов: {len(elements)}")
                    for i, element in enumerate(elements):
                        print(f"   Элемент {i + 1}: отображается = {element.is_displayed()}")
            except Exception as e:
                print(f"Ошибка с селектором {selector}: {e}")