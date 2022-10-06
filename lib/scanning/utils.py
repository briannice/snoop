from utils import SnoopException


class HostState():
    HOST_STATES = {
        0: "UP",
        1: "DOWN",
        2: "UNKOWN"
    }

    def __init__(self, state: int = 0):
        if state < 0 or state > len(self.HOST_STATES):
            raise SnoopException("Invalid state number for host.")
        self.state = state

    def __str__(self) -> str:
        return self.get_state_name()

    def get_state_name(self) -> str:
        for key, value in self.HOST_STATES:
            if key == self.state:
                return value


class PortState():

    PORT_STATES = {
        0: "OPEN",
        1: "CLOSED",
        2: "FILTERED",
        3: "UNFILTERED",
        4: "OPEN | FILTERED",
        5: "CLOSED | FILTERED",
    }

    def __init__(self, state: int = 0):
        if state < 0 or state > len(self.PORT_STATES):
            raise SnoopException("Invalid state number for port.")
        self.state = state

    def __str__(self) -> str:
        return self.get_state_name()

    def get_state_name(self) -> str:
        for key, value in self.HOST_STATES:
            if key == self.state:
                return value
