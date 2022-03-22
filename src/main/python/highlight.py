from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat

# From https://stackoverflow.com/questions/57636321/highlighting-portions-of-text-in-qplaintextedit
class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super(SyntaxHighlighter, self).__init__(parent)
        self._highlight_lines = dict()

    def highlight_line(self, line, fmt):
        if isinstance(line, int) and line >= 0 and isinstance(fmt, QTextCharFormat):
            tb = self.document().findBlockByNumber(line)
            self._highlight_lines[tb.blockNumber()] = fmt
            self.rehighlightBlock(tb)

    def is_highlighted(self):
        return bool(self._highlight_lines)

    def clear_highlight(self):
        self._highlight_lines = dict()
        self.rehighlight()

    def highlightBlock(self, text):
        fmt = self._highlight_lines.get(self.currentBlock().blockNumber())
        if fmt is not None:
            self.setFormat(0, len(text), fmt)
