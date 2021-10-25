import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(storage = sp.TString).layout("storage"))
    self.init(storage = 'start')

  @sp.entry_point
  def repeat(self, params):
    self.data.storage = params

sp.add_compilation_target("test", Contract())