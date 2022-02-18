import pyautogui

class MouseControler():
    def __init__(self, speed: int, mvt_duration: int, resolution : list, min_treshold: int, buffer_size: int) -> None:

        self.rows = resolution[0]
        self.cols = resolution[1]
        self.min_treshold = min_treshold
        self.command = "space"
        self.command_buffer = ["space"] * buffer_size

        self.num_pixel = self.computeFromSpeed(speed, mvt_duration)

    def computeFromSpeed(self, speed : int, mvt_duration) -> int:
        return speed * mvt_duration

    def assignCommandFromData(self, x: float , y : float) -> str:

        command = "space"
        if (abs(x) < self.min_treshold and abs(y) < self.min_treshold ):
            return command
        else: 
            if(x > 0  and abs(y) < 0.5 * x):
                command = "left"
            if(x < 0  and abs(y) < 0.5 * abs(x)):
                command = "right"
            if(y > 0  and abs(x) < 0.5 * y):
                command = "down"
            if(y < 0  and abs(x) < 0.5 * abs(y)):
                command = "up"

        return command
    
    def all_equal(self, iterator):
        iterator = iter(iterator)
        try:
            first = next(iterator)
        except StopIteration:
            return True
        return all(first == x for x in iterator)

    def assign_new_command(self,data_x: float, data_y:float) -> None:

        new_command = self.assignCommandFromData(data_x, data_y)
        self.command_buffer.pop()
        self.command_buffer.insert(0,new_command)

        if self.all_equal(self.command_buffer):
            self.command = new_command
    
    def moveMouse(self,data_x: float, data_y:float) -> None:

        self.assign_new_command(data_x,data_y)

        if(self.command == "down"):
            pyautogui.moveRel(0, self.num_pixel)  # move mouse num_pixel pixels down

        if(self.command == "up"):
            pyautogui.moveRel(0, -self.num_pixel)  # move mouse num_pixel pixels down

        if(self.command == "right"):
            pyautogui.moveRel(self.num_pixel, 0)  # move mouse num_pixel pixels down
        
        if(self.command == "left"):
            pyautogui.moveRel(-self.num_pixel, 0)  # move mouse num_pixel pixels down
