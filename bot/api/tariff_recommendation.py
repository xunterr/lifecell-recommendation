import json
from pathlib import Path
from azureml.core.workspace import Workspace, Webservice
from bot.config import Config

class TarifRecommendationAPI:
    def __init__(self, config: Config) -> None:
        self.config = config

    def get_recommendation(self):
        ws = Workspace.get(
            name=self.config.azure_api.workspace_name,
            subscription_id=self.config.azure_api.subscription_id,
            resource_group=self.config.azure_api.resource_group
        )
        service = Webservice(ws, self.config.azure_api.service_name)
        sample_file_path = '_samples.json'
        
        with open(sample_file_path, 'r') as f:
            sample_data = json.load(f)
        score_result = service.run(json.dumps(sample_data))
        print(f'Inference result = {score_result}')
    
