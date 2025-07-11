#json module
import json
name=input("Enter your name: ")
age=int(input("Enter your age: "))
data={"name":name,"age":age }
# stringify the data
# stringify_json is used for converting a Python object into a JSON string
stringify_json=json.dumps(data)
print("Stringified JSON:", stringify_json)