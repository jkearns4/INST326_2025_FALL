# Survival Game

This is a text-based survival game where the player tries to survive 20 days in a zombie-filled city. Each day, you choose an action, deal with stat changes, and sometimes face random events. The goal is simple: make smart decisions and keep your health above zero until Day 20.

---

## Files in This Project

### **survival_game.py**
The main Python script. It contains:
- the Player class  
- the Game class  
- the stat update system  
- random event handling  
- action outcome logic  
- the main game loop  

### **survival_config.json**
This file holds all the game data, including:
- starting stats  
- daily stat decay values  
- action outcomes  
- random events  
- number of days to survive  

The game loads everything from this file so nothing is hardcoded.

### **README.md**
The file you’re reading now. It explains how to run and play the game and who contributed to which parts.

---

## How to Run the Game

These steps assume macOS, but other systems use the same idea.

1. Open Terminal  
2. Go to the folder where your game files are located:

```bash
cd path/to/your/folder
