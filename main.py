from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="Qwen/Qwen3.5-4B",
    model_provider="openai"
)

def get_weather(city: str) -> str:
    """获取指定城市的天气"""

    return f"{city}最近都是晴天!"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一名天气问答助手"
)

result = agent.invoke(
    {
        "messages": [{
            "role": "user",
            "content": "重庆天气怎么样"
        }]
    }
)

# print(result["messages"][-1].content_blocks)
print(result)
