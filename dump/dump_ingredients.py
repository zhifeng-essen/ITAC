import pandas as pd
from rambler.models import Ingredient

df = pd.read_excel('dump/data/SymMap/SymMap v1.0, SMIT file.xlsx')

for i in df.index.values:
    ingredient = Ingredient(
        Ingredient_id=df.ix[i, 'MOL_id'],
        ID='IT' + '0' * (7 - len(str(df.ix[i, 'MOL_id']))) + str(df.ix[i, 'MOL_id']),
        Molecule_name=df.ix[i, 'Molecule_name'],
        Molecule_formula=df.ix[i, 'Molecule_formula'],
        Molecule_weight=str(df.ix[i, 'Molecule_weight']),
        OB_score=str(df.ix[i, 'OB_score']),
        Alias=df.ix[i, 'Alias'],
        PubChem_id=str(df.ix[i, 'PubChem_id']).rstrip('.0'),
        CAS_id=str(df.ix[i, 'CAS_id']),
        TCMID_id=str(df.ix[i, 'TCMID_id']),
        TCM_ID_id=str(df.ix[i, 'TCM-ID_id']),
        TCMSP_id=str(df.ix[i, 'TCMSP_id']),
        # targets =
    )
    ingredient.save()
