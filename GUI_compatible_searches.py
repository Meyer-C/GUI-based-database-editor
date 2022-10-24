from Compound_From_XLS import get_compounds as gc

def GUI_quick_search(search_type, search_term, filepath, advanced_search_terms, return_type):
    compound_list = gc(filepath)

    potential_compounds = []
    # making flags to return only specific data
    # talk to Correy if this is a good feature to add

    # naming search type
    # add synonyms in this one as well
    if search_type == 'Name':
        for x in range(1, len(compound_list)):
            compound = compound_list[x]
            name = compound[1]
            if name is not None:
                if search_term.lower() in name.lower():
                    potential_compounds.append([compound_list[0], compound])

    # mass search type
    elif search_type == 'Mass':

        if '-' in search_term:
            low_bound = float(search_term[0:search_term.index('-')])
            high_bound = float(search_term[search_term.index('-') + 1::])
            for x in range(1, len(compound_list)):
                compound = compound_list[x]
                if 'NA' != compound[15] and compound[15] is not None:
                    mass = float(compound[15])
                    if low_bound <= mass <= high_bound:
                        potential_compounds.append([compound_list[0], compound])

        else:
            target_mass = float(search_term)
            for x in range(1, len(compound_list)):
                compound = compound_list[x]
                if 'NA' != compound[15] and compound[15] is not None:
                    mass = float(compound[15])
                    if mass == target_mass:
                        potential_compounds.append([compound_list[0], compound])




    elif search_type == 'InChiKey':
        for x in range(1, len(compound_list)):
            compound = compound_list[x]
            inchikey = compound[25]
            if inchikey != None:
                if search_term.lower() in inchikey.lower():
                    potential_compounds.append([compound_list[0], compound])

    if advanced_search_terms is None:
        if return_type == 'str':
            return search_return(potential_compounds)
        else:
            return potential_compounds
    else:
        if return_type == 'str':
            return advanced_search_return(potential_compounds, advanced_search_terms)
        else:
            return potential_compounds




def search_return(potential_compounds):
    output = []
    for compound in potential_compounds:
        this_compound_str = ''
        naming = compound[0]
        compound_info = compound[1]
        for x in range(len(naming)):
            if naming[x] is not None:
                this_compound_str += f'{str(naming[x]):40} {str(compound_info[x])}\n'
        this_compound_str += '\n-------------------------------------------------------------------\n\n'
        output.append(this_compound_str)

    else:
        output.append(0)

    return output



def advanced_search_return(potential_compounds, advanced_search_terms):
    output = []

    if len(potential_compounds) >= 1:
        for compound in potential_compounds:
            this_compound_str = ''
            naming = compound[0]
            compound_info = compound[1]
            for x in range(len(naming)):
                for y in range(len(advanced_search_terms)):
                    a = advanced_search_terms[y]
                    if x == a:
                        if naming[x] is not None:
                            this_compound_str += f'{str(naming[x]):40} {str(compound_info[x])}\n'
            this_compound_str += '\n-------------------------------------------------------------------\n\n'
            output.append(this_compound_str)

    else:
        output.append(0)

    return output

