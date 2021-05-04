from behave import *
from Pages.Page import PageConv
from driverHelper import DriverHelper

_driver = DriverHelper.driver
page = PageConv(_driver)


class Step:

    @given('Open the Unit Conversion app')
    def step_impl(context):
        page.AppOpen()

    @given('the app Unit Conversion has opened')
    def step_impl(context):
        page.AppOpenVerify()

    @when('the user selects the menu icon')
    def step_impl(context):
        page.NavDrawer()

    @then('the Menu becomes visible')
    def step_impl(context):
        page.NavDrawerVerify()

    @when('length is selected')
    def step_impl(context):
        page.length()

    @then('length conversion window becomes visible')
    def step_impl(context):
        page.lengthVerify()

    @when('C is selected')
    def step_impl(context):
        page.clear()

    @then('the converted value clears')
    def step_impl(context):
        page.clearVerify()

    @when('kilometres is selected as first unit')
    def step_impl(context):
        page.firstUnit()
        page.unitKM()

    @when('miles is selected as second unit')
    def step_impl(context):
        page.secondUnit()
        page.unitMiles()

    @when('value 200 is entered')
    def step_impl(context):
        page.num2()
        page.num0()
        page.num0()

    @then('"{value}" is displayed as the converted measurements')
    def step_impl(context, value):
        page.result(value)
