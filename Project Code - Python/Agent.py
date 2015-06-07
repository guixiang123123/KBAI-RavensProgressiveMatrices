# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
	# problem.name - string containing the name of the problem
	# problem.problemType - string containing the type of problem
	# problem.hasVisual - boolean on if pictures included
	# problem.hasVerbal - boolean on if text included
	# problem.figures - dictionary for figures & solutions

        # Get all the objects in a figure (if verbal)
        def GetVerbalObjs(Figure):
            Objs = []
            for obj in list(Figure.objects):
                Objs.append([Figure.objects[obj].name, Figure.objects[obj].attributes])
            return Objs

        # Calculate the difference between two objects in regards to attributes
        def CalcObjDelta(Obj1, Obj2):
            Value = 0
            Delta = {}
            Attr1 = list(Obj1)
            Attr2 = list(Obj2)
            for Attr in Attr1:
                if Attr in Obj2:
                    if Obj1[Attr] != Obj2[Attr]:
                        Value += 1
                        Delta[Attr]=[Obj1[Attr],Obj2[Attr]]
                else:
                    Value+=1
                    Delta[Attr]=[Obj1[Attr],None]
            for Attr in Attr2:
                if Attr not in Obj1:
                    Value+=1
                    Delta[Attr]=[None,Obj2[Attr]]
            return [Value, Delta]

        # Match up objects between two different figures
        def FigureObjMatch(Fig1, Fig2):
            Objs1 = GetVerbalObjs(Fig1)
            Objs2 = GetVerbalObjs(Fig2)
            return None

        if problem.problemType == "2x2":
            TopLeft = problem.figures['A']
            TopRight = problem.figures['B']
            BotLeft = problem.figures['C']
            Solutions = [problem.figures['1'], problem.figures['2'],
	    	             problem.figures['3'], problem.figures['4'],
	                     problem.figures['5'], problem.figures['6']]
            if problem.hasVerbal:
                TLO = GetVerbalObjs(TopLeft)
                TRO = GetVerbalObjs(TopRight)
                BLO = GetVerbalObjs(BotLeft)
                SLO = []
                for Sol in Solutions:
                    SLO.append(GetVerbalObjs(Sol))
                print problem.name
                print TLO
                print TRO
                [V,D] = CalcObjDelta(TLO[0][1],TRO[0][1])
                print V
                print D


        if problem.problemType == "3x3":
            TopLeft = problem.figures['A']
            TopCenter = problem.figures['B']
            TopRight = problem.figures['C']
            MidLeft = problem.figures['D']
            MidCenter = problem.figures['E']
            MidRight = problem.figures['F']
            BotLeft = problem.figures['G']
            BotCenter = problem.figures['H']
            Solutions = [problem.figures['1'], problem.figures['2'],
	   		     problem.figures['3'], problem.figures['4'],
			     problem.figures['5'], problem.figures['6'],
			     problem.figures['7'], problem.figures['8']]

        BestGuess = 1
        ActualSolution = problem.checkAnswer(int(BestGuess))
        return BestGuess

