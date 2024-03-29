class Solution:
    def reformatDate(self, date: str) -> str:
        date, month, year = date.split()
        month_number = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09',"Oct":'10', "Nov":'11', "Dec":'12'}
        date = '0' + date[:-2] if len(date) == 3 else date[:-2]
        formated = [year,month_number[month], date]
        return '-'.join(formated)
        
