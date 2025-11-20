from pages.checkpage import Checkpage
from pages.mainpage import Mainpage


def test_moreinfo(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.click_moreinfo()
    checkpage = Checkpage(browser)
    checkpage.checktitle_moreinfo('Форматы сотрудничества')

def test_leavereq(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.click_leavereq()
    checkpage = Checkpage(browser)
    checkpage.checktitle_leavereq('Свяжитесь с нами')

def test_vacancy(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_vacancy('Вакансии')
    mainpage.click_vacancy()

def test_review(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_review('Отзывы')
    mainpage.click_review()

def test_aboutus(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_aboutus('О нас')
    mainpage.click_aboutus()

def test_contact(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_contact('Контакты')
    mainpage.click_contact()

def test_outstaff(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_outstaff('Аутстафф')
    mainpage.click_outstaff()

def test_employment(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_employment('Трудоустройство')
    mainpage.click_employment()

def test_consultation(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_consultation('Консультация')
    mainpage.click_consultation()

def test_policy(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_policy('Политика конфиденциальности')
    mainpage.click_policy()

def test_termofuse(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_termofuse('Условия использования')
    mainpage.click_termofuse()

def test_actvacancies(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_actvacancies('Актуальные вакансии')
    mainpage.click_actvacancies()

def test_captcha(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    checkpage = Checkpage(browser)
    checkpage.checktitle_captcha()
    mainpage.is_captcha_present()
