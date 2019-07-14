import data

def our_colours(colours=[]):
  '''
  Extract hexcodes for our colours
  Returns a list of hexcodes for the specified colours.
  Method from https://drsimonj.svbtle.com/creating-corporate-colour-palettes-for-ggplot2.
  - colours, list of strings

  Returns a list of hexcodes for the specified colours. If a colour is
  not in our_colours_raw will return a keyerror.

  Examples:
  data.our_colours_raw
  our_colours()
  our_colours('green', 'blue', 'green')
  our_colours('not a colour', 'also not a colour', 'green')
  our_colors('blue')
  '''
  if len(colours) == 0:
    return data.our_colours_raw
  return [data.our_colors_raw[i] for i in colours]

def our_colors():
    '''
    Alias for our_colours()
    '''
    return our_colours()
