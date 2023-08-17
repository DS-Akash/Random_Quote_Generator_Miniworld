import random

# Collection of quotes for each category
quotes = {
    "motivation": [
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",
        "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
    ],
    "success": [
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will. - Vince Lombardi",
        "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
        "Success is not in what you have, but who you are. - Bo Bennett"
    ],
    "life": [
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "Life is either a daring adventure or nothing at all. - Helen Keller",
        "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
        "The biggest adventure you can ever take is to live the life of your dreams. - Oprah Winfrey",
        "Life isn't about finding yourself. It's about creating yourself. - George Bernard Shaw",
        "The only way to do great work is to love what you do. - Steve Jobs"
    ],
    "love": [
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "Love is composed of a single soul inhabiting two bodies. - Aristotle",
        "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves. - Victor Hugo",
        "The best and most beautiful things in this world cannot be seen or even heard, but must be felt with the heart. - Helen Keller",
        "Love is not only something you feel, it is something you do. - David Wilkerson",
        "Love is an endless act of forgiveness. Forgiveness is an endless act of love. - Beyoncé"
    ],
    "inspiration": [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis"
    ],
    "friendship": [
        "A real friend is one who walks in when the rest of the world walks out. - Walter Winchell",
        "Friendship is born at that moment when one person says to another, 'What! You too? I thought I was the only one.' - C.S. Lewis",
        "Friendship is the only cement that will ever hold the world together. - Woodrow Wilson",
        "A friend is someone who knows all about you and still loves you. - Elbert Hubbard",
        "Friendship is the only thing in the world concerning the usefulness of which all mankind are agreed. - Cicero",
        "A single rose can be my garden... a single friend, my world. - Leo Buscaglia",
        "Friends show their love in times of trouble, not in happiness. - Euripides",
        "A friend is someone who gives you total freedom to be yourself. - Jim Morrison"
    ],
    "happiness": [
        "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
        "The grand essentials of happiness are something to do, something to love, and something to hope for. - Allan K. Chalmers",
        "The best way to predict the future is to create it. - Abraham Lincoln",
        "The greatest happiness you can have is knowing that you do not necessarily require happiness. - William Saroyan",
        "The only joy in the world is to begin. - Cesare Pavese",
        "Happiness is not a goal... it's a by-product of a life well-lived. - Eleanor Roosevelt",
        "Happiness is a direction, not a place. - Sydney J. Harris",
        "The greatest happiness you can have is knowing that you do not necessarily require happiness. - William Saroyan",
        "Success is getting what you want, happiness is wanting what you get. - W.P. Kinsella",
        "If you want to be happy, be. - Leo Tolstoy"
    ],
    
}

def display_categories():
    print("\nAvailable categories:")
    for category in quotes.keys():
        print("- " + category.capitalize())

def get_user_input(prompt):
    return input(prompt).strip()

def main():
    print("Welcome to the Personalized Random Quote Generator!")
    
    while True:
        name = get_user_input("\nPlease enter your name: ")
        
        display_categories()
        
        chosen_category = get_user_input("Category: ").lower()
        
        if chosen_category in quotes:
            selected_quote = random.choice(quotes[chosen_category])
            personalized_quote = selected_quote.replace("{name}", name)
            
            print("\nHere's your personalized quote:")
            print(personalized_quote)
        else:
            print("Invalid category. Please choose a valid category.")
        
        retry = get_user_input("\nDo you want to generate another quote? (yes/no): ")
        if retry.lower() != "yes":
            print("\nThank you for using the Personalized Random Quote Generator!")
            break

if __name__ == "__main__":
    main()
