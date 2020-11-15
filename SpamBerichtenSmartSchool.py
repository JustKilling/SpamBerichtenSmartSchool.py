import time, selenium, getpass, stdiomask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

school = input("Geef je school in: ")
"""
gebruikersnaam = input("Geef je gebruikersnaam in: ")
wachtwoord = stdiomask.getpass(prompt="Geef je wachtwoord in: ", mask="*")
"""
print(
    "Welkom bij mijn eerste project met python! In dit project kan je iemand op je school spammen!"
    "\nZorg er wel voor dat je school niet boos word!")
isIngelogd = False
while True:

    # input verkrijgen van user
    aantalKeer = int(input("Hoeveel keer wil je het versturen?: "))
    naarWie = input("Naar wie wil je het versturen?: ")
    welkeTitel = input("Welke titel wil je gebruiken?: ")
    watSturen = input("Wat wil je sturen naar " + naarWie + "?: ")

    if not isIngelogd:

        # web browser openen
        PATH = "chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get("https://" + school + ".smartschool.be")
        print(driver.title)
        time.sleep(0.5)
        """
        login = driver.find_element_by_id("login_form__username")
        login.send_keys(gebruikersnaam, Keys.RETURN)
        login = driver.find_element_by_id("login_form__password")
        login.send_keys(wachtwoord, Keys.RETURN)
        """
        
        try:
            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/button"))
            )
        except:

            driver.quit()

        button = driver.find_element_by_xpath("/html/body/header/nav/div[2]/button")
        button.click()
        button = driver.find_element_by_link_text("Berichten")
        button.click()

        isIngelogd = True
    isGeopend = False
    for x in range(aantalKeer):
        driver.get(
            "https://" + school +
            ".smartschool.be/index.php?module=Messages&file=composeMessage&boxType=inbox&composeType=0&msgID=undefined")
        time.sleep(0.2)

        # iets typen
        def typIets(bericht):
            typiets = ActionChains(driver)
            typiets.send_keys(bericht).perform()

        # i keer op enter drukken
        def drukOpEnter(i):
            drukopenter = ActionChains(driver)
            drukopenter.send_keys(Keys.RETURN * i).perform()

        # i keer op tab drukken
        def drukOpTab(i):
            drukoptab = ActionChains(driver)
            drukoptab.send_keys(Keys.TAB * i).perform()

        # navigeren in het berichtenvenster en berichten typen
        typIets(naarWie)
        time.sleep(0.4)
        drukOpEnter(1)
        time.sleep(0.1)
        drukOpTab(3)
        typIets(welkeTitel)
        drukOpTab(1)
        time.sleep(0.1)
        typIets(watSturen)

        versturen = driver.find_element_by_id("submitbtn")
        versturen.click()
        driver.get("https://" + school + ".smartschool.be/index.php?module=Messages&file=index&function=main")

    while True:
        wilVerderdoen = input('Wil je nog een bericht sturen? (ja/nee): ').lower()
        if wilVerderdoen in ('ja', 'nee', 'n', 'j', 'y', 'no', 'yes'):
            break
        print("foute ingave")

    if wilVerderdoen in ('ja', 'j', 'y', 'yes'):
        continue
    else:
        print("daaaaaaaaaaaaaag")
        break

driver.quit()
