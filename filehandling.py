def modify_file():
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        #  Try to open and read the file
        with open(filename, "r") as f:
            content = f.read()

        # Modify content (convert to uppercase for demo)
        modified_content = content.upper()

        #  Create a new file to save modified version
        new_filename = "modified_" + filename
        with open(new_filename, "w") as f:
            f.write(modified_content)

        print(f"File processed successfully! Modified file saved as '{new_filename}'.")

    except FileNotFoundError:
        print(" Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" Unexpected error: {e}")


# Run the function
modify_file()
