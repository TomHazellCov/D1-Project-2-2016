# Bargain Hunt

HOW TO USE GITHUB:

If you want to submit a change you have to: 
1) PULL (download everything) from the repository 				(git pull)
2) Change or ADD files you want									(git add)
3) COMMIT changes with an appropriate comment					(git commit)
4) PUSH (upload to server) changes to server					(git push)

Upload all screenshots, designs etc. to Documents folder.

Pong files will be deleted later on, they are here just for learning purposes (to get hang of how Kivy API works).

Also, don't worry about files ending with "~" character, these are backup files made by my (Ed) editor.

Each class(or a set of simmilar classes or functions) should have their own file. For example: SortingAlgorithms, SQLManager, Main etc.

-----------------------------IMPORTANT:-----------------------------

We need mutual agreement on naming conventions so that the could would look nicer and there would be less misunderstandings when using someone else's written code. If this is alright with everyone, we will use this NAMING CONVENTION:

1) Class names should always start with uppercase letter and each new word should start with uppercase letter:

    class VectorThing:
        __init__(self, x, y):
            self.x = x
            self.y = y
	
2) Method, function, variable, parameter and class attribute names should start with first lowercase letter and each new word should start with uppercase letter:

        def methodName(self, argumentFirst, argumentSecond):
                x = ...
                y = ...
                count = ...
                otherThing = ...
                nextThing = ...
                otherFucntion(count,otherThing,nextThing)
                return VectorThing(x,y)

3) Classes should have no private attributes



