import json
import os


class get_inform():
    def __init__(self):
        self.seu = self.gps_inform = {}
        self.serverchan = "0"
        self.load_json()

    def load_json(self):
        inform = json.loads(os.environ["SEU_REPORT_INFORM"])
        self.seu = inform["seu_account"]
        self.serverchan = inform['serverchan']
