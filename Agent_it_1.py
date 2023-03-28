from re import I
from turtle import position
from mesa import Agent
import numpy as np

# print (my_pos)
# documentation of agent in MESA and examples of calling position of agent

class PersonAgent1(Agent):

    def __init__(self, unique_id, model):
        
        super().__init__(unique_id, model)
        self.wealth = 1
        # x_coord = self.pos[0]
        # y_coord = self.pos[1]
        # self.position_x = [x_coord]
        # self.position_y = [y_coord]
    
    def position(self):
        # global my_pos
        my_pos = np.array(self.pos)
        return my_pos

    def step(self) -> None:
        self.move()
        
# learn about current clock information..potentially to guide the motion
# keep track of motion for dynamic adjustments

    def move(self) -> None:
        
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore = False, include_center = True, radius = 1)       # defines motion
        x = possible_steps[1]
        # x = self.pos1
        new_position = x
        self.model.grid.move_agent(self, new_position)      # defines new position for the agent
        self.wealth += 1

        # converting tuple into int..
        # x_coord = self.pos[0]
        # y_coord = self.pos[1]

    # def pos1(self):
    #     possible_steps1 = self.model.grid.get_neighborhood(self.pos, moore = False, include_center = True, radius = 1)       # defines motion
    #     x1 = possible_steps1[1]
    #     new_position1 = x1
    #     return new_position1

# class SensorAgent1(Agent):
#     def __init__(self, unique_id, model) -> None:
#         super().__init__(unique_id, model)

