# Cognitive Assessment Games

A collection of interactive cognitive assessment games built with Python and Pygame to test and train different aspects of memory and reaction time.

## 🎮 Games Included

### 1. Memory Retention Game (`MemoryRetention.py`)
A classic memory matching game where players flip cards to find matching pairs of shapes and colors.
- **Objective**: Match all pairs of identical icons
- **Skills Tested**: Visual memory, pattern recognition, concentration
- **Features**: Animated card reveals, randomized board layout, automatic game restart

### 2. Reaction Time Test (`ReactionTime.py`)
Test your reflexes with this simple but effective reaction time measurement tool.
- **Objective**: Click as quickly as possible when the screen turns green
- **Skills Tested**: Reaction time, alertness, hand-eye coordination
- **Features**: Random delay intervals, precise millisecond timing, visual feedback

### 3. Verbal Memory Test (`VerbalMemory.py`)
Challenge your ability to remember and recall sequences of words.
- **Objective**: Memorize word sequences and type them back correctly
- **Skills Tested**: Verbal memory, sequential recall, typing accuracy
- **Features**: Progressive difficulty, scoring system, immediate feedback

### 4. Short Term Memory Test (`ShortTermMemory.py`)
*(Referenced in menu but file not provided)*
Test your short-term memory capabilities.

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Pygame library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cognitive-assessment-games.git
cd cognitive-assessment-games
```

2. Install required dependencies:
```bash
pip install pygame
```

### Running the Games

#### Option 1: Main Menu (Recommended)
Run the main menu to access all games:
```bash
python Menu.py
```

#### Option 2: Individual Games
Run games directly:
```bash
python MemoryRetention.py    # Memory matching game
python ReactionTime.py       # Reaction time test
python VerbalMemory.py       # Verbal memory test
```

## 🎯 How to Play

### Memory Retention Game
1. Click on cards to reveal their icons
2. Try to remember the location of matching pairs
3. Match all pairs to win and advance to the next level
4. The game automatically restarts with a new layout

### Reaction Time Test
1. Click "Click to Start" to begin
2. Wait for the screen to turn from yellow to green
3. Click as quickly as possible when you see "Click NOW!"
4. Your reaction time will be displayed in milliseconds
5. Click to play again

### Verbal Memory Test
1. Click "Start Game" to begin
2. Memorize the sequence of words displayed
3. Type each word in the input box when prompted
4. Progress through increasingly difficult sequences
5. View your final score and choose to play again

## 🛠️ Technical Details

### Built With
- **Python 3.x** - Core programming language
- **Pygame** - Game development library for graphics and input handling

### Key Features
- **Modular Design**: Each game is self-contained and can run independently
- **User-Friendly Interface**: Clean, intuitive controls and visual feedback
- **Performance Tracking**: Scoring systems and performance metrics
- **Responsive Controls**: Smooth mouse and keyboard input handling
- **Cross-Platform**: Runs on Windows, macOS, and Linux

### File Structure
```
├── Menu.py              # Main menu system
├── MemoryRetention.py   # Memory matching game
├── ReactionTime.py      # Reaction time test
├── VerbalMemory.py      # Verbal memory test
└── README.md           # This file
```

## 🎨 Game Configuration

### Memory Retention Game
- **Board Size**: 10x7 grid (70 cards, 35 pairs)
- **Card Size**: 40x40 pixels
- **Shapes**: Donut, Square, Diamond, Lines, Oval
- **Colors**: Red, Green, Blue, Yellow, Orange, Purple, Cyan

### Reaction Time Test
- **Delay Range**: 1-10 seconds (randomized)
- **Measurement Precision**: Milliseconds
- **Display Resolution**: 720x720 pixels

### Verbal Memory Test
- **Starting Difficulty**: 2 words
- **Maximum Difficulty**: 5 words
- **Word Pool**: Common fruit names
- **Display Time**: 2 seconds per sequence

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Report Bugs**: Open an issue describing the problem
2. **Suggest Features**: Propose new games or improvements
3. **Submit Pull Requests**: Add new features or fix existing issues
4. **Improve Documentation**: Help make the README and code comments clearer

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Acknowledgments

- Built with [Pygame](https://www.pygame.org/) - Python game development library
- Inspired by cognitive assessment tools used in psychology and neuroscience
- Thanks to the open-source community for continuous inspiration

## 📞 Contact

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com

---

**Note**: These games are designed for entertainment and basic cognitive assessment. They are not intended as professional diagnostic tools.
