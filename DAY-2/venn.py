from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Create three sample sets
set_a = {'apple', 'banana', 'orange', 'grape'}
set_b = {'orange', 'grape', 'kiwi', 'mango'}

# Create and display the Venn diagram
venn2([set_a, set_b], set_labels=('Fruits A', 'Fruits B'))
plt.title('Venn Diagram of Fruit Sets')

# Show the plot
plt.show()

# Calculate and print set operations
union = set_a.union(set_b)
intersection = set_a.intersection(set_b)
diff_a = set_a - set_b
diff_b = set_b - set_a

print("Union of sets:", union)
print("Intersection of sets:", intersection)
print("Elements unique to Set A:", diff_a)
print("Elements unique to Set B:", diff_b)
