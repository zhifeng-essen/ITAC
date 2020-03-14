from django.db import models
from django.core import serializers


# Create your models here.
class Disease(models.Model):
    """
    Disease_id: the primary ID of each disease recorded in SymMap.
    Disease_name: the name of each disease.
    Disease_definition: the definition for some diseases.
    Alias: multiple aliases separated by a ‘|’ for each disease collected from diverse resources.
    MeSH_id: the cross reference of each disease in the MeSH database.
    OMIM_id: the cross reference of each disease in the OMIM database.
    Orphanet_id: the cross reference of each disease in the Orphanet database.
    ICD10CM_id: the cross reference of each disease in the ICD (tenth clinical modification) database.
    UMLS_id: the cross reference of each disease in the UMLS database.
    MedDRA_id: the cross reference of each disease in the MedDRA database.
    """
    Disease_id = models.IntegerField(primary_key=True)
    ID = models.CharField(max_length=100, null=True, blank=True)
    Disease_name = models.CharField(max_length=500, null=True, blank=True)
    Disease_definition = models.TextField(max_length=200, null=True, blank=True)
    Alias = models.CharField(max_length=200, null=True, blank=True)
    MeSH_id = models.CharField(max_length=200, null=True, blank=True)
    OMIM_id = models.CharField(max_length=200, null=True, blank=True)
    Orphanet_id = models.CharField(max_length=200, null=True, blank=True)
    ICD10CM_id = models.CharField(max_length=200, null=True, blank=True)
    UMLS_id = models.CharField(max_length=200, null=True, blank=True)
    MedDRA_id = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('-Disease_id',)

    def __str__(self):
        return self.Disease_name

    @staticmethod
    def getPatialData(id):
        return list(
            Disease.objects.filter(
                Disease_id=id
            ).values(
                'ID',
                'Disease_name',
                # 'Disease_definition',
                # 'Alias',
                # 'MeSH_id',
                'OMIM_id',
                'Orphanet_id',
                # 'ICD10CM_id',
                # 'UMLS_id',
                # 'MedDRA_id'
            ))

    @staticmethod
    def getColumns():
        return [
            {"field": "ID", "formatter": "", "title": "Disease id"},
            {"field": "Disease_name", "title": "Disease name"},
            {"field": "OMIM_id", "title": "OMIM id"},
            {"field": "Orphanet_id", "title": "Orphanet id"}
        ]


class Target(models.Model):
    """
    Target_id：the primary ID of each target recorded in SymMap.
    Gene_symbol: the gene symbol of each target.
    Chromosome: the chromosome number in which each target located.
    Gene_name: the gene name of each target.
    Protein_name: the protein name of each target.
    Alias: multiple aliases separated by a ‘|’ for each target collected from diverse resources.
    HIT_id: the cross reference of each target in the HIT database.
    TCMSP_id: the cross reference of each target in the TCMSP database.
    Ensembl_id: the cross reference of each target in the Ensembl database.
    NCBI_id: the cross reference of each target in the NCBI database.
    HGNC_id: the cross reference of each target in the HGNC database.
    Vega_id: the cross reference of each target in the Vega database.
    GenBank_Gene_id: the cross reference of each target in the GenBank_Gene database.
    GenBank_Protein_id: the cross reference of each target in the GenBank_Protein database.
    Uniprot_id: the cross reference of each target in the Uniprot database.
    PDB_id: the cross reference of each target in the PDB database.
    OMIM_id: the cross reference of each target in the OMIM database.
    miRBase_id: the cross reference of each target in the miRBase database.
    IMGT/GENE-DB_id: the cross reference of each target in the IMGT/GENE-DB database.
    """
    Target_id = models.IntegerField(primary_key=True)
    ID = models.CharField(max_length=100, null=True, blank=True)
    Gene_symbol = models.CharField(max_length=200, null=True, blank=True)
    Chromosome = models.CharField(max_length=200, null=True, blank=True)
    Gene_name = models.CharField(max_length=500, null=True, blank=True)
    Protein_name = models.CharField(max_length=500, null=True, blank=True)
    Alias = models.TextField(null=True, blank=True)
    HIT_id = models.CharField(max_length=200, null=True, blank=True)
    TCMSP_id = models.CharField(max_length=200, null=True, blank=True)
    Ensembl_id = models.CharField(max_length=200, null=True, blank=True)
    NCBI_id = models.CharField(max_length=200, null=True, blank=True)
    HGNC_id = models.CharField(max_length=200, null=True, blank=True)
    Vega_id = models.CharField(max_length=200, null=True, blank=True)
    GenBank_Gene_id = models.CharField(max_length=200, null=True, blank=True)
    GenBank_Protein_id = models.CharField(max_length=200, null=True, blank=True)
    Uniprot_id = models.CharField(max_length=200, null=True, blank=True)
    PDB_id = models.CharField(max_length=200, null=True, blank=True)
    OMIM_id = models.CharField(max_length=200, null=True, blank=True)
    miRBase_id = models.CharField(max_length=200, null=True, blank=True)
    IMGT_GENE_DB_id = models.CharField(max_length=200, null=True, blank=True)
    diseases = models.ManyToManyField(Disease)

    class Meta:
        ordering = ('-Target_id',)

    def __str__(self):
        return self.Gene_symbol

    @staticmethod
    def getPatialData(id):
        return list(
            Target.objects.filter(
                Target_id=id
            ).values(
                'ID',
                'Gene_symbol',
                'Chromosome',
                'Gene_name',
                'Protein_name',
                # 'Alias',
                # 'HIT_id',
                # 'TCMSP_id',
                'Ensembl_id',
                # 'NCBI_id',
                # 'HGNC_id',
                # 'Vega_id',
                # 'GenBank_Gene_id',
                # 'GenBank_Protein_id',
                'Uniprot_id',
                # 'PDB_id',
                # 'OMIM_id',
                # 'miRBase_id',
                # 'IMGT_GENE_DB_id',
                # 'diseases'
            ))

    @staticmethod
    def getColumns():
        return [
            {"field": "ID", "formatter": "", "title": "Target id"},
            {"field": "Gene_symbol", "title": "Gene symbol"},
            {"field": "Chromosome", "title": "Chromosome"},
            {"field": "Gene_name", "title": "Gene name"},
            {"field": "Protein_name", "title": "Protein name"},
            {"field": "Ensembl_id", "title": "Ensembl id"},
            {"field": "Uniprot_id", "title": "UniProt id"}
        ]


class Ingredient(models.Model):
    """
    Ingredient_id：the primary ID of each ingredient recorded in SymMap.
    Molecule_name：the common name of each ingredient. Generally, we selected the first name appeared in the PubChem database.
    Molecule_formula: the molecule formula for each ingredient.
    Molecule_weight: the molecule weight for each ingredient.
    OB_score：the oral bioavailability score for each ingredient.
    Alias: multiple aliases separated by a ‘|’ for each ingredient collected from diverse resources.
    PubChem_id: the cross reference of each ingredient in the PubChem database.
    CAS_id: the cross reference of each ingredient in the CAS database.
    TCMID_id: the cross reference of each ingredient in the TCMID database.
    TCM-ID_id: the cross reference of each ingredient in the TCM-ID database.
    TCMSP_id: the cross reference of each ingredient in the TCMSP database.
    """
    Ingredient_id = models.IntegerField(primary_key=True)
    ID = models.CharField(max_length=100, null=True, blank=True)
    Molecule_name = models.CharField(max_length=500, null=True, blank=True)
    Molecule_formula = models.CharField(max_length=200, null=True, blank=True)
    Molecule_weight = models.CharField(max_length=200, null=True, blank=True)
    OB_score = models.CharField(max_length=200, null=True, blank=True)
    Alias = models.TextField(null=True, blank=True)
    PubChem_id = models.CharField(max_length=200, null=True, blank=True)
    CAS_id = models.CharField(max_length=200, null=True, blank=True)
    TCMID_id = models.CharField(max_length=200, null=True, blank=True)
    TCM_ID_id = models.CharField(max_length=200, null=True, blank=True)
    TCMSP_id = models.CharField(max_length=200, null=True, blank=True)
    targets = models.ManyToManyField(Target)

    class Meta:
        ordering = ('-Ingredient_id',)

    def __str__(self):
        return self.Molecule_name

    @staticmethod
    def getPatialData(id):
        return list(
            Ingredient.objects.filter(
                Ingredient_id=id
            ).values(
                'ID',
                'Molecule_name',
                'Molecule_formula',
                'Molecule_weight',
                'OB_score',
                # 'Alias',
                'PubChem_id',
                'CAS_id',
                # 'TCMID_id',
                # 'TCM_ID_id',
                # 'TCMSP_id',
                # 'targets'
            ))

    @staticmethod
    def getColumns():
        return [
            {"field": "ID", "formatter": "", "sortable": True, "title": "Ingredient id"},
            {"field": "Molecule_name", "title": "Molecule name"},
            {"field": "Molecule_formula", "title": "Molecule formula"},
            {"field": "Molecule_weight", "title": "Molecule weight"},
            {"field": "OB_score", "title": "OB score"},
            {"field": "PubChem_id", "title": "PubChem id"},
            {"field": "CAS_id", "title": "CAS id"}
        ]


class Herb(models.Model):
    """
    Herb_id：the primary ID of each herb recorded in SymMap.
    Chinese_name：the herb name in Chinese.
    Pinyin_name：the herb name in Pinyin.
    Latin_name：the Latin name for the species of the herbs.
    English_name: the herb name in English.
    Properties: the property description of the herb using the terms from traditional Chinese medicine.
    Meridians: the meridian description of the herb using the terms from traditional Chinese medicine.
    Function: the function description of the herb using the terms from traditional Chinese medicine.
    Class_Chinese: the classification of the herb in Chinese using the terms from TCM.
    Class_English: the classification of the herb in English using the terms from TCM.
    UsePart: the part of the herb plants to be used in medicine.
    TCMID_id: the cross reference of each herb in the TCMID database.
    TCM-ID_id: the cross reference of each herb in the TCM-ID database.
    TCMSP_id: the cross reference of each herb in the TCMSP database.
    """
    Herb_id = models.IntegerField(primary_key=True)
    ID = models.CharField(max_length=100, null=True, blank=True)
    Chinese_name = models.CharField(max_length=200, null=True, blank=True)
    Pinyin_name = models.CharField(max_length=200, null=True, blank=True)
    Latin_name = models.CharField(max_length=200, null=True, blank=True)
    English_name = models.CharField(max_length=200, null=True, blank=True)
    Properties = models.CharField(max_length=200, null=True, blank=True)
    Meridians = models.CharField(max_length=200, null=True, blank=True)
    Function = models.TextField(null=True, blank=True)
    Class_Chinese = models.CharField(max_length=200, null=True, blank=True)
    Class_English = models.CharField(max_length=200, null=True, blank=True)
    UsePart = models.CharField(max_length=200, null=True, blank=True)
    TCMID_id = models.CharField(max_length=200, null=True, blank=True)
    TCM_ID_id = models.CharField(max_length=200, null=True, blank=True)
    TCMSP_id = models.CharField(max_length=200, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)

    class Meta:
        ordering = ('-Herb_id',)

    def __str__(self):
        return self.Chinese_name

    @staticmethod
    def getPatialData(id):
        # return serializers.serialize("json", Herb.objects.filter(Herb_id__lt=id))
        return list(
            Herb.objects.filter(
                Herb_id=id
            ).values(
                'ID',
                'Chinese_name',
                'Pinyin_name',
                'Latin_name',
                'English_name',
                # 'Properties',
                # 'Meridians',
                # 'Function',
                'Class_Chinese',
                'Class_English',
                # 'UsePart',
                # 'TCMID_id',
                # 'TCM_ID_id',
                # 'TCMSP_id',
                # 'ingredients'
            ))

    @staticmethod
    def getColumns():
        return [
            {"field": "ID", "formatter": "", "title": "Herb id"},
            {"field": "Chinese_name", "title": "Chinese name"},
            {"field": "Pinyin_name", "title": "Pinyin name"},
            {"field": "Latin_name", "title": "Latin name"},
            {"field": "English_name", "title": "English name"},
            {"field": "Class_Chinese", "title": "Class in Chinese"},
            {"field": "Class_English", "title": "Class in English"}
        ]


class Prescription(models.Model):
    """
    Prescription_id: the primary ID of each prescription recorded in TCMID.
    Pinyin_name:
    Chinese_name:
    Composition:
    Pinyin_composition:
    Indication:
    Use_method:
    References:
    """
    Prescription_id = models.IntegerField(primary_key=True)
    ID = models.CharField(max_length=100, null=True, blank=True)
    Pinyin_name = models.CharField(max_length=200, null=True, blank=True)
    Chinese_name = models.CharField(max_length=200, null=True, blank=True)
    Composition = models.CharField(max_length=200, null=True, blank=True)
    Pinyin_composition = models.CharField(max_length=200, null=True, blank=True)
    Indication = models.CharField(max_length=200, null=True, blank=True)
    Use_method = models.TextField(null=True, blank=True)
    References = models.TextField(null=True, blank=True)
    herbs = models.ManyToManyField(Herb)

    class Meta:
        ordering = ('-Prescription_id',)

    def __str__(self):
        return self.Chinese_name

    @staticmethod
    def getPatialData(id):
        return list(
            Prescription.objects.filter(
                Prescription_id=id
            ).values(
                'ID',
                'Pinyin_name',
                'Chinese_name',
                # 'Composition',
                # 'Pinyin_composition',
                # 'Indication',
                # 'Use_method',
                # 'References',
                # 'herbs'
            ))

    @staticmethod
    def getColumns():
        return [
            {"field": "ID", "formatter": "", "title": "Prescription id"},
            {"field": "Pinyin_name", "title": "Pinyin name"},
            {"field": "Chinese_name", "title": "Chinese name"}
        ]
