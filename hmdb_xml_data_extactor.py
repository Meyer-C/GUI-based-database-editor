import requests
from bs4 import BeautifulSoup

class hmdbData:
    def __init__(self, path, accession, name, synonyms, formula, avg_mol_weight, monoisotopic_mass, iupac_name, cas,
                 smiles, inchi, inchikey, ):
        self.path = path
        self.accession = accession
        self.name = name
        self.synonyms = synonyms
        self.formula = formula
        self.avg_mol_weight = avg_mol_weight
        self.monoisotopic_mass = monoisotopic_mass
        self.iupac_name = iupac_name
        self.cas = cas
        self.smiles = smiles
        self.inchi = inchi
        self.inchikey = inchikey

def find_xml(HMDB_accession_num):
    if 'HMDB' in HMDB_accession_num:
        accession_num = HMDB_accession_num.replace('HMDB', '')

    else:
        accession_num = HMDB_accession_num

    try:

        hmdb_file = str(fr'https://hmdb.ca/metabolites/HMDB{accession_num}.xml')
        document = requests.get(hmdb_file)
        soup = BeautifulSoup(document.content, 'lxml-xml')

        # find relevant data
        accession_nums = [accession.string for accession in soup.find_all('accession')]
        name = soup.find('name').string
        synonyms = [synonym.string for synonym in soup.find_all('synonym')]
        formula = soup.find('chemical_formula').string
        avg_mol_weight = float(soup.find('average_molecular_weight').string)
        monoisotopic_mass = float(soup.find('monisotopic_molecular_weight').string)
        iupac_name = soup.find('iupac_name').string
        cas = soup.find('cas_registry_number').string
        smiles = soup.find('smiles').string
        inchi = soup.find('inchi').string
        inchikey = soup.find('inchikey').string

    # create a new chemical object
        return hmdbData(path=hmdb_file, accession=accession_nums, name=name, synonyms=synonyms, formula=formula,
                        avg_mol_weight=avg_mol_weight, monoisotopic_mass=monoisotopic_mass, iupac_name=iupac_name,
                        cas=cas, smiles=smiles, inchi=inchi, inchikey=inchikey)
    except:
        return 'Invalid Accession'







