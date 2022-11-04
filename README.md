# Chemical Database Editor

# Search an excel formatted database, add chemicals, edit the database, create a personal database to export data, and save for later
This is all accessible through the main GUI interface which will be updated along the way to add new features to make chemical searches more intuitive.
The completed .exe file is only available for windows devices at the moment, but an updated Mac file will be released soon.

# App Setup

1. The app can be downloaded the [Database_V2.exe](https://drive.google.com/file/d/1VPwz_KzmrtNJU0M0jbiBVRoHrNyziMJg/view?usp=sharing) google drive link! When the link opens, select download. If the virus screen pops up, select download anyways.

2. Once the app is downloaded on your system, double click the icon wherever it is stored (should be in downloads to start). Windows will now ask you to trust the app before running because it is not a recognized windows app. Click on "more info", then run anyways.

3. The app will take a moment to set up, but once it boots navigate to the "File" tab.

4. To make all features of the database work, enter the absolute path to the excel database you will be using (T:\path\info\example.xlsx) and then click update filepaths. If you want to add a personal database to have a subset of data for faster searching, enter a personal database path in the "My_Database_1" field (C:\path\info\example.xlsx), then click update (see add personal path for more info bellow).

5. You're all set up and ready to start using the database!



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
> If you want to see more information on any of the chemicals, you can select their checkboxes and then click the "" button. This will create a new tab for each of the selected chemicals and will have all of their information displayed!
>> You can also export the chemical information to your personal excel database!
>> 1. First, click the "" button at the bottom of the screen.
>> 2. You will be prompted to select a database to add to. You can choose one of the databases that you created on the file tab, or create a new excel database! If you're creating a new database, enter what you would like the new database to be named as well as the filepath (C:\path\info\example.xlsx), then click ""
>> 3. Your chemicals will be added to your personal database!








# Main GUI
  - class windowCount
      Used to count the windows and window types that are currently open to ensure that new windows added with Dear PyGUI have the same tag.
      Every time this function is called, make sure to add 1 to whatever window count is being called.
        Types of window counts: manual_count, search_count, pubchem_count, search_popup_count, pubchem_popup, invalid_filepath_popup_count, output_tab_count,  
        hmdb_add_count 
