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

        def iter_fact(self,num):
            total = 1
            for i in range(1,num+1):
                total = total * i
            return total

        def recur_fact(self,n):

            if n == 1:
                return 1
            return n * self.recur_fact(n - 1)



if __name__ == "__main__":

    rec = Utility()
    print(rec.recur_fact(5))
