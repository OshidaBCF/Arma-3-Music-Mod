# Arma-3-Music-Mod
A python script to automatically make a Music Mod for Arma3 

# Requierement
1. ```pip install -r requirements.txt```
2. Python 3
3. [Chromedriver.exe](https://chromedriver.chromium.org/downloads)

# How to use
1. Download the script somewhere on your computer
2. Download the chromedriver and store it somewhere on your computer
3. Replace "Absolute_path_to_folderç_where_modpackFile_is_located" on line 14 by the path to the modpack file
4. Replace "Absolute_path_to_chromedriver" on line 43 by the path to the chromedriver.exe
5. Replace "Absolute_path_to_image" on line 54 by the path to the image for your collection, has to be square shaped and at least 195x195 px
6. Before running the script :
    - You need to be sure you are logged in your steam account on chrome
    - You need to start chrome with the additional parameter ```--remote-debugging-port=9222```
    - In the likeliness that you installed chrome in the default folder, run this command in cmd or windows+r ```"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222```
    - If chrome was already running, you'll need to stop it completly (3 dot menu then "quit")
    - You need to be sure that you are subscribed to every mods listed in the html file, if one is missing the script will stop
    - You can simpely drop the html in the arma launcher and it will subscribe to any missing mods
8. Run the python script, it should open a new tab in chrome, go to the steam page and generate a collection
9. At the end it will pause for 20-40 seconds and check for when steam finish analyzing the collection, it will then print the link of the collection, and if you want it can also send the link on discord via a webhook.


There shouldn't be any issue but i know that my explanations can be very bad sometimes.
If there is any problem please open an issue and i'll try to help
