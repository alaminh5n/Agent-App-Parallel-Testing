"""Agent app is a business app feature tests."""
import pytest
from activities.login_view_activity import LoginPinInputActivity
from activities.home_activity import HomeActivity, HomeActivityValidation
from activities.cash_in_activity import CashInActivity
from activities.b2b_request_activity import B2BRequestActivity
from activities.common_insert_amount_activity import InsertAmountActivity
from activities.common_insert_pin_activity import InsertPinActivity
from activities.tap_and_hold_activity import TapAndHoldActivity
from activities.common_success_failure_activities import ConfirmationValidation, ConfirmationActivity
from activities.registration_activity import RegistrationActivity
from driver.appium_driver import AppiumDriver


from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


@pytest.fixture(scope='function')
def login():
    AppiumDriver().launch_the_app()
    RegistrationActivity().change_language_to_english()
    LoginPinInputActivity().click_on_input_pin()
    LoginPinInputActivity().press_key(1)
    LoginPinInputActivity().press_key(2)
    LoginPinInputActivity().press_key(1)
    LoginPinInputActivity().press_key(2)
    LoginPinInputActivity().press_key(1)
    LoginPinInputActivity().press_login()


# =============================================================
# ====================== All Scenarios ========================
# =============================================================


@scenario('features/app.feature', 'successful login')
def test_successful_login():
    """successful login."""


@scenario('features/app.feature', 'successful cash in')
def test_successful_cash_in():
    """successful cash in."""


@scenario('features/app.feature', 'successful b2b transfer')
def test_successful_b2b_transfer():
    """successful b2b transfer"""


@scenario('features/app.feature', 'successful e money request')
def test_successful_e_money_request():
    """successful e money request"""


@scenario('features/app.feature', 'successful cash request')
def test_successful_cash_request():
    """successful cash request"""


# =============================================================
# ====================== All Given ============================
# =============================================================


@given('app is in home page')
def app_is_in_home_page(login):
    """app is in home page."""


@given('app login page is displayed')
def app_login_page_is_displayed():
    """app login page is displayed."""


@given('the Agent app will be opened in mobile')
def the_agent_app_will_be_opened_in_mobile():
    """the Agent app will be opened in mobile."""


# =============================================================
# ====================== All When =============================
# =============================================================


@when('the user will change the language')
def the_user_will_change_the_language():
    """the user will change the language."""
    RegistrationActivity().change_language_to_english()


@when('the user will click proceed to the next step')
def the_user_will_click_proceed_to_the_next_step():
    """the user will click proceed to the next step."""
    CashInActivity().click_on_proceed_to_the_next_step()


@when(parsers.parse('the user will insert amount "{amount}"'))
def the_user_will_insert_amount_150(amount):
    """the user will insert amount "150"."""
    InsertAmountActivity().enter_amount(amount)


@when(parsers.parse('the user will insert customer number "{customer_number}"'))
def the_user_will_insert_customer_number_01810189667(customer_number):
    """the user will insert customer number "01810189667"."""
    CashInActivity().enter_customer_numer(customer_number)


@when('the user will insert login pin')
def the_user_will_insert_login_pin():
    """the user will insert login pin."""
    LoginPinInputActivity().click_on_input_pin()
    LoginPinInputActivity().press_key(1)
    LoginPinInputActivity().press_key(2)
    LoginPinInputActivity().press_key(1)
    LoginPinInputActivity().press_key(2)
    LoginPinInputActivity().press_key(1)


@when('the user will insert pin')
def the_user_will_insert_pin():
    """the user will insert pin."""
    InsertPinActivity().click_on_input_pin()
    InsertPinActivity().press_key(1)
    InsertPinActivity().press_key(2)
    InsertPinActivity().press_key(1)
    InsertPinActivity().press_key(2)
    InsertPinActivity().press_key(1)


@when('the user will press Tap and hold')
def the_user_will_press_tap_and_hold():
    """the user will press Tap and hold for Cash In."""
    TapAndHoldActivity().press_and_hold()


@when('the user will press confirm')
def the_user_will_press_confirm():
    """the user will press confirm."""
    InsertPinActivity().press_confirm()


@when('the user will press login')
def the_user_will_press_login():
    """the user will press login."""
    LoginPinInputActivity().press_login()


@when('the user will press proceed to the next step')
def the_user_will_press_proceed_to_the_next_step():
    """the user will press proceed to the next step."""
    InsertAmountActivity().click_on_proceed_to_next_step()


@when('the user will tap on Cash In')
def the_user_will_tap_on_cash_in():
    """the user will tap on Cash In."""
    HomeActivity().click_on_cash_in()


@when('the user will tap on b2b transfer')
def the_user_will_tap_on_b2b_transfer():
    """the user will tap on b2b transfer"""
    HomeActivity().click_on_b2b_transfer()


@when('the user will tap on b2b request')
def the_user_will_tap_on_b2b_request():
    """the user will tap on b2b request"""
    HomeActivity().click_on_b2b_request()


@when('the user will click on e money request')
def the_user_will_click_on_e_money_request():
    """the user will click on e money request"""
    B2BRequestActivity().click_on_e_money_request()


@when('the user will click on cash request')
def the_user_will_click_on_cash_request():
    """the user will click on cash request"""
    B2BRequestActivity().click_on_cash_request()


# =============================================================
# ====================== All then =============================
# =============================================================


@then('close the app')
def close_the_app():
    """close the app."""
    AppiumDriver().close_app_()


@then('the user will be on home page')
def the_user_will_be_on_home_page():
    """the user will be on home page."""
    assert HomeActivityValidation().get_recent_transaction_title() == 'Recent Transactions'


@then(parsers.parse('the user will see this message "{text}"'))
def the_user_will_see_this_message_your_cash_in_transfer_is_complete(text):
    """the user will see this message "Your Cash In transfer is complete." """
    """the user will see this message "Your B2B Transfer is complete." """
    """the user will see this message "Your E-Money Request is Successful" """
    """the user will see this message "Your Cash Request is Successful" """
    assert ConfirmationValidation().get_confirmation_title() == text


@then('the user will click yes on the confirmation')
def the_user_will_click_yes_on_the_confirmation():
    """the user will click yes on the confirmation"""
    HomeActivity().click_yes_on_confrim_b2b()


@then('the user will press on very good')
def the_user_will_press_on_very_good():
    """the user will press on very good"""
    HomeActivity().click_on_very_good()


@then('the user will press back to home')
def the_user_will_press_back_to_home():
    """the user will press back to home"""
    ConfirmationActivity().press_on_back_to_home()

