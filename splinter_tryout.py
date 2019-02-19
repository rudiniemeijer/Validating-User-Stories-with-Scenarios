from splinter import Browser

browser = Browser('chrome')

browser.visit("http://www.google.com")
browser.fill('q', 'Retro website geserveerd vanaf een Raspberry Pi 3')
button = browser.find_by_name('btnG')
button.click()

# Alternatively
# browser.find_by_name('btnG').click()

if browser.is_text_present('Retro-Lab'):
  print("Found it!")
else:
  print("Did not find it!")

browser.quit()
