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

### Menu-Driven Interface
| Option | Action |
|--------|--------|
| `1` | Generate Pattern (Right-angled triangle) |
| `2` | Analyze a range of numbers |
| `3` | Exit the program |

## ▶ Demo Video

<a href="https://drive.google.com/file/d/1qXj0XwXhMrAhzs6iRmYEFLChqDCnXhsq/view?usp=drive_link" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/▶-Watch%20Demo%20Video-181717?style=for-the-badge&logo=github&logoColor=white" alt="Watch Demo Video" />
</a>

## Program Flowchart
<img width="2541" height="3408" alt="logic_box_flowchart (1)" src="https://github.com/user-attachments/assets/87ed27c1-ea2a-44fd-8b04-22c0810237b8" />

## Output of Code
<img width="730" height="883" alt="image" src="https://github.com/user-attachments/assets/69ff50b8-3aa0-4602-a624-7a9811f1d931" /> 
<img width="533" height="205" alt="image" src="https://github.com/user-attachments/assets/03745d97-d76e-4818-b6d3-7eccc5924171" />

## Concepts Used

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
