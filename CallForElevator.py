class CallForElevator:
    def __init__(self, time, src, dest, state, elev):
        self.time = time
        self.src = src
        self.dest = dest
        self.state = state
        self.elev = elev
        self.type = (dest-src)/abs(dest-src)

    def __str__(self):
        return ", ".join([
            str(self.time),
            str(self.src),
            str(self.dest),
            str(self.state),
            str(self.elev),
            str(self.type)])
