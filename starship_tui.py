from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Input, ProgressBar

class ProgressRow(Horizontal):
    def __init__(self, label: str, value: int, total: int, **kwargs):
        super().__init__(**kwargs, classes="progress-row")
        self.label_text = label
        self.value = value
        self.total = total

    def compose(self) -> ComposeResult:
        yield Static(f"{self.label_text:>10} : ", classes="stat-label")
        bar = ProgressBar(total=self.total, show_eta=False)
        bar.update(progress=self.value)
        yield bar


class ShipBuilderUI(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #panel {
        border: round green;
        width: 60;
        padding: 1 2;
    }
    .progress-row {
        height: auto;
        padding: 0 1;
    }
    .stat-label {
        width: 14;
    }
    #component-box {
        border: round blue;
        height: 5;
        content-align: center middle;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        with Container(id="panel"):
            with Horizontal():
                yield Static("Ship Name:")
                yield Input(id="ship-name", placeholder="Enter name")
            yield Static("=== Build Progress ===", id="progress-title")
            yield ProgressRow("Mass", 40, 100)
            yield ProgressRow("Volume", 30, 100)
            yield ProgressRow("Power Draw", 20, 100)
            yield ProgressRow("Crew", 5, 20)
            yield Static("Select Component:", id="component-label")
            yield Static("", id="component-box")


if __name__ == "__main__":
    app = ShipBuilderUI()
    app.run()
