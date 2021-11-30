from Log_employee import Log_employee
from Log_building import Log_building
from Log_contractor import Log_contractor
from Log_maintenance import Log_maintenance
from Log_work_order import Log_work_order


class Data_wrapper:
    def __init__(self) -> None:
        self.building = Log_buildings()
        self.employee = Log_employee()


    def instructions(self, instruction):
        if instruction["instrcution"] == "log_person":
            self.employee.write_to_file(instruction["data"])
        
    def write(self):
        pass

    def read(self):
        pass