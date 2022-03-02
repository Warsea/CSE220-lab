'''
Name: Warsi Sarjeel Rahman
ID: 21101057

Running the file should output the answers in order. 

For questions where the output is a manipulated version of the source array(Example: Linear array question 1), only the output is printed.
For questions where the output something other than a manipulated array(Example: linear array question 5), the source array is printed alongside the output, as printing the instance displays the format along with the question count.

'''

import random


class LinearArray:
    question_count = 0
    def __init__(self, source):
        self.s = source

    # 1
    def shiftLeft(self, m):
        i = 0
        while i< len(self.s):
            if i+m >= len(self.s):
                self.s[i] = 0
                i+=1
            else:
                self.s[i] = self.s[i+m]
                i+=1

    # 2
    def rotateLeft(self, k):
        i = 0
        while i< len(self.s):
            if i+k >= len(self.s):
                i+=1
            else:
                temp = self.s[i]
                self.s[i] = self.s[i+k]
                self.s[i+k] = temp
                i+=1

    # 3
    def remove(self, size, idx):
        self.s[idx] = 0
        i = idx
        while i<size:
            if i+1>=size:
                self.s[i]= 0
                i+=1
            else:
                self.s[i] = self.s[i+1]
                i+=1

    # 4
    def removeAll(self, size, item):
        i = 0
        while i < size:
            if self.s[i] == item:
                self.remove(size, i)
                i-=1
            i+=1 

    # 5
    def balancinator(self):
        i = 0 
        output= 'false'
        while i<len(self.s):
            j = 0
            count_left = 0
            count_right = 0
            while j<len(self.s):
                if j < i:
                    count_left+= self.s[j]
                else:
                    count_right+= self.s[j]
                j+=1
            if count_left == count_right:
                output='true'
            i+=1
        print(output)

    # 6
    @staticmethod
    def patternedReverse(l, n, start, skip):
        i = start
        end = start + n
        while i < end:
            if i<start + skip:
                pass
            else:
                l[i] = n - (i - start)
            i+=1

    @classmethod
    def seriesinator(cls, n):
        l= [0]*n*n
        i = 0
        skip = n-1
        while i< len(l):
            cls.patternedReverse(l,n,i, skip)
            i+=n
            skip-=1
        return cls(l)

    # 7
    def largest_bunch(self):
        i = 0
        count = 1
        largest_count = 1
        last = None
        while i< len(self.s):
            if last==None:
                last = self.s[i]
                i+=1
                continue

            if self.s[i] == last:
                count+=1
            else:
                count = 1
            if count >largest_count:
                    largest_count = count
            last = self.s[i]
            i+=1
        print(f"Largest bunch has {largest_count} items.")

    # 8
    def repitition(self):
        repitition_list = []
        output = False
        done = []
        for i in self.s:
            repeat = 0
            if i in done:
                continue
            for j in self.s:
                if i == j:
                    repeat +=1
                    
            if i not in done:
                done.append(i)
            
            if repeat in repitition_list:
                output = True
                break
            elif repeat>1:
                repitition_list.append(repeat)
        print(output)


    
    def __str__(self):
        print("==========")
        LinearArray.question_count+=1
        print(f"Question {self.question_count}\n")
        return str(self.s)


    
print("==========")
print("Linear Array")


source=[10,20,30,40,50,0,0]
shiftlist = LinearArray(source)
shiftlist.shiftLeft(3)
print(shiftlist)


source=[10,20,30,40,50,60]
rotatelist = LinearArray(source)
rotatelist.rotateLeft(3)
print(rotatelist)

source=[10,20,30,40,50,0,0]
removedlist = LinearArray(source)
removedlist.remove(5,2)
print(removedlist)

source=[10,2,30,2,50,2,2,0,0]
rmvOcc = LinearArray(source)
rmvOcc.removeAll(7, 2)
print(rmvOcc)

source =  [10, 3, 1, 2, 10]
is_balance = LinearArray(source)
print(is_balance)
is_balance.balancinator()

series = LinearArray.seriesinator(3)
print(series)


bunch = LinearArray([1, 2, 2, 3, 4, 4, 4])
print(bunch)
bunch.largest_bunch()

repeat = LinearArray([4,5,6,6,4,3,6,4])
print(repeat)
repeat.repitition()

print("===============")
print("Circular Array")

class CircularArray:
    question_count = 0
    def __init__(self, source):
        self.s = source

    # 1
    def pallindrome(self, start, size):
        length= len(self.s)
        output = True
        index=0 
        i= start
        j = (start+size-1)%length
        while index<start+size-1:
            if self.s[i] != self.s[j]:
                output = False 
                break
            i = (i+1)%length
            j = (j-1)%length
            index+=1
        print("Output:", output)

    # 2
    @classmethod       
    def intersection(cls, ca1, start1, size1, ca2, start2, size2):
        l = [0]*size1
        index1= 0
        i1 = start1
        l_i = 0
        while index1<size1:
            index2 = 0 
            i2 = start2
            while index2< size2:
                if ca1[i1] == ca2[i2]:
                    l[l_i] = ca1[i1]
                    l_i+=1
                index2+=1
                i2=(i2+1)%len(ca2)
            index1+=1
            i1=(i1+1)%len(ca1)
        return cls(l[:l_i])

    # 3
    @staticmethod
    def rotateClockwise(particpants=[3,4,2,5,1,6,7]):
        index=0
        i=0
        length = len(particpants)
        temp1 = particpants[i]
        while index< len(particpants):
            temp2 = temp1
            temp1 = particpants[(i+1)%length]
            particpants[(i+1)%length] = temp2
            i=(i+1)%length
            index+=1

    def playMusicalChair(self):
        while len(self.s)>1:
            self.rotateClockwise(self.s)
            stop_value = random.randint(0,3)
            if stop_value == 1:
                eliminated = len(self.s)//2
                new_chairs = [0]*(len(self.s)-1)
                i_new = 0
                i_old = 0
                while i_new<len(new_chairs):
                    if i_old== eliminated:
                        i_old+=1
                        continue
                    else:
                        new_chairs[i_new] = self.s[i_old]
                    i_new+=1
                    i_old+=1
                self.s = new_chairs
        return self.s[0]



    def __str__(self):
        print("==========")
        CircularArray.question_count+=1
        print(f"Question {self.question_count}\n")
        return str(self.s)


source = [20,10,0,0,0,10,20,30] 
pal = CircularArray(source)
print(pal)
pal.pallindrome(5,5)


source1 = [40,50,0,0,0,10,20,30]
source2 = [10,20,5,0,0,0,0,0,5,40,15,25]
intersect = CircularArray.intersection(source1, 5,5, source2, 8,7)
print(intersect)


players = ['Micheal', 'Jim', 'Pam', 'Dwight', "Karen",'Toby', 'Andy']
game = CircularArray(players)
print(game)
winner = game.playMusicalChair()
# The winner will be different for each game
print("Winner:", winner) 
