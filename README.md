# 🐍 Snake Game — Pygame Edition

A classic Snake game built using Python and Pygame with clean visuals, adjustable difficulty, and restart functionality. This simulation features real-time interaction, performance tuning, and executable packaging options.

---

## 🧠 What This Project Covers

- 🎮 Real-time snake movement and control using arrow keys  
- ⚙️ Adjustable difficulty with speed scaling (Easy, Normal, Hard)  
- ♻️ Instant restart after Game Over via keyboard  
- 🧱 Grid-based rendering using `pygame` rectangles  
- 📦 Standalone executable creation via PyInstaller

---

## 📁 File Structure

```
Snake_Game/
├── updated_snake_game.py       # Main game script
├── requirements.txt            # Contains pygame dependency
├── README.md                   # This file
├── dist/
│   └── updated_snake_game.exe  # Built executable (via PyInstaller)
```

---

## 🚀 How to Run the Game

### ▶️ Run via Python

```bash
python updated_snake_game.py
```

> Requires Python 3.8+ and Pygame installed

### 🛠 Build a Windows Executable

Use PyInstaller:

```bash
pyinstaller --onefile updated_snake_game.py
```

> Output will be in the `dist/` directory.

Optional with icon:

```bash
pyinstaller --onefile --icon=icon.ico updated_snake_game.py
```

---

## ⌨️ Controls

| Action                  | Key             |
|-------------------------|-----------------|
| Move Up                | ↑ Arrow         |
| Move Down              | ↓ Arrow         |
| Move Left              | ← Arrow         |
| Move Right             | → Arrow         |
| Restart After Game Over| `E`             |
| Select Difficulty       | `1`, `2`, or `3` at launch |

---

## 🧠 Conceptual Highlights

| Feature              | Description                                               |
|----------------------|-----------------------------------------------------------|
| Difficulty Modes     | Game speed changes with selected mode (FPS scaling)       |
| Restart Capability   | Game over state allows pressing `E` to restart instantly  |
| Clean Rendering      | `pygame.draw.rect()` used for minimal yet effective design|
| Score Display        | Real-time score + difficulty label rendered to screen     |

---

## 🛠 Requirements

- Python 3.8+
- Pygame

Install dependencies:

```bash
pip install pygame
```

Or use:

```bash
pip install -r requirements.txt
```

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 👨‍💻 Author

**Mugdho Jeferson Rozario**  
Engineering Physics (Nuclear), McMaster University  
GitHub: [@mugjeff12](https://github.com/mugjeff12)
