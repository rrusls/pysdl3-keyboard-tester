# pysdl3-keyboard-tester
A very simple Keyboard Tester fully written in Python using PySDL3

# Description
This is a simple keyboard tester written fully on Python without libraries like keyboard or pynput.keyboard. Code is fully written with Simple DirectMedia Layer.
Useful for testing keyboard input and checking stuck or non-working keys.

# Features
  - Visual keyboard layout
  - Key press & holding highlighting
  - SDL3 + SDL_image
  - Console warning what button did user press
# Requirements
  - Python 3.x
  - SDL3
  - SDL_image
  - keyboard_layout.png 
# Run
Make sure 'keyboard_layout.png' is in the same folder as the script. 
Run with:
  ```
  python keyboard_tester.py
  ```
# Future
  - honeslty no idea abt this, maybe expand it to be keyboard + mouse tester, but we'll see
  - make code more clear (??)
# Good to know
When running, there is a chance there would be some problems with the version of pySDL3. Make sure you install a PySDL3 version which is compatible. Mine is 0.9.8b1.

Also when running, interpretator can show messages like ```Warning: Version mismatch with binary: 'SDL3_net.dll' (expected: 3.0.0, got: none)```. It is safe to not care about this, program will start regardless.

The snake is pretty much immortal, since there is no logic of it's death, so you can play endlessly. I thought its much more fun than dying.

Write, contribute, test. It's all will be appreciated anytime.

That's it. Thank you for your attention.
P.S: fn button does not work bruh

