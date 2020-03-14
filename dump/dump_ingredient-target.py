import re
from rambler.models import Ingredient, Target


datadir = '../data/SymMap/SMIT-data/'

for i in range(1, 19596):
    print(i)
    with open(datadir+'SMIT-'+str(i)+'.js', 'r') as f:
        fl = f.readlines()[0]
        target_ids = re.findall('{"classes": "Gene", "data": {"id": "(.*?)",.*?}', fl)
        if len(target_ids) > 0:
            ingredient = Ingredient.objects.get(Ingredient_id=i)
            for target_id in target_ids:
                target = Target.objects.get(Target_id=int(target_id.lstrip('SMTT')))
                ingredient.targets.add(target)

