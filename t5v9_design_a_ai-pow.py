import os
import json
from typing import List, Dict

class AICLIController:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> Dict:
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def get_commands(self) -> List[str]:
        return list(self.config['commands'].keys())

    def execute_command(self, command: str, args: List[str]) -> str:
        if command in self.config['commands']:
            func = self.config['commands'][command]['func']
            return eval(func)(*args)
        else:
            return "Command not found"

    def add_command(self, command: str, func: str) -> None:
        self.config['commands'][command] = {'func': func}
        self.save_config()

    def remove_command(self, command: str) -> None:
        if command in self.config['commands']:
            del self.config['commands'][command]
            self.save_config()

    def save_config(self) -> None:
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def main():
    config_file = 'config.json'
    controller = AICLIController(config_file)

    # Initialize commands
    controller.add_command('add', 'add(a, b)')
    controller.add_command('subtract', 'subtract(a, b)')

    while True:
        command = input("Enter command: ")
        args = input("Enter arguments: ").split()
        result = controller.execute_command(command, args)
        print(result)

if __name__ == "__main__":
    main()