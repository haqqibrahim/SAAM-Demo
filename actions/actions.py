from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

scores = []

class ActionScore(Action):
    
    def name(self) -> Text:
        return "action_score"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        intent = tracker.latest_message["intent"].get('name')
        
        if intent == 'affirm':
            score = 5
            scores.append(score)
        elif intent == 'average':
            score = 3
            scores.append(score)
        else:
            score = 1
            scores.append(score)
            
        return []
    
class ActionResult(Action):
    
    def name(self) -> Text:
        return "action_result"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
       
        sum_scores = sum(scores)
        evaluation = sum_scores/25
        percentage = evaluation * 100
        
        if percentage >= 70:
            dispatcher.utter_message(text="Your anxiety level is {}".format(percentage))
            dispatcher.utter_message(text="This is quite high, please see a professional")

        elif percentage >= 50:
                dispatcher.utter_message(text="Your anxiety level is {}".format(percentage))
                dispatcher.utter_message(text="This is an average score, you are free to see a professional if you want to")

        else:
            dispatcher.utter_message(text="Your anxiety level is {}".format(percentage))
            dispatcher.utter_message(text="This is a great score, you don't have anxiety issues")


        return []

    
    
            
