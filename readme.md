# Matplotlib Tips and Examples

This is ongoing and constantly updated for new tips and tricks. While it is *lightly* organized, the main idea is as a dumping ground.

As of 2019-12-06, all examples are developed and tested with Python 3.6+ only. However, I will *try* to avoid using non-compatible syntax when I can.

I will also *focus* on the object-oriented interface falling back to pyplot (i.e. `plt`) when needed or to generate the figures

## Preambles

All notebooks start with the following (though `%matplotlib inline` may be omitted at times)

```python
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
%matplotlib inline 

import sys

print('Matplotlib Version: ' + mpl.__version__)
print('NumPy Version: ' + np.version.full_version)
print('Python Version: ' + sys.version)

import datetime
now  = datetime.datetime.now().isoformat()
print('Ran on ' + now)
```


## Sections

* [Fonts and Scientific Notation](Plotting_Fonts_and_Sci_Notation.ipynb)
* [Subplots](subplots.ipynb)
* [Ticks, Grids, Labels, and Legends](ticks_grids_labels_legends.ipynb)
* [Colorbars](Colorbars.ipynb)
* [Line Colors](Line_Colors.ipynb)
* [Multiple Y-Axes](Multiple_YAxes.ipynb)
* [3D Plots: Contours and Surfaces](Three_Dimensional_Data.ipynb)
* [Pathes and Hatches](Patches_and_Hatches.ipynb)
* [Inset Plots](Inset_Plots.ipynb)
* [Bar Charts](Bar_Charts.ipynb)
* [Scattered Data](Scattered_Data.ipynb)
* [Scaled Colors](Scaled_Colors.ipynb)
* [Styles -- Custom and Built-in](Styles.ipynb)
* [Visualizing Arrays](Visualize_Arrays.ipynb)
* [Misc](Misc.ipynb)

## Export Issues

By default, Jupyter exports images as `png`. In addition, at least with Chrome, only `png` can be viewed

Below is the command to export as PDF as well. However, markdown export tends to break (doesn't show images) when you do both exports. See workaround below

```python
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png','pdf')  # Exports both png and pdf. See below for issues
set_matplotlib_formats('png') # Just pngs. Good for development
```

### Markdown Export Workaround

As noted above, markdown export images do not work with the PDF option (though PDF export does work). The workaround is as follows:

1. Include the above code block, run the code, export as markdown
2. Remove the above code (or just have `set_matplotlib_formats('png')`), run the code, export to markdown
3. Find/Replace `png)` with `pdf)` and copy the corresponding pdf files into that directory



## Changelog

* 2018-09-21 - Added color controls. Removed the function demo for `pcolormesh` since it didn't add anything. Added palette plots 
* 2018-10-30 - Added my style and also updated how to remove an axis
* 2018-12-06 - Minor fix with regular bar charts. Added stacked. Noted python 2 vs 3
* 2019-12-06 - Reworked into multiple notebooks
