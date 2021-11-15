[1]. ERROR

```
We reached our target!
Objective:         31.5109
Max update time:   130.915 ms
Av update time:    48.0859 ms
Traceback (most recent call last):
  File "omg.py", line 33, in <module>
    problem.save_movie('scene')
  File "/usr/local/lib/python3.8/dist-packages/omgtools/execution/plotlayer.py", line 364, in save_movie
    from matplotlib2tikz import save as tikz_save
  File "/usr/local/lib/python3.8/dist-packages/matplotlib2tikz/__init__.py", line 29, in <module>
    raise RuntimeError("matplotlib2tikz has been renamed to tikzplotlib <https://pypi.org/project/tikzplotlib>")
RuntimeError: matplotlib2tikz has been renamed to tikzplotlib <https://pypi.org/project/tikzplotlib>
```
Solution:
1. code /usr/local/lib/python3.8/dist-packages/omgtools/execution/plotlayer.py
2. Goto line 364
3. Modify
```
  # from matplotlib2tikz import save as tikz_save #old for python2
            from tikzplotlib import save as tikz_save #new <== for python3, why? "RuntimeError: matplotlib2tikz has been renamed to tikzplotlib"
```


[2]. ERROR: ModuleNotFoundError: No module named 'tikzplotlib'

Solution: pip3 install tikzplotlib


[3]. ERROR:
```
We reached our target!
Objective:         31.5109
Max update time:   117.075 ms
Av update time:    53.6487 ms
Traceback (most recent call last):
  File "omg.py", line 33, in <module>
    problem.save_movie('scene')
  File "/usr/local/lib/python3.8/dist-packages/omgtools/execution/plotlayer.py", line 395, in save_movie
    tikz_save(path, figurewidth=figurewidth,
  File "/home/rajendra/.local/lib/python3.8/site-packages/tikzplotlib/_save.py", line 260, in save
    code = get_tikz_code(*args, filepath=filepath, **kwargs)
TypeError: get_tikz_code() got an unexpected keyword argument 'figurewidth'
```

Solution:
1. code /usr/local/lib/python3.8/dist-packages/omgtools/execution/plotlayer.py
2. Goto line 394-395
3. Modify
```
                    if figureheight is None:
                        # tikz_save(path, figurewidth=figurewidth, #old
                        tikz_save(path, axis_width=figurewidth, #new <== why? https://github.com/nschloe/tikzplotlib/issues/421
                                  extra_axis_parameters={'scale only axis=' +
                                         str(scaleonlyaxis).lower()})
                        # tikz requires a lowercase true/false
                    else:
                        # tikz_save(path, figurewidth=figurewidth, #old
                        #           figureheight=figureheight,     #old
                        tikz_save(path, axis_width=figurewidth,    #new <== why? https://github.com/nschloe/tikzplotlib/issues/421
                                  axis_height=figureheight,        #new
                                  extra_axis_parameters={['scale only axis=' +
                                          str(scaleonlyaxis).lower()]})
                        # tikz requires a lowercase true/false
                    _cleanup_rubbish(path, info, root)
```
