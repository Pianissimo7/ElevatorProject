import json
from Elevator import Elevator


class Building:
    def __init__(self, buildingjson):
        self.buildingjson = buildingjson
        self.elevators = []

        f = open(buildingjson)
        data = json.load(f)

        self.minfloor = data["_minFloor"]
        self.maxfloor = data["_maxFloor"]

        for i in data["_elevators"]:
            self.elevators.append()
            #print()


        f.close()
    def __str__(self):
        return ""
