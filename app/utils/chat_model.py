from enum import Enum

class ChatModel(str, Enum):
    claude = "anthropic.claude-v2:1"
    titan = "amazon.titan-text-express-v1"
