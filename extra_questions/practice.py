temp = {
    "Consumer Packaged Goods": {
        "Edible": {
            "Beverages": {
                "Coffee & Tea": {
                    "Coffee Filters": 80,
                    "Tea": {
                        "Bags/loose": 99
                    }
                }
            }
        }
    }
}
l = ["Consumer Packaged Goods", "Edible"]
for i in range(2):
    temp_dict = temp
    for j in l:
        if j in temp_dict:
            temp_dict = temp_dict[j]
        else:
            break
    temp_dict['Beverages'] = 45
    print(temp)
    break