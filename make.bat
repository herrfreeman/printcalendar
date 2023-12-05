del calendar_*
py main.py
for %%f in (*.tex) do latex -output-format=pdf %%f
del calendar_*.aux
del calendar_*.log
del calendar_*.tex


