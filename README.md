# ZeroCross

**Working**

a. *Room Creation-*
Player1 sends a create_room() request to the server. Server searches for available room id and returns it, or an Error code in case all rooms are full.

b. *Game Play-*

  1. Player1 sends create_room() request to server. The other player joins room using join_room().

  2. A Player makes a move, thereby sending an update() request to server. The other player keeps sending game_status() request to server until the game_status changes.

  3. Server updates the board config, and executes check_status(). If it returns 0/1 then p1/p2 has won the game, if it returns 3 then game has ended in a tie. If it returns 2,        the game will continue and board config is refreshed for both players.

  4. If game ends, there can be a new game on the same room id by relpay(), or end_game() api can be called.

c. *Quit Game-* 
Call end_game api.

d. *Replay Game-*
Call replay api, effectively resetting the board.

**NOTE-** 
Only the player who has played last can choose between Quit Game and Replay Game.



**File Description**

Board contains the board class

Server.py contains all the apis
