import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(certified = sp.TMap(sp.TAddress, sp.TString), certifier = sp.TAddress).layout(("certified", "certifier")))
    self.init(certified = {},
              certifier = sp.address('tz1Ytv9pMTm6sg7qyuJ1uzWaoYujKUVdYCwQ'))

  @sp.entry_point
  def certify(self, params):
    sp.verify(sp.sender == self.data.certifier)
    self.data.certified[params.address] = params.name

sp.add_compilation_target("test", Contract())