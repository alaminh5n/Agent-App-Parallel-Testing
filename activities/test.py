from activities.login_view_activity import LoginPinInputActivity
from activities.home_activity import HomeActivity
from activities.cash_in_activity import CashInActivity
from activities.b2b_request_activity import B2BRequestActivity
from activities.common_insert_amount_activity import InsertAmountActivity
from activities.common_insert_pin_activity import InsertPinActivity
from activities.tap_and_hold_activity import TapAndHoldActivity
from activities.common_success_failure_activities import ConfirmationValidation


# LoginPinInputActivity().click_on_input_pin()
# LoginPinInputActivity().press_key(1)
# LoginPinInputActivity().press_key(2)
# LoginPinInputActivity().press_key(1)
# LoginPinInputActivity().press_key(2)
# LoginPinInputActivity().press_key(1)
# LoginPinInputActivity().press_login()
# HomeActivity().click_on_cash_in()
# CashInActivity().enter_customer_numer()
# CashInActivity().click_on_proceed_to_the_next_step()
# InsertAmountActivity().enter_amount()
# InsertAmountActivity().click_on_proceed_to_next_step()
# InsertPinActivity().click_on_input_pin()
# InsertPinActivity().press_key(1)
# InsertPinActivity().press_key(2)
# InsertPinActivity().press_key(1)
# InsertPinActivity().press_key(2)
# InsertPinActivity().press_key(1)
# InsertPinActivity().press_confirm()
# TapAndHoldActivity().press_and_hold()
# print(ConfirmationValidation().get_confirmation_title())


LoginPinInputActivity().click_on_input_pin()
LoginPinInputActivity().press_key(1)
LoginPinInputActivity().press_key(2)
LoginPinInputActivity().press_key(1)
LoginPinInputActivity().press_key(2)
LoginPinInputActivity().press_key(1)
LoginPinInputActivity().press_login()
# HomeActivity().click_on_b2b_transfer()
HomeActivity().click_on_b2b_request()
# B2BRequestActivity().click_on_e_money_request()
B2BRequestActivity().click_on_cash_request()
InsertAmountActivity().enter_amount()
InsertAmountActivity().click_on_proceed_to_next_step()
InsertPinActivity().click_on_input_pin()
InsertPinActivity().press_key(1)
InsertPinActivity().press_key(2)
InsertPinActivity().press_key(1)
InsertPinActivity().press_key(2)
InsertPinActivity().press_key(1)
InsertPinActivity().press_confirm()
TapAndHoldActivity().press_and_hold()
print(ConfirmationValidation().get_confirmation_title())


#  @successful-onboard
#  Scenario: Successful valid agent onboarding
#    Given the Agent app registration page is displayed
#    When the user will change the language
#    And the user will insert agent number "01321188766"
#    And the user will click Next
#    And the user will select operator
#    And the user will allow app to read and insert OTP
#    Then the user will seen the field for "Agent PIN"
##    And close the app



"""Agent app is a business app feature tests."""
from activities.registration_activity import RegistrationActivity
from activities.registration_pin_input import RegistrationPinInput
from activities.login_view_activity import LoginPinInputValidation

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


@scenario('../features/app.feature', 'Successful valid agent onboarding')
def test_successful_valid_agent_onboarding():
    """Successful valid agent onboarding."""


@given('the Agent app registration page is displayed')
def the_agent_app_registration_page_is_displayed():
    """the Agent app registration page is displayed."""


@when('the user will allow app to read and insert OTP')
def the_user_will_allow_app_to_read_and_insert_otp():
    """the user will allow app to read and insert OTP."""
    RegistrationPinInput().click_on_allow_to_read_and_insert_the_pin()


@when('the user will change the language')
def the_user_will_change_the_language():
    """the user will change the language."""
    RegistrationActivity().change_language()


@when('the user will click Next')
def the_user_will_click_next():
    """the user will click Next."""
    RegistrationActivity().click_on_next()


@when(parsers.parse('the user will insert agent number "{number}"'))
def the_user_will_insert_agent_number_01321188766(number):
    """the user will insert agent number "01321188766"."""
    RegistrationActivity().enter_mobile_number(number)


@when('the user will select operator')
def the_user_will_select_operator():
    """the user will select operator."""
    RegistrationActivity().operator_selection()


# @then('close the app')
# def close_the_app():
#     """close the app."""
#     raise NotImplementedError


@then(parsers.parse('the user will seen the field for "{text}"'))
def the_user_will_seen_the_field_for_agent_pin(text):
    """the user will seen the field for "Agent PIN"."""
    assert LoginPinInputValidation().get_the_text_of_pin_input_field() == text







