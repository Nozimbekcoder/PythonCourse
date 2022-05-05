"""
Muallif: Nozimjon Bozorov
Sana: 31.03.2022
Mavzu: Modullar
"""

from pprint import pprint as chiqar

def avto(kompaniya, model, rangi, yili, narh=None):
    """Avtomobillar haqida ma'lumotlar"""
    avtomobil = {
        'kompaniya': kompaniya,
        'model': model,
        'rangi': rangi,
        'yili': yili,
        'narhi': narh
    }
    return avtomobil

# chiqar(avto('gm','nexia','qora',2012,2000))
# chiqar(avto('gm','nexia','qora',2012,1500))
# chiqar(avto('gm','nexia','qora',2012))


a=100


def salom(ism):
 print("Salom "+ism)
def xayr(ism):
 print("Xayr "+ism)
