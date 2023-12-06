import os
# import argparse

# # Define the argument parser
# parser = argparse.ArgumentParser()
# parser.add_argument("input_path", metavar="input_path", type=str, help="Enter your input path")
# parser.add_argument("--o", metavar="output_path", type=str, help="(Optional) Enter your output path. Default is the input path")
# parser.add_argument("--tg", metavar="tree_ignore", type=str, help="(Optional) Enter your path for .treeignore. Default is the input path")

# # Parse arguments
# args = parser.parse_args()
# input_path = args.input_path
# output_path = args.o if args.o else args.input_path
# tree_ignore_path = args.tg if args.tg else args.input_path

# print(f"Received input path: {input_path}")

# if args.o:
#     print(f"Received output path: {output_path}")
# else:
#     print(f"Not received output path. Using input path: {input_path}")

# if args.tg:
#     print(f"Received tree ignore path: {tree_ignore_path}")
# else:
#     print(f"Not received tree ignore path. Using input path: {input_path}")

# treeignore_path = os.path.join(tree_ignore_path, ".treeignore")

# # Optional: Reads provided '.treeignore' to not consider certain files/folders
# ignore_folders = []
# if os.path.isfile(treeignore_path):
#     with open(treeignore_path) as f:
#         ignore_folders = f.read().split("\n")
#     print("Tree Ignore FOUND! Not considering the following files/folders \n", ignore_folders)
# else:
#     print("Tree Ignore NOT Found. Continuing the process...")


class FTree():
    def __init__(self, input_path, out_path=None, treeignore_path=None):
        self.input_path = input_path
        print(f"Received input path: {input_path}")

        if out_path:
            print(f"Received output path: {out_path}")
        else:
            print(f"Not received output path. Using input path: {input_path}")

        if treeignore_path:
            print(f"Received tree ignore path: {treeignore_path}")
        else:
            print(f"Not received tree ignore path. Using input path: {input_path}")
        
        self.out_path = out_path if out_path else input_path
        self.treeignore_path = treeignore_path if treeignore_path else input_path


    def create_file_tree(self, path, last_folder=False):
        """
        Creates a file tree when given a path.
        
        Args:
                path (string): A string containing the path of the folder
                last_folder (boolean): A boolean indicating if the path given is the last folder in the tree.
                                    Intended to be used by sub-folders so don't touch it unless you have to.
                                    Used to help formatting. 
            Returns:
                out (string): A string containing the file tree of the given path 
        """
        # Uncomment for debugging
        # print(path)
        
        out = ""
        files = os.listdir(path)
        files = [f for f in files if f not in ignore_folders]  # O(N*K)
        
        # Handle edge case
        if len(files) == 0:
            return out
        elif len(files) == 1:
            if os.path.isfile(files[0]):
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
        
        print("Starting the process...")
        out = create_file_tree(input_path)
        with open(os.path.join(output_path, "out.txt"), "w", encoding="utf-8") as f:
            f.write(out)
        print("Successfully Completed :D")
        print(f"Output stored at... {os.path.join(output_path, 'out.txt')}")
        
        return out