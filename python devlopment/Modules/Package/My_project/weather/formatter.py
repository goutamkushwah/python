def format_output(city, data):
    return f"--- {city} Weather ---\nTemp: {data['temp']}°C\nCondition: {data['desc']}"