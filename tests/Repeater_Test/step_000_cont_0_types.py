import smartpy as sp

tstorage = sp.TRecord(storage = sp.TString).layout("storage")
tparameter = sp.TVariant(repeat = sp.TString).layout("repeat")
tglobals = { }
tviews = { }
