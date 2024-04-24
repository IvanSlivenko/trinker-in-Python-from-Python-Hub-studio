import psutil as pt
from time import sleep

class CpuBar():
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()

    def cpu_percent_return(self):
        return pt.cpu_percent(percpu=True) #---------------------------- Детальне завантаження процесора

# x =  CpuBar()
#
# for i in range(10):
#     print(x.cpu_percent_return())
#     sleep(1)

    def cpu_one_return(self):
        return pt.cpu_percent()#---------------------------------------- Сумарне завантаження процесора

    def ram_usage(self):
        return pt.virtual_memory()

    # def temp_usage(self):
    #     return pt.sensors_temperatures()



# print(CpuBar().ram_usage())