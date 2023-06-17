import os, shutil, audioread, sys

modID = "OshidasMusicMod3" #Replace with the "id" of the mod you wish to make, only letters, numbers and _
modName = "Oshida\'s Music Mod" # Beware to "escape" any special character
modAuthor = "Oshida"

shutil.rmtree(modID + "\\folderwithtracks", ignore_errors=True)
shutil.rmtree(modID, ignore_errors=True)

shutil.copytree(R"template", modID) # If an error appear here, delete the mod folder named like modID
file = open(modID + "\\FileListWithMusicTracks.hpp", "w", encoding="UTF-8")
musicList = os.listdir("Music")
os.mkdir(modID + "\\folderwithtracks")
for i in range(len(musicList)):
    if musicList[i].lower().endswith('.ogg'): # Only Copy OGG Files
        shutil.copy("Music\\" + musicList[i], modID + "\\folderwithtracks\\" + str(i) + ".ogg")
        with audioread.audio_open(modID + "\\folderwithtracks\\" + str(i) + ".ogg") as audioFile:
            length = int(audioFile.duration)
            #print(musicList[i] + ' : ' + str(length))
        file.write("class " + modID + "Song" + str(i) + '\n')
        file.write("{\n")
        file.write("\tname = \"" + musicList[i][:-4] + "\";\n")
        file.write("\tsound[] = {\"" + modID + "\\folderwithtracks\\" + str(i) + ".ogg\",db+0,1};\n")
        file.write("\tduration = " + str(length) +";\n")
        file.write("\tmusicClass = \"" + modID + "\";\n")
        file.write("};\n")
        print(musicList[i])
file.close()

modCpp = open(modID + "\\mod.cpp", "w", encoding="UTF-8")
modCpp.write("name = \"" + modName + "\";\n")
modCpp.write("picture = \"logo.paa\";\n")
modCpp.write("description = \"\";\n")
modCpp.write("logo = \"logo.paa\";\n")
modCpp.write("logoOver = \"logo.paa\";\n")
modCpp.write("tooltip = \"" + modName + "\";\n")
modCpp.write("tooltipOwned = \"" + modName + " Owned\";\n")
modCpp.write("overview = \"" + modName + "\";\n")
modCpp.write("author = \"" + modAuthor + "\";\n")
modCpp.write("overviewPicture = \"logo.paa\";\n")
modCpp.write("overviewText = \"" + modName + "\";\n")
modCpp.write("overviewFootnote = \"\";\n")
modCpp.close()


configCpp = open(modID + "\\config.cpp", "w", encoding="UTF-8")
configCpp.write("class CfgPatches\n")
configCpp.write("{\n")
configCpp.write("\tclass " + modID + "\n")
configCpp.write("\t{\n")
configCpp.write("\t\tname = \"" + modName + "\";\n")
configCpp.write("\t\tauthor = \"" + modAuthor + "\";\n")
configCpp.write("\t\trequiredVersion = 1.00;\n")
configCpp.write("\t\trequiredAddons[] = {};\n")
configCpp.write("\t\tunits[] = {};\n")
configCpp.write("\t\tweapons[] = {};\n")
configCpp.write("\t\tworlds[] = {};\n")
configCpp.write("\t};\n")
configCpp.write("};\n")
configCpp.write("class CfgMusic\n")
configCpp.write("{\n")
configCpp.write("\t#include \"FileListWithMusicTracks.hpp\"\n")
configCpp.write("};\n")
configCpp.write("class CfgMusicClasses\n")
configCpp.write("{\n")
configCpp.write("\tclass " + modID + "\n")
configCpp.write("\t{\n")
configCpp.write("\t\tdisplayName = \"" + modName + "\";\n")
configCpp.write("\t};\n")
configCpp.write("};\n")
configCpp.close()

if os.path.exists('@' + modID):
    print("A mod folder already exist, to prevent overwriting the script was stopped, either change the ID or delete the old mod folder then restart the script")
    sys.exit()

os.makedirs('@' + modID + "\\Addons")
shutil.copy(modID + "\\logo.paa", '@' + modID + "\\logo.paa")
shutil.copy(modID + "\\mod.cpp", '@' + modID + "\\mod.cpp")
shutil.copy(modID + "\\steamLogo.png", '@' + modID + "\\steamLogo.png")
