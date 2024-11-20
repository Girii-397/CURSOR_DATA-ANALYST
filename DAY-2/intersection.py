from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Create two sample sets
set1 = set(['A', 'B', 'C', 'D'])
set2 = set(['C', 'D', 'E', 'F'])

# Create and display the Venn diagram
venn2([set1, set2], set_labels=('Set 1', 'Set 2'))
plt.title('Intersection of Two Sets')

# Show the plot
plt.show()

# Print the intersection
intersection = set1.intersection(set2)
print("Intersection of sets:", intersection)