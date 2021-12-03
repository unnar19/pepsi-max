from Logic.Base import Base

class Contractor(Base):
    
    def __init__(self) -> None:
        super().__init__("contractor", "id")

    def get_all(self, data: str):
        return super().get_all(data)

    def get(self, data: str):
        return super().get(data)

    def post(self, data: str):
        return super().post(data)

    def put(self, data: str):
        return super().put(data)
