import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

"""
Translate English to French
"""
def english_to_french(english_text):
    #write the code here

    try:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        # print(json.dumps(translation, indent=2, ensure_ascii=False))

        return french_text["translations"][0]["translation"]
    except:
        return None
    finally:
        print("Strange")

"""
Translate French to English
"""
def french_to_english(french_text):
    #write the code here
    try:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

        return english_text["translations"][0]["translation"]
    except:
        return None
    finally:
        print("Strange")

# print(englishToFrench("Hello, how are you"))
#print(frenchToEnglish("Bonjour, comment vous êtes aujourd'hui?"))

