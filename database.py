import json
import os
from datetime import datetime

class UserDatabase:
    def __init__(self):
        self.db_file = 'user_data.json'
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}
    
    def save_data(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_test_result(self, username, test_data):
        if username not in self.data:
            self.data[username] = {'tests': []}
        
        test_result = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'questionnaire_score': test_data.get('questionnaire_score', 0),
            'camera_score': test_data.get('camera_score', 0),
            'voice_score': test_data.get('voice_score', 0),
            'total_score': test_data.get('total_score', 0),
            'percentage': test_data.get('percentage', 0),
            'status': test_data.get('status', 'Normal'),
            'camera_reason': test_data.get('camera_reason', ''),
            'voice_reason': test_data.get('voice_reason', [])
        }
        
        self.data[username]['tests'].append(test_result)
        self.save_data()
    
    def get_user_tests(self, username):
        if username in self.data:
            return self.data[username]['tests']
        return []
    
    def get_all_users(self):
        return list(self.data.keys())

# Global database instance
db = UserDatabase()
