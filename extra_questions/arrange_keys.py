import json

def arrange_key(input_dict: dict) -> dict:
    '''
    arranges key in levels

    Args:
        input_dict (dict): input dictionary
    Returns:
        dict: output dictionary
    '''
    output_dict = {}
    
    for key in input_dict:

        multiple_keys = key.split(" - ")
        temp_dict = output_dict

        index = 0
        last_key = ''
        for mkey in multiple_keys:

            if mkey in temp_dict:
                temp_dict = temp_dict[mkey]
                last_key = mkey
            else:
                value = input_dict[key]
                rev_key = multiple_keys[index:][::-1]

                last_key = multiple_keys[index-1]
                for rkeys in rev_key:
                    temp = {}
                    temp[rkeys] = value
                    value = temp
                
                temp_dict.update(value)
                break

            index += 1
                    
    return json.dumps(output_dict,indent=4)

def main():
    input =  {
    "Apps - Health and Fitness Apps": 50,
    "Apps - Lifestyle Apps": 20,
    "Arts and Entertainment - Experiences and Events - Concerts": 45,
    "Arts and Entertainment - Experiences and Events - Theatre and Musicals": 75,
    "Consumer Packaged Goods - Edible - Beverages - Coffee & Tea - Coffee Filters": 80,
    "Consumer Packaged Goods - Edible - Beverages - Coffee & Tea - Tea - Bags/loose": 99,
    "Consumer Packaged Goods - Non-edible - Household Appliances - Air Conditioners": 95,
    "Consumer Packaged Goods - Non-edible - Household Appliances - Air Purifiers": 77,
    "Consumer Packaged Goods - Non-edible - Household Appliances - Blenders": 67,
    "Consumer Packaged Goods - Non-edible - Beauty - Hair Care - Home Permanent/Relaxer Kits": 85,
    "Consumer Packaged Goods - Non-edible - Beauty - Personal Cleansing - Bath Products": 45,
    "Consumer Packaged Goods - Non-edible - Beauty - Personal Cleansing - Bath/Body Scrubbers/Massagers": 35,
    "Consumer Packaged Goods - Non-edible - General Merchandise - Miscellaneous General Merch - Firelog/Firestarter/Firewood": 75,
    "Consumer Packaged Goods - Non-edible - Beauty - Hair Care - Hair Conditioner": 61
    }


    ans = arrange_key(input)
    print(ans)

if __name__ == "__main__":
    main()