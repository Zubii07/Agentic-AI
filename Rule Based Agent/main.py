class RuleBasedVacuumAgent:
    def __init__(self):
        # starting position and environment status
        self.location = 'A'
        self.environment = {'A': 'Dirty', 'B': 'Dirty'}

    def perceive(self):
        # perceive the current status and location
        return self.location, self.environment[self.location]
    
    def rule(self,location,status):
        if status == 'Dirty':
            return 'Clean'
        elif location == 'A':
            return 'Move to B'
        elif location == 'B':
            return 'Move to A'
        else:
            return 'Stay'
        

    def act(self, action):
        if action == 'Clean':
            self.environment[self.location] = 'Clean'
            print(f"Action: {action} at {self.location} → Cleaned.")
        elif action == 'Move to B':
            self.location = 'B'
            print(f"Action: {action} → Moved to Room B.")
        elif action == 'Move to A':
            self.location = 'A'
            print(f"Action: {action} → Moved to Room A.")
        else:
            print(f"Action: {action} at {self.location} → No action taken.")

    def run(self, steps=10):
        for _ in range(steps):
            location, status = self.perceive()
            action = self.rule(location, status)
            self.act(action)
            if all(state == 'Clean' for state in self.environment.values()):
                print("All rooms are clean. Agent stops.")
                break


# Example usage
if __name__ == "__main__":
    agent = RuleBasedVacuumAgent()
    agent.run(steps=10)
    print("Final environment state:", agent.environment)
    print("Final agent location:", agent.location)
    print("Agent has completed its task.")

