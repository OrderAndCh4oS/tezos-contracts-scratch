import smartpy as sp

tstorage = sp.TRecord(certified = sp.TBigMap(sp.TAddress, sp.TString), certifier = sp.TAddress).layout(("certified", "certifier"))
tparameter = sp.TVariant(certify = sp.TRecord(address = sp.TAddress, name = sp.TString).layout(("address", "name"))).layout("certify")
tglobals = { }
tviews = { }
