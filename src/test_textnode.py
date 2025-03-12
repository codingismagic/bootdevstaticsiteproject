import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        # Add additional test methods here
    def test_different_text(self):
        node1 = TextNode("Text one", TextType.BOLD)
        node2 = TextNode("Text two", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_different_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
    
    def test_different_url(self):
        # Test that nodes with different URLs are not equal
        node1 = TextNode("Link text", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Link text", TextType.LINK, "https://blog.boot.dev")
        self.assertNotEqual(node1, node2)
    
    def test_url_none_vs_url(self):
        # Test explicitly comparing a node with URL=None vs a node with a URL
        node1 = TextNode("Link text", TextType.LINK)  # Default URL is None
        node2 = TextNode("Link text", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
