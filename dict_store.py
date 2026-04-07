def temp_and_color(data):
    temp_value = data.get("temp", None)
    color_value = data.get("color", None)
    return (temp_value, color_value)

if __name__ == "__main__":
    data1 = {"temp": 22.5, "color": "blue", "status": "ok"}
    print(temp_and_color(data1))

    data2 = {"status": "ok"}
    print(temp_and_color(data2))
