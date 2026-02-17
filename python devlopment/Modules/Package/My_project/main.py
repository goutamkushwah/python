import weather

city_name = "Mumbai"

# Fetch data using the package
raw_data = weather.fetch_weather(city_name)

# Format and print
report = weather.format_output(city_name, raw_data)
print(report)