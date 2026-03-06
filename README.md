# Unit Test Assignment

This repository contains Python solutions to several HackerRank problems. The project utilizes `uv` for dependency management, test execution, and code coverage reporting.

## Getting Started

### 1. Install `uv`
To run this project, you first need to install `uv` (an extremely fast Python package and project manager). Follow the official documentation [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/)

### 2. Run the Main Application
There is an interactive command-line application that allows you to easily execute all of the assignment algorithms below. Run it using `uv`:
```bash
uv run main.py
```

---

## Assignment Algorithms

The core logic for this assignment is implemented in various modules located inside the `_6810110042` directory. Here are the highlighted functions along with examples of their expected test cases:

*   **[Funny String](_6810110042/funny_string.py)**
    Determines whether a string is "Funny" or "Not Funny" by calculating the absolute differences between the ASCII values of consecutive characters and comparing them to those of its reversed version.
    *   **Example:**
        *   Input: `s = "acxz"`
        *   Output: `Funny`

*   **[Alternating Characters](_6810110042/alternating_characters.py)**
    Calculates the minimum number of character deletions required to ensure that there are no consecutive matching characters in a sequence of 'A' and 'B'.
    *   **Example:**
        *   Input: `s = "AABAAB"`
        *   Output: `2` (Drop the alternating consecutive A's to leave "ABAB")

*   **[Caesar Cipher](_6810110042/caesar_cipher.py)**
    Encrypts a string by shifting each letter by a specified numeric amount down the alphabet, wrapping around the alphabet at the end, and meticulously preserving character types and letter casing.
    *   **Example:**
        *   Input: `s = "middle-Outz", k = 2`
        *   Output: `"okffng-Qwvb"`

*   **[Two Characters](_6810110042/two_characters.py)**
    Finds the length of the longest string that can be formed by strategically deleting all occurrences of all but two distinct characters from the original string, optimizing so that the remaining two characters strictly alternate.
    *   **Example:**
        *   Input: `s = "beabeefeab"`
        *   Output: `5` (Leaves "babab")

*   **[Grid Challenge](_6810110042/grid_challenge.py)**
    Given a grid of characters, the function evaluates whether or not it is possible to rearrange grid elements within their respective rows so that all resultant columns will be perfectly sorted in ascending alphabetical order.
    *   **Example:**
        *   Input: `grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]`
        *   Output: `YES`

---

## Project Structure

*   `main.py`: Interactive command-line executable. Run this to test out the logic of the HackerRank functions through simple CLI prompts.
*   `_6810110042/`: Contains the primary function implementations.
*   `tests/`: Comprehensive test-coverage suite asserting behaviors and edge cases for the modules in `_6810110042`.
*   `.vscode/tasks.json`: Provides integrated Visual Studio Code task runner definitions.

## Running Tests with `uv` in VS Code

Testing within this project is strictly managed by `uv` and is mapped directly to seamless Visual Studio Code shell execution commands.

The process includes gathering assertions via `nose2` and building an HTML-based test coverage report:

### Quick Execution
Instead of manually typing long CLI arguments, you can leverage native vs-code tasks defined in `.vscode/tasks.json`.

1. Press `Ctrl + Shift + B` (or select `Terminal > Run Build Task...` from the application toolbar).
2. Because **"Run Tests & Coverage"** is set as the default build task (`isDefault: true`), this will automatically sequence the tasks for execution.

This command will:
1.  **Execute `uv run coverage run -m nose2 -v`**: Run all the tests displaying a verbose output.
2.  **Execute `uv run coverage html`**: Seamlessly compile an interactive code coverage overview within a generated `htmlcov/` directory.

### Running Manually

If you prefer to test via terminal directly, use:

```bash
uv run coverage run -m nose2 -v
uv run coverage html
```
Then, you can open `htmlcov/index.html` in your browser to inspect test coverage analytics.

---

<div align="center">

## Author

### **Jirakorn Sukmee** [psu6810110042](https://github.com/psu6810110042)
Student ID: `6810110042`
<br>
*Department of Computer Engineering*
<br>
**Faculty of Engineering**, Prince of Songkla University
</div>
