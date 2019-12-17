# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from mysql.connector import MySQLConnection

config = {
  'user': 'alkem',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'alkembot',
  'raise_on_warnings': True
}



class ActionDescription(Action):

    def name(self) -> Text:
        return "action_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('I was called')
        product_brand = tracker.get_slot('ProductBrand')
        if product_brand is not None:
            cnx = MySQLConnection(**config)
            cursor = cnx.cursor()
            cursor.execute(f"select desciption from bot_product_brand where name = '{product_brand}'")
            product_description = cursor.fetchone()
            print(type(product_description))
            product_description = str(product_description[0])
            cursor.close()
            cnx.close()

            dispatcher.utter_message(product_description)
        else :
            dispatcher.utter_message("Hello World!")

        return []
