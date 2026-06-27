## Logic Box — Pattern Generator & Number Analyzer

## Objective

Develop a Python program called **Pattern Generator and Number Analyzer** that emphasizes:

- `for` and `while` loops
- `range()` function
- Control statements: `break`, `continue`, `pass`
- Nested loops for pattern generation
- Menu-driven interface design

This program allows students to **practice programming concepts** and **logical problem-solving skills**.

---

## Features

### 🔷 Pattern Generator
- Generates patterns based on user input using **nested loops**
- Uses both `for` and `while` loops
- Prompts user to enter the number of rows
- Currently implements: **Right-angled Triangle** 

### 🔷 Number Analyzer
- Accepts a **start** and **end** number from the user
- Uses `range()` to iterate over the range
- For each number in the range, displays:
  - **Odd or Even** check
  - **Sum of all numbers** from start to end

### 🔷 Control Statements
- Uses `break` to stop pattern generation on invalid row input
- Uses `pass` as a placeholder for future logic
- Input validation with re-prompting

### 📋 Menu-Driven Interface
| Option | Action |
|--------|--------|
| `1` | Generate Pattern (Right-angled triangle) |
| `2` | Analyze a range of numbers |
| `3` | Exit the program |

---

## 🚀 How to Run

```bash
# Clone or download the project
git clone https://github.com/your-username/logic-box.git

# Navigate to the folder
cd logic-box

# Run the program
python main.py
```

---

## 🔄 Program Flow

```
START
  │
  ▼
Display Welcome Message & Instructions
  │
  ▼
Show Menu Options
  ├── [1] Pattern Generation
  │       └── Ask rows → Validate → Generate triangle with nested loops
  ├── [2] Number Analysis
  │       └── Ask start & end → range() → Check odd/even → Sum
  └── [3] Exit
          └── Thank user → END
```

---

## 📁 Project Structure

```
logic-box/
│
├── main.py              # Main menu-driven program
├── pattern.py           # Pattern generator module
├── analyzer.py          # Number analyzer module
├── README.md            # This file
└── generate_readme.py   # Dynamic README generator script
```

---

## 🧠 Concepts Used

| Concept | Where Used |
|--------|------------|
| `for` loop | Pattern rows, number range iteration |
| `while` loop | Menu loop, input retry |
| `range()` | Number analysis, row/column control |
| `break` | Exit loop on invalid input |
| `continue` | Skip invalid iterations |
| `pass` | Placeholder logic |
| Nested loops | Triangle pattern (rows × columns) |
| Input validation | Error messages, re-prompting |

---

## 📌 Error Handling

- Row count must be a **positive integer**
- End of range must be **greater than** start
- Invalid inputs show an **error message** and prompt again

---
