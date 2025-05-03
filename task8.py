def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            
            content = file.read()

            
            words = content.split()

            
            return len(words)
    
    except FileNotFoundError:
        return f"The file '{filename}' was not found."
    except Exception as e:
        return f"An error occurred: {e}"

filename = "testfile.txt"  
print(count_words_in_file(filename))
