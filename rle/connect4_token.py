import colours


class Token:
    def __init__(self, identifier: str, symbol: str, colour: colours, is_player=True):
        self.symbol = symbol
        self.identifier = identifier
        self.colour = colour
        self.is_player = is_player

    def get_formatted(self):
        return self.colour + self.symbol + colours.RESET
