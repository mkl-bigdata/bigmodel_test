import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.environ['api_key'],
    base_url=os.environ['base_url'],
)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather", # 工具的名称： 小写、下划线， v开头
            "description": "Get weather of a location, the user should supply a location first.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city_name": {  # 入参属性名
                        "type": "string",  # 属性的类型： string、number、boolean
                        "description": "The city and state, e.g. San Francisco, CA",  #  参数的说明
                    }
                },
                "required": ["city_name"]  # 参数是否是必填的
            },
        }
    },
]

#定义函数
def get_weather(city_name):
    # 这里可以调用实际的天气API获取天气信息
    return f"{city_name}的天气是晴天，温度25摄氏度。"

def available_functions():
    return {
        "get_weather": get_weather
    }

message  = [ {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "请告诉我北京和上海的天气。"}]
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=message,
    tools=tools,
    parallel_tool_calls=True,  # 开启并行工具调用， 可能不同的模型支持的程度不同
)

import json


def execute_tool_calls(message, response):
    message.append(response.choices[0].message.model_dump())
    tool_calls = response.choices[0].message.tool_calls

    for tool_call in tool_calls:
        # 拿到要调用的函数
        function_name = tool_call.function.name
        # 函数的参数
        arguments = json.loads(tool_call.function.arguments)
        if function_name in available_functions():
            result = available_functions()[function_name](**arguments)
            message.append({
                "role": "tool",  # 固定写法，表示这是工具调用的结果
                "tool_call_id": tool_call.id,  # 关联到具体的工具调用
                "content": str(result)
            })

message = execute_tool_calls(message, response)
print(message)

# second_response = client.chat.completions.create(
#     model="deepseek-v4-pro",
#     messages=message
# )
#
# second_response.choices[0].message.content