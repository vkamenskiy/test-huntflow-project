from selene.support.conditions import have, be
from selene.support.shared import browser


def test_password_errors_item_success():
    browser.open('/account/login')
    browser.element('#password').type('1111111111')
    browser.element('.password-errors__item_success').should(be.visible)


def test_password_errors_item_fail():
    browser.open('/account/login')
    browser.element('#password').type('111')
    browser.element('.button--Gh4nT').click()
    browser.element('.password-errors__item_error').should(be.visible)


def test_wrong_email():
    browser.open('/account/login')
    browser.element('#email').type('test')
    browser.element('.button--Gh4nT').click()
    browser.element('.form-group_invalid .form-group__error').should(have.text('Некорректная почта'))


def test_email_not_fill():
    browser.open('/account/login')
    browser.element('.button--Gh4nT').click()
    browser.element('.form-group_invalid .form-group__error').should(have.text('Введите адрес эл. почты'))


def test_password_not_fill():
    browser.open('/account/login')
    browser.element('#email').type('test@test.ru')
    browser.element('.button--Gh4nT').click()
    browser.element('.form-group_invalid .form-group__error').should(have.text('Введите пароль'))

