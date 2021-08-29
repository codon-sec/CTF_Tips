import base64

# decode base64
test_data = "input_data"

with open("b64output.zip", "wb") as f2:
    f2.write(base64.b64decode(test_data))
