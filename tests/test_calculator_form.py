import sys

from selene.support.conditions import have
from selene.support.shared import browser

from selenium.webdriver import Keys

modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
delete_text = modifier_key + 'a' + Keys.DELETE


def test_successful_fill_calculator_form():
    browser.open('/calc')
    browser.element('#calc-amount').send_keys(delete_text).type('4')
    browser.element('#calc-salary').send_keys(delete_text).type('60000')
    browser.element('#calc-resume_per_day').send_keys(delete_text).type('10')
    browser.element('#calc-mail_per_day').send_keys(delete_text).type('8')
    browser.element('#calc-cal_per_day').send_keys(delete_text).type('2')
    browser.element('#calc-mail_tpl_per_day').send_keys(delete_text).type('5')
    browser.element('.economy-calc-form__content .button_black').click()
    browser.element('.economy-calc-summary__money').should(have.text('429 060 руб/год'))