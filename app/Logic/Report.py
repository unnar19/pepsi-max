from Logic.Base import Base

class Report(Base):
    
    def __init__(self) -> None:
        super().__init__("report", "id")

    def get_all(self, data: str):
        return super().get_all(data)

    def get(self, data: str):
        return super().get(data)

    def post(self, data: str):
        return super().post(data)

    def put(self, data: str):
        return super().put(data)
    
    def __is_new(self, data: str):
        return super().__is_new(data)

    def __valid_put_data(self, ui_load: dict):
        return super().__valid_put_data(ui_load)

    def __is_boss(self, data: str):
        return super().__is_boss(data)

