import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from matplotlib_venn import venn2_circles

# Create the Venn diagram
venn2(subsets=(1, 0, 0), set_labels=('A', 'U'))
venn2_circles(subsets=(1, 0, 0))

# Add title
plt.title("Complement of Set A (A')")

# Customize colors
# Get the current axes
ax = plt.gca()
# Color the complement (outside of A) in red
for patch in ax.patches:
    if patch.get_facecolor() == (1, 1, 1, 1):  # if white
        patch.set_facecolor('red')
        patch.set_alpha(0.3)

# Add A' label to the complement region
plt.text(0.5, 0.5, "A'", ha='center', va='center', color='red')

plt.show()