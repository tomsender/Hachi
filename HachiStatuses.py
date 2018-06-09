from state import State


class StarvingState(State):
    def on_event(self, event):
        if event == 'ate':
            return HyperactiveState()

        return self

    def get_status(self):
        return "I Want to eat!!!"


class HyperactiveState(State):
    def on_event(self, event):
        if event == 'walked':
            return SatisfiedState()

        return self

    def get_status(self):
        return "I have kaki, take me out!!!"


class SatisfiedState(State):
    def on_event(self, event):
        return self

    def get_status(self):
        return "Everything is good :)"
