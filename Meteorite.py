"""Meteorite"""
def main(met_weight, num_broken, weight_safe):
    """Meteorite"""
    missile = 0
    num_met = 1
    while met_weight >= weight_safe:
        missile += num_met
        met_weight = met_weight / num_broken
        num_met = num_met * num_broken
    print(missile)
main(float(input()), int(input()), float(input()))
