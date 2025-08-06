import time

class Timer2:
    # Timer that meshures time all the while while the program, 
    # but doesn't update it before self.time_it(dt) gets updated 
    def __init__(self, time_duration_between_event):
        # time in seconds
        self.time_duration = time_duration_between_event
        self.start_time = 0
        self.has_started = False

    def time_it(self, dt):
        if not self.has_started:
            self.has_started = True
            self.start_time = time.time()
        else:
            if time.time()-self.start_time >= self.time_duration:
                self.has_started = False
                return True
        return False
    


class Timer:
    # Timer that meshures time and updates it only when self.time_it(dt) gets updated
    def __init__(self, time_duration_between_event):
        # time in seconds
        self.time_duration = time_duration_between_event
        self.time_passed = 0
        self.has_started = False

    def time_it(self, dt):
        if not self.has_started:
            self.has_started = True
            self.time_passed = 0
        else:
            self.time_passed += dt

            if self.time_passed >= self.time_duration:
                self.has_started = False
                return True
        return False