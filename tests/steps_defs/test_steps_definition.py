"""Agent app is a business app feature tests."""
import pytest
from activities.login_view_activity import LoginPinInputActivity, LoginPinInputValidation
from activities.common_banner import BannerActivity,BannerValidation
from activities.home_activity import HomeActivity, HomeActivityValidation
from activities.cash_in_activity import CashInActivity
from activities.b2b_request_activity import B2BRequestActivity
from activities.common_insert_amount_activity import InsertAmountActivity
from activities.common_insert_pin_activity import InsertPinActivity
from activities.tap_and_hold_activity import TapAndHoldActivity
from activities.common_success_failure_activities import ConfirmationValidation, ConfirmationActivity
from activities.registration_activity import RegistrationActivity
from activities.registration_otp_input import RegistrationOTPInput
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
    # AppiumDriver().create_driver()
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


@scenario('features/app.feature', 'successful on-boarding of valid agent')
def test_successful_on_boarding_of_valid_agent():
    """successful on-boarding of valid agent"""


@scenario('features/app.feature', 'successful login')
def test_successful_login():
    """successful login."""


@scenario('features/app.feature', 'unsuccessful login twice due to incorrect pin and see Attention message')
def test_unsuccessful_login_twice_due_to_incorrect_pin_and_see_attention_message():
    """unsuccessful login twice due to incorrect pin and see Attention message"""


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


@scenario('features/app.feature', 'unsuccessful login due to incorrect pin')
def test_unsuccessful_login_due_to_incorrect_pin():
    """unsuccessful login due to incorrect pin"""


@scenario('features/app.feature', 'duplicate transaction detection while cash in')
def test_duplicate_transaction_detection_while_cash_in():
    """duplicate transaction detection while cash in"""


# =============================================================
# ====================== All Given ============================
# =============================================================


@given('app registration page is displayed')
def app_registration_page_is_displayed():
    """app registration page is displayed"""
    """app registration page is displayed"""
    # main = AppiumDriverHelper()
    # main.create_driver()
    # main.launch_the_app_for_onboard()
    AppiumDriver().launch_the_app_for_onboard()

@given('app is in home page')
def app_is_in_home_page(login):
    """app is in home page."""
    HomeActivity().click_okay_on_tooltip()


@given('app login page is displayed')
def app_login_page_is_displayed():
    """app login page is displayed."""
    AppiumDriver().launch_the_app()


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
def the_user_will_insert_amount(amount):
    """the user will insert amount "150"."""
    InsertAmountActivity().enter_amount(amount)


@when(parsers.parse('the user will insert customer number "{customer_number}"'))
def the_user_will_insert_customer_number(customer_number):
    """the user will insert customer number "01810189667"."""
    CashInActivity().click_okay_on_tooltip()
    CashInActivity().enter_customer_numer(customer_number)


@when(parsers.parse('the user will insert agent number'))
def the_user_will_insert_agent_number():
    """the user will insert agent number "01810189668"."""
    RegistrationActivity().enter_mobile_number()


@when('the user will click Next')
def the_user_will_click_next():
    """the user will click Next"""
    RegistrationActivity().click_on_next()


@when('the user will select operator')
def the_user_will_select_operator():
    """the user will select operator"""
    RegistrationActivity().operator_selection()


@when('the user will allow app to read and insert OTP')
def the_user_will_allow_app_to_read_and_insert_otp():
    """the user will allow app to read and insert OTP"""
    RegistrationOTPInput().click_on_allow_to_read_and_insert_the_otp()


@when('the user will insert incorrect login pin')
def the_user_will_insert_incorrect_login_pin():
    """the user will insert incorrect login pin"""
    LoginPinInputActivity().click_on_input_pin()
    LoginPinInputActivity().press_key(1)
    LoginPinInputActivity().press_key(2)
    LoginPinInputActivity().press_key(1)
    LoginPinInputActivity().press_key(2)
    LoginPinInputActivity().press_key(3)


@then('the user will insert login pin')
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


@then('the user will press login')
@when('the user will press login')
def the_user_will_press_login():
    """the user will press login."""
    LoginPinInputActivity().press_login()
    HomeActivity().click_okay_on_tooltip()


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


@when('the user will click cross button to close the banner')
def the_user_will_click_cross_button_to_close_the_banner():
    """the user will click cross button to close the banner"""
    BannerActivity().click_on_close_button()


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


@then(parsers.parse('the user will see the pin field text "{text}"'))
def the_user_will_see_the_pin_field_text(text):
    """the user will see the pin field text "Agent PIN"."""
    assert LoginPinInputValidation().get_the_text_of_pin_input_field() == text


@then(parsers.parse('the user will see error banner with "{text}" message'))
def the_user_will_see_error_banner_with_text_message(text):
    """the user will see error banner with "Incorrect PIN" message"""
    """the user will see error banner with "Attention! One more incorrect attempt will lock your PIN" message"""
    assert BannerValidation().get_banner_text() == text


@then('the user will click yes on the confirmation')
def the_user_will_click_yes_on_the_confirmation():
    """the user will click yes on the confirmation"""
    HomeActivity().click_yes_on_confrim_b2b()


@then('the user will press on very good')
def the_user_will_press_on_very_good():
    """the user will press on very good"""
    HomeActivity().click_on_very_good()


@when('the user will press back to home')
@then('the user will press back to home')
def the_user_will_press_back_to_home():
    """the user will press back to home"""
    ConfirmationActivity().press_on_back_to_home()


@then('the user will turn on the agent status')
def the_user_will_turn_on_the_agent_status():
    """the user will turn on the agent status"""
    HomeActivity().turn_on_agent_status()

