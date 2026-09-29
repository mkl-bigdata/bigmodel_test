from 包装函数.exec_tools import exec_tools
from 包装函数.genclient import genclient
from 包装函数.tools import get_tools
from IPython.display import Markdown
messages = [
    {"role": "user", "content": "请帮我查询北京和上海的天气情况，并将天气结果通知给makuolang"}
]

#第一次调用模型
response = genclient(messages, "deepseek-v4-pro", get_tools())

#第一次结合模型的返回值调用工具
messages = exec_tools(messages, response)

#第二次调用模型结合第一次调用工具的结果
second_response = genclient(messages, "deepseek-v4-pro", get_tools())

#第二次结合模型的返回值调用工具
messages = exec_tools(messages, second_response)

#最后一次调用模型结合第二次调用工具的结果
third_response = genclient(messages, "deepseek-v4-pro", get_tools())

#发送消息和气温的数据
print(third_response.choices[0].message.content)
