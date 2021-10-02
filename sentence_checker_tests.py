import unittest
import sentence_checker

class TestSentenceCheckerMethods(unittest.TestCase):

    # Valid Sentence Tests

    def test_sentence_is_valid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('The quick brown fox said hello Mr lazy dog.')
        self.assertTrue(sentence_checker_result.success)
   
    def test_sentence_with_quotes_is_valid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('The quick brown fox said “hello Mr lazy dog”.')
        self.assertTrue(sentence_checker_result.success)

    def test_sentence_starting_with_mixed_number_formats_is_valid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('One lazy dog is too few, 13 is too many.')
        self.assertTrue(sentence_checker_result.success)

    def test_sentence_with_numbers_as_text_is_valid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('One lazy dog is too few, thirteen is too many.')
        self.assertTrue(sentence_checker_result.success)

    def test_sentence_with_question_mark_and_quotes_is_valid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('How many "lazy dogs" are there?')
        self.assertTrue(sentence_checker_result.success)

    #Invalid Sentence Tests

    def test_empty_sentence_is_invalid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('')
        self.assertFalse(sentence_checker_result.success)        
        self.assertTrue(sentence_checker_result.error_message == 'Sentences can not be empty')        

    def test_sentence_with_stray_period_is_invalid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('The quick brown fox said "hello Mr. lazy dog".')
        self.assertFalse(sentence_checker_result.success)
        self.assertTrue(sentence_checker_result.error_message == 'This sentence is invalid as it contains a period at a position other than the end of the sentence!')

    def test_sentence_with_lowercase_first_letter_is_invalid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('the quick brown fox said “hello Mr lazy dog".')
        self.assertFalse(sentence_checker_result.success)   
        self.assertTrue(sentence_checker_result.error_message == 'This sentence is invalid as the first letter of your sentence is NOT uppercase!')        

    def test_sentence_with_incorrect_number_of_quotes_is_invalid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('The quick brown fox said ""hello Mr lazy dog".')
        self.assertFalse(sentence_checker_result.success)
        self.assertTrue(sentence_checker_result.error_message == 'This sentence is invalid as it contains an odd number of quotes!')          
        

    def test_sentence_with_incorrect_number_format_is_invalid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('One lazy dog is too few, 12 is too many.')
        self.assertFalse(sentence_checker_result.success)      
        self.assertTrue(sentence_checker_result.error_message == 'This sentence is invalid, please write numbers 0-12 as words') 
        

    def test_sentence_with_incorrect_number_format_due_to_comma_is_invalid(self):                                               
        sentence_checker_result = sentence_checker.is_valid_sentence('Are there 11,12, or 13 lazy dogs?')
        self.assertFalse(sentence_checker_result.success)
        self.assertTrue(sentence_checker_result.error_message == 'This sentence is invalid, please write numbers 0-12 as words')
       

    def test_sentence_with_no_punctuation_is_invalid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('There is no punctuation in this sentence')
        self.assertFalse(sentence_checker_result.success)
        self.assertTrue(sentence_checker_result.error_message == 'The sentence is invalid, it does not contain any of the following termination characters: .,!,?')


    def test_sentence_with_multiple_issues_is_invalid(self):
        sentence_checker_result = sentence_checker.is_valid_sentence('this ""sentence" contains more than. 12 issues')
        self.assertFalse(sentence_checker_result.success)
        self.assertTrue(sentence_checker_result.error_message == '''This sentence is invalid as the first letter of your sentence is NOT uppercase!. This sentence is invalid as it contains an odd number of quotes!. The sentence is invalid, it does not contain any of the following termination characters: .,!,?. This sentence is invalid as it contains a period at a position other than the end of the sentence!. This sentence is invalid, please write numbers 0-12 as words''')
        


if __name__ == '__main__':
    unittest.main()