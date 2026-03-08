Week 3 — Recursion and Trees
This is the week that separates programmers who think iteratively from programmers who think like engineers. Recursion is the hardest concept to learn — but once it clicks, it never un-clicks.
Before any code, one question to get your brain ready:
A folder can contain files or other folders. Those folders can contain more files or folders, and so on forever. How would you write code to count every single file no matter how deep they're nested?
Think about it — a normal loop can't do this because you don't know how deep it goes. What's your instinct on how to solve it?
How deep does it go? You don't know. It could be 2 levels. It could be 10. Could be 100. A while loop needs to know when to stop — but you don't know the depth upfront. And a dict can't tell you "go into this folder then that folder then that one" without already knowing the path.

The Real Question
What if I told you the problem solves itself with this logic:
"To count all files in a folder — count the files directly inside it, then do the same thing for each subfolder inside it."
Read that again. The function calls itself for each subfolder. That's recursion.
count_files(Documents)
    → count files in Documents directly
    → count_files(Work)          ← same function, smaller problem
        → count_files(Projects)  ← smaller again
            → count_files(2024)  ← smallest — just files, no folders
        → count files in Work
    → count_files(Personal)
        → count_files(photos)
Each call handles one folder. Then trusts the same function to handle everything inside it.

The Key Insight
Recursion works when a problem has this shape:
"This big problem is just a small version of itself, repeated."
A folder containing folders is the same problem at a smaller scale. That's the trigger for recursion.

Before We Code — One Question
In the logic above, when does the function stop calling itself?
Think about it — what kind of folder has no subfolders inside it? What's the stopping condition?
Answer that and we write the code together.
You said: "when the inside function call is satisfied or ended"
That's vague. Think more concretely. Go back to the folder example:
Documents/
    Work/
        report.pdf    ← just a file, no folders inside
    photos/
        holiday.jpg   ← just a file, no folders inside
The function stops calling itself when it reaches a folder that has no subfolders inside it — only files. There's nothing left to go deeper into. That's the stopping condition.
In recursion this is called the base case. Every recursive function has two parts:
Base case — the condition where the function stops calling itself. The simplest version of the problem that needs no further breaking down.
Recursive case — where the function calls itself on a smaller version of the problem.

The Folder Counter — In Plain English
def count_files(folder):

    BASE CASE:
    if folder has no subfolders:
        return number of files directly in it

    RECURSIVE CASE:
    total = files directly in this folder
    for each subfolder:
        total += count_files(subfolder)  ← calls itself
    return total

Your Exercise
Before we write real file system code, let's practice recursion on something simpler — a nested dictionary that represents a folder structure:
pythonfolder = {
    "files": ["notes.txt", "photo.jpg"],
    "subfolders": [
        {
            "files": ["report.pdf"],
            "subfolders": []
        },
        {
            "files": ["music.mp3", "video.mp4"],
            "subfolders": [
                {
                    "files": ["data.csv"],
                    "subfolders": []
                }
            ]
        }
    ]
}
Write a recursive function count_files(folder) that counts every file at every level.
The answer should be 7 — notes.txt, photo.jpg, report.pdf, music.mp3, video.mp4, data.csv = 6... count them yourself first to verify.
Two hints:
Hint 1 — base case is when subfolders is empty — just return len(folder["files"])
Hint 2 — recursive case adds len(folder["files"]) plus calls itself on each subfolder
Write it and paste back. This is the concept that unlocks trees, graphs, and everything in Week 

if not folder["subfolders"]:
    return len(folder["files"])      # ✅ base case — no subfolders, count files

total_files = len(folder["files"])   # ✅ count files at current level
for subfolder in folder["subfolders"]:
    total_files += count_files(subfolder)  # ✅ recursive case — trust the function
return total_files                   # ✅ return total
```

And the answer is 6 — notes.txt, photo.jpg, report.pdf, music.mp3, video.mp4, data.csv.

---

## What Just Happened in Your Code

When you called `count_files(folder)` Python built this call stack:
```
count_files(Documents)        → 2 files
  count_files(Work)           → 1 file
  count_files(Personal)       → 2 files
    count_files(nested)       → 1 file
                              = 6 total
```

Each call solved a smaller version of the same problem. Each one trusted the function below it to handle the rest. That's recursion working exactly as designed.

---

## The Two Rules of Recursion — Memorise These

**Rule 1 — Always have a base case.** The condition that stops the function calling itself. Without it you get infinite recursion and Python crashes.

**Rule 2 — Every recursive call must move toward the base case.** Each call works on something smaller than the previous one. Subfolders are always smaller than the parent folder.

---

## Now The Real Challenge — Fibonacci

This is the classic recursion problem every programmer learns. It also teaches you why recursion can be slow — and how to fix it.

The Fibonacci sequence: `1, 1, 2, 3, 5, 8, 13, 21...`

Each number is the sum of the two before it.
```
fib(1) = 1
fib(2) = 1
fib(3) = fib(2) + fib(1) = 2
fib(4) = fib(3) + fib(2) = 3
fib(5) = fib(4) + fib(3) = 5