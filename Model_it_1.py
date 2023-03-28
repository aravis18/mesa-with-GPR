from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import numpy as np

from Agent_it_1 import PersonAgent1

from GPR_1 import prediction



# print(prediction([1]))
# print(agent_wealth)
# global var
var = 1
# print(agent.position for agent in model.schedule.agents)

def compute_response(model):
    # global agent_wealth
    N = prediction([var])
     
    # N = x[0]
    # N = prediction([x])
    return N*10
    # agent_position = [agent.position for agent in model.schedule.agents]
    # return agent_position
    
    # if x == 1:
    #     return 0.5
    # elif x == 2:
    #     return 0.77
    # elif x == 3:
    #     return 0.89
    # y = 5 - (x-1)
    # return y

    ## get position of agent at each time stamp
    # p1 = [agent.position for agent in model.schedule.agents]
    ## p1 = PersonAgent1.pos
    # s1 = prediction([p1])

    # return s1
    # return 0


def compute_response2(model):
    # p2 = PersonAgent1.pos
    # s2 = prediction([p2])
    return 0
    
        
    # agent_wealth = [agent.wealth for agent in model.schedule.agents]
    # x = sorted(agent_wealth)
    # N = model.num_agents
    # B = sum(xi * (N - i) for i,xi in enumerate(x)) / (N * sum(x))
    # return (1 + (1/N) - 2 * B)



class PersonModel1(Model):

    def __init__(self, number_of_agents, width, height):
        # self.position = position
        self.num_agents = number_of_agents
        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivation(self)
        self.running = True     #to be able to run simulation in server and potentially add condition to stop the simulation
        
        # Create agents
        for i in range(self.num_agents):
            a = PersonAgent1(i, self)
            self.schedule.add(a)

            # Add agent to grid in the cell
            if i == 0:
                x = 5
                y = 4
                self.position = self.grid.place_agent(a, (x,y))

                
            elif i == 1:
                x = 7
                y = 0
                self.grid.place_agent(a, (x,y))
            elif i == 2:
                x = 3
                y = 0
                self.grid.place_agent(a, (x,y))

            # for i in range(self.num_agents):
            #     if i==0:
            #         global position1
            #         position1 == 0
    
        
       

        self.datacollector = DataCollector(model_reporters={"Response": compute_response})
        self.datacollector = DataCollector(model_reporters={"Response 2": compute_response2})
    
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()            # Advance the model by one step
    
    # def posit(self):
    #     for agent in self.position:
    #         global x,y
    #         x,y = agent.position
    #         print (x)

        
# print (x)
# PersonModel1.posit(PersonModel1)