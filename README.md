# Uninstallation 
1. Run install/uninstall.sh

# Installation
WARNING: If you have clara installed already, you will need to run the uninstallation script
1. First of all, build. See instructions bellow   
2. Then, run install/install.sh    


# Building 
WARNING: This only builds+works on linux (unless someone adds windows support in a PR)    
1. run ./deps.sh
2. run ./build.sh 
3. wait for the AI to train (depending on your hardware, this could take up to an hour)
4. the final build is located in dist/
5. To run the thing, run python exec.py

# Usage 
To execute a command, press super (the windows key), and then ` (right next to the one key)        
Then type your command. For example, "play snow on the beach by taylor swift", or "set a 30 minute timer"     
Then press enter, and it will run the command.    