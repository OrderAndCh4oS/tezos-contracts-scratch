# KT1GdYsJeKuqdsw8jwVcXZBYpiMT1uDv1F1e
# Originated by Alice

import smartpy as sp


class Summarise(sp.Contract):
    def __init__(self):
        self.init(storage=sp.nat(0))

    @sp.entry_point(name='sum')
    def sum(self, x):
        sp.verify((x >= 5) & (x <= 100), "Not in range 5–100")
        with sp.for_("i", sp.range(1, x + 1)) as i:
            self.data.storage += i


@sp.add_test(name="Summarise Test")
def test():
    scenario = sp.test_scenario()
    contract = Summarise()

    scenario += contract
    scenario += contract.sum(5)
    scenario += contract.sum(50)
    scenario += contract.sum(100)
    scenario += contract.sum(0).run(valid=False, exception="Not in range 5–100")
    scenario += contract.sum(3).run(valid=False, exception="Not in range 5–100")
    scenario += contract.sum(101).run(valid=False, exception="Not in range 5–100")
    scenario += contract.sum(1001).run(valid=False, exception="Not in range 5–100")

    sp.catch_exception(contract.sum(-1), t=sp.TUnknown)


sp.add_compilation_target("summarise_compiled", Summarise())
