number_items = int(input("Enter the number of items:"))
items = []
for k in range(number_items):
    print(f"\nitem{k + 1}:")
    weight = int(input("Enter the weight:"))
    value = int(input("Enter the value:"))
    items.append((weight, value))

max_item = int(input("Enter the max item:"))


def knapsack(item, max_i):
    number = len(item)
    dp = [[0] * (max_i + 1) for _ in range(number + 1)]
    for i in range(1, number + 1):
        weight_i = item[i - 1][0]
        value_i = item[i - 1][1]
        for w in range(1, max_i + 1):
            if weight_i > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight_i] + value_i)
        w = max_i
        selected_item = []
        for j in range(number, 0, -1):
            if dp[j][w] != dp[j - 1][w]:
                selected_item.append(j)
                w -= item[j - 1][0]

        return dp[number][max_i], selected_item[::-1]


max_item, selected = knapsack(items, max_item)
print(f"max value:{max_item}")
print("Selected item:")
for ite in selected:
    print(f"Item{ite}  (weight:{items[ite][0]})  (value:{items[ite][1]})")
