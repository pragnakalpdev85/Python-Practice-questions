import os

def validate_filename_input(file_name: str) -> bool:
    flag = False
    ext = ""

    for ch in file_name:
        if flag:
            ext += ch
        if ch == '.':
            flag = True

    if ext != "txt":
        print("File format is incorrect, Enter file name again")
        return False

    if not os.path.exists(file_name):
        print("File does not exist, Enter file name again")
        return False

    return True


def character_to_uppercase(character: str) -> str:
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"

    index = 0
    for ch in lower:
        if ch == character:
            return upper[index]
        index += 1

    return character


def character_to_lowercase(character: str) -> str:
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"

    index = 0
    for ch in upper:
        if ch == character:
            return lower[index]
        index += 1

    return character


def remove_extra_spaces(file_data: str) -> str:
    ans = ""
    prev_space = False

    for ch in file_data:
        if ch == ' ':
            if not prev_space:
                ans += ch
            prev_space = True
        else:
            ans += ch
            prev_space = False

    # remove leading and trailing spaces manually
    start = 0
    end = 0
    size = 0

    for _ in ans:
        size += 1

    while start < size and ans[start] == ' ':
        start += 1

    end = size - 1
    while end >= 0 and ans[end] == ' ':
        end -= 1

    final = ""
    index = start
    while index <= end:
        final += ans[index]
        index += 1

    return final


def format_punctuation_spacing(file_data: str) -> str:
    ans = ""
    index = 0
    size = 0

    for _ in file_data:
        size += 1

    while index < size:
        ch = file_data[index]

        if ch == '.' or ch == ',' or ch == '?' or ch == '!' or ch == ';' or ch == ':':
            ans += ch
            if index + 1 < size and file_data[index + 1] != ' ':
                ans += ' '
        else:
            ans += ch

        index += 1

    return ans


def capitalize_first_letter(file_data: str) -> str:
    ans = ""
    capitalize = True

    for ch in file_data:
        if capitalize and ch >= 'a' and ch <= 'z':
            ans += character_to_uppercase(ch)
            capitalize = False
        else:
            ans += ch

        if ch == '.' or ch == '?' or ch == '!':
            capitalize = True
        elif ch != ' ':
            capitalize = False

    return ans


def break_long_lines(file_data: str) -> str:
    ans = ""
    count = 0
    last_space_index = -1
    index = 0

    for ch in file_data:
        ans += ch
        count += 1

        if ch == ' ':
            last_space_index = index

        if count > 80 and last_space_index != -1:
            new_ans = ""
            i = 0
            for c in ans:
                if i == last_space_index:
                    new_ans += '\n'
                else:
                    new_ans += c
                i += 1

            ans = new_ans
            count = 0
            last_space_index = -1

        index += 1

    return ans


def is_blank_line(line: str) -> bool:
    for ch in line:
        if ch != ' ' and ch != '\n':
            return False
    return True


def formate_beautify_text(input_file_name: str, output_file_name: str) -> str:
    try:
        data = ""

        with open(input_file_name, 'r') as file:
            for line in file:
                if is_blank_line(line):
                    continue

                line = remove_extra_spaces(line)
                line = format_punctuation_spacing(line)
                line = capitalize_first_letter(line)
                line = break_long_lines(line)

                data += line + "\n"

        # safely remove last newline
        size = 0
        for _ in data:
            size += 1

        final = ""
        if size > 0:
            index = 0
            for ch in data:
                if index != size - 1:
                    final += ch
                index += 1

        with open(output_file_name, 'w') as file:
            file.write(final)

        return final

    except FileNotFoundError:
        print("File Not Found.")
    except OSError:
        print("File error occurred.")


def main():
    input_file_name = ""
    output_file_name = ""

    valid = False
    while not valid:
        input_file_name = input("Enter input file name: ")
        valid = validate_filename_input(input_file_name)

    output_file_name = input("Enter output file name: ")

    result = formate_beautify_text(input_file_name, output_file_name)
    if result is not None:
        print(result)


if __name__ == "__main__":
    main()
