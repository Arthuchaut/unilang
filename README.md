# Unilang

A brainfuck like interpreter that support our own syntaxic set.  

- [Unilang](#unilang)
  - [Requirements](#requirements)
  - [Usage guide](#usage-guide)
  - [Modify the statements syntax](#modify-the-statements-syntax)
    - [Example](#example)
- [Interpretation rules](#interpretation-rules)
  - [Supported characters](#supported-characters)
  - [The instruction string length](#the-instruction-string-length)
  - [Ambigous instructions](#ambigous-instructions)

## Requirements

No virtual environment or any external dependencies are required.

- Python >= 3.9


## Usage guide

The interpreter can be used by passing the instructions directly in the command line or by specifying a file pass to an Unilang script.  

**Example:**

```sh
python -m src "<unilang_instructions>"
```

**Or:**

```sh
python -m src ./path/to/my/unilang/script.uni
```

:pencil: Notice that the `.uni` extension is just a conventional way to distinguish an Unilang script from another file. You can define whatever you want as well.

## Modify the statements syntax

The statements are specified in the `src/config.py` file so we can modified these pattern as we wish.  

### Example

Acording to the Brainfuck specifications, the instructions set can be defined as follow:  

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

:pencil: Notice that each instruction can be defined with a string length between 1 and "infinit" so every syntaxe is possible while there are matching with the [interpretation rules](#interpretation-rules).  
As a result, we can define an [Esolang](https://esolangs.org/wiki/Ook!) or a [PenisScript](https://esolangs.org/wiki/PenisScript) if we want as well!
 
Also, every pattern that is not in the instructions set is interpreted like a comment.  
So the current script can be run "as is" acording to the defined instructions set:

```
++++++++++    Add 10 to the pointer 0
++++++++++    Add 10 to the pointer 0
++++++++++    Add 10 to the pointer 0
++++++++++    Add 10 to the pointer 0
++++++++++    Add 10 to the pointer 0
++++++++++    Add 10 to the pointer 0
++++++++++    Add 10 to the pointer 0
++++++++++    Add 10 to the pointer 0
++++++++++    Add 10 to the pointer 0
++++          Add 4 to the pointer 0

.             Print the ASCII value of the pointer 0
.             Again print the ASCII value of the pointer 0
```

# Interpretation rules

This section describe the interpreter rules to define the instructions set.

## Supported characters

All unicode characters can be used to define an instruction set.

## The instruction string length

An instruction can be defined with a string length from 1 to "infinit" (of course it should be ridiculous to define a statement with a length of 1 000 000 😏).

## Ambigous instructions

An ambigous instruction is an statement that can be confused with another due to the similarity of these pattern.  

**For example:**

```
Meow        Increment the pointer
MeowMeow    Decrement the pointer
```

**Same as:**

```
Meow        Increment the pointer
Meow Meow   Decrement the pointer
```

Are ambigous instructions because the interpreter will always increment the pointer when it meet a `Meow` instruction.

**While this following set:**

```
Meow        Increment the pointer
Meor        Decrement the pointer 
```

Is a correct instructions set.