from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
  latitude: float
  longitude: float

p = Position(latitude=10, longitude=30)
print(p)

t = Position(latitude=90, longitude=p.longitude)
t.longitude = 20
