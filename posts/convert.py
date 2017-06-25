import glob
import os

stems = [os.path.splitext(p)[0] for p in glob.glob("*.txt")]
print stems

for stem in stems:
    


