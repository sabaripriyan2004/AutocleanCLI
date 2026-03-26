import typer
from cleanmydata.loader import load
from cleanmydata.analyzer import analyze
from cleanmydata.cleaner import clean

app = typer.Typer(invoke_without_command=True)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        pass

@app.command()
def run(file: str):
    print("Running cleanmydata...\n")

    # Load
    df = load(file)

    # Analyze
    report = analyze(df)

    print("\nAnalysis Result:\n")
    for col, info in report.items():
        print(f"{col} -> {info}")

    # Intelligent Cleaning
    df = clean(df)

if __name__ == "__main__":
    app()