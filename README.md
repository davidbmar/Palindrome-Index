# Palindrome-Index

Given a string, , of lowercase letters, determine the index of the character whose removal will make  a palindrome. If  is already a palindrome or no such character exists, then print . There will always be a valid solution, and any correct answer is acceptable. For example, if  "bcbc", we can either remove 'b' at index  or 'c' at index .

Input Format

The first line contains an integer, , denoting the number of test cases. 
Each line  of the  subsequent lines (where ) describes a test case in the form of a single string, .

Constraints

All characters are lowercase English letters.
Output Format

Print an integer denoting the zero-indexed position of the character that makes  not a palindrome; if  is already a palindrome or no such character exists, print .

Sample Input

3
aaab
baa
aaa
Sample Output

3
0
-1
Explanation

Test Case 1: "aaab" 
Removing 'b' at index  results in a palindrome, so we print  on a new line.

Test Case 2: "baa" 
Removing 'b' at index  results in a palindrome, so we print  on a new line.

Test Case 3: "aaa" 
This string is already a palindrome, so we print ; however, , , and  are also all acceptable answers, as the string will still be a palindrome if any one of the characters at those indices are removed.
