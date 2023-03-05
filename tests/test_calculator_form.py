import sys

import allure
from selene import command
from selene.support.conditions import have
from selenium.webdriver import Keys


delete_text = Keys.CONTROL + 'a' + Keys.DELETE


@allure.tag('web')
@allure.label('owner', 'vkamenskiy')
def test_successful_fill_calculator_form(setup_chrome):
    browser = setup_chrome
    browser.open('/calc')
    browser.element('#calc-amount').send_keys(delete_text).type('4')
    browser.element('#calc-salary').send_keys(delete_text).type('60000')
    browser.element('#calc-resume_per_day').send_keys(delete_text).type('10')
    browser.element('#calc-mail_per_day').send_keys(delete_text).type('8')
    browser.element('#calc-cal_per_day').send_keys(delete_text).type('2')
    browser.element('#calc-mail_tpl_per_day').send_keys(delete_text).type('5')
    browser.element('.economy-calc-form__content .button_black').perform(command.js.click)
    browser.element('.economy-calc-summary__money').should(have.text('429 060 руб/год'))
