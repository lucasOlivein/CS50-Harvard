# 🏰 Knights
> In 1978, logician Raymond Smullyan published *What Is the Name of This Book?*, a book of logical puzzles. Among the puzzles in the book was a class of puzzles that Smullyan called "Knights and Knaves".

Inspired by these problems, write a program to solve Knights and Knaves puzzles.

## 🚀  Summary
This project implements a solver for classic *Knights and Knaves* logic puzzles using propositional logic and model checking. Each puzzle is translated into a formal knowledge base, and an inference algorithm is used to determine which characters are knights (truth-tellers) and which are knaves (liars).

The goal is not only to solve the puzzles, but also to demonstrate how logical reasoning can be encoded and executed programmatically using artificial intelligence techniques.

## 📄  Official Description (Adapted)

In a Knights and Knaves puzzle, the following information is given:
- Each character is either a **knight** or a **knave**
- A **knight** will always tell the truth (i.e., if a knight states a sentence, then that sentence is *true*)
- A **knave** will always lie (i.e, if a knave states a sentence, then that sentence is *false*)

### 🧭 Goal
Given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave. 

 For example, a simple puzzle with just a single character named A:

- A says “I am both a knight and a knave.”
    - We know that each character is either a knight or a knave, but not both. 
    - So, we could conclude, A must be a knave.

That puzzle was on the simpler side. With more characters and more sentences, the puzzles can get trickier! 

The task in this problem is to determine how to represent these puzzles using **propositional logic**, such that an AI running a **model-checking algorithm** could solve these puzzles for us.

### 🔍 Code Overview
- ### 🧠  `logic.py`
    The file `logic.py`, introduced in Lecture 1, defines several classes for different types of logical connectives (such as `And`, `Or`, `Not`, etc.).
     
    These connectives can be composed to build complex logical expressions. For example:

    ```
    And(Not(A), Or(B, C))
    ```
    This expression represents the logical sentence that:
    - Symbol **A is false**, and  
    - Either **B or C is true** (inclusive OR).

    Although it’s not necessary to understand the full implementation, it’s important to know that this file provides the underlying structures to represent logical knowledge.
    
- ### 🧪 *model_check* 
    The file `logic.py` also defines the function `model_check`, which performs inference using model checking.
    - It takes two inputs:
        - a **knowledge base** (a single logical sentence), and
        - a **query** (a statement to be tested).
    - If multiple statements exist, they are combined into one using `And`.
    - The function systematically evaluates all possible models.
    - It returns:
        - `True` if the knowledge base **entails** the query,
        - `False` otherwise.
    


- ### 🧩  `puzzle.py`
    In `puzzle.py`, six propositional symbols are defined:

    - `AKnight`, `AKnave`
    - `BKnight`, `BKnave`
    - `CKnight`, `CKnave`

    Each symbol represents a statement such as:
    - `"A is a knight"`
    - `"B is a knave"`

    #### 📚  Knowledge Bases 
    Four knowledge bases are declared:

    - `knowledge0`
    - `knowledge1`
    - `knowledge2`
    - `knowledge3`

    Each one corresponds to a specific puzzle (Puzzles 0–3).   
    Initially, all knowledge bases are empty — the task is to fill them with proper logical constraints.

    #### ⚙️ Program Execution

    The `main` function iterates over all puzzles and applies model checking to each one.  
    For every character, it determines whether:
    - the character must be a **knight**, or  
    - the character must be a **knave**.

    Finally, the results are printed based on what the model-checking algorithm can logically conclude.

### ⚙️  Specification

📌 Add knowledge to knowledge bases `knowledge0`, `knowledge1`, `knowledge2`, and `knowledge3` to solve the following puzzles.

#### ✅  Puzzle 0
This is the puzzle from the Background section. It contains a single character, **A**.
- A says: *"I am both a knight and a knave."*
    
#### ✅ Puzzle 1
This puzzle has two characters: **A** and **B**.  
- A says: *"We are both knaves."*
- B says nothing.

#### ✅ Puzzle 2  
This puzzle also has two characters: **A** and **B**.

- A says: *"We are the same kind."*
- B says: *"We are of different kinds."*
    
#### ✅ Puzzle 3  
This puzzle has three characters: **A**, **B**, and **C**.

- A says either *"I am a knight."* or *"I am a knave."*, but you do not know which.
- B says: *"A said 'I am a knave.' "*
- B then says: *"C is a knave."*
- C says: *"A is a knight."*

### 📜 Rules

In each puzzle:
- Every character is either a **knight** or a **knave**.
- Every sentence spoken by a **knight** is true.
- Every sentence spoken by a **knave** is false.

### ▶️ Running the Program

Once you have completed the knowledge base for a puzzle, run:

```bash
python puzzle.py
```
to see the solution produced by the model-checking algorithm.

### 💡  Hints Provided

- For each knowledge base, you should encode two types of information:
  1. The **structure of the problem itself** (i.e., the general rules of Knight and Knave puzzles), and  
  2. The **statements made by the characters**.

- Carefully consider what it means for a character to say a sentence:
  - When is that sentence true?
  - When is it false?
  - How can you formally represent this relationship using propositional logic?
    
- There are multiple ways to construct a correct knowledge base for each puzzle.  
  Aim for a representation that is:
  - a direct translation of the puzzle’s statements, and  
  - as concise and readable as possible.  


- For example, in Puzzle 0, assigning  
  `knowledge0 = AKnave`  
  would technically yield the correct result, since we can reason on our own that A must be a knave.  
  However, this defeats the purpose of the exercise — the goal is for the **AI to perform the reasoning**, not for you to encode the answer directly.

- You should not need to modify `logic.py` in any way to complete this problem.

### 🎯  Solution
| Feature | Commit |
|----------|--------|
| Puzzle 0, 1, 2 and 3 | [9c1a26f](https://github.com/lucasOlivein/CS50-Harvard/commit/9c1a26f27703609bab420d1ed54590e8a943d65f)


### 📚 Source
Based on the *Knights* project from Harvard’s CS50 AI course: [https://cs50.harvard.edu/ai/projects/1/knights/](https://cs50.harvard.edu/ai/projects/1/knights/)  
Download the distribution code from: https://cdn.cs50.net/ai/2023/x/projects/1/knights.zip  