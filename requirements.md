# Scope (In/Out)
* IN - What will your product do
  * Allow users to control a space-faring python that shoots lazers
  * Fend off against enemies that shoot back
  * Gain power-ups such as extra lazers, shields and extra lives
  * Get points for taking down enemies. Lose lives when hit by enemies
  * Game over when user runs out of lives
* OUT - What will your product not do.
  * Not multiplayer
  * Console application only

# Minimum Viable Product
  * Side to side snake movement
  * Shooting towards enemies
  * Enemies moving
  * Hit detection
  * Have sprite/image for the snake “python”
  * Game over page
# Stretch
  * Power Ups
    * Additional lazers 
    * Missiles (splash damage)
    * Shields (invulnerbility to a few shots)
    * Extra lives
    * Timed invulnerbility (invulnerbility to unlimited shots within a timeframe)
  * Boss opponents
  * Sound Effects
  * Laser
  * Enemy noises
  * Sprites/images for enemies, etc
  * Start page with link to About Us
  
# Functional Requirements
  * Allow users to move the space-faring python across the screen
  * Allow users to fire lazers from the python towards enemies
  * Moving enemies that fire lazers towards enemies.
  * Collision detection when friendly lazer hits enemy or enemy lazer hits python
  * Game ends when the user is out of lives. User is taken to a game over page that shows the score and provides a link to an about page.

# Data Flow
  * When the user executes the application, they are taken to the main game where they are able to control the python with the arrow keys and shoot lazers with the spacebar. Users will be taken to a start page if stretch goal is reached. Enemies populate the screen and the user attempts to take down as many enemies as possible with the python’s lazer. The user will attempt to stay alive for as long as possibile while taking down as many enemies as possible. Once the user runs out of lives by getting hit by enemy lazers, they will be taken to a game-over page that shows their score, an option to replay the game, and an option to exit the application. The game-over page also contains a link to an about page that provides information about the team. Users can play as many times as they want. When they are satisfied, they can exit the application. 

# Non-Functional Requirements (301 & 401 only)
* Security
  * Security-wise, this console application will not have any access to user information. It is in no way connected to any networks, and it will not contain any backdoors for bad actors. Users should be able to download the game and play it.
* Usability 
  * Controls for the game will be super simple. Users will move the python with the arrow keys and fire lazers (or powered-up weapons) with the spacebar. All other interface interactions (replay button, navigate to about page, exit application) will be done with the mouse. 
