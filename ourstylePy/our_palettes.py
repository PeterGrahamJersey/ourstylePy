import data
import our_colours

def our_palettes(palette = None, n = None, reverse = False):
    '''
    Access our colour palettes as hexcodes

    - palette: string,  which palette should be accessed, should match a name from our_palettes_raw
    - n: integer, number of colours to generate from palette
    - reverse: boolean, should the order of colours be reversed?

    Returns: If palette is NA, return the raw palette data. If n is NA, return
    the hexcodes of colours in the data, otherwise return n colours interpolated
    from the chosen palette

    Examples:
    our_palettes()
    our_palettes('default')
    our_palettes('default', reverse = TRUE)
    our_palettes('default', 10)
    our_palettes('default', 2)
    '''
    if palette is None:
        return data.our_palettes_raw
    else:
        if n is None:
            pal = our_colours.our_colours(data.our_palettes_raw[palette])
            if reverse:
                pal = rev(pal)
            return pal
        else:
            return our_palettes_interpolator(palette, reverse)(n)
