import re
from rambler.models import Target, Disease


datadir = '../data/SymMap/SMTT-data/'

for i in range(1, 4303):
    print(i)
    with open(datadir+'SMTT-'+str(i)+'.js', 'r') as f:
        fl = f.readlines()[0]
        disease_ids = re.findall('{"classes": "Disease", "data": {"id": "(.*?)",.*?}', fl)
        if len(disease_ids) > 0:
            target = Target.objects.get(Target_id=i)
            for disease_id in disease_ids:
                disease = Disease.objects.get(Disease_id=int(disease_id.lstrip('SMDE')))
                target.diseases.add(disease)

