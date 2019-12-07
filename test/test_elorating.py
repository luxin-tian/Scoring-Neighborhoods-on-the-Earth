import unittest
import elorating
import os
import csv

class Test_constructor(unittest.TestCase): 
    
    def test_Elo_constructor(self): 
        '''
        Test Elo.__init__() property setter. 
        '''
        with self.assertRaises(TypeError):
            self.elo_project = elorating.Elo(scale='abc')
        
        self.assertIsInstance(elorating.Elo(scale=100), elorating.Elo)

    def test_Element_constructor(self): 
        '''
        Test Element.__init__() 
        '''
        self.assertIsInstance(elorating.Element((65, 65), info=chr(65)+chr(65)), elorating.Element)

        
class Test_elorating_operations(unittest.TestCase):

    def setUp(self): 
        self.elo_project = elorating.Elo(scale=100)
        self.ele1 = elorating.Element((65, 65), info=chr(65)+chr(65))
        self.ele2 = elorating.Element((65, 66), info=chr(65)+chr(66))
        self.ele3 = elorating.Element((65, 65), info=chr(65)+chr(66))
        self.elo_project.element_space = {self.ele1: self.elo_project.base_score, self.ele2: self.elo_project.base_score}
       
    def test_Elo_add(self):
        '''
        Test Elo.add()
        '''
        # test repetition check
        with self.assertRaises(KeyError): 
            self.elo_project.add(self.ele3)
        
        # test add
        self.assertIn(self.ele1, self.elo_project.element_space)
        self.assertIn(self.ele2, self.elo_project.element_space)
        
        # test instance check
        with self.assertRaises(TypeError): 
            self.elo_project.add(100)
    
    def test_Elo_membership(self): 
        '''
        Test Elo.__contains__()
        '''
        self.assertTrue((self.ele1 in self.elo_project))

    def test_Elo_remove(self): 
        '''
        Test Elo.remove()
        '''
        self.elo_project.remove(self.ele1)
        self.assertFalse((self.ele1 in self.elo_project.element_space))
        self.elo_project.element_space = {self.ele1: self.elo_project.base_score}
        with self.assertRaises(TypeError): 
            self.elo_project.remove(100)
    
    def test_Elo_iter(self): 
        '''
        Test Elo is iterable
        '''
        self.assertTrue(hasattr(self.elo_project, '__iter__'))

    def test_Element_hashability(self):
        '''
        Test whether an Element object is hashable
        '''
        testset = {self.ele1, self.ele3}
        self.assertTrue((hash(self.ele2) == hash(self.ele2)))
        self.assertSetEqual(testset, {self.ele1})
        self.assertSetEqual(testset, {self.ele3})

    def test_Elo_win_prob(self): 
        '''
        Test Elo.win_prob()
        '''
        self.assertEqual(self.elo_project.win_prob(self.ele1, self.ele2), 0.5)

    def test_Elo_update_rating(self): 
        '''
        Test Elo.update_rating()
        '''
        with self.assertRaises(ValueError): 
            self.elo_project.update_rating(self.ele1, self.ele2, 3)
        
        self.elo_project.update_rating(self.ele1, self.ele2, vote=1)
        self.assertEqual(self.elo_project.element_space[self.ele1], 1005.0)
        self.assertEqual(self.elo_project.element_space[self.ele2], 995.0)

    def test_Elo_stats(self): 
        '''
        Test Elo.stats()
        '''
        self.elo_project.update_rating(self.ele1, self.ele2, vote=1)
        self.assertEqual(self.elo_project.stats(option='all'), '\nHighest: 1005.0\nLowest: 995.0\nMean: 1000.0\nStdev: 7.0710678118654755')
        self.assertEqual(self.elo_project.stats(option='max'), 1005.0)


class Test_elorating_fileio(unittest.TestCase): 
    
    def setUp(self):
        self.elo_project = elorating.Elo(scale=100)
        self.ele1 = elorating.Element((65, 65), info=chr(65)+chr(65))
        self.ele2 = elorating.Element((65, 66), info=chr(65)+chr(66))
        self.elo_project.element_space = {self.ele1: self.elo_project.base_score, self.ele2: self.elo_project.base_score}
        with open('elorating_log_test.csv', 'w') as test_file: 
            test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            test_writer.writerow(["ID", "Info", "RatingScore", "StandardizedScore"])
            test_writer.writerow(['test_id', 'test_info', 123, 456])
    
    def tearDown(self):
        os.remove('elorating_log_test.csv')

    def test_Elo_save_data(self): 
        '''
        Test Elo.save_data()
        '''
        filename = self.elo_project.save_data(mute=1)
        self.assertTrue(os.path.exists(filename))
        if os.path.exists(filename): 
            os.remove(filename)
        
    def test_Elo_import_data(self): 
        '''
        Test Elo.import_data()
        '''
        with self.assertRaises(InterruptedError): 
            self.elo_project.import_data('elorating_log_test.csv')
        
        self.elo_project.element_space = {}
        self.elo_project.import_data('elorating_log_test.csv')
        self.assertTrue(self.elo_project.element_space == {elorating.Element('test_id', info='test_info'): 123.0})


if __name__ == '__main__': 
    unittest.main()

