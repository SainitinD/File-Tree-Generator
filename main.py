import os

input_path = "C:\\Users\\geniu\\OneDrive\\Desktop\\BuzzBot\\BuzzBot"
treeignore_path = os.path.join(input_path, ".treeignore")

# Optional: Reads provided '.treeignore' to not consider certain files/folders
ignore_folders = []
if os.path.isfile(treeignore_path):
    with open(treeignore_path) as f:
        ignore_folders = f.read().split("\n")
    print("Tree Ignore FOUND! Not considering the following files/folders \n", ignore_folders)


def create_file_tree(path, last_folder=False):
    # Uncomment for debugging
    # print(path)
    
    out = ""
    files = os.listdir(path)
    files = [f for f in files if f not in ignore_folders]  # O(N*K)
    
    # Handle edge case
    if len(files) == 0:
        return out
    elif len(files) == 1:
        out += f"└── {files[0]}\n"
        return out

    for i, file_name in enumerate(files):
        # Add files/folders into file tree
        cur_path = os.path.join(path, file_name)
        if i != len(files)-1:
            out = out +  f"├── {file_name}\n"
        else:
            out += f"└── {file_name}\n"
        

        # if file is a folder, format and add contents of the folder into the file tree
        if not os.path.isfile(cur_path):
            is_last_folder = False if i != len(files)-1 else True

            folder_out = create_file_tree(cur_path, is_last_folder)
            folder_out = folder_out.split("\n")[:-1]
            for line in folder_out:
                if is_last_folder:
                    out = out + "    " + line + "\n"
                else:
                    out = out + "│   " + line + "\n"
    return out


out = create_file_tree(input_path)
with open("out.txt", "w", encoding="utf-8") as f:
    f.write(out)
print("DONE :D")