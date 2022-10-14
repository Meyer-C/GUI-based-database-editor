import pubchempy as pc

def search_pubchem():

    search_type = pubchem_search_starter()
    search_term = input('Search: ')
    results = pc.get_compounds(search_term, search_type)

    return results

def search_pubchem_input(search_term, search_type):
    if search_type != 'cid':
        return pc.get_compounds(search_term, search_type)
    else:
        return pc.Compound.from_cid(search_term)


def pubchem_search_starter():
    search_type = ''
    inpt = ''

    while inpt != 'q':

        inpt = input('What kind of PubChem search would you like to do?\nFor pubchem search types type "t": ')

        if inpt == 'n':
            search_type = 'name'
            break

        elif inpt == 'sm':
            search_type = 'smiles'
            break

        elif inpt == 'inc':
            search_type = 'inchi'
            break

        elif inpt == 'inck':
            search_type = 'inchikey'
            break

        elif inpt == 'f':
            search_type = 'formula'
            break

        # these final 2 stay in the while loop until there is a search type entered or the search is terminated
        elif inpt == 't':
            print('For name searches type "n"\nFor smile searches type "sm"\nFor InChi searches type "inc"\nFor InChiKey searches type "inck\nFor formula searches type "f"\n')

        else:
            print('Unrecognized command')

    return search_type


