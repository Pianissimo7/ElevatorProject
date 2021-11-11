import json
from Building import Building
from Elevator import Elevator


def parse_json(json_path):
    with open(json_path) as f:
        data = json.load(f)

        elevators = [Elevator(
            e["_id"],
            e["_speed"],
            e["_minFloor"],
            e["_maxFloor"],
            e["_closeTime"],
            e["_openTime"],
            e["_startTime"],
            e["_stopTime"])
            for e in data["_elevators"]]
        building = Building(data["_minFloor"], data['_maxFloor'], elevators)
        print(building)
        return building


if __name__ == '__main__':
    path = "files/Ex1_Buildings/B1.json"
    parse_json(path)
