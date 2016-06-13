def jump_in_rain(height):
    """Compute number of droplets when Totoro jumps.

    Args:
        height: (float) altitude reached by totoro

    Returns:
        (int) number of droplets
    """
    if height < 0:
        raise ValueError("totoro jumps above ground")

    return height * 10
