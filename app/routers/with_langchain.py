from fastapi import APIRouter
from langchain_aws import ChatBedrock
from langchain.schema import HumanMessage

chat_langchain = APIRouter(prefix="/chat_langchain", tags=["chat_langchain"])

@chat_langchain.get("/api/langchain")
async def chat_claude():
	chat = ChatBedrock(
		model_id="anthropic.claude-v2:1", # なんか3.5Sonnetだとエラーが出る
  		model_kwargs={"temperature": 0.1, "top_p": 0.9, "max_tokens": 10000}
	)

	result = chat.invoke([
		HumanMessage(content="AWSについて教えて。"),
	])

	print(result.content)
	return result.content
