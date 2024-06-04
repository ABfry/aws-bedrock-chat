from fastapi import APIRouter
import boto3
import json

from utils.chat_model import ChatModel

chat_bedrock = APIRouter(prefix="/chat_bedrock", tags=["chat_bedrock"])


@chat_bedrock.get("/api/bedrock")
async def chat_claude(model: ChatModel = ChatModel.claude):
    bedrock = boto3.client(service_name="bedrock-runtime", region_name="ap-northeast-1")

    body = json.dumps(
        {
            "prompt": "\n\nHuman:AWSについて教えて。\n\nAssistant:",
            "max_tokens_to_sample": 1024,
            "temperature": 0.1,
            "top_p": 0.9,
        }
    )

    modelId = model
    accept = "application/json"
    contentType = "application/json"

    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )

    response_body = json.loads(response.get("body").read())

    print(response_body.get("completion"))
    pass
