"""This is module doc string"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url( url )


def englishToFrench(english_text):
    """ Translate English language string to French"""
    #write the code here
    translation = language_translator.translate(
    text= english_text,
    model_id='en-fr').get_result()
    translation =  translation['translations'][0]['translation']
    return translation

def frenchToEnglish(french_text):
    """ Translate French language string to English"""
    #write the code here
    translation = language_translator.translate(
    text= french_text,
    model_id='fr-en').get_result()
    translation =  translation['translations'][0]['translation']
    return translation
