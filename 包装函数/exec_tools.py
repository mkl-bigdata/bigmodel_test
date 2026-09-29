def exec_tools(message, response):
    import json
    from 包装函数.functions import available_functions

    message.append(response.choices[0].message.model_dump())
    tool_calls = response.choices[0].message.tool_calls

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        if function_name in available_functions:
            result = available_functions[function_name](**arguments)
            message.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })
    return message