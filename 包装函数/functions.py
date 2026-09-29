def get_weather(city):
    return {
        "城市": city,
        "天气": "晴",
        "温度": "25°C",
        "湿度": "60%",
        "风速": "5 km/h"
    }
def send_msg(message):
    """
    发送天气提醒给用户
    """
    return {
        "status": "success",
        "message": f"已发送消息: {message}"
    }

available_functions = {
    "get_weather": get_weather,
    "send_msg": send_msg
}