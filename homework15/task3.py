CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_ = 0
        self.all_channel = len(channels) - 1
    
    def first_channel(self):
        self.current_channel_ = 0
        return self.channels[self.current_channel_]
    
    def last_channel(self):
        self.current_channel_ = self.all_channel
        return self.channels[self.current_channel_]
    
    def turn_channel(self, num):
        self.current_channel_ = num - 1
        return self.channels[self.current_channel_]
        
    def next_channel(self):
        if self.current_channel_ == self.all_channel:
            self.current_channel_ = 0
        
        else:
            self.current_channel_ += 1
        return self.channels[self.current_channel_]

    def previous_channel(self):
        if self.current_channel_ == 0:
            self.current_channel_ = self.all_channel
        
        else:
            self.current_channel_ -= 1
        return self.channels[self.current_channel_]
    
    def current_channel(self):
        return self.channels[self.current_channel_]
            
    def exists(self, channel):
        if channel in self.channels:
            return 'Yes'
        
        elif type(channel) == int:
            if self.all_channel >= channel:
                return self.channels[channel - 1]
            
            else:
                return 'No'
        
        return 'No'


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "BBC"

assert controller.exists(4) == "No"

assert controller.exists("BBC") == "Yes"