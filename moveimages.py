import re
from pathlib import Path

filename = input("Enter the filename: ")
filepath = Path(filename)

if (not filepath.is_file()):
    print("File does not exist")
    exit(1)

with open(filepath, 'r') as file:
    data = file.read()

imagematches = re.findall(r'!\[.*\]\((.*)\)', data)
folder = filepath.parent

for i, imagename in enumerate(imagematches, 1):
    imagefile = Path(folder, imagename)
    if (not imagefile.is_file()):
        print("Image file does not exist")
        continue

    newimagefile = Path("Images", f"{filepath.stem}-{i:02d}.png")
    
    imagefile.rename(newimagefile)
    data = data.replace(imagename, f"../Images/{newimagefile.name}")

with open(filepath, 'w') as file:
    file.write(data)

print("Done!")
