from fastapi import APIRouter
import boto3
import json

from utils.chat_model import ChatModel

chat_bedrock = APIRouter(prefix="/chat_converse", tags=["chat_converse"])


@chat_bedrock.get("/api/converse")
async def chat_claude():
    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

    prompt = "AWSについて教えて。"
    print(f"Prompt: {prompt}")

    # model_idsで設定したリストの分だけ実行
    for model in model_ids:
        response = bedrock_converse(bedrock, model, prompt)
        print(f"Model : {model}\n{response}")
    pass

# 使用したいモデルのリスト
model_ids = {
 	"anthropic.claude-v2:1",
  	"anthropic.claude-3-haiku-20240307-v1:0",
    "anthropic.claude-3-5-sonnet-20240620-v1:0"
}

def bedrock_converse(client, id, prompt, max_tokens=300, temperature=0, top_p=0.9):
    response = ""
    response = client.converse(
        modelId=id,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ],
            }
        ],
        inferenceConfig={
            "temperature": temperature,
            "maxTokens": max_tokens,
            "topP": top_p
        }
    )

    # 結果の抽出
    result = response['output']['message']['content'][0]['text'] \
    + '\n--- Latency: ' + str(response['metrics']['latencyMs']) \
    + 'ms - Input tokens:' + str(response['usage']['inputTokens']) \
    + ' - Output tokens:' + str(response['usage']['outputTokens']) + ' ---\n'
    return result
