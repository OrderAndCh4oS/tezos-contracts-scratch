import smartpy as sp


class Certification(sp.Contract):
    def __init__(self, certifier):
        self.init(certified=sp.big_map(tkey=sp.TAddress, tvalue=sp.TString), certifier=certifier)

    @sp.entry_point()
    def certify(self, params):
        sp.verify(sp.sender == self.data.certifier)
        self.data.certified[params.address] = params.name


@sp.add_test(name='Test Certification')
def test():
    alice = sp.test_account("Alice")
    bob = sp.test_account("Bob")
    jill = sp.test_account("Jill")

    contract = Certification(certifier=alice)
    scenario = sp.test_scenario()

    scenario += contract
    scenario += contract.certify(address=bob.address, name=bob.seed).run(sender=alice)
    scenario += contract.certify(address=jill.address, name=jill.seed).run(sender=alice)


certifier = sp.record(
    address=sp.address("tz1VSUr8wwNhLAzempoch5d6hLRiTh8Cjcjb")
)
sp.add_compilation_target("certification_compiled", Certification(certifier=certifier))
