from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Static, Input, ProgressBar


class ShipBuilderUI(App):
    """A simple Textual UI mockup for building a starship."""

    CSS = """
    Screen {
        align: center middle;
        background: black;
        color: green;
    }

    #window {
        border: round green;
        padding: 1 2;
        width: 60;
    }

    .label {
        width: 12;
        text-align: right;
        padding-right: 1;
    }

    #progress-title {
        dock: top;
        margin-top: 1;
        text-align: center;
    }

    .progress-row {
        height: auto;
        align: left middle;
        margin: 0 0 1 0;
    }

    #component-box {
        border: round green;
        height: 10;
        margin-top: 1;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Container(self._build_window(), id="window")

    def _build_window(self) -> Container:
        window = Container()
        # Ship name row
        with window:
            with Horizontal():
                window.mount(Static("Ship Name:", classes="label"))
                window.mount(Input(placeholder="Enter name", id="ship-name"))

            window.mount(Static("=== Build Progress ===", id="progress-title"))

            # Progress bars with placeholder values
            stats = [
                ("Mass", 70, 100),
                ("Volume", 40, 100),
                ("Power Draw", 20, 100),
                ("Crew", 15, 100),
            ]
            for label, value, total in stats:
                with Horizontal(classes="progress-row"):
                    window.mount(Static(f"{label:10}:", classes="label"))
                    bar = ProgressBar(total=total, show_eta=False)
                    bar.update(progress=value)
                    window.mount(bar)

            window.mount(Static("Select Component:", id="component-label"))
            window.mount(Static("(component list goes here)", id="component-box"))
        return window


if __name__ == "__main__":
    app = ShipBuilderUI()
    app.run()
