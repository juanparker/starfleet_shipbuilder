from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Input, Static, ProgressBar
from textual.widgets import Label
from textual.widget import Widget
from textual.reactive import reactive


class StatusBar(Widget):
    """A labeled progress bar widget."""

    def __init__(self, label: str, value: int = 0, maximum: int = 100) -> None:
        super().__init__()
        self.label_text = label
        self.value = reactive(value)
        self.maximum = reactive(maximum)

    def compose(self) -> ComposeResult:
        yield Label(self.label_text)
        yield ProgressBar(total=self.maximum, show_percentage=True, id="bar")

    def watch_value(self, old: int, new: int) -> None:
        bar = self.query_one("#bar", ProgressBar)
        bar.update(self.value, total=self.maximum)


class BuilderApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    #window {
        width: 60%;
        min-height: 70%;
        border: round yellow;
        padding: 2 4;
    }

    #input-container {
        layout: horizontal;
        height: auto;
    }

    #progress-container {
        border: round green;
        padding: 1 2;
        margin-top: 1;
    }

    #component-box {
        border: round blue;
        height: 8;
        content-align: center middle;
        margin-top: 1;
    }

    ProgressBar {
        height: 1;
    }
    """

    def compose(self) -> ComposeResult:
        with Container(id="window"):
            with Container(id="input-container"):
                yield Static("Ship Name:")
                yield Input(placeholder="Enter name", id="ship-name")
            yield Static("=== Build Progress ===", id="progress-label")
            with Container(id="progress-container"):
                self.mass_bar = StatusBar("Mass      ", 40, 100)
                self.volume_bar = StatusBar("Volume    ", 30, 100)
                self.power_bar = StatusBar("Power Draw", 20, 100)
                self.crew_bar = StatusBar("Crew      ", 10, 100)
                yield self.mass_bar
                yield self.volume_bar
                yield self.power_bar
                yield self.crew_bar
            yield Static("Select Component:", id="component-box")

    async def on_ready(self) -> None:
        await self.set_focus(self.query_one("#ship-name", Input))


if __name__ == "__main__":
    app = BuilderApp()
    app.run()
