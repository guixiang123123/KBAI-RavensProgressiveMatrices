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

        # Clean up Attributes
        def CleanAttributes(Attributes):
            shapes={'circle':1,'triangle':3,'right-triangle':3,
                    'square':4,'rectangle':4,'diamond':4,'pentagon':5,
                    'hexagon':6,'octogon':8,'pac-man':2.5,'heart':1.5}
            size={'very small':0,'small':1,'medium':2,'large':3,
                  'very large':4,'huge':5}
            for Att in Attributes:
                if Att == 'shape':
                    if Attributes['shape'] in shapes:
                        Attributes['shape']=shapes[Attributes['shape']]
                if Att == 'size':
                    if Attributes['size'] in size:
                        Attributes['size']=size[Attributes['size']]
                if Att == 'inside':
                    Attributes['inside']=(len(str(Attributes['inside']))+1)/2
            return Attributes

        # Get all the objects in a figure (if verbal)
        def GetVerbalObjs(Figure):
            Objs = []
            for obj in list(Figure.objects):
                Objs.append([Figure.objects[obj].name, CleanAttributes(Figure.objects[obj].attributes)])
            return Objs

        # Calculate the difference between two objects in regards to attributes
        def CalcObjDelta(Obj1, Obj2):
            Value = 0
            Delta = {}
            Attr1 = list(Obj1)
            Attr2 = list(Obj2)
            for Attr in Attr1:
                if Attr in Obj2:
                    if (Obj1[Attr] != Obj2[Attr]) and (Attr == 'size'):
                        Value += 1.1
                        Delta[Attr]=[Obj1[Attr],Obj2[Attr]]
                    elif Obj1[Attr] != Obj2[Attr]:
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
            Score = []
            Delta = []
            for Obj1 in Objs1:
                SRow = []
                DRow = []
                for Obj2 in Objs2:
                    [V,D] = CalcObjDelta(Obj1[1], Obj2[1])
                    SRow.append(V)
                    DRow.append(D)
                Score.append(SRow)
                Delta.append(DRow)
            Match1 = []
            Match2 = []
            for i in range(len(Score)):
                LowestVal = None
                for j in range(len(Score)):
                    for k in range(len(Score[j])):
                        if ((LowestVal == None) and (j not in Match1) and (k not in Match2)):
                            LowestVal = [Score[j][k], j, k]
                        if ((j not in Match1) and (k not in Match2)):
                            if (Score[j][k] < LowestVal[0]):
                                LowestVal = [Score[j][k], j, k]
                if (LowestVal != None):
                    Match1.append(LowestVal[1])
                    Match2.append(LowestVal[2])
            NetMatches = []
            for i in range(len(Match1)):
                NetMatches.append([Objs1[Match1[i]], Objs2[Match2[i]], Delta[Match1[i]][Match2[i]]])
            for i in range(len(Objs1)):
                if i not in Match1:
                    NetMatches.append([Objs1[i],[None],'Deleted'])
            for i in range(len(Objs2)):
                if i not in Match2:
                    NetMatches.append([[None],Objs2[i],'Added'])
            return NetMatches
            
        # Match up objects between two different figures
        def SolObjMatch(Fig, Objs2):
            Objs1 = GetVerbalObjs(Fig)
            Score = []
            Delta = []
            for Obj1 in Objs1:
                SRow = []
                DRow = []
                for Obj2 in Objs2:
                    [V,D] = CalcObjDelta(Obj1[1], Obj2[1])
                    SRow.append(V)
                    DRow.append(D)
                Score.append(SRow)
                Delta.append(DRow)
            Match1 = []
            Match2 = []
            for i in range(len(Score)):
                LowestVal = None
                for j in range(len(Score)):
                    for k in range(len(Score[j])):
                        if ((LowestVal == None) and (j not in Match1) and (k not in Match2)):
                            LowestVal = [Score[j][k], j, k]
                        if ((j not in Match1) and (k not in Match2)):
                            if (Score[j][k] < LowestVal[0]):
                                LowestVal = [Score[j][k], j, k]
                if (LowestVal != None):
                    Match1.append(LowestVal[1])
                    Match2.append(LowestVal[2])
            NetMatches = []
            for i in range(len(Match1)):
                NetMatches.append([Objs1[Match1[i]], Objs2[Match2[i]], Delta[Match1[i]][Match2[i]]])
            for i in range(len(Objs1)):
                if i not in Match1:
                    NetMatches.append([Objs1[i],[None],'Deleted'])
            for i in range(len(Objs2)):
                if i not in Match2:
                    NetMatches.append([[None],Objs2[i],'Added'])
            Score = 0
            for Match in NetMatches:
                if Match[2] == 'Deleted':
                    Score += 2
                elif Match[2] == 'Added':
                    Score += 2
                elif len(Match[2]) > 0:
                    Score += len(Match[2])
            return Score
            
        def ApplyDeltas(Figure, Del1, Del2):
            Objs = GetVerbalObjs(Figure)
            for Delta in Del1:
                for Obj in Objs:
                    if Delta[0][0] == Obj[0]:
                        if Delta[2] == 'Deleted':
                            Objs.remove(Obj)
                        else:
                            Obj[1] = Delta[1][1]
                if Delta[2] == 'Added':
                    Objs.append(Delta[1])
            for Delta in Del2:
                for Obj in Objs:
                    if Delta[0][0] == Obj[0]:
                        if Delta[2] == 'Deleted':
                            Objs.remove(Obj)
                        else:
                            Obj[1] = Delta[1][1]
                if Delta[2] == 'Added':
                    Objs.append(Delta[1])
            return Objs
        
        BestGuess = 1 

        if problem.problemType == "2x2":
            TopLeft = problem.figures['A']
            TopRight = problem.figures['B']
            BotLeft = problem.figures['C']
            Solutions = [problem.figures['1'], problem.figures['2'],
	    	             problem.figures['3'], problem.figures['4'],
	                     problem.figures['5'], problem.figures['6']]
            if problem.hasVerbal:
                ObjMatchTLTR = FigureObjMatch(TopLeft,TopRight)
                ObjMatchTLBL = FigureObjMatch(TopLeft,BotLeft)
                TRBR = ApplyDeltas(problem.figures['A'], ObjMatchTLTR, ObjMatchTLBL)
                BLBR = ApplyDeltas(problem.figures['A'], ObjMatchTLBL, ObjMatchTLTR)
                TRSolScore = []
                BLSolScore = []
                for Sol in Solutions:
                    TRSolScore.append(SolObjMatch(Sol,TRBR))
                    BLSolScore.append(SolObjMatch(Sol,BLBR))
                MinSolScore = TRSolScore[0]+BLSolScore[0]
                BestGuess = 1
                for i in range(len(TRSolScore)):
                    if (TRSolScore[i] + BLSolScore[i]) < MinSolScore:
                        MinSolScore = (TRSolScore[i] + BLSolScore[i])
                        BestGuess = i+1


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

        ActualSolution = problem.checkAnswer(int(BestGuess))
        return BestGuess

