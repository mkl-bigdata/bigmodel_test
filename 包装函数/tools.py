def get_tools ():
    tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的天气情况，一次只能查询一个城市",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "要查询的城市名称，例如：北京",
                    }
                },
                "required": ["city"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_msg",
            "description": "发送天气提醒给用户，只要含有通知字样的，调用这个工具",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "发送天气提醒给用户，只要含有通知字样的，调用这个工具",
                    }
                },
                "required": ["message"]
            },
        }
    },
]

    return tools