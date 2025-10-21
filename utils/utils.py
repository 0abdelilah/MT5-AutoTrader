
def percent_to_color(percent: float) -> str:
    r = int(255 - (percent * 2.55))   # goes from 255 → 0
    g = int(percent * 2.55)           # goes from 0 → 255
    b = 0
    return f"\033[38;2;{r};{g};{b}m"