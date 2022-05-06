# Unilang

A brainfuck like interpreter that support our own syntaxic set.  

## Example

Acording to the Brainfuck specifications, the instructions set can be specify as follow:  

```
>   Increment the pointer​
<​   Decrement the pointer
+​   Increment the byte in the current pointed memory case 
-​   Decrement the byte in the current pointed memory case
.​   Write the ASCII value of the current pointed memory case
,​   Read the value and pass it to the current pointed memory case
[​   Jump after the matched ] if the pointed byte equal 0
]​   Back after the matched [ if the pointed byte is different than 0
```

Then, the following programm will print an `Hello World!`:
```
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```

So far, we can modify the syntax of the instructions set as follow:

```
🐇   Increment the pointer​
🐬   Decrement the pointer
🐌   Increment the byte in the current pointed memory case 
🦧   Decrement the byte in the current pointed memory case
🙈   Write the ASCII value of the current pointed memory case
🐢   Read the value and pass it to the current pointed memory case
🦆   Jump after the matched 🦛 if the pointed byte equal 0
🦛   Back after the matched 🦆 if the pointed byte is different than 0
```

And the follow `Hello World!` programm will looks like:

```
🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🦆🐇🐌🐌🐌🐌🐌🐌🐌🐇🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐇🐌🐌🐌🐇🐌🐬🐬🐬🐬🦧🦛🐇🐌🐌🙈🐇🐌🙈🐌🐌🐌🐌🐌🐌🐌🙈🙈🐌🐌🐌🙈🐇🐌🐌🙈🐬🐬🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🐌🙈🐇🙈🐌🐌🐌🙈🦧🦧🦧🦧🦧🦧🙈🦧🦧🦧🦧🦧🦧🦧🦧🙈🐇🐌🙈🐇🙈
```

:pencil: Notice that each instruction can be defined with a string length between 1 and "infinit".  
Also, every character that is not in the instructions set is interpreted like a comment.  
So the current script can be run "as is":

```
++++++++++    Add 10 to the pointer 0.
++++++++++    Add 10 to the pointer 0.
++++++++++    Add 10 to the pointer 0.
++++++++++    Add 10 to the pointer 0.
++++++++++    Add 10 to the pointer 0.
++++++++++    Add 10 to the pointer 0.
++++++++++    Add 10 to the pointer 0.
++++++++++    Add 10 to the pointer 0.
++++++++++    Add 10 to the pointer 0.
++++          Add 4 to the pointer 0.

.             Print the ASCII value of the pointer 0.
.             Again print the ASCII value of the pointer 0.
```

## Usage guide

The interpreter can be used by passing the instructions directly in the command line or by specifying a file pass to an Unilang script.  

**Example:**

```sh
python -m src "<unilang_instructions>"
```

**Or:**

```sh
python -m src ./path/to/my/unilang/script
```

To change the syntax of the instructions set, we have to hard code them in the `_Statement` enumerator of the `./src/engine.py` file.  
Maybe I'll implement a config file later but I'm too lazy for that now. 🐇