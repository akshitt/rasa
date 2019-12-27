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
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'alkembot',
  'raise_on_warnings': True
}

def query_db(sql_code):
    cnx = MySQLConnection(**config)
    cursor = cnx.cursor()
    cursor.execute(sql_code)
    row = cursor.fetchone()
    lst_row= []
    while row is not None:
        print(row, type(row))
        lst_row.append(row[0])
        row = cursor.fetchone()
        
    cursor.close()
    cnx.close()
    return lst_row

dict_intent = {'ProductBrandDescription':'description', 'ProductBrandMRPDescription':'mrp',
 'ProductBrandRoleofIngredientsDescription': 'role_of_ingredients',
 'ProductBrandStrengthDescription':'strength' , 'ProductBrandTargetCustomersDescription':'target_customers',
  'ProductBrandUSPsDescription':'usps', 'ProductFormDescription':'form_id',
 'ProductBrandCompetitorsDescription':'competitors', 'ProductBrandCompositionDescription':'composition',
  'ProductBrandDosageDescription':'dosage', 'ProductBrandIndicationDescription':'indication'}


class ActionProductBrand(Action):

    def name(self) -> Text:
        return "action_product_brand"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_brand = tracker.get_slot('ProductBrand')
        intent = tracker.latest_message["intent"].get("name")
        print(tracker.latest_message['entities'])

        if product_brand is not None and intent in dict_intent.keys():
            column_db = dict_intent[intent]
            sql_code = f"select {column_db} from bot_product_brand where name = '{product_brand}'"
            data = query_db(sql_code)
            if intent=='ProductFormDescription': # form is stored in id
                data = int(data)
                sql_code = f"select name from bot_product_form where id={data}"
                data = query_db(sql_code) 
            utterance = str(data[0])
            dispatcher.utter_message(utterance)
        elif product_brand is None and intent in dict_intent.keys():
            dispatcher.utter_message("Can please specify the product name?")



        return []


class ActionProductLineDescription(Action):

    def name(self) -> Text:
        return "action_product_line_description"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_line = tracker.get_slot('ProductLine')
        data_list = query_db(f'select description from bot_product_line where name={ProductLine}')
        data_str = str(data_list)[1:-1]
        dispatcher.utter_message(data_str)

        return []

class ActionDivisionDescription(Action):

    def name(self) -> Text:
        return "action_division_description"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        division = tracker.get_slot('Division')
        data_list = query_db(f"select description from bot_division where name='{division}'")
        data_str = str(data_list)[1:-1]
        dispatcher.utter_message(data_str)

        return []

class ActionComapanyDescription(Action):

    def name(self) -> Text:
        return "action_company_description"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_list = query_db('select description from bot_company_master where name=Alkem')
        data_str = str(data_list)[1:-1]
        dispatcher.utter_message(data_str)

        return []


def list2buttons(lst):
    buttons = []
    for element in lst:
        dict_entity = {'ProductLine':element}
        buttons.append({'title':element, 'payload':'/ProductLineDescription'+str(dict_entity) })

class ActionProductLineList(Action):

    def name(self) -> Text:
        return "action_product_line_list"
    

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_list = query_db('select name from bot_product_line')
        data_str = ', '.join(data_list)
        buttons = list2buttons(data_list)
        dispatcher.utter_message('Alkem has amazing product lines catering to your various needs which cover the following:', buttons=buttons)

        return []


class ActionDivisionList(Action):

    def name(self) -> Text:
        return "action_division_list"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_list = query_db('select name from bot_division')
        data_str = ', '.join(data_list)
        dispatcher.utter_message(data_str)

        return []

class ActionProductBrandList(Action):

    def name(self) -> Text:
        return "action_product_brand_list"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_list = query_db('select name from bot_division')
        data_str = str(data_list)[1:-1]
        dispatcher.utter_message(data_str)
