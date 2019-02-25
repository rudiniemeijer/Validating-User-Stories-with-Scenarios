from behave import *
from hamcrest import *

@given(u'the home page is in front of me')
def step_impl(context):
  context.browser.visit(context.basicurl)

@given(u'I see a button with a country flag')
def step_impl(context):
  context.execute_steps("Given the home page is in front of me")
  
@when(u'I select my preferred language flag')
def step_impl(context):
    context.browser.visit(context.basicurl + "/" + context.userdata["preferred_language"])

@then(u'the page is translated into my preferred language')
def step_impl(context):
    if context.userdata["preferred_language"] == "en":
        assert_that(context.browser.html, contains_string("What's on"))

@given(u'I have selected the English language')
def step_impl(context):
    context.browser.visit(context.basicurl + "en/")

@then(u'I see the following subjects')
def step_impl(context):
    for row in context.table:
        context.loggit.info("Checking subject <%s> on this page", row["subject"])
        # do some tests here

@given(u'I am on the {subject} page')
def step_impl(context, subject):
    context.loggit.info("Fetching basic url: <%s>, subject is <%s>", context.basicurl + "en/", subject)
    context.browser.visit(context.basicurl + "en/")
    context.browser.click_link_by_text(subject)
    context.loggit.info("Clicked it")

@when(u'I scan the page')
def step_impl(context):
    pass

@then(u'I find information about {nugget}')
def step_impl(context, nugget):
    #assert_that(context.current_page, contains_string(nugget))
    assert_that(context.browser.is_text_present(nugget))
