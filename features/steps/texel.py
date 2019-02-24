from behave import *
import hamcrest

@given(u'I have navigated to the Texel.net website')
def step_impl(context):
  context.browser.visit(context.basicurl)


@given(u'the home page is in front of me')
def step_impl(context):
  context.browser.visit(context.basicurl)


@given(u'I see a button with a country flag')
def step_impl(context):
  context.execute_steps("I have navigated to the Texel.net website")

  
@when(u'I select my preferred language flag')
def step_impl(context):
    context.preferred_language = "en"    context.browser.visit(context.basicurl + "/" + context.userdata["preferred_language"])


@then(u'the page is translated into my preferred language')
def step_impl(context):
    if context.userdata["preferred_language"] == "en":
        assert_that(context.browser.html, contains_text("WHAT'S ON"))


@given(u'I have selected the English language')
def step_impl(context):
    context.browser.visit(context.basicurl + "/en/")


@then(u'I see the following subjects')
def step_impl(context):
    for subject in context.table:
        assert_that(context.browser.html, contains_text(subject))


@given(u'I am on the {subject} page')
def step_impl(context, subject):
    raise NotImplementedError(u'STEP: Given I am on the WHAT\'S ON page')


@when(u'I scan the page')
def step_impl(context):
    context.current_page = context.browser.html


@then(u'I find information about {nugget}')
def step_impl(context, nugget):
    assert_that(context.current_page, contains_text(nugget))
