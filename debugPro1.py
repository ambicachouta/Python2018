num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']


def nested_loop():
    for number in num_list:
        print(number)
        for letter in alpha_list:
            print(letter)

if __name__ == '__main__':
    nested_loop()


"""
How To Use the Python Debugger

Working Interactively with the Python Debugger
The Python debugger comes as part of the standard Python distribution as a module called pdb. The debugger is also extensible, and is defined as the class Pdb. You can read the official documentation of pdb to learn more.

We’ll begin by working with a short program that has two global variables, a function that creates a nested loop, and the if __name__ == '__main__': construction that will call the nested_loop() function.



We can now run this program through the Python debugger by using the following command:

python -m pdb looping.py
The -m command-line flag will import any Python module for you and run it as a script. In this case we are importing and running the pdb module, which we pass into the command as shown above.

Upon running this command, you’ll receive the following output:


In the output, the first line contains the current module name (as indicated with <module>) with a directory path, and the printed line number that follows (in this case it’s 1, but if there is a comment or other non-executable line it could be a higher number). The second line shows the current line of source code that is executed here, as pdb provides an interactive console for debugging. You can use the command help to learn its commands, and help command to learn more about a specific command. Note that the pdb console is different than the Python interactive shell.

The Python debugger will automatically start over when it reaches the end of your program. Whenever you want to leave the pdb console, type the command quit or exit. If you would like to explicitly restart a program at any place within the program, you can do so with the command run.


Using the Debugger to Move through a Program
When working with programs in the Python debugger, you’re likely to use the list, step, and next commands to move through your code. We’ll go over these commands in this section.

Within the shell, we can type the command list in order to get context around the current line. From the first line of the program looping.py that we displayed above — num_list = [500, 600, 700] — that will look like this:

(Pdb) list

(Pdb) list 3, 7

(Pdb) step

(Pdb) next

While going through your code, you may want to examine the value passed to a variable, which you can do with the pp command, which will pretty-print the value of the expression using the pprint module:

(Pdb) pp num_list

"""