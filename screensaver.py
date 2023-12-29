import time

#refresh_long_wait = 43200.0
refresh_long_wait = 5
refresh_short_wait = 0.5
idle_interval = 5
class Refresher:
    def __init__(self):
        self.active = False
        self.list_of = ("RED","BLUE","GREEN")
        self.current_color = 0
        self.color = self.list_of[0]
        self.interval = time.monotonic()
        self.screen_refresh = time.monotonic()  # using monotonic
        self.input_refresh = time.monotonic()
        self.refresh_interval = refresh_long_wait  # sec 12H
        self.idle_interval = idle_interval
        
    def refresh(self):
        self.screen_refresh = time.monotonic()
        print(self.list_of[self.current_color])
        if  self.list_of[self.current_color] == "GREEN":
            self.refresh_interval = refresh_long_wait  # sec 12H
            self.current_color = 0
        else:
            self.refresh_interval = refresh_short_wait = 0.5
            self.current_color = self.current_color + 1
            


screen = Refresher()
while True:
    if (time.monotonic() - screen.screen_refresh  > screen.refresh_interval):
        print ("Input")
        if(time.monotonic() - screen.input_refresh > screen.idle_interval):
            screen.refresh()
        else:
            screen.screen_refresh = time.monotonic() #сброс до следующего цикла, добавить убрать экран
            screen.refresh_interval = refresh_long_wait
            screen.current_color = 0
