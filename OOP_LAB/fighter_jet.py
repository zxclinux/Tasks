from airplane import Airplane
from log_decorator import log_method_call

class FighterJet(Airplane):

    @log_method_call
    def cost(self):
        return super().cost() * 2
