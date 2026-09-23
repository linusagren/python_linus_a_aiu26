# Accuracy: TP+TN/TP+TN+FP+FN
# TP: True Positive
# TN: True Negative
# FP: False Positive
# FN: False Negative

TP = 2
TN = 985
FP = 2
FN = 11

accuracy = (TP + TN) / (TP+TN+FP+FN)
error_rate = round(1 - accuracy, 3)

print(f"Overall model accuracy: {accuracy * 100}%")
print(f"Overall error rate: {error_rate * 100}%")
print()
# Overall success rate of 98.7% and an overall error rate of 1.3%.

# Calculate using only fires that happened
print(f"Correctly identified fires: {round(TP/(TP+FN) * 100, 2)}%")
print(f"Incorrectly identified fires: {round(FN/(TP+FN) * 100, 2)}%")

# Successfully identified fires: ~15.38%, Missed fires: ~84.62% of them.

"""Concluson:
The model reports an overall success rate of 98.7% and an error rate of 1.3%.
On paper this looks good, until you look at the dataset and start isolating it.
The dataset is imbalanced. It has much more negative cases (no fire) than positive cases (fire)
which may suggest the model isn't as capable of detecting real fires.

Additionally, once you isolate the dataset from the true negatives, we can see that the model has 
correctly identified no more than 15.38% of the actual real fires, missing a staggering
84.62% of them.

This immediately tells me that this model is very bad and unreliable."""