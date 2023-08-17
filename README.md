# Random_Quote_Generator_Miniworld
Importing Required Module:
The script begins with importing the random module, which is used to select random quotes.

Defining Quote Categories:
The quotes dictionary holds different categories of quotes, each with a list of quotes associated with that category.

Displaying Categories:
The display_categories() function prints the available categories to the user.

Getting User Input:
The get_user_input(prompt) function takes a prompt as an argument and gets user input after displaying the prompt.

Main Function:
The main() function serves as the main part of the program. It displays a welcome message and then enters a loop that keeps running until the user decides to stop generating quotes.

Getting User's Name:
The user is prompted to enter their name using the get_user_input() function.

Displaying Categories and Choosing Category:
The available categories are displayed using display_categories(). The user is then prompted to choose a category by entering the name of the category.

Generating and Displaying Personalized Quote:
If the chosen category is valid (exists in the quotes dictionary), a random quote from that category is selected using random.choice() and stored in selected_quote. The user's name is inserted into the selected quote, creating a personalized quote. This personalized quote is then printed to the user.

Retry Prompt:
After displaying the personalized quote, the user is asked if they want to generate another quote. If the user's response is not "yes," the loop breaks, and the program displays a thank you message.

Executing the Main Function:
Finally, the script checks if it's being executed as the main program using if __name__ == "__main__":. If this condition is true, the main() function is called, and the program execution begins.

The script essentially creates an interactive experience where the user can input their name, choose a category, and receive a personalized random quote from the chosen category. The process can be repeated as many times as the user desires.
