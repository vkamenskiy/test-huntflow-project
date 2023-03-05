import allure
from selene.support.conditions import have, be


@allure.tag('web')
@allure.label('owner', 'vkamenskiy')
def test_password_errors_item_success(setup_chrome):
    browser = setup_chrome
    browser.open('/account/login')
    browser.element('#password').type('1111111111')
    browser.element('.password-errors__item_success').should(be.visible)


@allure.tag('web')
@allure.label('owner', 'vkamenskiy')
def test_password_errors_item_fail(setup_chrome):
    browser = setup_chrome
    browser.open('/account/login')
    browser.element('#password').type('111')
    browser.element('.button--Gh4nT').click()
    browser.element('.password-errors__item_error').should(be.visible)


@allure.tag('web')
@allure.label('owner', 'vkamenskiy')
def test_wrong_email(setup_chrome):
    browser = setup_chrome
    browser.open('/account/login')
    browser.element('#email').type('test')
    browser.element('.button--Gh4nT').click()
    browser.element('.form-group_invalid .form-group__error').should(have.text('Некорректная почта'))


@allure.tag('web')
@allure.label('owner', 'vkamenskiy')
def test_email_not_fill(setup_chrome):
    browser = setup_chrome
    browser.open('/account/login')
    browser.element('.button--Gh4nT').click()
    browser.element('.form-group_invalid .form-group__error').should(have.text('Введите адрес эл. почты'))


@allure.tag('web')
@allure.label('owner', 'vkamenskiy')
def test_password_not_fill(setup_chrome):
    browser = setup_chrome
    with allure.step('Открываем страницу с авторизацией'):
        browser.open('/account/login')

    with allure.step('Зполняем данные'):
        browser.element('#email').type('test@test.ru')
        browser.element('.button--Gh4nT').click()

    with allure.step('Проверяем вывод сообщения'):
        browser.element('.form-group_invalid .form-group__error').should(have.text('Введите пароль'))

