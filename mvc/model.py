import json
import os

class Counter:
    def __init__(self):
        self.file_path = "current-count.json"
        self.value = self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data.get('value', 0)
        return 0

    def _save(self):
        with open(self.file_path, 'w') as file:
            json.dump({'value': self.value}, file)

    def add_one(self):
        self.value += 1
        self._save()
        return self.value

    def subtract_one(self):
        self.value -= 1
        self._save()
        return self.value

    def get_value(self):
        return self.value
