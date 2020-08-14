# lamrop
### Welcome to lamrop!
### this is a programming language with some simple functions:

### [there is an array, an integer for the array's pointer, an output string, and a storing variable (preset to 1) the moment you start.]

## Functions:

`l` - makes the array pointer go left. 

`a` - adds s to the number pointed to in the array.

`m` - subtracts s from the number pointed to in the array.

`r` - makes the array pointer go right.

`o` - displays the output string.

`p` - adds a new element to the right of the array (preset to 0).

`s` - changes the stored variable's value to the number pointed to in the array.

`+` -

    if immediately followed by 'c', it adds the ASCII character equivalent of the number to the right of the output string.
    
    if not, it adds the number itself to the right of the output string.
    
`.` - resets the output string to `''`.

`i` - sets the storing variable to the user's next input, with the current output string displayed as the input text.
    
    input types:
        if - if 'i' is immediately followed by 'f', the storing variable gets set to the float input.
        ii - if 'i' is immediately followed by 'i', the storing variable gets set to the integer input.
        ic - if 'i' is immediately followed by 'c', the array pointer checks the string and assigns the ASCII character value it is pointing at to the storing variable.
        
`n` - compares the number pointed to in the array with the stored variable.

    comparisons:
        nl - greater than or equal to
        ng - less than or equal to
        ne - not equal to
        ee - equal to
        ll - less than
        gg - greater than
        
    if these comparisons turn out to be true it will process the code inside the 'n' and ':'. if false it will skip the code.
    
    example code: ppiiaiiraslnllr+ol:nggs+o:
    input two numbers and it will output the one with larger value.
    
Enjoy!
