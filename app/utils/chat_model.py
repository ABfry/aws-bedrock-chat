from enum import Enum

class ChatModel(str, Enum):
    claude2 = "anthropic.claude-v2:1"
    claude35 = "anthropic.claude-3-5-sonnet-20240620-v1:0"
