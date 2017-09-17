import pandas as pd
import numpy as np

arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
    np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])]



s = pd.DataFrame(index=arrays)
s2 = pd.MultiIndex.from_product([np.array(['bar',  'baz',  'foo',  'qux']),np.array(['one', 'two'])])
                                
print (s)
print(s2)
