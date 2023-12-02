# File-Tree-Generator

A project that when given a folder path, generates a tree of all the files inside it. I created this using pure python and its base packages.

I made it because I couldn't find any python packages that did this. I intend to publish it into pip soon (whenever their website allows me to)

# Run this project

Assuming the project is being run in _C:\Users\sample_, run it using the following ...

`python3 main.py "C:\Users\sample\SAMPLEPROJECT" --tg ".\" --o ".\"`

Where

```
"C:\Users\sample\SAMPLEPROJECT" is the input path (REQUIRED)

--tg ".\" refers to the location of the .treeignore file (OPTIONAL)
--o ".\" refers to the location of where you want to see the output file (OPTIONAL)
```

# How to not include some files in tree

Create `.treeignore` and add the file/folders you don't want to see in the tree
Then use `--tg PATH` and add the _PATH_ when running the file

Example `.treeignore` file

```
.git
.gitignore
```
