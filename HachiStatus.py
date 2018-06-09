from HachiStatuses import SatisfiedState


class HachiStatus(object):

    def __init__(self):
        self.state = SatisfiedState()

    def on_event(self, event):
        self.state = self.state.on_event(event)

    def get_status(self):
        self.state = self.state.get_status()
