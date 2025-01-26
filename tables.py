
import math, csv
class Table:
    def __init__(self,content,padx = 1):
        if type(content) != list or type(content) != tuple:
            if type(content) == str:
                with open(content, "r") as file:
                    content = list(csv.reader(file))
        
        content = [[(str(item) + '') for item in sublist] for sublist in content]
        self.content = content
        self.padx = padx
        self.no_rows = len(self.content[0])
        self.no_columns = len(self.content)
        
        #temp var
        maxsize_columns = [0 for x in self.content[0]]
        for columns in self.content:
            for j in range(len(columns)):
                maxsize_columns[j] = len(columns[j]) if maxsize_columns[j] < len(columns[j]) else maxsize_columns[j]    
            if self.no_rows != len(columns) or type(columns) != list and type(columns) != tuple:
                raise ValueError
        self.maxsize_columns = maxsize_columns
    def disp_table(self,style = "smooth", bg = " "):
        padx = self.padx
        #designs = {top left(tl), top right(tr), bottom left(bl), bottom right(br), horizontal(h), vertical(v), top intersection(ti), bottom intersection(bi), left intersection(li), right intersection(ri), middle intersection(mi)}
        #style = {"tl":"", "tr": "", "bl":"", "br":"", "h":"", "v":"", "ti":"", "bi":"", "li":"", "ri":"", "mi":""}
        style_1 = {"tl":"╭", "tr": "╮", "bl":"╰", "br":"╯", "h":"─", "v":"│", "ti":"┬", "bi":"┴", "li":"├", "ri":"┤", 'mi':"┼"}
        style_2 = {"tl":"┌", "tr": "┐", "bl":"└", "br":"┘", "h":"─", "v":"│", "ti":"┬", "bi":"┴", "li":"├", "ri":"┤", "mi":"┼"}
        style_3 = {"tl":"┏", "tr": "┓", "bl":"┗", "br":"┛", "h":"━", "v":"┃", "ti":"┳", "bi":"┻", "li":"┣", "ri":"┫", "mi":"╋"}
        style_4 = {"tl":"*", "tr": "*", "bl":"*", "br":"*", "h":"-", "v":"|", "ti":"-", "bi":"-", "li":"|", "ri":"|", "mi":"*"}
        style_5 = {"tl":"*", "tr": "*", "bl":"*", "br":"*", "h":"*", "v":"*", "ti":"*", "bi":"*", "li":"*", "ri":"*", "mi":"*"}
        match style:
            case "smooth":
                units = style_1
            case "basic":
                units = style_2
            case "basicThicc":
                units = style_3
            case "classic":
                units = style_4
            case "stars":
                units = style_5
            case _:
                units = style_1
        #init helps to check where the programme is running (like the top of the table or the bottom of the table)
        init = 0
        temp = len(self.content) - 1
        for row in range(len(self.content)):
            #to print the first grid line
            if init == 0:
                print(units["tl"],end = '')
                
            for column_index in range(len(self.maxsize_columns)):
                #prints the top horizonal grid line of the element in the row index 'row' and in the column index 'column'
                print(units["h"] * 2 * padx + units["h"] * self.maxsize_columns[column_index], end = '')
                
                #if the programme is running the top line of the table and not in the last row of the column
                if column_index != len(self.maxsize_columns) - 1 and init == 0:
                    print(units['ti'], end = '')

                #if the prgm is running the mid section of the table
                elif column_index != len(self.maxsize_columns) - 1:
                    print(units['mi'], end = '')
                
                #if the prgm is in the top and is in the final row of the column
                elif init == 0:
                    print(units['tr'])

                #print the right intersection
                else:
                    print(units['ri'])
                    
                    
            for j in range(len(self.content[row])):
                spacing = (self.maxsize_columns[j] - len(self.content[row][j]))/2
                if spacing%1 != 0:
                    spacing = [math.floor(spacing) + i for i in reversed(range(2))]
                else:
                    spacing = [math.floor(spacing) for i in range(2)]
                print(units["v"] + bg * padx + bg * spacing[0] + self.content[row][j] + bg * spacing[1] + bg * padx, end = '')
            print(units['v'])
            if init != temp:
                print(units["li"],end = '')
            else:
                print(units["bl"],end = '')
                for j in range(len(self.maxsize_columns)):
                    ending = units["bi"] if len(self.maxsize_columns) - 1 != j else ''
                    print(units["h"] * 2 * padx + units["h"] * self.maxsize_columns[j], end = ending)
                print(units["br"])
            init+=1
        
if __name__ == '__main__':
    eg = [
        ("Experiment no.", "Trial no.", "Result"),
        ("12",1,"Pass"),
        ("12",2,"Fail"),
        ("12",3,"Pass"),
        ("12",4,"Fail"),
        ("12",5,"Fail"),
        ("12",6,"Pass"),
    ]
    root = Table(eg, padx = 5)
    root.disp_table(style = "smooth")


# bg = "█"