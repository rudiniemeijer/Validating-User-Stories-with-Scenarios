from splinter.browser import Browser
# from hamcrest import * # Can be used as an alternative
import logging

logging.basicConfig(level=logging.INFO) # logs to the screen

browser = Browser('chrome') #also: 'firefox'

browser.visit("https://duckduckgo.com")

browser.fill('q', 'raspberry pi retro website')
button = browser.find_by_id('search_button_homepage')
button.click()

if browser.is_text_present('Retro-Lab'):
  logging.info("Found it!")
else:
  logging.info("Did not find it!")

# Alternative
# assert_that(browser.html, contains_string('Retro-Lab'))

browser.quit()
