# PMF_database_editor

# Search an excel formatted database, add chemicals, edit the database, create a personal database to export data, and save for later
This is all accessible through the main GUI interface which will be updated along the way to add new features to make chemical searches more intuitive

# App Setup

1. The app can be downloaded directly from here this repository! 

# Main GUI
  - class windowCount
      Used to count the windows and window types that are currently open to ensure that new windows added with Dear PyGUI have the same tag.
      Every time this function is called, make sure to add 1 to whatever window count is being called.
        Types of window counts: manual_count, search_count, pubchem_count, search_popup_count, pubchem_popup, invalid_filepath_popup_count, output_tab_count,  
        hmdb_add_count 
