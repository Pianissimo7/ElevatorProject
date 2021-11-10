import json
from Building import Building
from Elevator import Elevator

if __name__ == '__main__':
    # f = open("files\Ex1_Buildings\B1.json")
    with open("files\Ex1_Buildings\B1.json") as f:
        data = json.load(f)
        print(json.dumps(data, indent=4))
        # print(data)
        # for k in data:
        #     print("{ ", k, ": ", data[k], "}");
        # f.close()
        # b = Building("files\Ex1_Buildings\B1.json")



def parse_json(json_path):
    with open(json_path) as f:
        data = json.load(f)

        elevators = [Elevator(e["_id"], e["_speed"] ) for e in data["_elevators"]]
        building = Building(data["_minFloor"], data['_maxFloor'], elevators)
        return building