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

def query_db(sql_code):
    cnx = MySQLConnection(**config)
    cursor = cnx.cursor()
    cursor.execute(sql_code)
    data = cursor.fetchone()
    cursor.close()
    cnx.close()
    return data

#!----------------------------------------------------------------------------------------------------

class ActionProductBrandDescription(Action):

    def name(self) -> Text:
        return "action_product_brand_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_brand = tracker.get_slot('ProductBrand')
        if product_brand is not None:
            
            sql_code = f"select desciption from bot_product_brand where name = '{product_brand}'"
            data = query_db(sql_code)
            description = str(data[0])
            dispatcher.utter_message(description)
        else :
            dispatcher.utter_message("Sorry, I couldn't understand what you were trying to convey")

        return []

#!----------------------------------------------------------------------------------------------------
class ActionProductBrandDescription(Action):

    def name(self) -> Text:
        return "action_product_brand_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_brand = tracker.get_slot('ProductBrand')
        if product_brand is not None:
            
            sql_code = f"select desciption from bot_product_brand where name = '{product_brand}'"
            data = query_db(sql_code)
            description = str(data[0])
            dispatcher.utter_message(description)
        else :
            dispatcher.utter_message("Sorry, I couldn't understand what you were trying to convey")

        return []
#!----------------------------------------------------------------------------------------------------
class ActionProductLineDescription(Action):

    def name(self) -> Text:
        return "action_product_line_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_line = tracker.get_slot('ProductLine')
        if product_line is not None:
            sql_code = f"select desciption from bot_product_line where name = '{product_line}'"
            data = query_db(sql_code)
            description = str(data[0])
            dispatcher.utter_message(description)
        else :
            dispatcher.utter_message("Sorry, I couldn't understand what you were trying to convey")

        return []


class ActionBrandDosageDescription(Action):

    def name(self) -> Text:
        return "action_brand_dosage_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_line = tracker.get_slot('ProductBrand')
        if product_line is not None:
            sql_code = f"select dosage from bot_product_line where name = '{product_line}'"
            data = query_db(sql_code)
            description = str(data[0])
            dispatcher.utter_message(description)
        else :
            dispatcher.utter_message("Sorry, I couldn't understand what you were trying to convey")

        return []

class ActionRoleofIngredientsDescription(Action):

    def name(self) -> Text:
        return "action_role_of_ingredients_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_line = tracker.get_slot('ProductBrand')
        if product_line is not None:
            sql_code = f"select role_of_ingredients from bot_product_line where name = '{product_line}'"
            data = query_db(sql_code)
            description = str(data[0])
            dispatcher.utter_message(description)
        else :
            dispatcher.utter_message("Sorry, I couldn't understand what you were trying to convey")

        return []


class ActionProductLineList(Action):

    def name(self) -> Text:
        return "action_role_of_ingredients_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_line = tracker.get_slot('ProductBrand')
        if product_line is not None:
            sql_code = f"select role_of_ingredients from bot_product_line where name = '{product_line}'"
            data = query_db(sql_code)
            description = str(data[0])
            dispatcher.utter_message(description)
        else :
            dispatcher.utter_message("Sorry, I couldn't understand what you were trying to convey")

        return []
