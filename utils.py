import os


def list_tex_files(path):
    tex_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".tex"):
                # get the relative path to the file
                tex_files.append(os.path.relpath(os.path.join(root, file), path))
    return tex_files

