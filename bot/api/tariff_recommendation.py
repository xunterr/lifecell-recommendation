import json
from pathlib import Path
from azureml.core.workspace import Workspace, Webservice
from bot.config import Config
from types import SimpleNamespace


class TarifRecommendationAPI:
    def __init__(self, config: Config) -> None:
        self.config = config

    def get_recommendation(self, input: dict):

        ws = Workspace.get(
            name=self.config.azure_api.workspace_name,
            subscription_id=self.config.azure_api.subscription_id,
            resource_group=self.config.azure_api.resource_group
        )
        service = Webservice(ws, self.config.azure_api.service_name)
        
        print(input)
        data = service.run(self.jsonify(input))
        result_json = json.loads(data)
        tariff_plan_prediction = result_json["result"][0][5]
        print(result_json)
        print(tariff_plan_prediction)
        if(round(tariff_plan_prediction) == 1):
            return "Просто Лайф"
        elif(round(tariff_plan_prediction)==2):
            return "Platinum Лайф"
    
    def jsonify(self, src: list):
        new_entry = {
            "Seconds of Use": src[0],
            "Frequency of use": src[1],
            "Frequency of SMS": src[2],
            "Age Group": src[3],
            "Tariff Plan": 0
        }
        return json.dumps([new_entry])

    
