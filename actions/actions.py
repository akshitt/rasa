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
  'password': 'root',
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

dict_intent = {'Description':'desciption', 'ProductBrandMRPDescription':'mrp',
 'ProductBrandRoleofIngredientsDescription': 'role_of_ingredients',
 'ProductBrandStrengthDescription':'strength' , 'ProductBrandTargetCustomersDescription':'target_customers',
  'ProductBrandUSPsDescription':'usps', 'ProductFormDescription':'form_id',
 'ProductBrandCompetitorsDescription':'competitors', 'ProductBrandCompositionDescription':'composition',
  'ProductBrandDosageDescription':'dosage', 'ProductBrandIndicationDescription':'indication'}

#!----------------------------------------------------------------------------------------------------

class ActionProductBrand(Action):

    def name(self) -> Text:
        return "action_product_brand"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_brand = tracker.get_slot('ProductBrand')
        intent = tracker.latest_message["intent"].get("name")

        if product_brand is not None and intent in dict_intent.keys() :
            column_db = dict_intent[intent]
            sql_code = f"select {column_db} from bot_product_brand where name = '{product_brand}'"
            data = query_db(sql_code)
            utterance = str(data[0])
            dispatcher.utter_message(utterance)
        else :
            dispatcher.utter_message("Sorry, I couldn't exactly understand what you were trying to convey")

        return []


