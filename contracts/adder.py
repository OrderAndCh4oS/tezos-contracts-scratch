# KT1FEwBk3XCpSEDHj5re1VnFyPr9oGpfr5Dy
# Originated by Alice

import smartpy as sp


class Adder(sp.Contract):
    def __init__(self):
        self.init(storage=0)

    @sp.entry_point
    def add(self, params):
        self.data.storage = params.a + params.b


@sp.add_test(name="Adder Test")
def test():
    contract = Adder()
    scenario = sp.test_scenario()

    scenario.register(contract, show=True)
    scenario += contract.add(a=2, b=3)


sp.add_compilation_target("adder_compiled", Adder())
