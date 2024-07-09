from fastapi import APIRouter
import boto3
import json

from utils.chat_model import ChatModel

chat_bedrock = APIRouter(prefix="/chat_bedrock", tags=["chat_bedrock"])


@chat_bedrock.get("/api/bedrock")
async def chat_claude(model: ChatModel = ChatModel.claude35):
    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

    body = json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 10000,
            "temperature": 0.1,
            "top_p": 0.9,
            "messages" : [
                {
                    "role": "user",
                    "content": "AWSについて教えて。",
                }
            ]
        }
    )

    modelId = model
    accept = "application/json"
    contentType = "application/json"

    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )

    response_body = json.loads(response.get("body").read())

    answer = response_body["content"][0]["text"]

    print(answer)
    pass
