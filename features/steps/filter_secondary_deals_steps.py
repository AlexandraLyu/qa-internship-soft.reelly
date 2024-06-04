from behave import *
from time import sleep


@given('the user is on the main page')
def step_impl(context):
    context.app.main_page.open('https://soft.reelly.io/')  # Ensure this URL is correct


@when('the user logs in with valid credentials')
def step_impl(context):
    context.app.main_page.login('lybchevskaya@icloud.com', 'Abundance88!')


@when('the user clicks on the "Secondary" option in the left side menu')
def step_impl(context):
    context.app.main_page.click_secondary_option()


@then('the user should be on the Secondary deals page')
def step_impl(context):
    context.app.secondary_deals_page.verify_on_page('https://soft.reelly.io/secondary-listings')


@when('the user filters the products by "want to sell"')
def step_impl(context):
    sleep(10)
    context.app.secondary_deals_page.filter_by_want_to_sell()


@then('the user verifies all cards have a "for sale" tag')
def step_impl(context):
    sleep(20)
    context.app.secondary_deals_page.verify_all_cards_have_for_sale_tag()

