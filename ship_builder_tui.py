from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Input, Label, ProgressBar, Static

class ShipBuilderApp(App):
    """Simple Textual UI mimicking a starship builder screen."""

    CSS = """
    Screen {
        align: center middle;
    }

    #window {
        border: round yellow;
        padding: 2 4;
        width: 60%;
        min-width: 60;
    }

    #progress-container {
        padding-top: 1;
        padding-bottom: 1;
    }

    .progress-row {
        height: auto;
        padding: 0 0 1 0;
    }

    #component-box {
        border: round green;
        height: 10;
        content-align: center middle;
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        with Container(id="window"):
            with Horizontal(id="name-row"):
                yield Label("Ship Name:")
                yield Input(placeholder="Enter name", id="ship-name")
            yield Static("=== Build Progress ===", id="progress-title")
            with Container(id="progress-container"):
                yield self._progress_row("Mass", 50)
                yield self._progress_row("Volume", 70)
                yield self._progress_row("Power Draw", 30)
                yield self._progress_row("Crew", 20)
            yield Static("Select Component:", id="component-box")

    def _progress_row(self, label: str, value: int) -> Container:
        bar = ProgressBar(total=100)
        bar.update(progress=value)
        row = Horizontal(Label(f"{label: <10}"), bar, classes="progress-row")
        return row

if __name__ == "__main__":
    app = ShipBuilderApp()
    app.run()
