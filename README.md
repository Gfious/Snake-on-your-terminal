# Snake-on-your-terminal
Just a small snake game, programmed in python, that'll run on the terminal.

## Development Log
Class skeleton done. Also Collision Check with walls, score and fruit spawn, snake movement, game_over state and exit after game_over done. 

## Future 
I want to implement the input handling, the snake growth and self collision

## Late Implementation
Poison spitting by the snake
Power-up fruits (speed up, phantom, range)
Mouse that will compete with snake for fruits
Mouse will flee the snake and eat fruits
Mouse will see all the fruits, but only can see snake in a determined range
Mouse will can have power-ups (range will be vision range as opposed to poison spit by the snake)
Snake droppings have a probability of happening, which will make the mouse run
Mouse droppings are toxic to the snake (reduce snake speed and decrements score)
Mouse path for food and snake/snake droppings escape
Snake can poison the mouse
Snake can poison the fruits
If a mouse eats a poisoned fruit, it will be poisoned
Poison paralyses mouse
Droppings exist for 30 seconds
Fruit points is 1
Mouse points is 10
Map randomly generated (walls will have some rules on their spawn)
Mouse has a probability of 30% to spawn every 60 seconds
There can be only 3 mice on the screen at once
Power-ups have a 10 seconds active time (stacked 4 times)
Poison spitting speed will be 2x snake speed
Game penalties will scale over time
Mouse can only appear after 1 minute in game (so it eases the player to the controls and mechanics)
    60s → mice unlock
    120s → more mice can spawn
    180s → dropping chance increases
    240s → powerups appear more frequently
Different ai's for the enemies: Passive and escapist mouse and aggressive when cornered rat
Mongoose timed event (mongoose will hunt the snake, poison only slows it down)

# Road map


## ✅ Phase 1 — Core Snake (MVP)

Goal: Fully playable Snake game in terminal.

* [x] Snake movement system
* [] Direction handling (WASD)
* [x] Food spawning (random, grid-based)
* [x] Score system
* [x] Wall collision detection
* [x] Game over state
* [x] Basic game loop (update → render → sleep)

---

## 🐛 Phase 2 — Snake Mechanics

Goal: Make the game feel like real Snake.

* [ ] Snake growth system
* [ ] Self-collision detection
* [ ] Prevent instant reverse direction (anti-suicide rule)
* [ ] Improved input handling (non-blocking if possible)

---

## 🖥️ Phase 3 — Terminal Rendering Upgrade

Goal: Turn debug output into a real game view.

* [ ] Grid-based rendering (board visualization)
* [ ] Snake body rendering (ASCII representation)
* [ ] Food rendering as symbol (*)
* [ ] Optional: borders / walls display
* [ ] Clear-screen rendering per frame

---

## 🧱 Phase 4 — World Systems

Goal: Add structure to the environment.

* [ ] Static wall generation
* [ ] Randomized map layouts (basic rules)
* [ ] Collision with walls integrated into game logic

---

## 🐭 Phase 5 — Mouse AI System

Goal: Introduce competing entity.

* [ ] Mouse spawning system (after 60 seconds)
* [ ] Mouse movement logic
* [ ] Mouse seeks food
* [ ] Mouse avoids snake (distance-based logic)
* [ ] Limit max number of mice (e.g. 3)

---

## 💥 Phase 6 — Dynamic Hazards

Goal: Create evolving battlefield.

* [ ] Snake droppings (temporary hazards)
* [ ] Mouse droppings (temporary hazards)
* [ ] Hazard lifetime system (expire after time)
* [ ] Hazard collision rules

---

## 🧪 Phase 7 — Status Effects System

Goal: Add gameplay depth via temporary effects.

* [ ] Poison system (snake & mouse)
* [ ] Slow effect
* [ ] Speed boost effect
* [ ] Phantom / invulnerability mode
* [ ] Effect duration system

---

## 🍎 Phase 8 — Power-ups & Advanced Items

Goal: Add variability and strategy.

* [ ] Power-up fruits (random spawn chance)
* [ ] Stackable or timed effects (limited initially)
* [ ] Risk/reward balancing

---

## 🧠 Phase 9 — AI Improvements

Goal: Make mouse behavior more intelligent.

* [ ] Vision range system
* [ ] Threat evaluation (snake proximity)
* [ ] Simple pathfinding (BFS or greedy)
* [ ] Escape behavior logic

---

## 🌍 Phase 10 — Advanced Simulation (Optional)

Goal: Turn game into ecosystem simulation.

* [ ] Multiple mice behavior interactions
* [ ] Environmental pressure systems
* [ ] Emergent gameplay tuning
* [ ] Balanced spawn rates over time

---

## 🎮 Phase 11 — Polish / Expansion

Goal: Make it feel like a finished game.

* [ ] Difficulty scaling over time
* [ ] Menu system (start/restart/quit)
* [ ] High score tracking
* [ ] Performance optimization
* [ ] Optional Pygame graphical version

---

### 🧭 Design Philosophy

* Keep Snake mechanics stable before adding complexity
* Each new system must interact with at least one existing system
* Prefer emergent gameplay over isolated features
* Add complexity only when the current system is fun and stable
