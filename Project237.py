import os

source = "Project.txt"

destination = "renamed.txt"

os.rename(source, destination)
print("renaming successfully completed!")