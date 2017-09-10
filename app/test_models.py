import unittest
from models import User, Shoppinglist,Item

class TestUser(unittest.TestCase):
    def setUp(self):
        """Setup a user instance to be used for testing throughout the app"""

        self.user = User("ruganda", "mubarak", "muba@gmail.com")

    def test_add_shoppinglist(self):

        self.assertEqual(self.user.add_shoppinglist("food"), "Shopping list added succesfully")
        self.assertEqual("food","shoppinglist already exists")

    


    #if __name__== '__main__':
        #main()


