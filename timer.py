import pygame
class Timer:
    def __init__(self, duration, func, autostart=False, one_time=False):
        self.time_out = False
        self.duration = duration
        self.autostart = autostart
        self.one_time = one_time
        self.start_time = None
        self.func = func
        self.active = False

        if self.autostart:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()
        self.time_out = False

    def deactivate(self):
        self.active = False
        self.start_time = None
        self.time_out = True


    def update(self):
        if self.active:
            if self.start_time is not None and self.start_time > 0:
                if pygame.time.get_ticks() - self.start_time >= self.duration:
                    self.func()
                    self.active = False
                    self.time_out = True

            if self.time_out:
                if self.one_time:
                    self.deactivate()
                else:
                    self.activate()