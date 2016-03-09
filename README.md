# Bargain Hunt
Developed by: Edvinas Kilbauskas, Zac Davies, Kelly Sam, Hend Almalik, Tom Hazell, Alex Stacey

TABLE OF CONTENTS:

1) ABOUT
2) HOW TO USE GITHUB
3) NAMING CONVETNIONS



HOW TO USE GITHUB:

If you want to submit a change you have to:

    1) PULL (download everything) from the repository     (git pull)
    2) Change or ADD files you want                       (git add)
    3) COMMIT changes with an appropriate comment         (git commit)
    4) PUSH (upload to server) changes to server          (git push)
	

-----------------------------NAMING CONVENTION:-----------------------------

We need mutual agreement on naming conventions so that the could would look nicer and there would be less misunderstandings when using someone else's written code. If this is alright with everyone, we will using PIP8 naming conventions. As it is the standard way of writing python.

Class names:
 Should always start with uppercase letter and each new word should start with uppercase letter:

    class VectorThing:
        __init__(self, x, y):
            self.x = x
            self.y = y
	
Method, function names should all be in a lower case:
        def method_name(self, argumentFirst, argumentSecond):
                x = ...
                y = ...
                count = ...
                otherThing = ...
                nextThing = ...
                otherFucntion(count,otherThing,nextThing)
                return VectorThing(x,y)

3) Classes should have no private attributes



