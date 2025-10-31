#Implement a Planning Agent

class PlanningAgent:
    def __init__(self, initial_state, goals, actions):
        self.state = initial_state
        self.goals = goals
        self.actions = actions

    def is_goal_reached(self):
        return all(self.state.get(k) == v for k, v in self.goals.items())

    def plan(self):
        plan = []
        while not self.is_goal_reached():
            for action in self.actions:
                if action.is_applicable(self.state):
                    plan.append(action)
                    self.state = action.apply(self.state)
                    break
            else:
                raise Exception("No applicable actions found, planning failed.")
        return plan
    
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def is_applicable(self, state):
        return all(state.get(k) == v for k, v in self.preconditions.items())

    def apply(self, state):
        new_state = state.copy()
        for k, v in self.effects.items():
            new_state[k] = v
        return new_state
    
if __name__ == "__main__":
    # Define initial state
    initial_state = {
        'has_key': False,
        'door_locked': True,
        'inside_room': False
    }

    # Define goals
    goals = {
        'inside_room': True
    }

    # Define actions
    actions = [
        Action(
            name='find_key',
            preconditions={'has_key': False},
            effects={'has_key': True}
        ),
        Action(
            name='unlock_door',
            preconditions={'has_key': True, 'door_locked': True},
            effects={'door_locked': False}
        ),
        Action(
            name='enter_room',
            preconditions={'door_locked': False},
            effects={'inside_room': True}
        )
    ]

    # Create a planning agent
    agent = PlanningAgent(initial_state, goals, actions)

    # Generate a plan
    try:
        plan = agent.plan()
        print("Plan found:")
        for action in plan:
            print(f"- {action.name}")
    except Exception as e:
        print(str(e))

        #explanation:
    # This code defines a simple planning agent that can generate a sequence of actions to achieve a specified goal from an initial state.
    # The PlanningAgent class manages the planning process, while the Action class represents individual actions with their preconditions and effects.

    