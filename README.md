Python scripts + Keyboard shortcuts
===================================

Sadly, I'm not sure if this is doable outside of Ubuntu :(

Introduction
------------

We write python scripts to help us in some tasks. In most cases, having a (good?) _command line interface_ is good enough, but if you find yourself:

* copy-pasting to and from the terminal
* dumping text on a file and then running the script

then this _cute_ trick might be useful for you.

We will illustrate this with 3 simple use cases:

1. Googling some text
2. Prettifying JSON
3. DNS lookup of some domain


Using keyboard shortcuts
------------------

`System Settings > Keyboard > Shortcuts > Custom Shortcuts`

Add the keyboard shortcut with the command as the python script.

Make sure its:

* Executable (`chmod +x ...`)
* Has the _shebang_ (`#! /usr/bin/python`)
* Or is set as a console script in the `setup.py`


What about input?
-----------------

When running python scripts using a keyboard shortcut, we lose the ability to dynamically add arguments or piping input to the command. A simple and natural way to get input is by using the __highlighted text at the time the script is run__ as input.

To do this, we use `xsel`, which can access and manipulate the selection and clipboard. Simply calling `xsel` returns the current highlighted text.

```python
data = subprocess.check_output('xsel')
```

What about output?
------------------
Aside from the original side-effect of your script (like writing to a file or opening new tab in the web browser, we have some other examples:

1. Utilize the clipboard ("copy-paste-ish")
2. Pop-up notifications (using `notify-send`)
3. Be creative :D

__Clipboard__

```python
def clipboard(output):
    p = subprocess.Popen(['xsel', '-ib'], stdin=subprocess.PIPE)
    p.communicate(output)
```

__Notifications__

```python
def pop_up(title, body):
    subprocess.call(['notify-send', title, body])
```
