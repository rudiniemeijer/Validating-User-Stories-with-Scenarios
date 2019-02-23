from splinter import Browser
import logging
logging.basicConfig(level=logging.INFO)

browser = Browser('chrome')

browser.visit("https://duckduckgo.com")
browser.fill('q', 'raspberry pi retro website')
button = browser.find_by_id('search_button_homepage')
button.click()

if browser.is_text_present('Retro-Lab'):
  logging.info("Found it!")
else:
  logging.warning("Did not find it!")

# Alternative 
# import hamcrest
# assert_true(browser.html, contains_string('Retro-Lab'))

browser.quit()
