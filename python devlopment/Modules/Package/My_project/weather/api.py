def fetch_weather(city):
    # In a real app, you'd use the 'requests' library here
    # For this example, we'll simulate a data response
    mock_data = {
        "Mumbai": {"temp": 30, "desc": "Sunny"},
        "Delhi": {"temp": 22, "desc": "Foggy"},
        "Bangalore": {"temp": 25, "desc": "Pleasant"}
    }
    return mock_data.get(city, {"temp": "N/A", "desc": "Unknown city"})