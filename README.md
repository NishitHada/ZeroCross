# ZeroCross

Working-
Room Creation-
Client sends a create_room() request to the server. Server searches for available room id and returns it or with Error code in case all rooms are full.


Game Playing- 
Client sends start_game() request to server.
Player makes a move, client sends an update() request to server. 
Server updates the board config, and executes check_status(). If it returns 0/1 then p1/p2 has won the game, if it returns 2, then game will continue and if it returns 3 then game has ended in a tie.
If game ends, there can be a new game on the same room id, else the room id 
is flagged as unused and end_game() api can be called.


Quit Game- 
Call end_game api.

File Description
Board contains the board class

Server.py contains all the apis
