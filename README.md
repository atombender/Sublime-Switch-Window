SwitchWindow
============

A Sublime Text 3 plugin for switching between open windows without having to open the Window menu.

This plugin works around a [known issue](https://github.com/SublimeText/Issues/issues/444) with the API by using AppleScript. For that reason, it only works on OS X.

On Mavericks, Sublime Text must be granted a permission to control windows. Open System Preferences, go to Security & Privacy, find Accessibility in the list, and make sure `Sublime Text` and `System Events` are both enabled.

### Install: ###

Via Package Control:

* Run `Package Control: Add Repository` command.
* Enter the Git repository URL.

Manually:

    # The path to Sublime Packages on OSX is usually /Users/{user}/Library/Application Support/Sublime Text 2/Packages/
    cd {SUBLIME_PACKAGES_PATH}
    git clone https://github.com/deborasetton/Sublime-Switch-Window.git SwitchWindow

### Usage: ###

The default key binding is `Command + Shift + .`.

### TODO: ###

- Bind to new window event (even though it doesn't look like it's possible);

### License ###

MIT License. Copyright 2013 Débora Setton.
