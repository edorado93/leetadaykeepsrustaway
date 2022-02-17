class Solution:
    def reformatDate(self, date: str) -> str:
        comp = date.split()
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day = comp[0][:-2]
        return "{0}-{1}-{2}{3}".format(comp[2], months[comp[1]], "0" if len(day) == 1 else "", day)
        
