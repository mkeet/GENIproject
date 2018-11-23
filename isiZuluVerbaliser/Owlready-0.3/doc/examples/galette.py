
from owlready import *

onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/crepes_et_galettes.owl")
onto.load()

ma_galette = onto.Galette()

ma_galette.a_pour_garniture = [ onto.Tomate(),
                                onto.Viande() ]



class GaletteNonVégétarienne(onto.Galette):
  equivalent_to = [
    onto.Galette
  & ( onto.a_pour_garniture(SOME, onto.Viande)
    | onto.a_pour_garniture(SOME, onto.Poisson)
    ) ]
  def manger(self): print("Beurk, je suis végétarien !")



onto.sync_reasoner()

print(ma_galette.__class__)

ma_galette.manger()
