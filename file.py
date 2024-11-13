def modify_file_content(content):
    # Example modification: Convert text to uppercase (or any other modification you want)
    return content.upper()

def main():
    # Ask the user for the filename
    filename = input("Enter the filename to read from: ")
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content has been saved to {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    
    except IOError:
        print("Error: The file could not be read. Please check the file permissions.")

if __name__ == "__main__":
    main()
