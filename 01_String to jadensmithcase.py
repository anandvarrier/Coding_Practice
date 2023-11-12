
def to_jaden_case(string):
    words = string.split()
    jaden_words = [word.capitalize() for word in words]
    jaden_sentence = ' '.join(jaden_words)
    return jaden_sentence

#Test Case Code. You may run this on Code Wars.
'''
from solution import to_jaden_case
import codewars_test as test

@test.describe('Sample test')
def basic_tests():
    @test.it('Simple text')
    def _():
        quote = "How can mirrors be real if our eyes aren't real"
        test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
'''