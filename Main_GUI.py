import dearpygui.dearpygui as dpg
from GUI_compatible_searches import *
from Compound_From_XLS import get_compounds as gc
from openpyxl import load_workbook
from PubChem_Search import search_pubchem_input as spc

dpg.create_context()
dpg.create_viewport(title='PMF Chemical Database', width=800, height=600)

class windowCount:
    manual_count = 0
    search_count = 0
    pubchem_count = 0
    search_popup_count = 0
    pubchem_popup = 0
    invalid_filepath_popup_count = 0
    output_tab_count = 0

class namingCount:
    count = 1

class NewChemical:
    info = []

def get_filepath():
    return dpg.get_value('file')
#    with open('filepath.txt') as a:
#        content = a.readlines()
#        return content[0]

# set up filepath page for this
#def change_filepath(new_path):
#    with open('filepath.txt', 'r+') as a:
#        a.truncate(0)
#        a.write(new_path)


# ---------------------------------------------------------------------------------------------------------------------
# All fxns and classes of search tabs
def search_starter():
    windowCount.output_tab_count += 1
    output_tab_tag = str(f'Outputs {windowCount.output_tab_count}')
    with dpg.tab(label='Outputs', parent='tabs', tag=output_tab_tag):
        search_type = dpg.get_value(f'type_{windowCount.search_count}')
        search_term = dpg.get_value(f'term_{windowCount.search_count}')
        dpg.add_text(GUI_quick_search(search_type, search_term, get_filepath(), None), parent=output_tab_tag)
        dpg.add_button(label='Close', parent=output_tab_tag, callback=close, user_data=output_tab_tag)

def advanced_search_starter(sender, app_data, user_data):
    advanced_return_nums = []
    for x in range(len(user_data)):
        if dpg.get_value(user_data[x]) == True:
            advanced_return_nums.append(x)
    windowCount.output_tab_count += 1
    output_tab_tag = str(f'Outputs {windowCount.output_tab_count}')
    with dpg.tab(label='Outputs', tag=output_tab_tag, parent='tabs'):
        search_type = dpg.get_value(f'type_{windowCount.search_count}')
        search_term = dpg.get_value(f'term_{windowCount.search_count}')
        dpg.add_text(GUI_quick_search(search_type, search_term, get_filepath(), advanced_return_nums), parent=output_tab_tag)
        dpg.add_button(label='Close', parent=output_tab_tag, callback=close, user_data=output_tab_tag)
        close(sender, app_data, str(f'Advanced Search {windowCount.search_popup_count}'))

class searchWindow():

    def search_window(self):
        if gc(get_filepath()) == 'Invalid filepath':
            invalid_filepath_popup()
        else:
            search_types = ['Name', 'Mass', 'InChiKey']
            windowCount.search_count += 1
            tab_tag = str(f'Search {windowCount.search_count}')
            with dpg.tab(label=tab_tag, tag=tab_tag, parent='tabs'):
                search_type_call = str(f'type_{windowCount.search_count}')
                search_term_call = str(f'term_{windowCount.search_count}')
                dpg.add_radio_button(tag=search_type_call, items=search_types, horizontal=True,
                                     default_value=search_types[0], parent=tab_tag)
                dpg.add_input_text(tag=search_term_call, label='Search Here', parent=tab_tag)
                dpg.add_button(label='Advanced Search Options', callback=searchWindowPopup.search_window_popup)
                dpg.add_button(label='Search!', callback=search_starter, parent=tab_tag)

class searchWindowPopup():

    def search_window_popup(self):
        windowCount.search_popup_count += 1
        window_name = str(f'Advanced Search {windowCount.search_popup_count}')
        with dpg.window(tag=window_name, width=400, height=300):
            compound_list = gc(get_filepath())
            names = compound_list[0]
            name_tags = []
            for x in range(len(names)):
                name = names[x]
                if name is not None:
                    name_tag = str(f'{x}. {names[x]} {windowCount.search_popup_count}')
                    name_tags.append(name_tag)
                    dpg.add_checkbox(label=name, tag=name_tag, parent=window_name)
            dpg.add_button(label='Advanced Search!', callback=advanced_search_starter, user_data=name_tags, parent=window_name)

# --------------------------------------------------------------------------------------------------------------------
# all classes and fxns of manual chemical addition

def update_input_text(sender, value, user_data):
        compound_list = gc(get_filepath())
        if compound_list != 'Invalid filepath':
            names = compound_list[0]
            if sender == 'f':
                namingCount.count += 1
                if names[namingCount.count] is not None:
                    dpg.set_value(user_data, names[namingCount.count])
                else:
                    dpg.add_button(label='Add Chemical!', parent='manual_add')
            elif sender == 'sv':
                print(dpg.get_value(namingCount.count))
            else:
                namingCount.count -= 1
                dpg.set_value(user_data, names[namingCount.count])

        else:
            dpg.set_value(user_data, 'Invalid Filepath')

class manualTabAdd:

    def manual_window(self):
        if gc(get_filepath()) == 'Invalid filepath':
            invalid_filepath_popup()
        else:
            filepath = get_filepath()
            windowCount.manual_count += 1
            tab_tag = str(f'Manual Chemical Add {str(windowCount.manual_count)}')
            with dpg.tab(tag=tab_tag, label=tab_tag, parent='tabs'):
                compounds = gc(filepath)
                if compounds == 'Invalid Filepath':
                    dpg.add_text('Invalid Filepath')
                else:
                    names = compounds[0]
                    name_tags = []
                    for x in range(1,len(names)):
                        if names[x] is not None:
                            name_tag = f'{windowCount.manual_count}-{x}. {names[x]}'
                            name_tags.append(name_tag)
                            dpg.add_text(name_tag, parent=tab_tag)
                            dpg.add_input_text(tag=name_tag, parent=tab_tag)
                    dpg.add_button(label='Add Chemical!', tag=f'{windowCount.manual_count}_add_chemical',
                                   callback=add_to_database, user_data=name_tags, parent=tab_tag)

def add_to_database(sender, app_data, user_data):
    wb = load_workbook(get_filepath())
    sheet = wb.active
    max_row = sheet.max_row
    prev_accession = sheet.cell(max_row, 1).value
    zeros = 6 - len(str(int(prev_accession[5::]) + 1))
    sheet.cell(max_row + 1, 1).value = str(prev_accession[0:5]) + str('0' * zeros) + str(int(prev_accession[5::]) + 1)

    for x in range(len(user_data)):
        sheet.cell(max_row + 1, x + 2).value = dpg.get_value(user_data[x])
    wb.save(get_filepath())

# ---------------------------------------------------------------------------------------------------------------------
# All classes and fxns of PubChem addition

class pubChemAdd:

    def pubchem_window(self):
        if gc(get_filepath()) == 'Invalid filepath':
            invalid_filepath_popup()
        else:
            windowCount.pubchem_count += 1
            tab_tag = str(f'PubChem Add {windowCount.pubchem_count}')
            search_types = ['Name', 'CID', 'Smiles', 'InChiKey', 'InChi', 'Formula']
            search_type_call = str(f'PubChem_type_{windowCount.pubchem_count}')
            with dpg.tab(tag=tab_tag, label=tab_tag, parent='tabs'):
                dpg.add_radio_button(tag=search_type_call, items=search_types, horizontal=True,
                                     default_value=search_types[0], parent=tab_tag)
                this_search = str(f'{tab_tag} Search')
                dpg.add_input_text(tag=this_search, parent=tab_tag)
                dpg.add_button(tag=str(f'{this_search}_button'),label='Search!', callback=search_pubchem,
                               user_data=[search_type_call, this_search])

# ASK WHAT KIND OF DATA SHOULD BE RETURNED FROM PUBCHEM?
def search_pubchem(sender, app_data, user_data):
    search_term = dpg.get_value(user_data[1])
    search_type = dpg.get_value(user_data[0]).lower()
    pubchem_popup(spc(search_term, search_type), search_term)


# Maybe do this as a popup to select the compound, then open a tab like the manual add
def pubchem_popup(compounds, search_term):
    windowCount.pubchem_popup += 1
    tab_tag = str(f'{windowCount.pubchem_popup}. Pubchem Search Results: {search_term}')
    with dpg.window(tag=tab_tag, label=tab_tag, width=600, height=300):
        dpg.add_text(label='Select the compounds you want to add!', parent=tab_tag)
        compound_strings = []
        compound_tags = []
        for compound in compounds:
            compound_strings.append(str(f'{"Name":20}{compound.iupac_name}\n{"Formula":20}{compound.molecular_formula}\n{"InChiKey":20}{compound.inchikey}'))
        for compound_string in compound_strings:
            compound_tag = str(f'{windowCount.pubchem_popup} {compound_string}')
            compound_tags.append(compound_tag)
            dpg.add_checkbox(tag=compound_tag, label=compound_string, parent=tab_tag)
        dpg.add_button(label='Add to Database, Continue to Next Step', parent=tab_tag, callback=pubchem_popup_add_info,
                       user_data=[compound_tags, compounds, tab_tag])

def pubchem_popup_add_info(sender, app_data, user_data):
    dpg.delete_item(sender)
    compounds_to_add = []
    compound_tags = user_data[0]
    compounds = user_data[1]
    tab_tag = user_data[2]
    for x in range(len(compound_tags)):
        if dpg.get_value(compound_tags[x]) == True:
            compounds_to_add.append(compounds[x])
            dpg.delete_item(compound_tags[x])
        else:
            dpg.delete_item(compound_tags[x])

    compounds = gc(get_filepath())
    names = compounds[0]
    name_tags = []
    label_tags = []
    for x in range(1, 13):
        if names[x] is not None:
            name_tag = str(f'{windowCount.pubchem_popup}. {names[x]}')
            labels = str(f'{x}. {names[x]}')
            label_tag = str(f'{windowCount}_{labels}')
            label_tags.append(label_tag)
            dpg.add_text(labels,tag=label_tag, parent=tab_tag)
            dpg.add_input_text(tag=name_tag, parent=tab_tag)
            name_tags.append(name_tag)
    button_tag = str(f'{windowCount.pubchem_popup}_add_pubchem_chemical')
    dpg.add_button(label='Add Chemical to Database!', tag=button_tag,
                   parent=tab_tag, callback=add_with_pubchem,
                   user_data=[compounds_to_add, name_tags, label_tags, button_tag, tab_tag])

def add_with_pubchem(sender, app_data, user_data):
    compounds_to_add = user_data[0]
    chosen_compound = compounds_to_add[0]
    name_tags = user_data[1]
    label_tags = user_data[2]
    button_tag = user_data[3]
    tab_tag = user_data[4]

    wb = load_workbook(get_filepath())
    sheet = wb.active
    max_row = sheet.max_row
    max_col = sheet.max_column
    new_row = max_row + 1

    # creating a new accession
    prev_accession = sheet.cell(max_row, 1).value
    zeros = 6 - len(str(int(prev_accession[5::]) + 1))
    sheet.cell(new_row, 1).value = str(prev_accession[0:5]) + str('0' * zeros) + str(int(prev_accession[5::]) + 1)

    for x in range(2, 14):
        if sheet.cell(1, x).value != None:
            sheet.cell(new_row, x).value = dpg.get_value(name_tags[x-2])

    # just calling all of the different chemical properties from PubChem :\
    sheet.cell(new_row, 14).value = int(chosen_compound.cid)
    sheet.cell(new_row, 15).value = chosen_compound.molecular_formula
    sheet.cell(new_row, 16).value = float(chosen_compound.molecular_weight)
    sheet.cell(new_row, 20).value = int(chosen_compound.cid)
    sheet.cell(new_row, 21).value = chosen_compound.molecular_formula
    sheet.cell(new_row, 22).value = float(chosen_compound.molecular_weight)
    sheet.cell(new_row, 23).value = chosen_compound.canonical_smiles
    sheet.cell(new_row, 24).value = chosen_compound.isomeric_smiles
    sheet.cell(new_row, 25).value = chosen_compound.inchi
    sheet.cell(new_row, 26).value = chosen_compound.inchikey
    sheet.cell(new_row, 27).value = chosen_compound.iupac_name
    # FIXME the excel sheet has a repetitive mass but is listed as iupac name
    sheet.cell(new_row, 29).value = float(chosen_compound.monoisotopic_mass)
    sheet.cell(new_row, 30).value = int(chosen_compound.tpsa)
    sheet.cell(new_row, 31).value = int(chosen_compound.complexity)
    sheet.cell(new_row, 32).value = int(chosen_compound.charge)
    sheet.cell(new_row, 33).value = int(chosen_compound.h_bond_donor_count)
    sheet.cell(new_row, 34).value = int(chosen_compound.h_bond_acceptor_count)
    sheet.cell(new_row, 35).value = int(chosen_compound.rotatable_bond_count)
    sheet.cell(new_row, 36).value = int(chosen_compound.heavy_atom_count)
    sheet.cell(new_row, 37).value = int(chosen_compound.isotope_atom_count)
    sheet.cell(new_row, 38).value = int(chosen_compound.atom_stereo_count)
    sheet.cell(new_row, 39).value = int(chosen_compound.defined_atom_stereo_count)
    sheet.cell(new_row, 40).value = int(chosen_compound.undefined_atom_stereo_count)
    sheet.cell(new_row, 41).value = int(chosen_compound.bond_stereo_count)
    sheet.cell(new_row, 42).value = int(chosen_compound.defined_bond_stereo_count)
    sheet.cell(new_row, 43).value = int(chosen_compound.undefined_bond_stereo_count)
    sheet.cell(new_row, 44).value = int(chosen_compound.covalent_unit_count)
    sheet.cell(new_row, 46).value = chosen_compound.fingerprint
    sheet.cell(new_row, 47).value = float(chosen_compound.xlogp)

    wb.save(get_filepath())

    for name_tag in name_tags:
        dpg.delete_item(name_tag)
    for label_tag in label_tags:
        dpg.delete_item(label_tag)
    dpg.delete_item(button_tag)

    dpg.add_text('Chemical has been added to the database!', parent=tab_tag)
    dpg.add_button(label='close', parent=tab_tag, callback=close, user_data=tab_tag)

# ----------------------------------------------------------------------------------------------------------------------
# Miscellaneous Features

def close(sender, app_data, user_data):
    dpg.delete_item(user_data)


def invalid_filepath_popup():
    windowCount.invalid_filepath_popup_count += 1
    with dpg.window(label='Invalid Filepath or No Filepath', tag=f'Invalid Filepath or No Filepath {windowCount.invalid_filepath_popup_count}'):
        dpg.add_text('Invalid Filepath or No Filepath\nEnter a new filepath on the Home page')
        dpg.add_button(label='Close', tag='Button Invalid Filepath or No Filepath {windowCount.invalid_filepath_popup_count}',
                       callback=close, user_data=f'Invalid Filepath or No Filepath {windowCount.invalid_filepath_popup_count}')




# ---------------------------------------------------------------------------------------------------------------------
# Home Screen

with dpg.window(label='PMF Chemical Database', width=600, height=300, tag='Primary Window'):
    with dpg.menu_bar():
        with dpg.menu(label='File'):
            dpg.add_menu_item(tag='filepath', label='Add Filepath to Database')
            dpg.add_menu_item(tag='save', label='Save')
        dpg.add_menu_item(tag='search', label='Search Database', callback=searchWindow.search_window)
        with dpg.menu(label='Edit Database'):
            with dpg.menu(label='Add to Database'):
                dpg.add_menu_item(label='Add Manually', callback=manualTabAdd.manual_window)
                dpg.add_menu_item(label='Add from PubChem', callback=pubChemAdd.pubchem_window)
        with dpg.tab_bar(tag='tabs', parent='Primary Window'):
            with dpg.tab(label='Home', tag='Home'):
                dpg.add_text('Welcome to the Database!', parent='Home')
                dpg.add_text('Enter Filepath to the Database Bellow', parent='Home')
                dpg.add_input_text(tag='file', parent='Home')




dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


