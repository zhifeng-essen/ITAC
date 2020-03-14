# import os
# import django
# os.environ.setdefault('DJANGO_SETTING_MODULE', 'tcmr.settings')
# django.setup()

# exec(open('dump/test.py').read())


from rambler.models import Prescription

Pid = 1

# with open('dump/data/TCMID/prescription-TCMID.v2.01.txt') as f:
with open('dump/data/TCMID/prescription_sample.txt') as f:
    f.readline()
    for line in f:
        ls = line.strip().split('\t')
        Prescription_id = Pid
        ID = 'PN' + '0' * (7 - len(str(Pid))) + str(Pid)
        Pinyin_name = ls[0]
        Chinese_name = ls[1]
        Composition = ls[2]
        Pinyin_composition = ls[3]
        Indication = ls[4]
        Use_method = ls[5]
        References = ls[6]
        # print(Pinyin_name)
        # break
        # herbs =

        prescription = Prescription(
            Prescription_id=Prescription_id,
            ID=ID,
            Pinyin_name=Pinyin_name,
            Chinese_name=Chinese_name,
            Composition=Composition,
            Pinyin_composition=Pinyin_composition,
            Indication=Indication,
            Use_method=Use_method,
            References=References,
            # herbs =
        )

        prescription.save()

        Pid += 1
