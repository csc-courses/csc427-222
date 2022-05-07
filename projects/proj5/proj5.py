#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 5: Regular Expressions
# 
# _csc427, semester 222
# <br>
# university of miami
# <br>
# date: 23 feb 2022_
# 

# ---
# 
# ### Student name:
# 
# ---

# ### Discussion
# 
# Regular expressions are a usefull programming skill. In this problem set, you will work with the regular expression library provided by Python. Glance through the [Regular Expression documentation](https://docs.python.org/3/library/re.html) at docs.python.org.
# 
# The regular expression package is imported with the 'import re' statement. The import statement used in this way brings in all the names (the functions) in the package, refered to first by the name 're', such as 're.search()'.
# 
# The regular expression itself is written using the special symbols,
# 
# - the star operator is written with a *.
# - the union operator is written with a |.
# - parenthesis can be used to group, so that (0|1)* is any string of 0's and 1's, 
#   while 01* would be any string starting with a 0 followed by any number of 1's.
# - the ^ matches the beginning of the string and $\$$ matches the end. 
# - for instance,  the regexp 01 searches for 01 anywhere in the string, 
#   the regexp ^01$\$$ matches only the 2 character sequence 01.
# - the regular expression language does not have the character for the empty string.
#   however the ? operator will help you get around this limitation.
# 
# The regular expression package will turn the regexp into an DFA, so that it can be run on strings. As we now know, it can be a large computation. Therefore the package can compile the the regexp, returning an object of type Pattern, that internal has the DFA to determine whether the string matches the regular expression.
# 
# 
# 
# 

# ### Exercise A
# 
# Following are seven descriptions of regular languages. The first four are given by NFA's, diagramed in the class textbook as machines N1, N2, N3 and N4.
# 
# The last three are by word descriptions.
# 
# Please provide python regular expressions that match for exactly the same langage.
# 
# With each language is a test vector giving a list of strings in the language and strings not in the language, to help your testing. The basic test is according to these strings; an extended test will be more extensive.
# 
# When testing, it is best to consider "typical" cases to be begin with, but then "edge cases" to refine your understanding of the problem.
# 
# 

# In[ ]:


# sipser N1: accepts all strings that contain either 101 or 11 as a substring.

N1_regexp = ''
N1_test = (['010110','101','11','1101','1011','00011','101000'],['','1','0','10','01','00100'])


# sipser N2: accepts all strings containing a 1 in the third position from the end
N2_regexp = ''
N2_test = (['100','111','0111','1111','00100'],['','1','0','011','1011'])


# sipser N3: accepts all strings of 0's of length k where k is a multiple of 2 or 3
N3_regexp = ''
N3_test = (['','00','000','0000','000000'],['0','00000','0000000','00000000000'])


# sipser N4: accepts all strings in (a | ba*(a|b)a )*
N4_regexp = ''
N4_test = (['','a','baba','baa'],['b','bb','babba'])

# strings over {a, b, c} where all a's occur before any b, all b's occur before any c.
abc_regexp = ''
abc_test = (['abc','aac','bbc','c'],['ba','ca','abca'])

# over {0,1} there string 11 does not appear as a substring
not11_regexp = ''
not11_test = (['1','01','0010','101'],['11','0110','1011','1100'])

# over {0,1} that do not contain  101 as a substring
not101_regexp = ''
not101_test = (['1','01','0010','111','1001'],['101','0101','1011','00101001'])


# ## Basic tests
# 
# Theses routines serve two functions. First they apply the regular expressions to the test vectors to see if the regular expression works correctly on the strings in the test vector.
# 
# It also demonstrates the code that is used inorder to use the re package in Python.

# In[ ]:


import re

class RegExp_Test:
    
    def __init__(self, name, regexp):
        self.re_pat= re.compile(regexp)
        self.name = name
        
    def test(self, test_vect, verbose=False):
        tv_true, tv_false = test_vect
        correct = 0 

        print(f'*** testing {self.name}')
        for string in tv_true:
            if re.search(self.re_pat,string):
                correct += 1
            else:
                print(f'should accept but does not: |{string}| ')
        print(f'\t{correct} correctly accepted out of {len(tv_true)} strings')
        passed = correct == len(tv_true)

        correct = 0 
        for string in tv_false:
            if not re.search(self.re_pat,string):
                correct += 1
            else:
                print(f'should reject but does not: |{string}| ')
        print(f'\t{correct} correctly rejected out of {len(tv_false)} strings')
 
        passed = passed and (correct == len(tv_false))
        if passed:
            print(f'*** PASSES\n')
        else:
            print(f'*** FAILS\n')
        return passed

# end class RegExp_Test


def basic_test(test_bundle):

    correct = 0 
    for test in test_bundle:
        desc ,reg_exp, test_v = test
        regexp = RegExp_Test(desc,reg_exp)
        if regexp.test(test_v):
            correct += 1
    print(f'{correct} correct out of {len(test_bundle)}')
    res = (correct == len(test_bundle))
    if res:
        print(f'*** congratulations you passed all tests')
    return res


all_tests = [
    ['Sipser N1', N1_regexp, N1_test ],
    ['Sipser N2', N2_regexp, N2_test],
    ['Sipser N3', N3_regexp, N3_test],
    ['Sipser N4', N4_regexp, N4_test],
    ['abc', abc_regexp, abc_test ],
    ['not11', not11_regexp, not11_test ],
    ['not101', not101_regexp, not101_test ]
]

basic_test(all_tests)


# In[ ]:





# ### End of assigment
# 
