# Supa File Tree

A project that when given a folder path, generates a tree of all the files inside it.

I created this using pure python and its base packages. I made it because I couldn't find any python packages that did this. The project is published on pypi on 12/6/2023. I intend to fix issues if they rise or any feature requests so feel free to add them here :D

Download the package using the following command `pip install SupaFileTree`

See the pypi file [here](https://pypi.org/project/SupaFileTree/)

# Project Output

I ran the program on a local copy of my [**tic-tac-toe**](https://github.com/SainitinD/Tic-Tac-Toe-with-GUI) project. Here is the generated output

```
├── assests
│   ├── null
│   │   └── null.png
│   ├── O_Assets
│   │   ├── O.png
│   │   ├── O_diag.png
│   │   ├── O_diag2.png
│   │   ├── O_hor.png
│   │   ├── O_hor2.png
│   │   ├── O_vert.png
│   │   └── O_vert2.png
│   ├── sounds
│   │   ├── Button_Sound.wav
│   │   └── license.txt
│   └── X_Assets
│       ├── X.png
│       ├── X_diag.png
│       ├── X_diag2.png
│       ├── X_hor.png
│       └── X_vert.png
├── ReadMe.txt
└── tic_tac_toe_GUI.py
```

# Run this project and get output in input path

Let's say you want the file tree of \_`C:\Users\otherfile\project`. So create a `test.py` or a python file, then write and run the following code

```
input_path = "C:\\Users\\otherfile\\project"

ftree = FileTree(input_path=input_path)
ftree.create()
```

This will create a file tree and store the output at \_`C:\Users\otherfile\project\out.txt`. Alternatively, you can also modify the last line to have a variable take the result of `ftree.create()` to capute the output like so

```
...
output = ftree.create()
```

# Run this project with a .treeignore file

Let's say you don't want certain files/folders to be shown in the file tree. Then you can create a `.treeignore` file and add it either in the input path or anywhere accessabile by your `test.py` file. For convience, I have mine where I'm running `test.py` file.

The `.treeignore` file works essentially like a .gitignore except you need to put subfolders as their own. So instead of `src/node_modules` you would put `node_modules` in the tree ignore.

```
input_path = "C:\\Users\\otherfile\\project"
tree_ignore_path = ".//"

ftree = FileTree(input_path=input_path, tree_ignore_path=tree_ignore_path)
ftree.create()  # Generates output and stores it at `C:\Users\otherfile\project\out.txt`
```

# Run the file and store the output elsewhere

You can also run the file and store the output in another location. For convience, I storing mine where I'm running `test.py` file.

```
input_path = "C:\\Users\\otherfile\\project"
out_path = ".//"

ftree = FileTree(input_path=input_path, out_path=out_path)
ftree.create()  # Generates output and stores it at `C:\Users\otherfile\project\out.txt`
```

# Debug while running the file

```
input_path = "C:\\Users\\otherfile\\project"

ftree = FileTree(input_path=input_path, debug=True)
ftree.create()  # Generates output and stores it at `C:\Users\otherfile\project\out.txt`
```

# Summary of FileTree variables

```
input_path is (REQUIRED)
out_path is (OPTIONAL) (Defaults to input path)
tree_ignore_path is (OPTIONAL)  (Defaults to input path)
```

# How to not include some files in tree

Create `.treeignore` and add the file/folders you don't want to see in the tree.

The `.treeignore` file works essentially like a .gitignore except you need to put subfolders as their own. So instead of `src/node_modules` you would put `node_modules` in the tree ignore.

Example `.treeignore` file

```
.git
.gitignore
```
