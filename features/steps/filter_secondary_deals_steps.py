from behave import *
import logging
import time


@given('the user is on the main page')
def step_impl(context):
    logging.info("Opening the main page.")
    context.app.main_page.open('https://soft.reelly.io/')  # Ensure this URL is correct


@when('the user logs in with valid credentials')
def step_impl(context):
    logging.info("Logging in with valid credentials.")
    context.app.main_page.login('lybchevskaya@icloud.com', 'Abundance88!')


@when('the user clicks on the "Secondary" option')
def step_impl(context):
    logging.info("Clicking on the Secondary option.")
    context.app.main_page.click_secondary_option()


# @then('the user should be on the Secondary deals page')
# def step_impl(context):
#     logging.info("Waiting for the page to load before verifying the Secondary deals page.")
#     logging.info("Verifying the user is on the Secondary deals page.")
#     # context.app.secondary_deals_page.verify_on_page()


@when('the user filters the products by "want to sell"')
def step_impl(context):
    logging.info("Filtering the products by 'want to sell'.")
    context.app.secondary_deals_page.filter_by_want_to_sell()


@then('the user verifies all cards have a "for sale" tag')
def step_impl(context):
    logging.info("Verifying all cards have a 'for sale' tag.")
    context.app.secondary_deals_page.verify_all_cards_have_for_sale_tag()
