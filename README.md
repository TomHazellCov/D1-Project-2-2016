# Bargain Hunt
Developed by: Edvinas Kilbauskas, Zac Davies, Kelly Sam, Hend Almalik, Tom Hazell, Alex Stacey

HOW TO USE GITHUB:

If you want to submit a change you have to:

    1) PULL (download everything) from the repository     (git pull)
    2) Change or ADD files you want                       (git add)
    3) COMMIT changes with an appropriate comment         (git commit)
    4) PUSH (upload to server) changes to server          (git push)
	

Tom Hazell Individual part: GenarateItemList.py: This fills the DB with popular items from tescos website. 
Tested with python version 3.4, should work with any version 3.3+
Dependencys: bs4(pip), selenium(pip), PhantomJS(binery in path or wirking dir), kivy(installer), PyQt(installer)
	
Required parts of the program:

	Main Screen(robot's navigation, kivy)
	
	Robot Controler (telling the robot where to go and what to pick up)
	
	ItemEditor(PyQt)
	
	Settings(PyQt)
	
	SQL(for retreving/saving items)
	
	Saveing settings(JSON)
	
	SortedListView(PyQt)
	

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



