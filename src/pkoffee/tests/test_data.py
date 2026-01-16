def test_initial():
    from pkoffee.data import load_csv,pd

    assert 1 == 1
    #assert fibonacci(1) == 1


def test_load_csv():
    from pkoffee.data import load_csv
    from pathlib import Path

    df = load_csv(Path("analysis/coffee_productivity.csv"))
    assert not df.empty
    assert "productivity" in df.columns
    assert "cups" in df.columns
