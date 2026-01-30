# Question 8: Log File Analyzer 
# Write a program that analyzes server log files containing entries like: timestamp,ip_address,status_code,response_time. Generate statistics: total requests, unique IPs, status code distribution, average response time per IP, and identify problematic IPs (high error rates).

# Rules:

# You can use file operations: open(), read(), write(), close()
# Must use loops, dictionaries, sets, lists, and functions
# Create functions for parsing and analysis
# Handle edge cases (malformed entries, empty file)
# Write comprehensive report to output file

# Test Cases:

# Test Case 1:
# Input:
# 2024-01-01 10:00:00,192.168.1.1,200,150
# 2024-01-01 10:01:00,192.168.1.1,200,200
# 2024-01-01 10:02:00,192.168.1.2,404,50
# Output:
# Total Requests: 3
# Unique IPs: 2
# Status Distribution: {200: 2, 404: 1}
# Average Response Time:
# 192.168.1.1: 175ms
# 192.168.1.2: 50ms
# Problematic IPs: 192.168.1.2 (33.33% errors)

# Test Case 2:
# Input:
# 2024-01-01 10:00:00,10.0.0.1,500,1000
# 2024-01-01 10:01:00,10.0.0.1,500,1200
# Output:
# Total Requests: 2
# Unique IPs: 1
# Status Distribution: {500: 2}
# Average Response Time:
# 10.0.0.1: 1100ms
# Problematic IPs: 10.0.0.1 (100% errors)

# Test Case 3:
# Input:
# 2024-01-01 10:00:00,172.16.0.1,200,100
# Output:
# Total Requests: 1
# Unique IPs: 1
# Status Distribution: {200: 1}
# Average Response Time:
# 172.16.0.1: 100ms
# Problematic IPs: None

def read_data(file_name: str) -> list:
    '''
    read data and creat list of data
    
    Args:
        file_name (str): name of the input file
    Returns:
        list: list of tuples with name and marks
    '''
    ip_list = []
    status = {}
    problematic_reqs = []

    with open(file_name, 'r') as file:
        
        for line in file:
            data_size = 0
            #calculating length of the line
            for char in line:
                data_size += 1

            index = 0
            word = ''
            list_words = []
            count_words = 0
            for chars in line:
                #add all words in the list
                if chars == ',' or chars == '\n' or index == data_size-1:
                    if index == data_size-1 and chars != " " and chars != "\n":
                        word += chars
                
                    if word != '':
                        list_words += [word,]
                        count_words += 1
                        word = ''
                else:
                    if chars != " ":
                        word += chars
                index += 1

            #check the line has 4 word if not than data is incomplete
            if count_words != 4 and count_words != 0:
                raise ValueError()
            
            # for words in list_words:
            if count_words == 0:
                continue

            #storing ip with avg response time
            flag = False
            index = 0
            for ips in ip_list:
                if list_words[1] == ips[0]:
                    avg = (float(list_words[3]) + ips[1]) / 2
                    ip_list[index] = tuple((list_words[1],avg))
                    flag = True
                    break
                index += 1
            if flag != True:
                ip_list += [tuple((list_words[1],float(list_words[3])))]

            #storing status code count
            flag = False
            for codes in status:
                if codes == list_words[2]:
                    flag = True
                    break
            if flag == True:
                temp = status[list_words[2]] + 1
                status[list_words[2]] = temp
            else:
                status[list_words[2]] = 1

            #storing problematic ip with status code
            code = list_words[2][0]
            if code == '4' or code == '5':
                index = 0
                flag = False
                for ips in problematic_reqs:
                    if ips[0] == list_words[1]:
                        count = ips[1]+1
                        problematic_reqs[index] = tuple((list_words[1],count))
                        flag = True
                        break
                    index += 1
                if flag == False:
                    problematic_reqs += [tuple((list_words[1],1))]

        ans_dict = {}
        if ip_list != []:
            ans_dict = {'ips': ip_list,
                        'status_count' : status,
                        'problematic_req' : problematic_reqs}
        
        return ans_dict

def analyze_file_data(input_file_name: str, output_file_name: str) -> str:
    '''
    analyze log file data and write in the output file
    
    Args:
        input_file_name (str): name of the input file
        output_file_name (str): name of the output file
    Returns:
        str: returns analyzed data 
    '''
    try:
        #validating file format
        flag = False
        check_word1 = ''
        for chars in input_file_name:
            if flag == True:
                check_word1 += chars
            if chars == '.':
                flag = True
        
        flag = False
        check_word2 = ''
        for chars in output_file_name:
            if flag == True:
                check_word2 += chars
            if chars == '.':
                flag = True
        
        if check_word1 != 'txt' and check_word2 != 'txt':
            raise FileNotFoundError()
        
        data_dict = read_data(input_file_name)
        if data_dict == {}:
            return "There is no content in file."

        output = ''
        #counting total requests
        total_requests = 0
        data = data_dict['status_count']
        for req_count in data:
            total_requests += data[req_count]

        output += f"Total Requests: {total_requests}\n"

        #counting unique requests
        count_unique_req = 0
        ans_data = ''
        data = data_dict['ips']
        for ips in data:
            count_unique_req += 1
            temp_tuple = ips
            ans_data += f"\n{temp_tuple[0]} : {temp_tuple[1]}"

        output += f"Unique IPs: {count_unique_req}\n"
        output += f"Status Distribution: {data_dict['status_count']}\n"
        output += f"Average Response Time:{ans_data}"
        output += f"\nProblematic IPs: "

        #calculating persentage of error and adding in output with ip
        data = data_dict['problematic_req']
        count = 1
        for reqs in data:
            if count == 1:
                output += f"{reqs[0]} ({(reqs[1]/total_requests)*100 : 0.2f}%)"
            else:
                output += f", {reqs[0]} ({(reqs[1]/total_requests)*100 : 0.2f}%)"
            count += 1

        with open(output_file_name, 'w') as file:
            file.write(output)

        return output
    
    except FileNotFoundError as e:
        print("File Not Found or the given file name is incorrect, It should be a text file.")
    except OSError as e:
        print("Given File name is not defined")
    except TypeError as e:
        print("Invalid input data. Please enter valid data types in input file.")
    except ValueError as e:
        print("Invalid content structure in input file, Please enter valid data in input file.")

def main():
    try:
        flag = False
        while flag == False:
            input_file_name = input("Enter input file name: ")
            try:
                with open(input_file_name,'r') as f:
                    flag = True
            except FileNotFoundError:
                print("File not found Enter name again")

        flag = False
        output_file_name = ''
        while flag == False:
            output_file_name = input("Enter output file name: ")
            try:
                with open(input_file_name,'r') as f:
                    flag = True
            except FileNotFoundError:
                print("File not found Enter name again")

        ans = analyze_file_data(input_file_name, output_file_name)
        print(ans)
    except OSError as e:
        print("Given File name is not defined")
    except TypeError as e:
        print("Invalid input data Type.")
    except ValueError as e:
        print("Invalid input data.")

if __name__ == "__main__":
    main()