import json
import pathlib

from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False,
        "scaling": 69,
        "scalingType": 3,
        "scalingTypePdf": 3,
    }
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
for file in pathlib.Path.cwd().glob("*.html"):
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROMEDRIVER_PATH)
    driver.get(file.as_uri())
    driver.execute_script('window.print();')
    driver.quit()