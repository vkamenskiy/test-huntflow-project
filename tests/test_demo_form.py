from selene.support.conditions import have
from selene.support.shared import browser


def test_demo_form_have_all_placeholders():
    browser.open('')
    browser.element('.is-button .js-navigation-modal-close').click()
    browser.element('[name="company"]').should(have.attribute('placeholder').value('Название компании'))
    browser.element('[name="first_name"]').should(have.attribute('placeholder').value('Ваше имя'))
    browser.element('[name="last_name"]').should(have.attribute('placeholder').value('Ваша фамилия'))
    browser.element('.input[name="email"]').should(have.attribute('placeholder').value('Ваша эл. почта'))
    browser.element('[name="phone"]').should(have.attribute('placeholder').value('Ваш телефон'))
    browser.element('[name="position"]').should(have.attribute('placeholder').value('Ваша должность'))
    browser.element('[name="recruiters_amount"] option:nth-child(1)').should(have.text('Число рекрутеров'))
    browser.element('[name="software"] option:nth-child(1)').should(have.text('В чем ведете базу резюме сейчас'))
