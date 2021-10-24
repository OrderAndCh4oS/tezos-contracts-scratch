# KT1RFkCrdoSjZkXkBDA7PfRq4EHeBJ4Kg66g
# Originated by Alice

import smartpy as sp


class Repeater(sp.Contract):
    def __init__(self):
        self.init(storage=sp.int(0))

    @sp.entry_point
    def repeat(self, x):
        with sp.if_(x > 0):
            self.data.storage = x
        with sp.else_():
            self.data.storage = 0


@sp.add_test(name="Repeater Test")
def test():
    contract = Repeater()
    scenario = sp.test_scenario()

    scenario.register(contract, show=True)
    scenario += contract.repeat(-1)


sp.add_compilation_target("repeater_compiled", Repeater())
