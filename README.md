# Arma-3-Music-Mod
A python script to automatically make a Music Mod for Arma3 

# Requierement
1. Audioread : ```pip install audioread```
2. Python
3. Arma 3 Tools : [Steam Store](https://store.steampowered.com/app/233800/Arma_3_Tools/)

# How to use
1. Download the project somewhere on your computer
2. Create a folder named "Music" next to the py script
3. Copy the musics to be added to the mod into the "Music" folder (Must be as .ogg files)
4. Edit the python script, you need to change the "folder" variable at the begining, this is the "ID" of the mod. Only Letters, Numbers (_ and - may work but just in case don't)
5. (Optional) Modify the logo.paa and steamlogo.png in the template folder, this will be the logo of your mod
6. Run the python script, it should automatically copy the ogg from "Music" to the "folderwithtracks" folder, generate the hpp/cpp files
7. Use the Arma 3 Addons Builder to build the mod,
    - Select the created folder (the one named with the mod ID) as the source folder and the destination folder
    - Uncheck "binarize" (it apparently cause issues with sound mods)
    - Pack
8. Copy the pbo file from the created folder to the Addons Folder inside the folder starting with an @
9. The mod is now complete and can be uploaded to the workshop using the Publisher tool in the Arma 3 Toolbox


There shouldn't be any issue but i know that my explaining can be very bad sometime.
If there is any problem please open an issue and i'll try to help
