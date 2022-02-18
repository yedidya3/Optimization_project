# Optimization_project
Run codes for a project in an Introduction to Optimization course

# הוראות הרצה:
יש להוריד את כל הקבצים לתיקייה אחת ואז לבצע את ההוראות למטה

הקוד מתאים לריצה על מערכת הפעלה לינוקס עם פייתון 3

יצירת דאטה לבעיית הסוכן הנוסע:
לצורך הכנת הדאטה יש להריץ את הקובץ create_table_distance.py בפייתון 3 
הרצתו תיצור 500 קבצי מידע לקלט לקבצי הרצה של בעיות הסוכן הנוסע עם בשמות "TSPdataSIZE.csv" כאשר SIZE זהו משתנה של גודל המסמך

הרצת הסוכן הנוסע בשיטת ACO:

יש להריץ את הפקודה python3 run_tsp_ACO.py fileNameOfData כאשר fileNameOfData זה שם הקובץ של המידע שברצוננו להריץ.

הרצת הסוכן הנוסע בשיטת BNB:

יש להריץ את הפקודה python3 run_tsp_BNB.py fileNameOfData כאשר fileNameOfData זה שם הקובץ של המידע שברצוננו להריץ.

הרצת N מלכות בשיטת ACO:

יש להריץ את הפקודה python3 run_N_Queens_ACO.py SIZE כאשר SIZE זה מספר המלכות שברצוננו להריץ

הרצת N מלכות בשיטת BNB:

יש להריץ את הפקודה python3 run_N_Queens_BNB.py SIZE כאשר SIZE זה מספר המלכות שברצוננו להריץ.

התוצאות של ההרצות שאנו ביצענו מופיעות בתיקיות הresults בהתאמה, בנוסף יש בתוך כל תיקייה מחברת ipynb של ניתוח הקבצים ויצירת גרפים מתאימים של התוצאות.

# שמירת נתוני הריצות
בכל ריצה הנתונים של הריצה ישמרו בקבצים מותאמים:

עבור בעיית N_queens ע"י BNB הנתונים ישמרו בקבצים: memory_BNB_N_queens, time_BNB_N_queens.
עבור בעיית N_queens ע"י ACO הנתונים ישמרו בקבצים: memory_ACO_N_queens,time_ACO_N_queens.


עבור בעייתTSP ע"י BNB הנתונים ישמרו בקבצים: time_BNB_TSP,memory_BNB_TSP,length_path_BNB_TSP.
עבור בעיית TSP ע"י ACO הנתונים ישמרו בקבצים: time_ACO_TSP,memory_ACO_TSP,length_path_ACO_TSP.
