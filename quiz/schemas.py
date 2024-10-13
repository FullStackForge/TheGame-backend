# In schemas.py
from ninja import Schema

class ScoreSchema(Schema):
    player: str  # Optionally include player name
    score: int
    time_taken: float  # or int, depending on how you want to store the time
class SubmitScoreSchema(Schema):
    score: int
    time_taken: float  # Time in seconds or as a float