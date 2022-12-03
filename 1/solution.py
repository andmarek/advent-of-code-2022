with open('data', 'r') as f:
    food_collections = f.read().split("\n\n")
    highest = 0
    sum_list = []
    for food_collection in food_collections:
        food = food_collection.split("\n")

        for i in range(len(food)):
            food[i] = int(food[i])

        sum_food = sum(food)
        sum_list.append(sum_food)

    print(sum_list)
    sorted_sum_list = sorted(sum_list, key=int, reverse=True)
    print(sorted_sum_list)
    print(sorted_sum_list[0] + sorted_sum_list[1] + sorted_sum_list[2])