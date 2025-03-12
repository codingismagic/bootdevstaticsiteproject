# Import the necessary classes from textnode.py
from textnode import TextNode, TextType

def main():
    # Create a TextNode object with dummy values
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    # Print the TextNode object
    print(text_node)

# Call the main function
if __name__ == "__main__":
    main()
