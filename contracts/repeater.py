# KT19QYTtX2aDxiaR1AEvZqS2t12CpXSxS8ef
# Originated by Alice

import smartpy as sp


class Repeater(sp.Contract):
    def __init__(self):
        self.init(storage='start')

    @sp.entry_point
    def repeat(self, params):
        self.data.storage = params


@sp.add_test(name="Repeater Test")
def test():
    contract = Repeater()
    scenario = sp.test_scenario()

    scenario.register(contract, show=True)
    scenario += contract.repeat('end')


sp.add_compilation_target("repeater_compiled", Repeater())
