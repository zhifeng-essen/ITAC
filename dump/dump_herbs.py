import pandas as pd
import math
from rambler.models import Herb

df = pd.read_excel('dump/data/SymMap/SymMap v1.0, SMHB file.xlsx')

# print(df.index)
# print(type(df.ix[1, 'Herb_id']))
# print(df.ix[0, 'UsePart'])
for i in df.index.values:
    # print(type(df.ix[i, 'Chinese_name']))
    herb = Herb(
        Herb_id=df.ix[i, 'Herb_id'],
        ID='HB'+'0'*(7-len(str(df.ix[i, 'Herb_id'])))+str(df.ix[i, 'Herb_id']),
        Chinese_name=df.ix[i, 'Chinese_name'],
        Pinyin_name=df.ix[i, 'Pinyin_name'],
        Latin_name=df.ix[i, 'Latin_name'],
        English_name=df.ix[i, 'English_name'],
        Properties=df.ix[i, 'Properties'],
        Meridians=df.ix[i, 'Meridians'],
        Function=df.ix[i, 'Function'],
        Class_Chinese=df.ix[i, 'Class_Chinese'],
        Class_English=df.ix[i, 'Class_English'],
        UsePart=df.ix[i, 'UsePart'],
        TCMID_id=str(df.ix[i, 'TCMID_id']).rstrip('.0'),
        TCM_ID_id=str(df.ix[i, 'TCM-ID_id']).rstrip('.0'),
        TCMSP_id=str(df.ix[i, 'TCMSP_id']).rstrip('.0'),
        # ingredients=
    )
    herb.save()


