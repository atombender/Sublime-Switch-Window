import sublime, sublime_plugin
import os
import os.path

from subprocess import Popen, PIPE

class SwitchWindowCommand(sublime_plugin.ApplicationCommand):

  def _window_items(self):
    child = Popen(['osascript', '-e',
      'tell application "System Events" to tell process ' +
      '"Sublime Text" to return name of every menu item ' +
      'of menu 1 of menu bar item "Window" of menu bar 1'],
      stdout = PIPE,
      stderr = PIPE,
      cwd = os.path.dirname(os.path.realpath(__file__)))

    output = child.stdout.read()
    (s, err) = child.communicate()
    if err:
      return (err.decode('utf-8'), [])
    else:
      data = output.decode("utf-8")
      items = [val for val in data.split(', ') if self._is_valid(val)]
      return (None, items)

  def _switch_window(self, title):
    sublime.set_timeout_async(lambda: self._switch_window_in_background(title), 0)

  def _switch_window_in_background(self, title):
    child = Popen(['osascript', '-e',
      'tell application "System Events" to tell application ' +
      'process "Sublime Text" to perform action "AXRaise" of ' +
      '(first window whose name contains "%s")' % title],
      stdout = PIPE,
      stderr = PIPE,
      cwd = os.path.dirname(os.path.realpath(__file__)))

    child.stdout.read()
    (_, err) = child.communicate()
    if err:
      sublime.error_message(err.decode('utf-8'))

  def _is_valid(self, val):
    return val.strip() not in [
      'Minimize',
      'Minimize All',
      'Zoom',
      'Zoom All',
      'missing value',
      'Bring All to Front',
      'Arrange in Front',
    ]

  def run(self):
    sublime.set_timeout_async(lambda: self.run_in_background(), 0)

  def run_in_background(self):
    (err, items) = self._window_items()
    if err:
      sublime.error_message(str(err))
    else:
      sublime.active_window().show_quick_panel(items,
        lambda index: self._switch_window(items[index]) if index != -1 else None)
