# PMF_database_editor

# Search an excel formatted database, add chemicals, edit the database, create a personal database to export data, and save for later
This is all accessible through the main GUI interface which will be updated along the way to add new features to make chemical searches more intuitive.
The completed .exe file is only available for windows devices at the moment, but an updated Mac file will be released soon.

# App Setup

1. The app can be downloaded the [Database_V2.exe](https://drive.google.com/file/d/1YEGfNXTLjPN7JRBxe4nfW_8CT4uIqrRh/view?usp=sharing) google drive link! When the link opens, select download. If the virus screen pops up, select download anyways.
2. Once the app is downloaded on your system, double click the icon wherever it is stored (should be in downloads to start). Windows will now ask you to trust the app before running because it is not a recognized windows app. Click on "more info", then run anyways.
3. The app will take a moment to set up, but once it boots navigate to the "File" tab.
4. To make all features of the database work, enter the absolute path to the excel database you will be using (T:\path\info\example.xlsx) and then click update filepaths. If you want to add a personal database to have a subset of data for faster searching, enter a personal database path in the "My_Database_1" field (C:\path\info\example.txt), then click update (see add personal path for more info bellow).
5. You're all set up and ready to start using the database!

# Main GUI
  - class windowCount
      Used to count the windows and window types that are currently open to ensure that new windows added with Dear PyGUI have the same tag.
      Every time this function is called, make sure to add 1 to whatever window count is being called.
        Types of window counts: manual_count, search_count, pubchem_count, search_popup_count, pubchem_popup, invalid_filepath_popup_count, output_tab_count,  
        hmdb_add_count 
