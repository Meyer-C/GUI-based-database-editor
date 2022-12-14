# Chemical Database Editor

**Search an excel formatted database, add chemicals, edit the database, create a personal database to export data, and save for later
This is all accessible through the main GUI interface which will be updated along the way to add new features to make chemical searches more intuitive.
The completed .exe file is only available for windows devices at the moment, but an updated Mac file will be released soon.**

---

# App Setup

1. The app can be downloaded the [Database_V2](https://drive.google.com/drive/folders/1QE8qKF911_otxtfWQJ-tup8bOx1GY_7F?usp=sharing) google drive link! When the link opens, select download. If the virus screen pops up, select download anyways. I recomend opening the google drive link in a chrome browser to make installation a little bit easier. Browsers like edge work as well but require a few extra steps to ensure that the file is safe to download and install.
> If downloading with edge, after you have clicked the download button in the google drive you will need to click the download button in the upper right hand of the screen (it should have a little warning icon on it). Hover over the Database_V2.exe file in this dropdown and then click the "..." icon. Click keep in this popup. It will ask you to trust the app. Click "Show more" and then "keep anyway". This should then download the app as a .exe, ready to run! 

2. Once the app is downloaded on your system, double click the icon wherever it is stored (should be in downloads to start). Windows will now ask you to trust the app before running because it is not a recognized windows app. Click on "more info", then run anyways.

3. The app will take a moment to set up, but once it boots navigate to the "File" tab.
> Once the app is downloaded and run for the first time, make sure that the "filepath.txt" is in the app folder as shown in the drive. Both the app and the filepath.txt will need to be in the same folder for the app to work. You can use the filepath.txt on the drive to download as a template. It can be edited within the app, so don't bother changing it for now, but make sure it is downloaded and is in the same folder as the Database_V2.exe. You will only need to do this step if the app is unable to create a new "filepath.txt" file on first opening. This should be fixed in Database_2.1.exe for easy set-up.

4. To make all features of the database work, enter the absolute path to the excel database you will be using (T:\path\info\example.xlsx) and then click update filepaths. Make sure your excel database is in the same format as the "library_subset.xlsx" in the google drive. If not, you can download and utilize this subset as a template. If you want to add a personal database to have a subset of data for faster searching, enter a personal database path in the "My_Database_1" field (C:\path\info\example.xlsx), then click update (see add personal path for more info bellow).

5. You're all set up and ready to start using the database!

---

# Usage

## File

The file tab is used to store your database information so you don't have to add a filepath every time you want to add chemicals to the database or search the database!

### Edit Main Database

> In this field, you can enter a path to the main database! this is **essential** for the app to run. When you open the app for the first time, make sure to enter the main database path (T:\path\info\example.xlsx). After that you most likely won't need to change this field. As a side note, you can change this to one of your personal database path's if you want to search your personal database!

### My_Database fields

> These fields are used to add personal databases. These can be useful if you want to make a subset of data from the main database. Enter the filepath to your personal database (C:\path\info\example.xlsx) and then hit the "Update Filepaths" button. If you want to add more personal databases you can click the "Add Personal Path" button. This function will also create a new excel file for your personal database if one doesn't currently exist! It will be created with the file name and path that you specify when entering the filepath!
>> If using add personal path, a popup will apear to allow you to add a new personal path. You will be prompted to add a name for the path and the path. Make sure that the name is memorable as it will appear later if you want to add data to this particular personal database. Next, enter a filepath (C:\path\info\example.xlsx). If a this file doesn't exist, it will create a new one for you! Close out of the popup tabs and close and reopen the "File" tab to ensure that the database path has been added!


## Search Database

This tab allows you to search your Main Database (specified on "File" page). Make sure that this database path is specified or it will not work!

1. First, specify the search type you want to do! You can search by the chemical name, mass (which can be either a specific mass or mass range ex. 400-500), or by InChiKey! Make sure to select the right search type you'll be using or you might get some *very* funky results.
2. Next, enter your search term! You can enter part of a name and it should be able to get your result, but you may need to filter it afterwards.
3. Click either "Search" or "Advanced Search Options"!
> If using Search, it will return all information on the chemical or chemicals in the output tab.
> If you click advanced search however, it will create a popup to allow you to select the data that you would like to see in the outputs tab (ex. name, mass, InChiKey). You can select as many of these boxes as you would like! Click the "Advanced Search" button at the bottom of the popup to search!
4. View the outputs in the new "Outputs" tab!
> If you want to see more information on any of the chemicals, you can select their checkboxes and then click the "More Information" button. This will create a new tab for each of the selected chemicals and will have all of their information displayed! From each of these new tabs you can also chose to export the chemical data to your personal excel datasheet using the "Export Data to .xlsx" button on the bottom of the tab!
5. You can also export the chemical information to your personal excel database!
> 1. First, click the "Export Data to .xlsx" button at the bottom of the screen.
> 2. You will be prompted to select a database to add to. You can choose one of the databases that you created on the file tab, or create a new excel database! If you're creating a new database, enter what you would like the new database to be named as well as the filepath (C:\path\info\example.xlsx), then click ""
> 3. Your chemicals will be added to your personal database!

## Edit Database

This tab allows you to add chemicals from your main database using a few different tools. You can add chemicals through 3 different methods: from PubChem, from HMDB, and you can also manually add chemicals. All of these will require you to manually enter data about how the chemical is stored at the lab. Beyond that, much of the data beyond that can be automatically filled in with PubChem or HMDB.

### Manual Chemical Add

> This is the most basic way to add chemicals to the main database, but it requires the most user input. When you click on the Manual Chemical Add button from the Edit Database dropdown menu, a new manual chemical add tab will be pulled up. Enter all of the data that you need for the chemical in the labeled fields. Once the fields are all filled, click "Add Chemical!" a the bottom of the screen! If the chemical has been successfully added, the tab will state that the chemcial has been added successfully!

### PubChem Add

> This tab allows you to add chemicals to your main database directly from PubChem! You can search the PubChem Database using a variety of different search types listed bellow and then select chemicals to add to your database for quicker and easier access! It fills in all of the chemical data from the PubChem Database and then will require you to fill in information on the chemical such as storage information within the lab.

1. First, navigate to the "PubChem Add" option in the "Edit Database" dropdown menu.
2. Once the Pubchem Add tab pops up, you will need to select the search type you would like to use. You can search PubChem by Name, CID, Smiles, InChiKey, InChi, or Chemical Formula. Select one of these buttons.
3. Enter a search term in the text box bellow. Make sure the search term you are using works with the search type you will be using (make sure to not search by name and then type out a chemical formula)
4. Click the search button! It may take a moment to retrieve the chemicals from PubChem so be patient.
5. Once the chemical or chemicals are found, a search popup will apear with the chemical information! This tab will include some basic chemical information including Name, Chemical Formula, and InChiKey.
6. If you want to add a chemical to the database, select one of the chemicals, and then click the "Add to database, continue to next step" button. Becasue you will need to add more storage information about the chemical, only select one chemical at a time.
7. Enter the storage information for the chemical at the lab and then click the "Add to Database" button.
8. If the chemical has been added successfully, a popup will apear saying that the chemical has been added to the database!

### HMDB Add

> This tab allows you to add chemicals directly from the Human Metabolome Data Base! In this early version of this search tool, it can only search by HMDB accession number (HMDB#####), but later versions will include more search options. As with the PubChem Add tool, you will need to add specific information about the chemical such as storage information within the lab.

1. First, navigate to the "HMDB Add" option in the "Edit Database" dropdown menu.
2. Once the HMDB Add tab pops up, there will be a search bar that will allow you to enter the HMDB accession number. You can search with just the accession number (#######), or with the full accession name/number (HMDB#######).
3. Click the "Search" button!
4. Once the chemical has been returned from HMDB, a popup will apear that will list any returned chemicals.
5. If you want to add a chemical to the database, click the button next to the chemical and then the "Add to database, continue to next step" button. Becasue you will need to add more storage information about the chemical, only select one chemical at a time.
7. Enter the storage information for the chemical at the lab and then click the "Add to Database" button.
8. If the chemical has been added successfully, a popup will apear saying that the chemical has been added to the database!








# Main GUI
  - class windowCount
      Used to count the windows and window types that are currently open to ensure that new windows added with Dear PyGUI have the same tag.
      Every time this function is called, make sure to add 1 to whatever window count is being called.
        Types of window counts: manual_count, search_count, pubchem_count, search_popup_count, pubchem_popup, invalid_filepath_popup_count, output_tab_count,  
        hmdb_add_count 
