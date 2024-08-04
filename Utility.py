class Utility:

        def recursive(self,start:int,table:int,times = 10):
            """recursive method that will print the tables with given times.
            Parameters:
            start - Which place is the table start from.
            times - How much time is table printed, By default 10
            table - What table"""
            print(table * start)
            if start == times:
                return
            start += 1
            return self.recursive(start,table,times)


if __name__ == "__main__":
    tables = Utility()
    tables.recursive(1,3,20)