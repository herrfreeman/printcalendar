import calendar

monthNames = ['ЯНВАРЬ','ФЕВРАЛЬ','МАРТ','АПРЕЛЬ','МАЙ','ИЮНЬ','ИЮЛЬ','АВГУСТ','СЕНТЯБРЬ','ОКТЯБРЬ','НОЯБРЬ','ДЕКАБРЬ']

year = 2023
cal = calendar.Calendar()
outputFile = open('calendar.tex','w', encoding='utf8')
print(r'''\documentclass[12pt]{article}
\usepackage[T2A]{fontenc}
\usepackage{geometry}
\usepackage{tabularx}
\geometry{margin=1cm}
\begin{document}
''', file=outputFile)


for month in range(1,13):
    print(r'\begin{center} \huge{%s} \\ ' % monthNames[month-1], file=outputFile)
    print(r'''\end{center}
  \begin{center}
  \begin{tabularx}{1\textwidth} { 
  | >{\centering\arraybackslash}X 
  | >{\centering\arraybackslash}X 
  | >{\centering\arraybackslash}X 
  | >{\centering\arraybackslash}X 
  | >{\centering\arraybackslash}X 
  | >{\centering\arraybackslash}X 
  | >{\centering\arraybackslash}X   
  | }
  \hline
  \huge{ПН} & \huge{ВТ} & \huge{СР} & \huge{ЧТ} & \huge{ПТ} & \textbf{\huge{СБ}} & \textbf{\huge{ВС}} \\ 
  \hline''', file=outputFile)
    monthCalendar = cal.monthdayscalendar(year,month)
    rowHeight = round(20 / len(monthCalendar),2)


    for week in monthCalendar:
        weekStr = ''
        for dayNum in range(0,7):
            day = ''
            if week[dayNum] > 0:
                day = r'\huge{%s}' % week[dayNum]
            if dayNum < 5:
                weekStr += day
            else:
                weekStr += r'\textbf{%s}' % day
            if dayNum < 6:
                weekStr += '&'

        print(weekStr, r'\\ [%scm] \hline' % rowHeight, file=outputFile)

    print(r'\end{tabularx} \end{center}', file=outputFile)
    if month < 12:
        print(r'\newpage', file=outputFile)

print(r'\end{document}', file=outputFile)