********************************************************************************
A: verify that you have json installed

B:  To create the files of data to populate the database with you need to run a
    few scripts to create the files. If you have already created the files then
    skip down after the numbered steps.
    1. run the equipmentcreator.py
        1.1 Required Files:
            Serial number file, model name file, manufacturer name file,
            servicetag file, smsu tag number file, mac address file,
            purchase price file, and the blank final
            save file titled equipmentlist.txt
    2. run the locationcreator.py
        2.1 Required Files:
            Just the final save file is required, everything else is generated.
            locationlist.txt
    3. run the clientcreator.py
        3.1 Required Files:
            list of names file, list of m numbers file, and the save file
            clientlist.txt
    4. run the checkoutcreator.py
        4.1 Required Files:
            All of the previous save files, so equipmentlist.txt,
            locationlist.txt, clientlist.txt, and the save file
            for checkout of checkoutlist.txt.

C:  Now you need to make sure the created data text files are in the
    populationfolders directory.

D:  Run the command "./manage.py populate" to populate the database.
    Note: This command needs to be run from an empty database or else there
    might be conflicts when entering the test database so you will want to
    delete your existing database and migrate prior to running
    the populate command.
********************************************************************************
