function checkAnagram(a, b) {
  
        // Not of same length, can't be Anagram
        if (a.length !== b.length) {
            return false;
        }
  
        // Inbuilt functions to rearrange the string
        var str1 = a.split('').sort().join(''); 
        var str2 = b.split('').sort().join('');
  
        var result = (str1 === str2);
        return result;
    }
  
    // Checking the output
    document.write(checkAnagram('abc', 'cba'));
