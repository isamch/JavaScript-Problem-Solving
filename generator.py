import os
import shutil

def create_directory_structure():
    # Create main directory
    main_dir = "Javascript-problem-solving"
    if os.path.exists(main_dir):
        shutil.rmtree(main_dir)
    os.makedirs(main_dir)
    
    # Create main README.md
    with open(os.path.join(main_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("# JavaScript Problem Solving Project\n\n")
        f.write("This project contains JavaScript exercises for different skill levels.\n\n")
        f.write("## Structure\n")
        f.write("- `intermediate/`: Intermediate level exercises (30 exercises)\n")
        f.write("- `advanced/`: Advanced level exercises (30 exercises)\n")
        f.write("\n## How to Use\n")
        f.write("1. Use `generate_structure.py` to generate the structure automatically.\n")
        f.write("2. Choose your level and start solving exercises.\n")
    
    # Create generate_structure.py
    with open(os.path.join(main_dir, "generate_structure.py"), "w", encoding="utf-8") as f:
        f.write('"""\n')
        f.write('This script automatically generates the JavaScript project structure\n')
        f.write('"""\n\n')
        f.write('print("Project structure generated successfully!")\n')
    
    # Create intermediate level with exercises
    create_level("intermediate", 30, main_dir)
    
    # Create advanced level with exercises
    create_level("advanced", 30, main_dir)
    
    print("Structure created successfully!")

def create_level(level_name, num_exercises, main_dir):
    level_dir = os.path.join(main_dir, level_name)
    exercises_dir = os.path.join(level_dir, "exercises")
    
    os.makedirs(exercises_dir)
    
    # Create level README.md
    with open(os.path.join(level_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# {level_name.capitalize()} JavaScript Exercises\n\n")
        f.write(f"This directory contains {num_exercises} {level_name} level exercises.\n\n")
        f.write("## Exercises List\n")
        
        for i in range(1, num_exercises + 1):
            exercise_name = get_exercise_name(level_name, i)
            f.write(f"{i}. {exercise_name}\n")
    
    # Create exercise files
    for i in range(1, num_exercises + 1):
        exercise_name = get_exercise_name(level_name, i)
        file_name = f"{i}. {exercise_name.replace(' ', '_')}.js"
        file_path = os.path.join(exercises_dir, file_name)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"// Exercise {i}: {exercise_name}\n\n")
            f.write(f"/*\n")
            f.write(f"  Description: {get_exercise_description(level_name, i)}\n")
            f.write(f"  Write a function that: {get_exercise_task(level_name, i)}\n")
            f.write(f"  Expected Output: {get_expected_output(level_name, i)}\n")
            f.write(f"*/\n\n")
            f.write(f"function {exercise_name.replace(' ', '_').lower()}() {{\n")
            f.write(f"  // Your code here\n")
            f.write(f"}}\n\n")
            f.write(f"// Test the function\n")
            f.write(f"console.log({exercise_name.replace(' ', '_').lower()}()); // Should return {get_expected_output(level_name, i)}\n")

def get_exercise_name(level, num):
    # Intermediate exercises
    if level == "intermediate":
        exercises = [
            "Count Vowels",
            "Longest Word",
            "Reverse String",
            "Check Palindrome",
            "Sort Numbers",
            "Remove Duplicates",
            "Sum Even Numbers",
            "Swap Case",
            "Calculate Average",
            "Find Element",
            "Merge Arrays",
            "Temperature Conversion",
            "Factorial",
            "Check Prime",
            "Print Star Pattern",
            "Date Difference",
            "Number to Words",
            "Generate UUID",
            "Parse String",
            "Simple Hash",
            "Roman Numerals",
            "Compress String",
            "Calculate Area",
            "Generate Password",
            "Decimal to Binary",
            "Binary to Decimal",
            "Fibonacci Sequence",
            "Pig Latin",
            "Compound Interest",
            "Multiplication Table"
        ]
        return exercises[num-1]
    
    # Advanced exercises
    elif level == "advanced":
        exercises = [
            "Array Intersection",
            "Deep Clone Object",
            "Jump Game",
            "Math Expression Parser",
            "Virtual DOM",
            "Event System",
            "Template Engine",
            "AES Encryption",
            "Caesar Cipher",
            "CSV Parser",
            "Custom JSON Parser",
            "Promise Library",
            "QR Code Generator",
            "Caching System",
            "Quick Sort",
            "Binary Search",
            "Theme System",
            "Auth System",
            "Digital Signature",
            "Markdown Parser",
            "PDF Generator",
            "Routing System",
            "Chart Generator",
            "Validation Library",
            "Notification System",
            "Random Code Generator",
            "State Management",
            "Auto Documentation",
            "Text Search Engine",
            "Unit Testing System"
        ]
        return exercises[num-1]

def get_exercise_description(level, num):
    if level == "intermediate":
        descriptions = [
            "Count the number of vowels in a given string",
            "Find the longest word in a sentence",
            "Reverse the order of characters in a string",
            "Check if a string reads the same forwards and backwards",
            "Sort an array of numbers in ascending or descending order",
            "Remove duplicate elements from an array",
            "Sum all even numbers in an array",
            "Swap uppercase to lowercase and vice versa in a string",
            "Calculate the average of numbers in an array",
            "Find an element in an array and return its index",
            "Merge two arrays while removing duplicates",
            "Convert between different temperature units",
            "Calculate the factorial of a number",
            "Check if a number is prime",
            "Print a star pattern in the shape of a triangle",
            "Calculate the difference between two dates in days",
            "Convert a number to its word representation",
            "Generate a simple UUID string",
            "Parse a string and extract required data",
            "Create a simple hash from a string",
            "Convert between Roman and Arabic numerals",
            "Compress a string by counting consecutive characters",
            "Calculate the area of different geometric shapes",
            "Generate a random password with specific requirements",
            "Convert a decimal number to binary",
            "Convert a binary number to decimal",
            "Generate a Fibonacci sequence up to a given limit",
            "Convert words to Pig Latin following specific rules",
            "Calculate compound interest over time",
            "Generate a multiplication table for given numbers"
        ]
        return descriptions[num-1]
    elif level == "advanced":
        descriptions = [
            "Find common elements between two arrays",
            "Create a deep clone of a complex object",
            "Solve the Jump Game problem using algorithms",
            "Parse and evaluate a mathematical expression",
            "Create a virtual DOM that can be manipulated",
            "Implement a custom event system for objects",
            "Build a simple template engine for HTML generation",
            "Implement AES encryption/decryption",
            "Implement Caesar cipher encryption/decryption",
            "Parse CSV content and extract data",
            "Build a custom JSON parser from scratch",
            "Implement a Promise library with basic functionality",
            "Generate QR codes from given text",
            "Implement a caching system with expiration",
            "Implement the Quick Sort algorithm",
            "Implement the Binary Search algorithm",
            "Create a dynamic theme system for applications",
            "Implement a simple authentication system",
            "Create a simple digital signature system",
            "Build a Markdown to HTML parser",
            "Generate PDF files from given content",
            "Implement a routing system for pages",
            "Create charts from given data",
            "Build a validation library for input data",
            "Implement a notification system",
            "Generate secure random codes for authentication",
            "Implement state management for applications",
            "Create auto-documentation from code comments",
            "Build a simple text search engine",
            "Implement a basic unit testing system"
        ]
        return descriptions[num-1]

def get_exercise_task(level, num):
    if level == "intermediate":
        tasks = [
            "Return the count of vowels (a, e, i, o, u) in the string",
            "Find and return the longest word in the sentence",
            "Reverse the string and return the result",
            "Check if the string is a palindrome (reads the same backwards)",
            "Sort the array in ascending or descending order based on parameter",
            "Remove duplicate elements from the array and return a new array",
            "Sum all even numbers in the array and return the total",
            "Swap character cases in the string and return the result",
            "Calculate the average of numbers in the array and return it",
            "Find the element in the array and return its index or -1 if not found",
            "Merge two arrays while removing duplicates and return new array",
            "Convert between Celsius, Fahrenheit and Kelvin units",
            "Calculate the factorial of the given number and return it",
            "Check if the number is prime and return true/false",
            "Print a star pattern triangle of given size and return as string",
            "Calculate the difference between two dates in days",
            "Convert the number to its English word representation",
            "Generate a random UUID string and return it",
            "Parse the string and extract the required data as specified",
            "Create a simple hash from the string using a basic algorithm",
            "Convert between Roman and Arabic numeral representations",
            "Compress the string by counting consecutive characters",
            "Calculate the area of the specified geometric shape",
            "Generate a random password meeting specified requirements",
            "Convert the decimal number to binary representation",
            "Convert the binary number to decimal representation",
            "Generate Fibonacci sequence up to the given limit",
            "Convert words to Pig Latin following the standard rules",
            "Calculate compound interest based on principal, rate and years",
            "Generate a multiplication table for numbers 1 to given number"
        ]
        return tasks[num-1]
    elif level == "advanced":
        tasks = [
            "Find and return common elements between two arrays",
            "Create a deep clone of the given object (including nested objects)",
            "Solve the Jump Game problem and return if reaching the end is possible",
            "Parse and evaluate the mathematical expression with parentheses",
            "Create a virtual DOM that can be manipulated with JavaScript functions",
            "Implement a custom event system with on, off, and emit functionality",
            "Build a template engine that replaces placeholders with object values",
            "Implement functions for AES-256 encryption and decryption",
            "Implement Caesar cipher with configurable shift for encryption/decryption",
            "Parse CSV content and extract data into an array of objects",
            "Build a JSON parser without using the built-in JSON.parse",
            "Implement a Promise library supporting then, catch, and finally",
            "Generate QR code from given text and return as string or image",
            "Implement a caching system with data expiration and memory management",
            "Implement the Quick Sort algorithm to sort an array",
            "Implement Binary Search algorithm on a sorted array",
            "Create a theme system that allows dynamic theme switching at runtime",
            "Implement an authentication system with login/logout functionality",
            "Create a simple digital signature system for data verification",
            "Convert Markdown text to HTML supporting common elements",
            "Generate PDF file from HTML content and return as binary data",
            "Implement a routing system supporting complex paths and parameters",
            "Create charts from given data using Canvas or SVG",
            "Build a validation library for different input types and rules",
            "Implement a notification system supporting different message types",
            "Generate secure random codes for authentication purposes",
            "Implement centralized state management for large applications",
            "Create auto-documentation that extracts comments from code",
            "Build a text search engine supporting phrase matching and fuzzy search",
            "Implement a basic unit testing system with describe and it functions"
        ]
        return tasks[num-1]

def get_expected_output(level, num):
    if level == "intermediate":
        outputs = [
            "For 'Hello World' → 3",
            "For 'The quick brown fox' → 'quick'",
            "For 'hello' → 'olleh'",
            "For 'madam' → true, for 'hello' → false",
            "[3,1,2] sorted asc → [1,2,3]",
            "[1,2,2,3] → [1,2,3]",
            "[1,2,3,4] → 6",
            "'Hello World' → 'hELLO wORLD'",
            "[1,2,3,4] → 2.5",
            "Find 3 in [1,2,3] → 2",
            "Merge [1,2] and [2,3] → [1,2,3]",
            "32°F → 0°C, 0°C → 273.15K",
            "5 → 120",
            "7 → true, 8 → false",
            "Size 3 → '*\\n**\\n***'",
            "01/01/2020 to 01/02/2020 → 31 days",
            "123 → 'one hundred twenty-three'",
            "→ 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' pattern",
            "Parse 'Name: John, Age: 30' → {name: 'John', age: 30}",
            "'password' → '5f4dcc3b5aa765d61d8327deb882cf99' (example)",
            "'IV' → 4, 4 → 'IV'",
            "'aaabbbcc' → 'a3b3c2'",
            "Circle r=3 → ~28.27, Rectangle 4×5 → 20",
            "→ 'A1b@C2d#' (example meeting complexity requirements)",
            "5 → '101'",
            "'101' → 5",
            "Limit 5 → [0,1,1,2,3]",
            "'hello' → 'ellohay', 'world' → 'orldway'",
            "Principal $1000, rate 5%, 10 years → $1628.89",
            "For 3 → [[1,2,3],[2,4,6],[3,6,9]]"
        ]
        return outputs[num-1]
    elif level == "advanced":
        outputs = [
            "[1,2,3] and [2,3,4] → [2,3]",
            "Cloned object should be deeply equal but not reference-equal",
            "[2,3,1,1,4] → true, [3,2,1,0,4] → false",
            "'3*(2+4)' → 18",
            "Virtual DOM should mirror real DOM operations",
            "Event system should trigger callbacks when events are emitted",
            "Template 'Hello {{name}}' with {name:'John'} → 'Hello John'",
            "Encrypted data should be decryptable to original",
            "'ABC' with shift 3 → 'DEF', 'DEF' with shift -3 → 'ABC'",
            "'a,b\\nc,d' → [{a:'c', b:'d'}]",
            "{'a':1} string → equivalent object",
            "Promise should resolve/reject and chain properly",
            "QR code should be generated and scannable",
            "Cached data should expire after specified time",
            "[3,1,2] → [1,2,3]",
            "Find 3 in [1,2,3,4,5] → 2 (index)",
            "Theme changes should apply to all components",
            "Should authenticate users and maintain session",
            "Signature should verify with correct key",
            "# Hello → <h1>Hello</h1>",
            "PDF should be generated with correct content",
            "Should route to correct components based on URL",
            "Chart should visualize provided data accurately",
            "Should validate inputs according to specified rules",
            "Notifications should appear and disappear as configured",
            "Generated codes should be random and secure",
            "State should be accessible and modifiable globally",
            "Documentation should reflect code structure and comments",
            "Search should return relevant results for queries",
            "Tests should pass/fail based on assertions"
        ]
        return outputs[num-1]

if __name__ == "__main__":
    create_directory_structure()