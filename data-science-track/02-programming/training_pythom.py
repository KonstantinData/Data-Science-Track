import matplotlib.pyplot as plt
import numpy as np

# Create a Venn diagram with the correct regions highlighted
from matplotlib_venn import venn2

# Define the subsets based on the provided set information
subset_sizes = {'10': 2, '01': 2, '11': 1}  # Size representation of A, B, and their intersection

# Create the figure
fig, ax = plt.subplots(figsize=(6,4))
v = venn2(subsets=subset_sizes, set_labels=('A', 'B'))

# Highlight the areas:
# - Outside A∪B (A complement union B complement) -> this should be shaded (Only background outside circles)
# - A∩B should remain visible (only middle part)

# Change colors
for area in ['10', '01']:  # These represent A only and B only, which we want to remove
    v.get_label_by_id(area).set_text('')
    v.get_patch_by_id(area).set_color('grey')

# Color the background green to represent A^c ∪ B^c
ax.set_facecolor("lightgreen")

# Keep intersection (A∩B) visible
v.get_patch_by_id('11').set_color('lightgrey')

# Add a title to indicate the desired region
plt.title("Highlighted: A∩B (gray) and A^c ∪ B^c (green background)")

# Show the diagram
plt.show()
