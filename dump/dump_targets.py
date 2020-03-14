import pandas as pd
from rambler.models import Target

df = pd.read_excel('dump/data/SymMap/SymMap v1.0, SMTT file.xlsx')

for i in df.index.values:
    target = Target(
        Target_id=df.ix[i, 'Gene_id'],
        ID='TT' + '0' * (7 - len(str(df.ix[i, 'Gene_id']))) + str(df.ix[i, 'Gene_id']),
        Gene_symbol=df.ix[i, 'Gene_symbol'],
        Chromosome=str(df.ix[i, 'Chromosome']).rstrip('.0'),
        Gene_name=df.ix[i, 'Gene_name'],
        Protein_name=df.ix[i, 'Protein_name'],
        # Alias=df.ix[i, 'Alias'],
        HIT_id=str(df.ix[i, 'HIT_id']),
        TCMSP_id=str(df.ix[i, 'TCMSP_id']),
        Ensembl_id=str(df.ix[i, 'Ensembl_id']),
        NCBI_id=str(df.ix[i, 'NCBI_id']).rstrip('.0'),
        HGNC_id=str(df.ix[i, 'HGNC_id']).rstrip('.0'),
        Vega_id=str(df.ix[i, 'Vega_id']),
        GenBank_Gene_id=str(df.ix[i, 'GenBank_Gene_id']),
        GenBank_Protein_id=str(df.ix[i, 'GenBank_Protein_id']).rstrip('.0'),
        Uniprot_id=str(df.ix[i, 'UniProt_id']),
        PDB_id=str(df.ix[i, 'PDB_id']),
        OMIM_id=str(df.ix[i, 'OMIM_id']).rstrip('.0'),
        miRBase_id=str(df.ix[i, 'miRBase_id']).rstrip('.0'),
        IMGT_GENE_DB_id=str(df.ix[i, 'IMGT/GENE-DB_id']).rstrip('.0'),
        # diseases=
    )
    target.save()
