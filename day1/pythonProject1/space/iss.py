from dataclasses import dataclass
from urllib.request import urlopen
import json
import webbrowser
from position import Position

def get_iss_position(url = 'http://api.open-notify.org/iss-now.json') -> Position:
    with urlopen(url) as response:
        data = json.loads(response.read())
        return Position(longitude=data["iss_position"]["longitude"], latitude=data["iss_position"]["latitude"])


def show_on_map(pos: Position) -> None:
    webbrowser.open(f"http://google.com/maps?q={pos.latitude},{pos.longitude}")


if __name__ == "__main__":
    pos = get_iss_position()
    show_on_map(pos)
