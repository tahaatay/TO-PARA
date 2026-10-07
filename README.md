# TO'PARA — Money Rush

A simple arcade-style 2D game made with Python and Pygame.

Control the slime with **W, A, S, D**, collect money to increase your score, and avoid negative money obstacles. As your score increases, the game becomes faster and more challenging.

### Features
   V1.0
*  Collect money to increase your score
*  Avoid negative money obstacles
*  Increasing difficulty
*  Error/life system
*  Pause system
*  Sound effects and background music
*  Restart system
*  Simple keyboard controls
  
   V1.1
*  Added high score tracking
*  Added music and sound effect toggles
*  Improved obstacle boundary handling
*  Fixed several gameplay bugs
*  Improved overall gameplay smoothness
  
# TO'PARA v1.2 — Gameplay Update

## Added

*  Added a **Health System** with 3 starting lives.
*  Added a **Healing Heart** that can randomly appear during gameplay.
*  Added a **Combo System**.
*  Higher combos now give more points per collected coin.
*  Added a second negative-money obstacle after reaching a certain score.
*  Improved the **High Score System** and new record handling.
*  Improved music controls on the Game Over screen.
*  Improved sound effect controls.
*  Added a **Combo counter** to the in-game HUD.
*  Increased the game update rate to **75 FPS**.

## Gameplay Changes

* Taking damage now reduces your health instead of immediately ending the game.
* Collecting negative-money obstacles resets your combo.
* The game ends when your health reaches 0 or your score goes below 0.
* The Healing Heart can restore one health point.
* Combo rewards increase as the combo gets higher, up to **+5 points per coin**.

## Bug Fixes & Improvements

* Improved the restart system.
* Restarting now correctly resets health, combo, special items and related game states.
* Improved Game Over music and sound behavior.
* Various gameplay and movement adjustments.

This project was created as my **first Pygame game** to practice game loops, collision detection, movement, sprites, sounds, and basic game mechanics.

