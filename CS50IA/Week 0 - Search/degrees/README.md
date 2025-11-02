This README is available in [Portuguese](README.pt-BR.md).

# Degrees
According to the *Six Degrees of Kevin Bacon* game, anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.

## Problem Description
In this problem, we’re interested in finding the shortest path between any two actors by choosing a sequence of movies that connects them. For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both starring in “Apollo 13.”

We can frame this as a search problem: 

- **States** are people. 
- **Actions** are movies, which take us from one actor to another (it’s true that a movie could take us to multiple different actors, but that’s okay for this problem). 
- The **initial state** and **goal state** are defined by the two people we’re trying to connect. 

By using **breadth-first search**, we can find the shortest path from one actor to another.


## Dataset Overview
The distribution code contains two sets of CSV data files: `large` and  `small` directory. Each contains files with the same names, and the same structure, but small is a much smaller dataset for ease of testing and experimentation.

Each dataset consists of three CSV files:
- `people.csv`: Each person has a unique `id`, a `name`, and `birth year`.
- `movies.csv`: Each movie has an `id`, `title`, and `year`.
- `stars.csv`: Each row links a `person_id` to a `movie_id`.

## Code Overview

Next, let’s look at `degrees.py`. At the top, several data structures are defined to store information from the CSV files. 
- `names`: maps names to a set of IDs
- `people`: maps each person’s ID to a dictionary of info
- `movies`: maps movie IDs to info and cast

The `load_data` function loads data from the CSV files into these data structures.

The `main` function in this program first loads data into memory (the directory from which the data is loaded can be specified by a command-line argument). Then, the function prompts the user to type in two names. 
The `person_id_for_name` function resolve these names by retrieving the ID for any person (and handles prompting the user to clarify, in the event that multiple people have the same name).

Once both IDs are found, the `shortest_path` function is called to compute the shortest connection between them using movie links. The result is then printed as a sequence of steps.

However, the `shortest_path` function is left unimplemented. That’s where you come in!

## Specification

Complete the implementation of the `shortest_path(source, target)` function such that it returns the shortest path from the person with ID source to the person with the ID target.

- Assuming there is a path from the source to the target, your function should return a list, where each list item is the next `(movie_id, person_id)` pair in the path from the source to the target. Each pair should be a tuple of two strings.
    - For example, if the return value of shortest_path were `[(1, 2), (3, 4)]`, that would means:
        - `Source` starred in movie `1` with person `2` 
        - Person `2` starred in movie `3` with person `4`  
        - Person `4` is the target.

- If there are multiple shortest paths, your function can return any of them.
- If there is no possible path between two actors, your function should return None.

You may call the `neighbors_for_person(person_id)` function, which returns a set of `(movie_id, person_id)` pairs for all people who starred in a movie with a given person.

## Hints
- While the implementation of search in lecture checks for a goal when a node is popped off the frontier, you can improve the efficiency of your search by checking for a goal as nodes are added to the frontier: if you detect a goal node, no need to add it to the frontier, you can simply return the solution immediately.
- You’re welcome to borrow and adapt any code from the lecture examples. We’ve already provided you with a file `util.py` that contains the lecture implementations for `Node`, `StackFrontier`, and `QueueFrontier`, which you’re welcome to use (and modify if you’d like).

## Source
This README was based on the documentation of the *Degrees* project from the Harvard AI course, available at: [https://cs50.harvard.edu/ai/2024/projects/0/degrees/](https://cs50.harvard.edu/ai/2024/projects/0/degrees/).
