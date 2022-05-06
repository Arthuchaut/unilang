# Unilang

A brainfuck like interpreter that support our own syntaxic set.  

## Example

Acording to the Brainfuck specifications, the instruction set can be specify as follow:  

```
>   Increment the pointer​
<​   Decrement the pointer
+​   Increment the byte in the current pointed memory case 
-​   Decrement the byte in the current pointed memory case
.​   Write the ASCII value of the current pointed memory case
,​   Read the value and pass it to the current pointed memory case
[​   Jump to after the matched ] if the pointed byte equal 0
]​   Back after the matched [ if the pointed byte is different than 0
```

Then, the following programm will print an `Hello World!`:
```
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```

So far, we can modify the syntax of the instruction set as follow:

```
🐇   Increment the pointer​
🐬   Decrement the pointer
🐌   Increment the byte in the current pointed memory case 
🦧   Decrement the byte in the current pointed memory case
🙈   Write the ASCII value of the current pointed memory case
🐢   Read the value and pass it to the current pointed memory case
🦆   Jump to after the matched 🦛 if the pointed byte equal 0
🦛   Back after the matched 🦆 if the pointed byte is different than 0
```

And the follow `Hello World!` programm will looks like:

```
🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🦆🐇🐌🐌🐌🐌🐌🐌🐌🐇🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐇🐌🐌🐌🐇🐌🐬🐬🐬🐬🦧🦛🐇🐌🐌🙈🐇🐌🙈🐌🐌🐌🐌🐌🐌🐌🙈🙈🐌🐌🐌🙈🐇🐌🐌🙈🐬🐬🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🙈🐇🙈🐌🐌🐌🙈🦧🦧🦧🦧🦧🦧🙈🦧🦧🦧🦧🦧🦧🦧🦧🙈🐇🐌🙈🐇🙈
```

:pencil: Notice that each instruction can be defined with a string length between 1 and "infinit".  
Also, every character that is not in the instruction set is interpreted like a comment.