def score_risks(unscored, scored):
    """Processes unscored risks and moves them to a new list."""
    while unscored:
        processing = unscored.pop()
        print(f"The {processing} risk is being scored.")
        scored.append(processing)

def show_scored(scored):
    """Shows which risks have been scored."""
    print(f"\nScored Risks:")
    for risk in scored:
        print({risk})