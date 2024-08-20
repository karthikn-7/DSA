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
        
        def printFromN(self,n):
            """Prints from 1 to the n numbers"""
            if n == 1:
                print(n)
                return 1
            print(n)
            return n - self.printFromN(n - 1)
        
        def printFromOne(self,n):
            if n > 0:
                self.printFromOne(n - 1)
                print(n)

        def factorial(self,n):
            if n == 1:
                return 1
            else:
                return n * self.factorial(n - 1)
                
        def is_palindrome_num(self,num):

            num = str(num)
            front = 0
            last = len(num) - 1

            while front <= last:
                if num[front] != num[last]:
                    return False
                front += 1
                last -= 1
            
            return True

        


if __name__ == "__main__":

    rec = Utility()
    print(rec.is_palindrome_num(10023001))