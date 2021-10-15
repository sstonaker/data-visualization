#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:52:19 2019

@author: stevenstonaker
"""

import unittest
import python_repos as pr

class PythonRepoTestCase(unittest.TestCase):
    """Tests for 'python_repos.py'"""
    
    def test_status_code(self):
        """Test that the status code returned is 200 (success)."""
        self.assertEqual(pr.r.status_code, 200)
        print(f"\n\nExpected 200, returned: {pr.r.status_code}")
        
    def test_total_repos(self):
        """
        Test that the total number of repos is > 100 (arbitrary non-zero).
        """
        self.assertGreater(pr.response_dict['total_count'], 100)
        print(f"\n\nExpected > 100, returned: {pr.response_dict['total_count']}")
        
        
    def test_repos_returned(self):
        """Test that the repos returned is 30 (max number)."""
        self.assertEqual(len(pr.repo_dicts), 30)
        print(f"\n\nExpected 30, returned: {len(pr.repo_dicts)}")
        
if __name__ == '__main__':
    unittest.main()        