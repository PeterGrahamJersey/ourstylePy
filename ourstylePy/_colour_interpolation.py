# Colour interpolators
# Sources:
# Color Gradient functions adapted from 'Color Gradients with Python' (Ben Southgate, 2017)
# https://bsou.io/posts/color-gradients-with-python
# Colour type conversion:
# https://python-colormath.readthedocs.io/en/latest/index.html
# We convert RGB -> CIE Lab, then apply linear interpolation to generate Gradients
# https://mode.com/blog/how-to-use-brand-color-palette-in-data-visualizations
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

def _hex_to_lab_tuple(hex):
    rgb = sRGBColor.new_from_rgb_hex(hex)
    lab = convert_color(rgb, LabColor)
    return LabColor.get_value_tuple(lab)

def _lab_to_hex(lab):
    rgb = convert_color(lab, sRGBColor)
    return sRGBColor.get_rgb_hex(rgb)

def _linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
    ''' returns a gradient list of (n) colors between
    two hex colors. start_hex and finish_hex
    should be the full six-digit color string,
    inlcuding the number sign ("#FFFFFF") '''
    # Starting and ending colors in RGB form
    s = _hex_to_lab_tuple(start_hex)
    f = _hex_to_lab_tuple(finish_hex)
    # Initilize a list of the output colors with the starting color
    lab_list = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate lab vector for color at the current value of t
        curr_vector = [
            int(s[j] + (float(t)/(n-1))*(f[j]-s[j]))
            for j in range(3)
        ]
        # Add it to our list of output colors
        lab_list.append(curr_vector)

    # Convert back to RGB
    hex_list = [_lab_to_hex(LabColor(lab[0], lab[1], lab[2])) for lab in lab_list]
    return hex_list

def _polylinear_gradient(colors, n):
  ''' returns a list of colors forming linear gradients between
      all sequential pairs of colors. "n" specifies the total
      number of desired output colors '''
  # The number of colors per individual linear gradient
  n_out = int(float(n) / (len(colors) - 1))
  # returns array of hexcodes
  gradient = _linear_gradient(colors[0], colors[1], n_out)

  if len(colors) > 1:
    for col in range(1, len(colors) - 1):
      next = _linear_gradient(colors[col], colors[col+1], n_out)
      # Exclude first point to avoid duplicates
      gradient += next[1:]

  return gradient
