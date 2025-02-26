from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests

# Configurer les options de Chrome pour le mode headless (sans interface graphique)
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Si vous avez installé chromedriver dans un dossier particulier, spécifiez le chemin ici
service = Service('C:/chromedriver/chromedriver.exe')

# Initialiser le navigateur Chrome
driver = webdriver.Chrome(service=service, options=options)

# Liste des URL à scraper
urls = [
    'https://www.codashop.com/en-ph/afk-journey',
    'https://www.codashop.com/en-my/afk-journey',
    'https://www.codashop.com/en-sg/afk-journey',
    'https://www.codashop.com/th-th/afk-journey',
    'https://www.codashop.com/en-tl/afk-journey',
    'https://www.codashop.com/fr-fr/afk-journey'
]

# Dictionnaire des devises
currencies = {
    '₱': 'PHP',
    'US$': 'USD',
    'Rp.': 'IDR',
    'RM': 'MYR',
    'S$': 'SGD',
    '฿': 'THB',
    '€t': 'EUR'
}

# Parcourir les URL avec index
for index, url in enumerate(urls, start=1):  # Commencer l'index à 1
    try:
        # Ouvrir la page
        driver.get(url)

        # Attendre que la page se charge
        time.sleep(5)

        # Extraire le prix de la gazette
        price_element = driver.find_element(By.CSS_SELECTOR, 'ul.denomination-card-group li.denom-card:nth-child(3) span.price-section__price__price-container__amount')
        price = price_element.text.strip()

        # Identifier la devise
        currency_symbol = None
        for symbol in currencies:
            if symbol in price:
                currency_symbol = symbol
                break

        if currency_symbol:
            # Supprimer le symbole de devise et convertir en float
            price_numeric = float(price.replace(currency_symbol, '').replace(',', ''))
            currency_code = currencies[currency_symbol]

            # Convertir le prix en EUR (si nécessaire)
            if currency_code != 'EUR':
                api_url = f"https://api.exchangerate-api.com/v4/latest/{currency_code}"
                response = requests.get(api_url)
                data = response.json()
                eur_rate = data['rates']['EUR']
                eur_price = price_numeric * eur_rate
                print(f"URL : {index}. {url}")
                print(f"Prix de la gazette en EUR : {eur_price:.2f} EUR")
            else:
                print(f"URL : {index}. {url}")
                print(f"Prix de la gazette en EUR : {price_numeric:.2f} EUR")
        else:
            print(f"URL : {index}. {url}")
            print(f"Prix de la gazette : {price}")

    except Exception as e:
        print(f"Erreur pour {index}. {url} : {str(e)}")

# Fermer le navigateur
driver.quit()