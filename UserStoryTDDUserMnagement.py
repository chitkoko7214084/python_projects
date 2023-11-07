'''
User story 1: User Registraton
As a new user, I want to be able to register for a new account
using email and password



User Story 2:Login 
As a registered user, I want to be able to log in to my account 
using email and password
'''

import unittest
from User import UserManagement
class TestUserMangement(unittest.TestCase):
    def test_registration(self):
        userManager = UserManagement()
        result = userManager.register("a@b.com", "password")
        self.asserTrue(result)
    
    def test_login(self):
        UserManager = UserManagement()
        UserManager.register("a@b.com", "password")
        result = UserManager.login("a@b.com", "password")
        self.assertTrue(result)
        