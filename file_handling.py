
try:
    # Open the file in write mode to create and write initial content
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("The number is 42.\n")
        file.write("This is line 3 with a mix of text and numbers: 1234.\n")
    print("File created and initial lines written successfully.")
    
    # Reading and Displaying Content
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File content after initial write:")
        print(content)
    
    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line 4.\n")
        file.write("Adding another line 5 with text and numbers: 5678.\n")
        file.write("Final appended line 6.\n")
    print("Lines appended successfully.")

    # Reading and Displaying Content Again
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("File content after appending:")
        print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access or modify the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operation attempted.")
