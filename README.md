# Build-your-own-Chatbot
This Python script is a simple chatbot program that generates responses based on predefined patterns in the user's input.

 Here's an explanation of the code:

1- responses Dictionary:

* This dictionary contains predefined responses for different patterns in user input.

* Each key represents a pattern, and the associated value is a list of possible responses for that pattern.

* For example, if the user says "hello," the chatbot can respond with one of the greetings in the list associated with the "hello" key.


2- get_response(user_input) Function:

* This function takes the user's input as an argument.

* It converts the user's input to lowercase to ensure case-insensitive matching.

* It iterates through the keys and values in the responses dictionary.

* If it finds a key that matches the user's input, it randomly selects and returns a response from the associated list.

* If no matching pattern is found, it returns a random response from the "default" category.


3-The while Loop:

* The script enters an infinite loop to continuously interact with the user.


4- User Input Handling:

* The program prompts the user for input with input('User said - ').

* If the user types "exit," the loop is terminated, and the program ends.


5- Generating Bot Responses:

* The user's input is passed to the get_response() function to retrieve an appropriate response.

* The response is printed with the format f'Bot said - {response}\n'.


6- Exiting the Program:

* If the user types "exit," the loop breaks, and the program prints "Goodbye!".


Overall, this script simulates a basic chatbot that responds to user input based on predefined patterns. If the user enters a recognized pattern (e.g., "hello," "bye"), the chatbot provides a relevant response. If the user inputs something not recognized, the chatbot provides a generic response from the "default" category.




