from typing import Tuple
from redbot.core import commands

import discord
default_team = {"channel":[], "created_channel":[], "goal_id":{}, "game_state":"Null", "period":0, "game_start":""}
class TeamEntry:
    def __init__(self, game_state:str, team_name: str, period:int,
                 channel: list, goal_id: dict, created_channel:list, game_start:str):
        super().__init__()
        self.game_state = game_state
        self.team_name = team_name
        self.period = period
        self.channel = channel
        self.goal_id = goal_id
        self.created_channel = created_channel
        self.game_start = game_start

    def to_json(self) -> dict:
        return {
            "team_name": self.team_name,
            "game_state": self.game_state,
            "channel": self.channel,
            "period": self.period,
            "created_channel": self.created_channel,
            "game_start": self.game_start,
            "goal_id": self.goal_id
        }

    @classmethod
    def from_json(cls, data: dict):
        return cls(data["team_name"], data["game_state"], data["game_start"],
                  data["channel"], data["period"], data["goal_id"], data["created_channel"])