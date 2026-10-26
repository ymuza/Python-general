"""Memento pattern: capture an object's internal state so it can be restored later,
without exposing that state. The Originator (TextEditor) creates Mementos, and the
Caretaker (History) stores them and hands them back to undo."""


class Memento:
    """Snapshot of the originator's state. Only the originator reads it."""
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state


class TextEditor:
    """Originator: owns the state and knows how to save/restore it."""
    def __init__(self):
        self.text = ""

    def write(self, words: str) -> None:
        self.text += words

    def save(self) -> Memento:
        """Create a memento with the current text."""
        return Memento(self.text)

    def restore(self, memento: Memento) -> None:
        """Go back to the text stored in the memento."""
        self.text = memento.get_state()


class History:
    """Caretaker: keeps the mementos but never looks inside them."""
    def __init__(self):
        self._mementos: list[Memento] = []

    def push(self, memento: Memento) -> None:
        self._mementos.append(memento)

    def pop(self) -> Memento:
        return self._mementos.pop()


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello")
    history.push(editor.save())

    editor.write(", world")
    history.push(editor.save())

    editor.write("!!! typo")
    print(f"Current text: {editor.text!r}")

    editor.restore(history.pop())  # undo
    print(f"After undo:   {editor.text!r}")

    editor.restore(history.pop())  # undo again
    print(f"After undo:   {editor.text!r}")
