https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/
https://kbroman.org/github_tutorial/pages/init.html


GIT:

kommando cmd:

LOCAL :

rm -rf .git // slett mappe

ls -la // sjekk mappe struktur

git status // status

touch .gitignore // lag en ignore fil for uønskede filer

git add -A // Add alt til stage area

git commit -m "Initial commit" //legg til forandringer

git reset // fjern alt fra "stage" area til working directory

git log // Log for commits

 - - - - 


REMOTE :

git clone <url> <where to clone> // for å klone repository


git diff // Vis endringer som er gjort til koden

git status // sjekk status

git add -A // legg til "staging" directory

git commit -m "endringer"

 - - - - 

git pull origin master // Legg til siste endringer av repository

git push origin master // send ut endringer til master "branch" til navn "origin"

 - - - - 

git remote add origin https://github.com/BackYardSoftware/CloudServer.git // legg til eksisterende remote depository

git remote -v // verify new remote

git remote rm destination // fjerner destinatsjon
