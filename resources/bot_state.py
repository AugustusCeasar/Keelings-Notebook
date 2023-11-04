import dataclasses
import json
import os
from dataclasses import dataclass

from dataclasses_json import dataclass_json


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


@dataclass_json
@dataclass(slots=True)
class ConnectedChannels:
    guild_id_a: int
    guild_id_b: int
    channel_id_a: int
    channel_id_b: int


@dataclass_json
@dataclass(slots=True)
class BotState:
    user_timezone_dict: dict[int, str]
    connected_channels: list[ConnectedChannels]

    def save_to_json(self, path, override=False) -> None:
        if os.path.isfile(path) and not override:
            raise FileExistsError(
                f"WARNING - {path} already exists. Specify the override flag if you want to replace it")
        with open(path, 'w') as dump_file:
            json.dump(self, dump_file, cls=EnhancedJSONEncoder)

    @classmethod
    def load_from_json_path(cls, path):
        with open(path, "r") as f:
            return BotState.from_json(f.read())

