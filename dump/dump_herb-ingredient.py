import re
from rambler.models import Herb, Ingredient


datadir = '../data/SymMap/SMHB-data/'

for i in range(1, 500):
    with open(datadir+'SMHB-'+str(i)+'.js', 'r') as f:
        fl = f.readlines()[0]
        mols = re.findall('{"classes": "Mol", "data": {"id": "(.*?)",.*?}', fl)
        # print(len(mols))
        # print(mols[0])
        herb = Herb.objects.get(Herb_id=i)
        for mol in mols:
            ingredient = Ingredient.objects.get(Ingredient_id=int(mol.lstrip('SMIT')))
            herb.ingredients.add(ingredient)



