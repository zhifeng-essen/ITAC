import pandas as pd
from rambler.models import Disease

df = pd.read_excel('dump/data/SymMap/SymMap v1.0, SMDE file.xlsx')

for i in df.index.values:
    disease = Disease(
        Disease_id=df.ix[i, 'Disease_id'],
        ID='DE' + '0' * (7 - len(str(df.ix[i, 'Disease_id']))) + str(df.ix[i, 'Disease_id']),
        Disease_name=df.ix[i, 'Disease_Name'],
        Disease_definition=df.ix[i, 'Disease_definition'],
        # Alias=df.ix[i, 'Alias'],
        MeSH_id=str(df.ix[i, 'MeSH_id']),
        OMIM_id=str(df.ix[i, 'OMIM_id']).rstrip('.0'),
        Orphanet_id=str(df.ix[i, 'Orphanet_id']).rstrip('.0'),
        ICD10CM_id=str(df.ix[i, 'ICD10CM_id']),
        UMLS_id=str(df.ix[i, 'UMLS_id']),
        MedDRA_id=str(df.ix[i, 'MedDRA_id']).rstrip('.0'),
    )
    disease.save()
