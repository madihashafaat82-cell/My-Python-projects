# Base Class
class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Robot Introduction")
        print("Name:", self.name)
        print("Model:", self.model)
        print("Purpose:", self.purpose)

    def perform_task(self):
        print(self.name, "is performing its task.")



class SmartRobot(Robot):
    def __init__(self, name, model, purpose, version):
        super().__init__(name, model, purpose)
        self.__version = version  


    def perform_task(self):
        print(self.name, "is performing smart AI tasks.")

    def show_version(self):
        print("Software Version:", self.__version)



name = input("Enter Robot Name: ")
model = input("Enter Robot Model: ")
purpose = input("Enter Robot Purpose: ")
version = input("Enter Software Version: ")


robot1 = SmartRobot(name, model, purpose, version)


robot1.introduce()
robot1.perform_task()
robot1.show_version()
