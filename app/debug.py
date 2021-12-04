#this will pass in setUp

import json
put_data_delete = json.dumps({"role": "boss",
                        "key": "employee",
                        "data": {
                            "id": str(1),
                            }
                        })

from Logic.LogicAPI import LogicAPI

emp_delete = json.dumps({
"role": "boss",
"key": "employee",
"data": {
    "id": 1,
    "name": "eeeee"
    }
})

LL = LogicAPI()

res = LL.delete(emp_delete)

