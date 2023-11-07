"""Write a program to solve a fractional Knapsack problem using a greedy 
method."""

# class Item:
#     def __init__(self, profit, weight):
#         self.profit = profit
#         self.weight = weight

# def fractionalKnapsack(w, arr):
#     arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
#     finalValue = 0.0
#     for item in arr:
#         if w >= item.weight:
#             finalValue += item.profit
#             w -= item.weight
#         else:
#             finalValue += item.profit * (w/item.weight)
#             break
#     return finalValue

# if __name__ == "__main__":
#     n = int(input("Enter number of items-\n"))
#     arr = []
#     for i in range(n):
#         profit = int(input("Enter profit of item " + str(i + 1) + "-\n"))
#         weight = int(input("Enter weight of item " + str(i + 1) + "-\n"))
#         arr.append(Item(profit, weight))
#     w = int(input("Enter capacity of knapsack-\n"))
#     print("Maximum value in knapsack: ", fractionalKnapsack(w, arr))

# class Item:
#     def __init__(self, value, weight):
#         self.value = value
#         self.weight = weight

def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)
    finalvalue = 0.0
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        else:
            finalvalue += item.value * W / item.weight
            break
    return finalvalue

if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    max_val = fractionalKnapsack(W, arr)
    print(max_val)


