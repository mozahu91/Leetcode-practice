  def countVowels(s):
    noOfVowels = 0
    vowels = set('AEIOUaeiou')
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count
    
 s = 'Zahid'
countVowels(s)
