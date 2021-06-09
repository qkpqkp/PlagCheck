# encoding: utf-8
# module gurobipy.gurobipy
# from C:\Users\Doly\Anaconda3\lib\site-packages\gurobipy\gurobipy.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\Doly\Anaconda3\lib\os.py
import math as math # <module 'math' (built-in)>
import types as types # C:\Users\Doly\Anaconda3\lib\types.py
import gc as gc # <module 'gc' (built-in)>
import itertools as itertools # <module 'itertools' (built-in)>
import re as re # C:\Users\Doly\Anaconda3\lib\re.py
import dis as dis # C:\Users\Doly\Anaconda3\lib\dis.py
import numbers as numbers # C:\Users\Doly\Anaconda3\lib\numbers.py
import sys as sys # <module 'sys' (built-in)>
import builtins as bi # <module 'builtins' (built-in)>
import operator as operator # C:\Users\Doly\Anaconda3\lib\operator.py
import fnmatch as fnmatch # C:\Users\Doly\Anaconda3\lib\fnmatch.py
import glob as glob # C:\Users\Doly\Anaconda3\lib\glob.py
import inspect as inspect # C:\Users\Doly\Anaconda3\lib\inspect.py
import logging as logging # C:\Users\Doly\Anaconda3\lib\logging\__init__.py
import atexit as atexit # <module 'atexit' (built-in)>
from _io import GRBStringIO


# functions

def abs_(*args, **kwargs): # real signature unknown
    """ Return the absolute value of x, or the absolute value general constraint """
    pass

def all_(*args, **kwargs): # real signature unknown
    """ Return the general constraint of type and """
    pass

def and_(*args, **kwargs): # real signature unknown
    """ Return the general constraint of type and """
    pass

def any_(*args, **kwargs): # real signature unknown
    """ Return the general constraint of type or """
    pass

def disposeDefaultEnv(): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        disposeDefaultEnv()
    
      PURPOSE:
        Release default Gurobi environment.
    
      ARGUMENTS:
        None.
    
      EXAMPLE:
        disposeDefaultEnv()
    """
    pass

def exprfactory(*args, **kwargs): # real signature unknown
    pass

def exprfactory_iter(*args, **kwargs): # real signature unknown
    pass

def getParamInfo(paramname): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        getParamInfo(paramname)
    
      PURPOSE:
        Get information about a parameter.
    
      ARGUMENTS:
        paramname (string): The name of the parameter.
    
      RETURN VALUE:
        A tuple containing the parameter name, the paramter type, the
        current value, the minimum allowed value, the maximum allowed value,
        and the default value.
    
      EXAMPLE:
        model.getParamInfo("NodeLimit")
    
      NOTES:
        The parameter name may contain the '*' and '?' wildcards.
    
        To get information about a parameter setting for a single model, use
        Model.getParamInfo().
    
        paramHelp() provides additional information on the available parameters.
    """
    pass

def help(*args, **kwargs): # real signature unknown
    pass

def max_(*args, **kwargs): # real signature unknown
    """ Return the general constraint of type max """
    pass

def min_(*args, **kwargs): # real signature unknown
    """ Return the general constraint of type min """
    pass

def models(): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        models()
    
      PURPOSE:
        Provide a list of currently loaded models.
    
      ARGUMENTS:
        None.
    
      EXAMPLE:
        models()
    """
    pass

def multidict(data): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        multidict(data)
      PURPOSE:
        Split a single dictionary into multiple dictionaries.
      ARGUMENTS:
        data: A dictionary that maps each key to a list of 'n' values.
      RETURN VALUE:
        A list of the shared keys, followed by individual tupledicts.
      EXAMPLE:
        (keys, dict1, dict2) = multidict( {
                 'key1': [1, 2],
                 'key2': [1, 3],
                 'key3': [1, 4] } )
    """
    pass

def or_(*args, **kwargs): # real signature unknown
    """ Return the general constraint of type or """
    pass

def paramHelp(paramname): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        paramHelp(paramname)
    
      PURPOSE:
        Obtain help on a Gurobi parameter.
    
      ARGUMENTS:
        paramname (string): The name of the parameter for which help is desired.
    
      EXAMPLE:
        paramHelp()
        paramHelp("NodeLimit")
        paramHelp("Heu*")
    
      NOTES:
        The parameter name may contain '*' and '?' wildcards.
    """
    pass

def quicksum(p_list): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        quicksum(list)
    
      PURPOSE:
        A quicker version of the Python built-in 'sum' function for building
        Gurobi expressions.
    
      ARGUMENTS:
        list: A list of terms.
    
      RETURN VALUE:
        An expression that represents the sum of the input arguments.
    
      EXAMPLE:
        expr = quicksum([x, y, z])
        expr = quicksum([1.0, 2*y, 3*z*z])
    """
    pass

def read(filename, env=None): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        read(filename, env=None)
    
      PURPOSE:
        Read an optimization model from a file.
    
      ARGUMENTS:
        filename (string): Path to a valid MPS or LP format input file.
        env (Env, optional): Specify a Gurobi environment that should
                             be used to create the Gurobi Model object.
                             Unless you need to control your own environments,
                             its value should be left at None; the
                             the default environment is used in this case.
    
      RETURN VALUE:
        A Model object.
    
      EXAMPLE:
        m = read("examples/model.mps.gz")
        m.optimize()
    
      NOTES:
        The file type is determined from the file name suffix, which must be
        one of .lp, .mps, .rew, or .rlp.  This routine can read files that have
        been compressed with either gzip or bzip2, so additional suffixes of
        .gz or .bz2 are accepted.
    
        The file name may contain the '*' and '?' wildcard characters.  If
        more than one file matches, this routine will read the first match.
    """
    pass

def readParams(filename): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        readParams(filename)
    
      PURPOSE:
        Read a set of parameter settings from a file.
    
      ARGUMENTS:
        filename (string): Path to a file containing a list of parameter settings.
    
      EXAMPLE:
        readParams("gurobi.prm")
    
      NOTES:
        The parameter file should contain name-value pairs, each on its own line.
        A hash symbol at the beginning of a line indicates that the line should be
        ignored.  Here is an example of a valid parameter file:
    
          # List of changed parameters
          TimeLimit      100
          IterationLimit 1000
    """
    pass

def resetParams(): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        resetParams()
    
      PURPOSE:
        Reset all parameters to their default values.
    
      ARGUMENTS:
        None.
    
      EXAMPLE:
        resetParams()
    """
    pass

def setParam(paramname, newvalue): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        setParam(paramname, newvalue)
    
      PURPOSE:
        Set a parameter to a new value.
    
      ARGUMENTS:
        paramname (string): The name of the parameter.
        newvalue: The desired new value.  The type of the value should be
                  compatible with the parameter type (e.g., an integer parameter
                  takes an integer value).  One important exception: the string
                  "default" will revert the specified parameter to its
                  default value.
    
      EXAMPLE:
        setParam("NodeLimit", 100)
        setParam("TimeLimit", "default")
    
      NOTES:
        The parameter name may contain the '*' and '?' wildcards.
    
        To change a parameter setting for a single model, use Model.setParam().
    
        paramHelp() provides additional information on the available parameters.
    """
    pass

def system(command): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        system(command)
    
      PURPOSE:
        Issue a system shell command.
    
      ARGUMENTS:
        command (string): The command to pass to the system shell.
    
      EXAMPLE:
        system("ls")
        system("rm junk")
    """
    pass

def writeParams(filename): # real signature unknown; restored from __doc__
    """
    ROUTINE:
        writeParams(filename)
    
      PURPOSE:
        Write non-default parameter settings to a file.
    
      ARGUMENTS:
        filename (string): The name of the file to which non-default parameter
                           settings should be written.
    
      EXAMPLE:
        writeParams("changed.prm")
    
      NOTES:
        Upon completion, the specified file will contain a set of name-value
        pairs, one per line, that indicates the set of parameters with
        non-default values.
    """
    pass

def __attrlist(*args, **kwargs): # real signature unknown
    pass

def __bytestostring(*args, **kwargs): # real signature unknown
    pass

def __getattr(*args, **kwargs): # real signature unknown
    pass

def __getattrinfo(*args, **kwargs): # real signature unknown
    pass

def __geterrormsg(*args, **kwargs): # real signature unknown
    pass

def __gettypedattrlist(*args, **kwargs): # real signature unknown
    pass

def __isscalar(*args, **kwargs): # real signature unknown
    pass

def __isstr(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_LinExpr(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_QuadExpr(*args, **kwargs): # real signature unknown
    pass

def __setattr(*args, **kwargs): # real signature unknown
    pass

def __settypedattrlist(*args, **kwargs): # real signature unknown
    pass

def __simpleexpr(*args, **kwargs): # real signature unknown
    pass

def __stringtobytes(*args, **kwargs): # real signature unknown
    pass

# classes

class AttrConstClass(object):
    """
    Attributes are used throughout the Gurobi interface to query and
      modify model properties.  You refer to them as you would any
      other object attribute.  For example, "print model.numConstrs"
      prints the number of constraints in a model.  You can assign new values to
      some attributes (e.g., model.ModelName = "New"), while others can only
      be queried.  Note that attribute modification is handled in a lazy fashion,
      so you won't see the effect of a change until after the next call to
      Model.update() or Model.optimize().
    
      Capitalization is ignored in Gurobi attribute names, so
      model.numConstrs and model.NumConstrs are equivalent.
    
      Gurobi attributes can be grouped into the following categories:
    
      General model attributes (e.g., model.numConstrs):
    
        numConstrs: Number of constraints
        numVars: Number of variables
        numSOS: Number of SOS constraints
        numQConstrs: Number of quadrtic constraints
        numGenConstrs: Number of general constraints
        numNZs: Number of non-zero coefficients
        numQNZs: Number of non-zero quadratic objective coefficients
        numIntVars: Number of integer variables (including binary variables)
        numBinVars: Number of binary variables
        modelName: Model name
        modelSense: Model sense: minimization (1) or maximization (-1)
        objCon: Constant offset for objective function
        objVal: Objective value for current solution
        objBound: Best available lower bound on solution objective
        poolObjBound: Bound on objective for undiscovered solutions
        poolObjVal: Retrieve the objective value of an alternate MIP solution
        MIPGap: Current relative MIP optimality gap
        runtime: Runtime (in seconds) for most recent optimization
        Status: Current status of model (help(GRB) gives a list of codes)
        solCount: Number of stored solutions
        iterCount: Number of simplex iterations performed
        nodeCount: Number of branch-and-cut nodes explored
        barIterCount: Number of barrier iterations performed
        isMIP: Indicates whether the model is MIP (1) or not (0)
        isQP: Indicates whether the model has a quadratic objective
        isQCP: Indicates whether the model has quadratic constraints
        isMultiObj: Indicates whether the model has multiple objectives
        IISMinimal: Is computed IIS minimal?
        kappa: Condition number of current LP basis
        maxCoeff: Maximum constraint coefficient (in absolute value)
        minCoeff: Minimum non-zero constraint coefficient (in absolute value)
        maxBound: Maximum finite variable bound (in absolute value)
        minBound: Minimum non-zero variable bound (in absolute value)
        maxObjCoeff: Maximum objective coefficient (in absolute value)
        minObjCoeff: Minimum objective coefficient (in absolute value)
        maxRHS: Maximum linear constraint right-hand side (in absolute value)
        minRHS: Minimum linear constraint right-hand side (in absolute value)
        maxQCRHS: Maximum quadratic constraint right-hand side (in absolute value)
        minQCRHS: Minimum quadratic constraint right-hand side (in absolute value)
        maxQCCoeff: Maximum quadratic constraint coefficient in quadratic part (in absolute value)
        minQCCoeff: Minimum non-zero quadratic constraint coefficient in quadratic part (in absolute value)
        maxQCLCoeff: Maximum quadratic constraint coefficient in linear part (in absolute value)
        minQCLCoeff: Minimum non-zero quadratic constraint coefficient in linear part (in absolute value)
        maxQObjCoeff: Maximum quadratic objective coefficient (in absolute value)
        minQObjCoeff: Minimum quadratic objective coefficient (in absolute value)
        farkasProof: Infeasible amount for Farkas proof for infeasible models
        numStart: number of MIP starts
    
      Variable attributes (e.g., var.lb):
    
        lb: Lower bound
        ub: Upper bound
        obj: Objective coefficient
        vType: Variable type (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER,
                              GRB.SEMICONT, or GRB.SEMIINT)
        varName: Variable name
        x: Solution value
        rc: Reduced cost
        xn: Solution value in alternate MIP solution
        start: Start vector (use GRB.UNDEFINED to leave a value unspecified)
        vBasis: Basis status
        varHintVal: Variable hint value
        varHintPri: Variable hint priority
        branchPriority: Variable branch priority
        partition: Variable partition
        IISLB: Does LB participate in IIS? (for infeasible models)
        IISUB: Does UB participate in IIS? (for infeasible models)
        SAObjLow: Smallest objective coefficient for which basis remains optimal
        SAObjUp: Largest objective coefficient for which basis remains optimal
        SALBLow: Smallest lower bound for which basis remains optimal
        SALBUp: Largest lower bound for which basis remains optimal
        SAUBLow: Smallest upper bound for which basis remains optimal
        SAUBUp: Largest upper bound for which basis remains optimal
        unbdRay: Unbounded ray
        pStart: Primal solution (for warm-starting simplex)
        preFixVal: The value of the variable (for variables fixed by presolve)
        varPreStat: Status of variable in presolved model
        VTag: Tag string for variables (each defined variable tag MUST be unique)
    
      Constraint attributes (e.g., constr.sense):
    
        sense: Constraint sense
        rhs: Constraint right-hand side value
        constrName: Constraint name
        pi: Dual value
        slack: Constraint slack
        cBasis: Basis status
        lazy: Lazy constraint flag
        IISConstr: Does constraint participate in IIS? (for infeasible models)
        SARHSLow: Smallest RHS value for which basis remains optimal
        SARHSUp: Largest RHS value for which basis remains optimal
        farkasDual: Farkas dual for infeasible models
        dStart: Dual solution (for warm-starting simplex)
        CTag: Tag string for constraints (each defined constraint tag MUST be unique)
    
      SOS (e.g., sos.IISSOS):
    
        IISSOS: Does SOS participate in IIS? (for infeasible models)
    
      Quadratic constraint attributes (e.g., qc.sense):
    
        QCsense: Quadratic constraint sense
        QCrhs: Quadratic constraint right-hand side value
        QCname: Quadratic constraint name
        IISQConstr: Does QC participate in IIS? (for infeasible models)
        QCpi: Dual value
        QCslack: Quadratic constraint slack
        QCTag: Tag string for quadratic constraints (each defined
               quadratic constraint tag MUST be unique)
    
      GenConstr (e.g., genconstr.IISGenConstr):
    
        GenConstrType: General constraint type (e.g., GRB.GENCONSTR_MAX)
        GenConstrName: General constraint name
        IISGenConstr: Does general constraint participate in IIS? (for infeasible models)
    
      GenConstr (only for function constraints)
    
        FuncPieceError: error allowed for PWL translation
        FuncPieceLength: piece length for PWL translation
        FuncPieceRatio: control whether to link function values or to have
                        pieces below or above the function
        FuncPieces: control PWL translation whether to use equal piece length,
                    to limit error or to limit the total number of pieces
    
    
      Solution quality (e.g., model.constrVio):
    
        You generally access quality information through Model.printQuality().
        Please refer to the Attributes section of the Gurobi Reference Manual for
        the full list of quality attributes.
    
      Multi-objectives
    
        ObjN: objectives of multi-objectives
        ObjNCon: constant terms of multi-objectives
        ObjNPriority: priorities of multi-objectives
        ObjNWeight: weights of multi-objectives
        ObjNRelTol: relative tolerances of multi-objectives
        ObjNAbsTol: absolute tolerances of multi-objectives
        ObjNVal: objective value for multi-objectives
        ObjNName: names of multi-objectives
        NumObj: number of multi-objectives
    
      Multi-scenarios
    
        ScenNLB: modification to lower bound vector in current scenario
        ScenNUB: modification to upper bound vector in current scenario
        ScenNObj: modification to objective coefficient vector in current scenario
        ScenNRHS: modification to right hand side vector in current scenario
        ScenNName: name of current scenario
        ScenNX: value in current solution of current scenario
        ScenNObjBound: objective bound of current scenario
        ScenNObjVal: objective value of current solution of current scenario
        NumScenarios: number of scenarios in multi-scenario model
    
      Batch Objects
    
        BatchErrorCode: Last error code for this batch request
        BatchErrorMessage: Last error string for this batch request
        BatchID: String ID for this batch request
        BatchStatus: Current status of batch request (help(GRB) gives a list of codes)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BarIterCount = 'BarIterCount'
    BarX = 'BarX'
    BatchErrorCode = 'BatchErrorCode'
    BatchErrorMessage = 'BatchErrorMessage'
    BatchID = 'BatchID'
    BatchStatus = 'BatchStatus'
    BoundSVio = 'BoundSVio'
    BoundSVioIndex = 'BoundSVioIndex'
    BoundSVioSum = 'BoundSVioSum'
    BoundVio = 'BoundVio'
    BoundVioIndex = 'BoundVioIndex'
    BoundVioSum = 'BoundVioSum'
    BranchPriority = 'BranchPriority'
    CBasis = 'CBasis'
    ComplVio = 'ComplVio'
    ComplVioIndex = 'ComplVioIndex'
    ComplVioSum = 'ComplVioSum'
    ConstrName = 'ConstrName'
    ConstrResidual = 'ConstrResidual'
    ConstrResidualIndex = 'ConstrResidualIndex'
    ConstrResidualSum = 'ConstrResidualSum'
    ConstrSResidual = 'ConstrSResidual'
    ConstrSResidualIndex = 'ConstrSResidualIndex'
    ConstrSResidualSum = 'ConstrSResidualSum'
    ConstrSVio = 'ConstrSVio'
    ConstrSVioIndex = 'ConstrSVioIndex'
    ConstrSVioSum = 'ConstrSVioSum'
    ConstrVio = 'ConstrVio'
    ConstrVioIndex = 'ConstrVioIndex'
    ConstrVioSum = 'ConstrVioSum'
    CTag = 'CTag'
    DStart = 'DStart'
    DualResidual = 'DualResidual'
    DualResidualIndex = 'DualResidualIndex'
    DualResidualSum = 'DualResidualSum'
    DualSResidual = 'DualSResidual'
    DualSResidualIndex = 'DualSResidualIndex'
    DualSResidualSum = 'DualSResidualSum'
    DualSVio = 'DualSVio'
    DualSVioIndex = 'DualSVioIndex'
    DualSVioSum = 'DualSVioSum'
    DualVio = 'DualVio'
    DualVioIndex = 'DualVioIndex'
    DualVioSum = 'DualVioSum'
    FarkasDual = 'FarkasDual'
    FarkasProof = 'FarkasProof'
    FuncPieceError = 'FuncPieceError'
    FuncPieceLength = 'FuncPieceLength'
    FuncPieceRatio = 'FuncPieceRatio'
    FuncPieces = 'FuncPieces'
    GenConstrName = 'GenConstrName'
    GenConstrType = 'GenConstrType'
    IISConstr = 'IISConstr'
    IISGenConstr = 'IISGenConstr'
    IISLB = 'IISLB'
    IISMinimal = 'IISMinimal'
    IISQConstr = 'IISQConstr'
    IISSOS = 'IISSOS'
    IISUB = 'IISUB'
    IntVio = 'IntVio'
    IntVioIndex = 'IntVioIndex'
    IntVioSum = 'IntVioSum'
    IsMIP = 'IsMIP'
    IsMultiObj = 'IsMultiObj'
    IsQCP = 'IsQCP'
    IsQP = 'IsQP'
    IterCount = 'IterCount'
    JobID = 'JobID'
    Kappa = 'Kappa'
    KappaExact = 'KappaExact'
    Lazy = 'Lazy'
    LB = 'LB'
    LicenseExpiration = 'LicenseExpiration'
    MaxBound = 'MaxBound'
    MaxCoeff = 'MaxCoeff'
    MaxObjCoeff = 'MaxObjCoeff'
    MaxQCCoeff = 'MaxQCCoeff'
    MaxQCLCoeff = 'MaxQCLCoeff'
    MaxQCRHS = 'MaxQCRHS'
    MaxQObjCoeff = 'MaxQObjCoeff'
    MaxRHS = 'MaxRHS'
    MinBound = 'MinBound'
    MinCoeff = 'MinCoeff'
    MinObjCoeff = 'MinObjCoeff'
    MinQCCoeff = 'MinQCCoeff'
    MinQCLCoeff = 'MinQCLCoeff'
    MinQCRHS = 'MinQCRHS'
    MinQObjCoeff = 'MinQObjCoeff'
    MinRHS = 'MinRHS'
    MIPGap = 'MIPGap'
    ModelName = 'ModelName'
    ModelSense = 'ModelSense'
    NodeCount = 'NodeCount'
    NumBinVars = 'NumBinVars'
    NumConstrs = 'NumConstrs'
    NumGenConstrs = 'NumGenConstrs'
    NumIntVars = 'NumIntVars'
    NumNZs = 'NumNZs'
    NumObj = 'NumObj'
    NumPWLObjVars = 'NumPWLObjVars'
    NumQCNZs = 'NumQCNZs'
    NumQConstrs = 'NumQConstrs'
    NumQNZs = 'NumQNZs'
    NumScenarios = 'NumScenarios'
    NumSOS = 'NumSOS'
    NumStart = 'NumStart'
    NumVars = 'NumVars'
    Obj = 'Obj'
    ObjBound = 'ObjBound'
    ObjBoundC = 'ObjBoundC'
    ObjCon = 'ObjCon'
    ObjN = 'ObjN'
    ObjNAbsTol = 'ObjNAbsTol'
    ObjNCon = 'ObjNCon'
    ObjNName = 'ObjNName'
    ObjNPriority = 'ObjNPriority'
    ObjNRelTol = 'ObjNRelTol'
    ObjNVal = 'ObjNVal'
    ObjNWeight = 'ObjNWeight'
    ObjVal = 'ObjVal'
    Partition = 'Partition'
    Pi = 'Pi'
    PoolObjBound = 'PoolObjBound'
    PoolObjVal = 'PoolObjVal'
    PreFixVal = 'PreFixVal'
    PStart = 'PStart'
    PWLObjCvx = 'PWLObjCvx'
    QCName = 'QCName'
    QCPi = 'QCPi'
    QCRHS = 'QCRHS'
    QCSense = 'QCSense'
    QCSlack = 'QCSlack'
    QCTag = 'QCTag'
    RC = 'RC'
    RHS = 'RHS'
    Runtime = 'Runtime'
    SALBLow = 'SALBLow'
    SALBUp = 'SALBUp'
    SAObjLow = 'SAObjLow'
    SAObjUp = 'SAObjUp'
    SARHSLow = 'SARHSLow'
    SARHSUp = 'SARHSUp'
    SAUBLow = 'SAUBLow'
    SAUBUp = 'SAUBUp'
    ScenNLB = 'ScenNLB'
    ScenNName = 'ScenNName'
    ScenNObj = 'ScenNObj'
    ScenNObjBound = 'ScenNObjBound'
    ScenNObjVal = 'ScenNObjVal'
    ScenNRHS = 'ScenNRHS'
    ScenNUB = 'ScenNUB'
    ScenNX = 'ScenNX'
    Sense = 'Sense'
    Server = 'Server'
    Slack = 'Slack'
    SolCount = 'SolCount'
    Start = 'Start'
    Status = 'Status'
    TuneResultCount = 'TuneResultCount'
    UB = 'UB'
    UnbdRay = 'UnbdRay'
    VarHintPri = 'VarHintPri'
    VarHintVal = 'VarHintVal'
    VarName = 'VarName'
    VarPreStat = 'VarPreStat'
    VBasis = 'VBasis'
    VTag = 'VTag'
    VType = 'VType'
    X = 'X'
    Xn = 'Xn'
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Attributes are used throughout the Gurobi interface to query and\\n  modify model properties.  You refer to them as you would any\\n  other object attribute.  For example, "print model.numConstrs"\\n  prints the number of constraints in a model.  You can assign new values to\\n  some attributes (e.g., model.ModelName = "New"), while others can only\\n  be queried.  Note that attribute modification is handled in a lazy fashion,\\n  so you won\\\'t see the effect of a change until after the next call to\\n  Model.update() or Model.optimize().\\n\\n  Capitalization is ignored in Gurobi attribute names, so\\n  model.numConstrs and model.NumConstrs are equivalent.\\n\\n  Gurobi attributes can be grouped into the following categories:\\n\\n  General model attributes (e.g., model.numConstrs):\\n\\n    numConstrs: Number of constraints\\n    numVars: Number of variables\\n    numSOS: Number of SOS constraints\\n    numQConstrs: Number of quadrtic constraints\\n    numGenConstrs: Number of general constraints\\n    numNZs: Number of non-zero coefficients\\n    numQNZs: Number of non-zero quadratic objective coefficients\\n    numIntVars: Number of integer variables (including binary variables)\\n    numBinVars: Number of binary variables\\n    modelName: Model name\\n    modelSense: Model sense: minimization (1) or maximization (-1)\\n    objCon: Constant offset for objective function\\n    objVal: Objective value for current solution\\n    objBound: Best available lower bound on solution objective\\n    poolObjBound: Bound on objective for undiscovered solutions\\n    poolObjVal: Retrieve the objective value of an alternate MIP solution\\n    MIPGap: Current relative MIP optimality gap\\n    runtime: Runtime (in seconds) for most recent optimization\\n    Status: Current status of model (help(GRB) gives a list of codes)\\n    solCount: Number of stored solutions\\n    iterCount: Number of simplex iterations performed\\n    nodeCount: Number of branch-and-cut nodes explored\\n    barIterCount: Number of barrier iterations performed\\n    isMIP: Indicates whether the model is MIP (1) or not (0)\\n    isQP: Indicates whether the model has a quadratic objective\\n    isQCP: Indicates whether the model has quadratic constraints\\n    isMultiObj: Indicates whether the model has multiple objectives\\n    IISMinimal: Is computed IIS minimal?\\n    kappa: Condition number of current LP basis\\n    maxCoeff: Maximum constraint coefficient (in absolute value)\\n    minCoeff: Minimum non-zero constraint coefficient (in absolute value)\\n    maxBound: Maximum finite variable bound (in absolute value)\\n    minBound: Minimum non-zero variable bound (in absolute value)\\n    maxObjCoeff: Maximum objective coefficient (in absolute value)\\n    minObjCoeff: Minimum objective coefficient (in absolute value)\\n    maxRHS: Maximum linear constraint right-hand side (in absolute value)\\n    minRHS: Minimum linear constraint right-hand side (in absolute value)\\n    maxQCRHS: Maximum quadratic constraint right-hand side (in absolute value)\\n    minQCRHS: Minimum quadratic constraint right-hand side (in absolute value)\\n    maxQCCoeff: Maximum quadratic constraint coefficient in quadratic part (in absolute value)\\n    minQCCoeff: Minimum non-zero quadratic constraint coefficient in quadratic part (in absolute value)\\n    maxQCLCoeff: Maximum quadratic constraint coefficient in linear part (in absolute value)\\n    minQCLCoeff: Minimum non-zero quadratic constraint coefficient in linear part (in absolute value)\\n    maxQObjCoeff: Maximum quadratic objective coefficient (in absolute value)\\n    minQObjCoeff: Minimum quadratic objective coefficient (in absolute value)\\n    farkasProof: Infeasible amount for Farkas proof for infeasible models\\n    numStart: number of MIP starts\\n\\n  Variable attributes (e.g., var.lb):\\n\\n    lb: Lower bound\\n    ub: Upper bound\\n    obj: Objective coefficient\\n    vType: Variable type (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER,\\n                          GRB.SEMICONT, or GRB.SEMIINT)\\n    varName: Variable name\\n    x: Solution value\\n    rc: Reduced cost\\n    xn: Solution value in alternate MIP solution\\n    start: Start vector (use GRB.UNDEFINED to leave a value unspecified)\\n    vBasis: Basis status\\n    varHintVal: Variable hint value\\n    varHintPri: Variable hint priority\\n    branchPriority: Variable branch priority\\n    partition: Variable partition\\n    IISLB: Does LB participate in IIS? (for infeasible models)\\n    IISUB: Does UB participate in IIS? (for infeasible models)\\n    SAObjLow: Smallest objective coefficient for which basis remains optimal\\n    SAObjUp: Largest objective coefficient for which basis remains optimal\\n    SALBLow: Smallest lower bound for which basis remains optimal\\n    SALBUp: Largest lower bound for which basis remains optimal\\n    SAUBLow: Smallest upper bound for which basis remains optimal\\n    SAUBUp: Largest upper bound for which basis remains optimal\\n    unbdRay: Unbounded ray\\n    pStart: Primal solution (for warm-starting simplex)\\n    preFixVal: The value of the variable (for variables fixed by presolve)\\n    varPreStat: Status of variable in presolved model\\n    VTag: Tag string for variables (each defined variable tag MUST be unique)\\n\\n  Constraint attributes (e.g., constr.sense):\\n\\n    sense: Constraint sense\\n    rhs: Constraint right-hand side value\\n    constrName: Constraint name\\n    pi: Dual value\\n    slack: Constraint slack\\n    cBasis: Basis status\\n    lazy: Lazy constraint flag\\n    IISConstr: Does constraint participate in IIS? (for infeasible models)\\n    SARHSLow: Smallest RHS value for which basis remains optimal\\n    SARHSUp: Largest RHS value for which basis remains optimal\\n    farkasDual: Farkas dual for infeasible models\\n    dStart: Dual solution (for warm-starting simplex)\\n    CTag: Tag string for constraints (each defined constraint tag MUST be unique)\\n\\n  SOS (e.g., sos.IISSOS):\\n\\n    IISSOS: Does SOS participate in IIS? (for infeasible models)\\n\\n  Quadratic constraint attributes (e.g., qc.sense):\\n\\n    QCsense: Quadratic constraint sense\\n    QCrhs: Quadratic constraint right-hand side value\\n    QCname: Quadratic constraint name\\n    IISQConstr: Does QC participate in IIS? (for infeasible models)\\n    QCpi: Dual value\\n    QCslack: Quadratic constraint slack\\n    QCTag: Tag string for quadratic constraints (each defined\\n           quadratic constraint tag MUST be unique)\\n\\n  GenConstr (e.g., genconstr.IISGenConstr):\\n\\n    GenConstrType: General constraint type (e.g., GRB.GENCONSTR_MAX)\\n    GenConstrName: General constraint name\\n    IISGenConstr: Does general constraint participate in IIS? (for infeasible models)\\n\\n  GenConstr (only for function constraints)\\n\\n    FuncPieceError: error allowed for PWL translation\\n    FuncPieceLength: piece length for PWL translation\\n    FuncPieceRatio: control whether to link function values or to have\\n                    pieces below or above the function\\n    FuncPieces: control PWL translation whether to use equal piece length,\\n                to limit error or to limit the total number of pieces\\n\\n\\n  Solution quality (e.g., model.constrVio):\\n\\n    You generally access quality information through Model.printQuality().\\n    Please refer to the Attributes section of the Gurobi Reference Manual for\\n    the full list of quality attributes.\\n\\n  Multi-objectives\\n\\n    ObjN: objectives of multi-objectives\\n    ObjNCon: constant terms of multi-objectives\\n    ObjNPriority: priorities of multi-objectives\\n    ObjNWeight: weights of multi-objectives\\n    ObjNRelTol: relative tolerances of multi-objectives\\n    ObjNAbsTol: absolute tolerances of multi-objectives\\n    ObjNVal: objective value for multi-objectives\\n    ObjNName: names of multi-objectives\\n    NumObj: number of multi-objectives\\n\\n  Multi-scenarios\\n\\n    ScenNLB: modification to lower bound vector in current scenario\\n    ScenNUB: modification to upper bound vector in current scenario\\n    ScenNObj: modification to objective coefficient vector in current scenario\\n    ScenNRHS: modification to right hand side vector in current scenario\\n    ScenNName: name of current scenario\\n    ScenNX: value in current solution of current scenario\\n    ScenNObjBound: objective bound of current scenario\\n    ScenNObjVal: objective value of current solution of current scenario\\n    NumScenarios: number of scenarios in multi-scenario model\\n\\n  Batch Objects\\n\\n    BatchErrorCode: Last error code for this batch request\\n    BatchErrorMessage: Last error string for this batch request\\n    BatchID: String ID for this batch request\\n    BatchStatus: Current status of batch request (help(GRB) gives a list of codes)\\n\\n  \', \'__setattr__\': <cyfunction AttrConstClass.__setattr__ at 0x00000248A608C608>, \'NumConstrs\': \'NumConstrs\', \'NumVars\': \'NumVars\', \'NumSOS\': \'NumSOS\', \'NumQConstrs\': \'NumQConstrs\', \'NumGenConstrs\': \'NumGenConstrs\', \'NumNZs\': \'NumNZs\', \'NumQNZs\': \'NumQNZs\', \'NumQCNZs\': \'NumQCNZs\', \'NumIntVars\': \'NumIntVars\', \'NumBinVars\': \'NumBinVars\', \'NumPWLObjVars\': \'NumPWLObjVars\', \'ModelName\': \'ModelName\', \'ModelSense\': \'ModelSense\', \'ObjCon\': \'ObjCon\', \'IsMIP\': \'IsMIP\', \'IsQP\': \'IsQP\', \'IsQCP\': \'IsQCP\', \'IsMultiObj\': \'IsMultiObj\', \'IISMinimal\': \'IISMinimal\', \'Kappa\': \'Kappa\', \'KappaExact\': \'KappaExact\', \'MaxCoeff\': \'MaxCoeff\', \'MinCoeff\': \'MinCoeff\', \'MaxBound\': \'MaxBound\', \'MinBound\': \'MinBound\', \'MaxObjCoeff\': \'MaxObjCoeff\', \'MinObjCoeff\': \'MinObjCoeff\', \'MaxRHS\': \'MaxRHS\', \'MinRHS\': \'MinRHS\', \'MaxQCRHS\': \'MaxQCRHS\', \'MinQCRHS\': \'MinQCRHS\', \'MaxQCCoeff\': \'MaxQCCoeff\', \'MinQCCoeff\': \'MinQCCoeff\', \'MaxQCLCoeff\': \'MaxQCLCoeff\', \'MinQCLCoeff\': \'MinQCLCoeff\', \'MaxQObjCoeff\': \'MaxQObjCoeff\', \'MinQObjCoeff\': \'MinQObjCoeff\', \'ObjVal\': \'ObjVal\', \'ObjBound\': \'ObjBound\', \'ObjBoundC\': \'ObjBoundC\', \'PoolObjBound\': \'PoolObjBound\', \'PoolObjVal\': \'PoolObjVal\', \'MIPGap\': \'MIPGap\', \'Runtime\': \'Runtime\', \'Status\': \'Status\', \'SolCount\': \'SolCount\', \'IterCount\': \'IterCount\', \'NodeCount\': \'NodeCount\', \'BarIterCount\': \'BarIterCount\', \'FarkasProof\': \'FarkasProof\', \'NumStart\': \'NumStart\', \'TuneResultCount\': \'TuneResultCount\', \'LicenseExpiration\': \'LicenseExpiration\', \'LB\': \'LB\', \'UB\': \'UB\', \'Obj\': \'Obj\', \'VType\': \'VType\', \'VarName\': \'VarName\', \'X\': \'X\', \'RC\': \'RC\', \'Xn\': \'Xn\', \'BarX\': \'BarX\', \'Start\': \'Start\', \'VarHintVal\': \'VarHintVal\', \'VarHintPri\': \'VarHintPri\', \'BranchPriority\': \'BranchPriority\', \'Partition\': \'Partition\', \'VBasis\': \'VBasis\', \'PWLObjCvx\': \'PWLObjCvx\', \'IISLB\': \'IISLB\', \'IISUB\': \'IISUB\', \'SAObjLow\': \'SAObjLow\', \'SAObjUp\': \'SAObjUp\', \'SALBLow\': \'SALBLow\', \'SALBUp\': \'SALBUp\', \'SAUBLow\': \'SAUBLow\', \'SAUBUp\': \'SAUBUp\', \'UnbdRay\': \'UnbdRay\', \'PStart\': \'PStart\', \'PreFixVal\': \'PreFixVal\', \'VarPreStat\': \'VarPreStat\', \'VTag\': \'VTag\', \'Sense\': \'Sense\', \'RHS\': \'RHS\', \'ConstrName\': \'ConstrName\', \'Pi\': \'Pi\', \'Slack\': \'Slack\', \'CBasis\': \'CBasis\', \'IISConstr\': \'IISConstr\', \'SARHSLow\': \'SARHSLow\', \'SARHSUp\': \'SARHSUp\', \'FarkasDual\': \'FarkasDual\', \'DStart\': \'DStart\', \'Lazy\': \'Lazy\', \'CTag\': \'CTag\', \'IISSOS\': \'IISSOS\', \'QCSense\': \'QCSense\', \'QCRHS\': \'QCRHS\', \'QCName\': \'QCName\', \'IISQConstr\': \'IISQConstr\', \'QCPi\': \'QCPi\', \'QCSlack\': \'QCSlack\', \'QCTag\': \'QCTag\', \'GenConstrType\': \'GenConstrType\', \'GenConstrName\': \'GenConstrName\', \'IISGenConstr\': \'IISGenConstr\', \'FuncPieceError\': \'FuncPieceError\', \'FuncPieceLength\': \'FuncPieceLength\', \'FuncPieceRatio\': \'FuncPieceRatio\', \'FuncPieces\': \'FuncPieces\', \'BoundVio\': \'BoundVio\', \'BoundSVio\': \'BoundSVio\', \'BoundVioIndex\': \'BoundVioIndex\', \'BoundSVioIndex\': \'BoundSVioIndex\', \'BoundVioSum\': \'BoundVioSum\', \'BoundSVioSum\': \'BoundSVioSum\', \'ConstrVio\': \'ConstrVio\', \'ConstrSVio\': \'ConstrSVio\', \'ConstrVioIndex\': \'ConstrVioIndex\', \'ConstrSVioIndex\': \'ConstrSVioIndex\', \'ConstrVioSum\': \'ConstrVioSum\', \'ConstrSVioSum\': \'ConstrSVioSum\', \'ConstrResidual\': \'ConstrResidual\', \'ConstrSResidual\': \'ConstrSResidual\', \'ConstrResidualIndex\': \'ConstrResidualIndex\', \'ConstrSResidualIndex\': \'ConstrSResidualIndex\', \'ConstrResidualSum\': \'ConstrResidualSum\', \'ConstrSResidualSum\': \'ConstrSResidualSum\', \'DualVio\': \'DualVio\', \'DualSVio\': \'DualSVio\', \'DualVioIndex\': \'DualVioIndex\', \'DualSVioIndex\': \'DualSVioIndex\', \'DualVioSum\': \'DualVioSum\', \'DualSVioSum\': \'DualSVioSum\', \'DualResidual\': \'DualResidual\', \'DualSResidual\': \'DualSResidual\', \'DualResidualIndex\': \'DualResidualIndex\', \'DualSResidualIndex\': \'DualSResidualIndex\', \'DualResidualSum\': \'DualResidualSum\', \'DualSResidualSum\': \'DualSResidualSum\', \'ComplVio\': \'ComplVio\', \'ComplVioIndex\': \'ComplVioIndex\', \'ComplVioSum\': \'ComplVioSum\', \'IntVio\': \'IntVio\', \'IntVioIndex\': \'IntVioIndex\', \'IntVioSum\': \'IntVioSum\', \'ObjN\': \'ObjN\', \'ObjNCon\': \'ObjNCon\', \'ObjNPriority\': \'ObjNPriority\', \'ObjNWeight\': \'ObjNWeight\', \'ObjNRelTol\': \'ObjNRelTol\', \'ObjNAbsTol\': \'ObjNAbsTol\', \'ObjNVal\': \'ObjNVal\', \'ObjNName\': \'ObjNName\', \'NumObj\': \'NumObj\', \'ScenNLB\': \'ScenNLB\', \'ScenNUB\': \'ScenNUB\', \'ScenNObj\': \'ScenNObj\', \'ScenNRHS\': \'ScenNRHS\', \'ScenNName\': \'ScenNName\', \'ScenNX\': \'ScenNX\', \'ScenNObjBound\': \'ScenNObjBound\', \'ScenNObjVal\': \'ScenNObjVal\', \'NumScenarios\': \'NumScenarios\', \'Server\': \'Server\', \'JobID\': \'JobID\', \'BatchErrorCode\': \'BatchErrorCode\', \'BatchErrorMessage\': \'BatchErrorMessage\', \'BatchID\': \'BatchID\', \'BatchStatus\': \'BatchStatus\', \'__dict__\': <attribute \'__dict__\' of \'AttrConstClass\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'AttrConstClass\' objects>})'


class Batch(object):
    """
    Gurobi batch object. Commonly used methods on this object are:
        abort(): Abort the execution of the batch request.
        discard(): Discard all related information to the batch from the Cluster Manager.
        dispose(): Free local resources associated with the object.
        getJSONSolution(): Get the solution of the batch request in JSON format.
        update(): Refresh all local attributes from the Cluster Manager.
    
      Batch objects have four attributes that can be queried:
        BatchErrorCode: Last error code for the batch object.
        BatchErrorMessage: Last error string for the batch object .
        BatchID: ID of the associated batch request.
        BatchStatus: Batch object status.
    
      Additional help can be obtained on any of these methods (e.g.,
      help(Batch.solution)).
    """
    def abort(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              abort()
        
            PURPOSE:
              This method instruct the Cluster Manager to abort the processing of
              the associated batch request, changing its status to GRB.BATCH_ABORTED.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              batch.abort()
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              close()
        
            Synonymous to Batch.dispose()
        """
        pass

    def discard(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              discard()
        
            PURPOSE:
              This method instruct the Cluster Manager to discard input and output
              data related to the batch in question, including the stored
              solution if available. Use this function once you have
              retrieved the solution from the Cluster Manager to save storage space
              on the server. Further queries for the associated batch will
              fail with the code GRB_ERROR_DATA_NOT_AVAILABLE.
        
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              batch.discard()
        """
        pass

    def dispose(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              dispose()
        
            PURPOSE:
              Free all resources associated with this Batch object.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              batch.dispose()
        
            NOTES:
              After this method is called, this Batch object must
              no longer be used.
        """
        pass

    def getJSONSolution(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getJSONSolution()
        
            PURPOSE:
              This method query from the Cluster Manager the stored solution of a
              completed batch object. The solution is returned
              as a JSON string, (see the reference manual for futher
              details on the format). Note that for this call to succeed,
              the status of the batch request must be GRB.BATCH_COMPLETED.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A JSON string representation to the current solution.
        
            EXAMPLE:
              print(batch.getJSONSolution())
        """
        pass

    def retry(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              retry()
        
            PURPOSE:
              This method instruct the Cluster Manager to retry optimization of a
              failed or aborted batch request, changing its status to
              GRB.BATCH_SUBMITTED.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              batch.retry()
        """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              update()
        
            PURPOSE:
              Update all attributes from the Cluster Manager. The attributes of
              Batch objects are locally cached; use this method to retrieve
              the latest values from the Cluster Manager.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              batch.update()
        """
        pass

    def writeJSONSolution(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              writeJSONSolution()
        
            PURPOSE:
              This method query from the Cluster Manager the stored solution of a
              completed batch object as a JSON string, and stores it in
              the given filename (see the reference manual for futher
              details on the format). Note that for this call to succeed,
              the status of the batch request must be GRB.BATCH_COMPLETED.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              print(batch.getJSONSolution())
        """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__doc__': '\\n  Gurobi batch object. Commonly used methods on this object are:\\n    abort(): Abort the execution of the batch request.\\n    discard(): Discard all related information to the batch from the Cluster Manager.\\n    dispose(): Free local resources associated with the object.\\n    getJSONSolution(): Get the solution of the batch request in JSON format.\\n    update(): Refresh all local attributes from the Cluster Manager.\\n\\n  Batch objects have four attributes that can be queried:\\n    BatchErrorCode: Last error code for the batch object.\\n    BatchErrorMessage: Last error string for the batch object .\\n    BatchID: ID of the associated batch request.\\n    BatchStatus: Batch object status.\\n\\n  Additional help can be obtained on any of these methods (e.g.,\\n  help(Batch.solution)).\\n  ', '__init__': <cyfunction Batch.__init__ at 0x00000248A608B328>, '__getattr__': <cyfunction Batch.__getattr__ at 0x00000248A608B3E0>, '__setattr__': <cyfunction Batch.__setattr__ at 0x00000248A608B498>, '__del__': <cyfunction Batch.__del__ at 0x00000248A608B550>, 'dispose': <cyfunction Batch.dispose at 0x00000248A608B608>, 'close': <cyfunction Batch.close at 0x00000248A608B6C0>, '__enter__': <cyfunction Batch.__enter__ at 0x00000248A608B778>, '__exit__': <cyfunction Batch.__exit__ at 0x00000248A608B830>, '__eq__': <cyfunction Batch.__eq__ at 0x00000248A608B8E8>, '__repr__': <cyfunction Batch.__repr__ at 0x00000248A608B9A0>, '__dir__': <cyfunction Batch.__dir__ at 0x00000248A608BA58>, 'abort': <cyfunction Batch.abort at 0x00000248A608BB10>, 'retry': <cyfunction Batch.retry at 0x00000248A608BBC8>, 'discard': <cyfunction Batch.discard at 0x00000248A608BC80>, 'update': <cyfunction Batch.update at 0x00000248A608BD38>, 'getJSONSolution': <cyfunction Batch.getJSONSolution at 0x00000248A608BDF0>, 'writeJSONSolution': <cyfunction Batch.writeJSONSolution at 0x00000248A608BEA8>, '__dict__': <attribute '__dict__' of 'Batch' objects>, '__weakref__': <attribute '__weakref__' of 'Batch' objects>, '__hash__': None})"
    __hash__ = None


class CallbackClass(object):
    """
    Callbacks are user methods that are called by the Gurobi solver
      during the optimization.  To use a callback, define a method
      that takes two integer arguments (model and where), and pass it
      as the argument to Model.optimize.  Once optimization begins,
      your method will be called with one of the following 'where' values:
    
      Possible 'where' values (e.g., where == GRB.Callback.MIP) are:
    
        POLLING:  Regular polling callback - no user queries allowed
        PRESOLVE: In presolve
        SIMPLEX:  In simplex
        BARRIER:  In barrier
        MIP:      In MIP
        MIPSOL:   New MIP incumbent available
        MIPNODE:  MIP node information available
        MULTIOBJ: In multi-objective optimization
        MESSAGE:  Optimizer output a message
    
      Your method can call Model.cbGet() to obtain detailed information
      on the progress of the optimization.  Allowed values depend
      on 'where'.  The prefix of the 'what' name indicate which
      ones are allowed for each 'where' (so 'PRE_COLDEL' can only
      be called when where == SIMPLEX).
    
      Allowed 'what' values (e.g., cbGet(GRB.Callback.MIP_OBJBND) are:
    
        RUNTIME: Elapsed solver runtime
        PRE_COLDEL: Deleted column count
        PRE_ROWDEL: Deleted row count
        PRE_SENCHG: Changed constraint sense count
        PRE_BNDCHG: Bound change count
        SPX_ITRCNT: Iteration count
        SPX_OBJVAL: Primal objective value
        SPX_PRIMINF: Primal infeasibility
        SPX_DUALINF: Dual infeasibility
        SPX_ISPERT: Has model been perturbed?
        BARRIER_ITRCNT: Barrier iteration count
        BARRIER_PRIMOBJ: Barrier iterate primal objective
        BARRIER_DUALOBJ: Barrier iterate dual objective
        BARRIER_PRIMINF: Barrier iterate primal infeasibility
        BARRIER_DUALINF: Barrier iterate dual infeasibility
        BARRIER_COMPL: Barrier iterate complementarity violation
        MIP_OBJBST: Best known objective bound
        MIP_OBJBND: Best known feasible objective
        MIP_NODCNT: Nodes explored so far
        MIP_SOLCNT: Solutions found so far
        MIP_CUTCNT: Cuts added to the model so far
        MIP_NODLFT: Unexplored nodes
        MIP_ITRCNT: Simplex iterations performed so far
        MIPSOL_SOL: Feasible solution (a vector)
        MIPSOL_OBJ: Objective value for feasible solution
        MIPSOL_OBJBST: Best known objective bound
        MIPSOL_OBJBND: Best known feasible objective
        MIPSOL_NODCNT: Node count for feasible solution
        MIPSOL_SOLCNT: Solutions found so far
        MIPNODE_STATUS: Optimization status of node relaxation
        MIPNODE_REL: Node relaxation solution or ray if unbounded
        MIPNODE_OBJBST: Best known objective bound
        MIPNODE_OBJBND: Best known feasible objective
        MIPNODE_NODCNT: Nodes explored so far
        MIPNODE_SOLCNT: Solutions found so far
        MIPNODE_SBRVAR: Node branching variable
        MULTIOBJ_OBJCNT: Objective count optimized so far
        MULTIOBJ_SOLCNT: Solutions found so far
        MULTIOBJ_SOL: Feasible solution (a vector)
        MSG_STRING: Output message
    
      Your callback method can call other methods on the model object:
        cbCut(), cbGet(), cbGetNodeRel(), cbGetSolution(), cbSetSolution()
    """
    def callback(self, *args, **kwargs): # real signature unknown
        pass

    def _solnow(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BARRIER = 7
    BARRIER_COMPL = 7006
    BARRIER_DUALINF = 7005
    BARRIER_DUALOBJ = 7003
    BARRIER_ITRCNT = 7001
    BARRIER_PRIMINF = 7004
    BARRIER_PRIMOBJ = 7002
    MESSAGE = 6
    MIP = 3
    MIPNODE = 5
    MIPNODE_BRVAR = 5007
    MIPNODE_NODCNT = 5005
    MIPNODE_OBJBND = 5004
    MIPNODE_OBJBST = 5003
    MIPNODE_REL = 5002
    MIPNODE_SOLCNT = 5006
    MIPNODE_STATUS = 5001
    MIPSOL = 4
    MIPSOL_NODCNT = 4005
    MIPSOL_OBJ = 4002
    MIPSOL_OBJBND = 4004
    MIPSOL_OBJBST = 4003
    MIPSOL_SOL = 4001
    MIPSOL_SOLCNT = 4006
    MIP_CUTCNT = 3004
    MIP_ITRCNT = 3006
    MIP_NODCNT = 3002
    MIP_NODLFT = 3005
    MIP_OBJBND = 3001
    MIP_OBJBST = 3000
    MIP_SOLCNT = 3003
    MSG_STRING = 6001
    MULTIOBJ = 8
    MULTIOBJ_OBJCNT = 8001
    MULTIOBJ_SOL = 8003
    MULTIOBJ_SOLCNT = 8002
    POLLING = 0
    PRESOLVE = 1
    PRE_BNDCHG = 1003
    PRE_COECHG = 1004
    PRE_COLDEL = 1000
    PRE_ROWDEL = 1001
    PRE_SENCHG = 1002
    RUNTIME = 6002
    SIMPLEX = 2
    SPX_DUALINF = 2003
    SPX_ISPERT = 2004
    SPX_ITRCNT = 2000
    SPX_OBJVAL = 2001
    SPX_PRIMINF = 2002
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': "\\n  Callbacks are user methods that are called by the Gurobi solver\\n  during the optimization.  To use a callback, define a method\\n  that takes two integer arguments (model and where), and pass it\\n  as the argument to Model.optimize.  Once optimization begins,\\n  your method will be called with one of the following \'where\' values:\\n\\n  Possible \'where\' values (e.g., where == GRB.Callback.MIP) are:\\n\\n    POLLING:  Regular polling callback - no user queries allowed\\n    PRESOLVE: In presolve\\n    SIMPLEX:  In simplex\\n    BARRIER:  In barrier\\n    MIP:      In MIP\\n    MIPSOL:   New MIP incumbent available\\n    MIPNODE:  MIP node information available\\n    MULTIOBJ: In multi-objective optimization\\n    MESSAGE:  Optimizer output a message\\n\\n  Your method can call Model.cbGet() to obtain detailed information\\n  on the progress of the optimization.  Allowed values depend\\n  on \'where\'.  The prefix of the \'what\' name indicate which\\n  ones are allowed for each \'where\' (so \'PRE_COLDEL\' can only\\n  be called when where == SIMPLEX).\\n\\n  Allowed \'what\' values (e.g., cbGet(GRB.Callback.MIP_OBJBND) are:\\n\\n    RUNTIME: Elapsed solver runtime\\n    PRE_COLDEL: Deleted column count\\n    PRE_ROWDEL: Deleted row count\\n    PRE_SENCHG: Changed constraint sense count\\n    PRE_BNDCHG: Bound change count\\n    SPX_ITRCNT: Iteration count\\n    SPX_OBJVAL: Primal objective value\\n    SPX_PRIMINF: Primal infeasibility\\n    SPX_DUALINF: Dual infeasibility\\n    SPX_ISPERT: Has model been perturbed?\\n    BARRIER_ITRCNT: Barrier iteration count\\n    BARRIER_PRIMOBJ: Barrier iterate primal objective\\n    BARRIER_DUALOBJ: Barrier iterate dual objective\\n    BARRIER_PRIMINF: Barrier iterate primal infeasibility\\n    BARRIER_DUALINF: Barrier iterate dual infeasibility\\n    BARRIER_COMPL: Barrier iterate complementarity violation\\n    MIP_OBJBST: Best known objective bound\\n    MIP_OBJBND: Best known feasible objective\\n    MIP_NODCNT: Nodes explored so far\\n    MIP_SOLCNT: Solutions found so far\\n    MIP_CUTCNT: Cuts added to the model so far\\n    MIP_NODLFT: Unexplored nodes\\n    MIP_ITRCNT: Simplex iterations performed so far\\n    MIPSOL_SOL: Feasible solution (a vector)\\n    MIPSOL_OBJ: Objective value for feasible solution\\n    MIPSOL_OBJBST: Best known objective bound\\n    MIPSOL_OBJBND: Best known feasible objective\\n    MIPSOL_NODCNT: Node count for feasible solution\\n    MIPSOL_SOLCNT: Solutions found so far\\n    MIPNODE_STATUS: Optimization status of node relaxation\\n    MIPNODE_REL: Node relaxation solution or ray if unbounded\\n    MIPNODE_OBJBST: Best known objective bound\\n    MIPNODE_OBJBND: Best known feasible objective\\n    MIPNODE_NODCNT: Nodes explored so far\\n    MIPNODE_SOLCNT: Solutions found so far\\n    MIPNODE_SBRVAR: Node branching variable\\n    MULTIOBJ_OBJCNT: Objective count optimized so far\\n    MULTIOBJ_SOLCNT: Solutions found so far\\n    MULTIOBJ_SOL: Feasible solution (a vector)\\n    MSG_STRING: Output message\\n\\n  Your callback method can call other methods on the model object:\\n    cbCut(), cbGet(), cbGetNodeRel(), cbGetSolution(), cbSetSolution()\\n  ", \'POLLING\': 0, \'PRESOLVE\': 1, \'SIMPLEX\': 2, \'MIP\': 3, \'MIPSOL\': 4, \'MIPNODE\': 5, \'MESSAGE\': 6, \'BARRIER\': 7, \'MULTIOBJ\': 8, \'PRE_COLDEL\': 1000, \'PRE_ROWDEL\': 1001, \'PRE_SENCHG\': 1002, \'PRE_BNDCHG\': 1003, \'PRE_COECHG\': 1004, \'SPX_ITRCNT\': 2000, \'SPX_OBJVAL\': 2001, \'SPX_PRIMINF\': 2002, \'SPX_DUALINF\': 2003, \'SPX_ISPERT\': 2004, \'BARRIER_ITRCNT\': 7001, \'BARRIER_PRIMOBJ\': 7002, \'BARRIER_DUALOBJ\': 7003, \'BARRIER_PRIMINF\': 7004, \'BARRIER_DUALINF\': 7005, \'BARRIER_COMPL\': 7006, \'MIP_OBJBST\': 3000, \'MIP_OBJBND\': 3001, \'MIP_NODCNT\': 3002, \'MIP_SOLCNT\': 3003, \'MIP_CUTCNT\': 3004, \'MIP_NODLFT\': 3005, \'MIP_ITRCNT\': 3006, \'MIPSOL_SOL\': 4001, \'MIPSOL_OBJ\': 4002, \'MIPSOL_OBJBST\': 4003, \'MIPSOL_OBJBND\': 4004, \'MIPSOL_NODCNT\': 4005, \'MIPSOL_SOLCNT\': 4006, \'MIPNODE_STATUS\': 5001, \'MIPNODE_REL\': 5002, \'MIPNODE_OBJBST\': 5003, \'MIPNODE_OBJBND\': 5004, \'MIPNODE_NODCNT\': 5005, \'MIPNODE_SOLCNT\': 5006, \'MIPNODE_BRVAR\': 5007, \'MSG_STRING\': 6001, \'RUNTIME\': 6002, \'MULTIOBJ_OBJCNT\': 8001, \'MULTIOBJ_SOLCNT\': 8002, \'MULTIOBJ_SOL\': 8003, \'__init__\': <cyfunction CallbackClass.__init__ at 0x00000248A608CEA8>, \'_solnow\': <cyfunction CallbackClass._solnow at 0x00000248A608CF60>, \'callback\': <cyfunction CallbackClass.callback at 0x00000248A608E048>, \'__dict__\': <attribute \'__dict__\' of \'CallbackClass\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'CallbackClass\' objects>})'


class Column(object):
    """
    Column class.  Columns consist of a set of coefficient, constraint
      pairs.  They capture the set of linear constraints in which a
      variable participates.
    
      The constructor for this class takes two arguments: Column(coeffs, constrs).
      The constrs argument gives a Constr or list of Constr.  The coeffs
      argument gives the corresponding coefficients
      (e.g., "col = Column([1.0, 2.0], [c0, c1])").
    
      Available methods on Column objects are:
        addTerms(coeffs, constrs): Add terms into a column.
        clear(): Set a column to zero.
        copy(): Copy a column.
        getCoeff(i): Return the coefficient for the term at index 'i'.
        getConstr(i): Return the constraint for the term at index 'i'.
        remove(i): Remove a term from the column.
        size(): Return the number of terms in the column.
    
      You can say "help(Column.method)" to get help on any method
      (e.g., help(Column.size)).
    """
    def addTerms(self, coeffs, constrs): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addTerms(coeffs, constrs)
        
            PURPOSE:
              Add a list of terms into a column.
        
            ARGUMENTS:
              coeffs (float or list of float): The coefficients for the new terms
              constrs (Constr or list of Constr): The constraints for the new terms
        
            EXAMPLE:
              c0.addTerms(1.0, x)
              c0.addTerms([1.0, 2.0], [x, y])
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              clear()
        
            PURPOSE:
              Clear a column.
        
            EXAMPLE:
              print(c0.clear())
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              copy()
        
            PURPOSE:
              Copy a column.
        
            EXAMPLE:
              c1 = c0.copy()
        """
        pass

    def getCoeff(self, i): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getCoeff(i)
        
            PURPOSE:
              Return the coefficient for the term at index 'i'.
        
            ARGUMENTS:
              i (Int): Index of term whose coefficient is requested
        
            RETURN VALUE:
              The requested coefficient.
        
            EXAMPLE:
              print(c0.getCoeff(i))
        """
        pass

    def getConstr(self, i): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getConstr(i)
        
            PURPOSE:
              Return the constraint for the term at index 'i'.
        
            ARGUMENTS:
              i (Int): Index of term whose constraint is requested
        
            RETURN VALUE:
              The requested constraint (a Constr object).
        
            EXAMPLE:
              print(c0.getConstr(i))
        """
        pass

    def remove(self, which): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              remove(which)
        
            PURPOSE:
              Remove a term from the column.
        
            ARGUMENTS:
              which: Term to remove.  Can be an Int, in which case the term at
                     index 'which' is removed, or a Constr, in which case all terms
                     that involve the Constr 'which' are removed.
        
            EXAMPLE:
              print(c0.remove(i))
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              size()
        
            PURPOSE:
              Return the number of terms in a column.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              Number of terms in column.
        
            EXAMPLE:
              print(c0.size())
        """
        pass

    def _normalize(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Column class.  Columns consist of a set of coefficient, constraint\\n  pairs.  They capture the set of linear constraints in which a\\n  variable participates.\\n\\n  The constructor for this class takes two arguments: Column(coeffs, constrs).\\n  The constrs argument gives a Constr or list of Constr.  The coeffs\\n  argument gives the corresponding coefficients\\n  (e.g., "col = Column([1.0, 2.0], [c0, c1])").\\n\\n  Available methods on Column objects are:\\n    addTerms(coeffs, constrs): Add terms into a column.\\n    clear(): Set a column to zero.\\n    copy(): Copy a column.\\n    getCoeff(i): Return the coefficient for the term at index \\\'i\\\'.\\n    getConstr(i): Return the constraint for the term at index \\\'i\\\'.\\n    remove(i): Remove a term from the column.\\n    size(): Return the number of terms in the column.\\n\\n  You can say "help(Column.method)" to get help on any method\\n  (e.g., help(Column.size)).\\n  \', \'__init__\': <cyfunction Column.__init__ at 0x00000248A6071550>, \'__repr__\': <cyfunction Column.__repr__ at 0x00000248A6071608>, \'_normalize\': <cyfunction Column._normalize at 0x00000248A60716C0>, \'addTerms\': <cyfunction Column.addTerms at 0x00000248A6071778>, \'size\': <cyfunction Column.size at 0x00000248A6071830>, \'getCoeff\': <cyfunction Column.getCoeff at 0x00000248A60718E8>, \'getConstr\': <cyfunction Column.getConstr at 0x00000248A60719A0>, \'remove\': <cyfunction Column.remove at 0x00000248A6071A58>, \'clear\': <cyfunction Column.clear at 0x00000248A6071B10>, \'copy\': <cyfunction Column.copy at 0x00000248A6071BC8>, \'__dict__\': <attribute \'__dict__\' of \'Column\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Column\' objects>})'


class Constr(object):
    """
    Gurobi constraint object.  Constraints have a number of attributes.
      Some can be set (e.g., c.rhs = 0.0), while others can only be queried
      (e.g., print(c.pi)).  The most commonly used constraint attributes are:
        sense: Constraint sense ('<', '>', or '=').
        rhs: Right-hand side value.
        constrName: Constraint name.
        pi: Dual value in current solution
        slack: Slack in current solution.
    
      Type "help(GRB.attr)" for a list of all available attributes.
    
      Note that attribute modifications are handled in a lazy fashion.  You
      won't see the effect of a change until after the next call to Model.update()
      or Model.optimize().
    """
    def getAttr(self, attrname): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getAttr(attrname)
        
            PURPOSE:
              Request the value of a constraint attribute.
        
            ARGUMENTS:
              attrname (string): The name of the requested attribute.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              print(constr.getAttr("constrName"))
        
            NOTES:
              Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass

    def sameAs(self, otherconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              sameAs(otherconstr)
        
            PURPOSE:
              Indicates whether two constraint objects refer to the same Gurobi model
              constraints.
        
            ARGUMENTS:
              otherconstr (Constr): The constraint to compare against.
        
            RETURN VALUE:
              True if both Constr objects refer to the same model constraint.
        
            EXAMPLE:
              constr1.sameAs(constr2)
        """
        pass

    def setAttr(self, attrname, newvalue): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setAttr(attrname, newvalue)
        
            PURPOSE:
              Change the value of a constraint attribute.
        
            ARGUMENTS:
              attrname (string): The name of the attribute.
              newvalue: The desired new value.  The type of the value should be
                        compatible with the attribute type (e.g., an integer parameter
                        will take an integer value).
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              constr.setAttr("constrName", "New name")
        
            NOTES:
              Constraint attributes that can be set are:
                constrName: Constraint name.
                sense:      Constraint sense.
                rhs:        Right-hand side value.
        
              Attributes changes are handled in a lazy fashion.  The effect of a
              change isn't visible until after the next call to Model.update() or
              Model.optimize().
        """
        pass

    def __cindex__(self, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __numrows__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    PROPERTY:
      index

    PURPOSE:
      Request the index of the constraint in the model.

    RETURN VALUE:
      = -2: removed
      = -1: not in model
      >= 0: index of the constraint in the model

    EXAMPLE:
      print(constr.index)
    """

    typeenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Gurobi constraint object.  Constraints have a number of attributes.\\n  Some can be set (e.g., c.rhs = 0.0), while others can only be queried\\n  (e.g., print(c.pi)).  The most commonly used constraint attributes are:\\n    sense: Constraint sense (\\\'<\\\', \\\'>\\\', or \\\'=\\\').\\n    rhs: Right-hand side value.\\n    constrName: Constraint name.\\n    pi: Dual value in current solution\\n    slack: Slack in current solution.\\n\\n  Type "help(GRB.attr)" for a list of all available attributes.\\n\\n  Note that attribute modifications are handled in a lazy fashion.  You\\n  won\\\'t see the effect of a change until after the next call to Model.update()\\n  or Model.optimize().\\n  \', \'__init__\': <cyfunction Constr.__init__ at 0x00000248A606ABC8>, \'__dir__\': <cyfunction Constr.__dir__ at 0x00000248A606AC80>, \'__cindex__\': <cyfunction Constr.__cindex__ at 0x00000248A606AD38>, \'__repr__\': <cyfunction Constr.__repr__ at 0x00000248A606ADF0>, \'__numrows__\': <cyfunction Constr.__numrows__ at 0x00000248A606AEA8>, \'typename\': <property object at 0x00000248A6067458>, \'typeenum\': <property object at 0x00000248A60674A8>, \'__getattr__\': <cyfunction Constr.__getattr__ at 0x00000248A6069100>, \'__setattr__\': <cyfunction Constr.__setattr__ at 0x00000248A60691B8>, \'getAttr\': <cyfunction Constr.getAttr at 0x00000248A6069270>, \'setAttr\': <cyfunction Constr.setAttr at 0x00000248A6069328>, \'index\': <property object at 0x00000248A60674F8>, \'sameAs\': <cyfunction Constr.sameAs at 0x00000248A6069498>, \'__dict__\': <attribute \'__dict__\' of \'Constr\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Constr\' objects>})'


class Env(object):
    """
    Gurobi environment object.  Methods on this object are:
        readParams(paramname): Read a set of parameter settings from a file.
        resetParams(): Reset all parameters to their default values.
        setParam(paramname, newval): Set a parameter to a new value.
        writeParams(paramname): Write the current parameter settings to a file.
    
      Additional help can be obtained on any of these methods (e.g.,
      help(Env.setParam)).  A list of all available parameters can be
      obtained by typing 'help(GRB.param)'.
    """
    @classmethod
    def ClientEnv(cls, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              close()
        
            Synonymous to Env.dispose().
        """
        pass

    @classmethod
    def CloudEnv(cls, *args, **kwargs): # real signature unknown
        pass

    def dispose(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              dispose()
        
            PURPOSE:
              Free all resources associated with this Env object.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              env.dispose()
        
            NOTES:
              Dispose of all models created in this environment before disposing
              of this Env object.
        
              After this method is called, this Env object must no longer be used.
        """
        pass

    @classmethod
    def OtherEnv(cls, *args, **kwargs): # real signature unknown
        pass

    def readParams(self, filename): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              readParams(filename)
        
            PURPOSE:
              Read a set of parameter settings from a file.
        
            ARGUMENTS:
              filename (string): A path to a file containing a list of parameter
                                 settings.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              env.readParams('gurobi.prm')
        
            NOTES:
              This routine should normally be called on the default environment or on
              a model object.
        
              The parameter file should contain "name value" pairs, each on its own
              line.  A hash symbol at the beginning of a line indicates that the line
              should be ignored.  Here is an example of a valid parameter file:
        
                # List of changed parameters
                TimeLimit      100
                IterationLimit 1000
        """
        pass

    def resetParams(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              resetParams()
        
            PURPOSE:
              Reset all parameters to their default values.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              env.resetParams()
        
            NOTES:
              This routine should normally be called on the default environment or on
              a model object.
        """
        pass

    def setParam(self, paramname, newvalue): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setParam(paramname, newvalue)
        
            PURPOSE:
              Set a parameter to a new value.
        
            ARGUMENTS:
              paramname (string): The name of the parameter.
              newvalue: The desired new value.  The type of the value should be
                        compatible with the parameter type (e.g., an integer parameter
                        will take an integer value).  One important exception: the
                        string "default" will return the specified parameter to its
                        default value.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              env.setParam("NodeLimit", 100)
              env.setParam("TimeLimit", "default")
        
            NOTES:
              Use this routine to change parameter values in the default environment.
              The default environment is used to initialize parameter values when a
              new model is created.  Once the model exists, changes to the default
              environment will no longer affect that model.  Use Model.setParam()
              to change parameter settings for an existing model.
        
              Routine paramHelp() provides additional information on the available
              parameters.
        """
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def writeParams(self, filename): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              writeParams(filename)
        
            PURPOSE:
              Write non-default parameter settings to a file.
        
            ARGUMENTS:
              filename (string): The name of the file to which non-default parameter
                                 settings should be written.
        
            RETURN VALUE:
              The Env object itself.
        
            EXAMPLE:
              env.writeParams('changed.prm')
        
            NOTES:
              This routine should normally be called on the default environment or on
              a model object.
        
              Upon completion, the specified file will contain a set of "name value"
              pairs, one per line, that indicates the set of parameters that current
              have non-default values in the specified model.
        """
        pass

    def _Env__setone(self, *args, **kwargs): # real signature unknown
        pass

    def _getParamInfo(self, *args, **kwargs): # real signature unknown
        pass

    def _message(self, *args, **kwargs): # real signature unknown
        pass

    def _paramlist(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': "\\n  Gurobi environment object.  Methods on this object are:\\n    readParams(paramname): Read a set of parameter settings from a file.\\n    resetParams(): Reset all parameters to their default values.\\n    setParam(paramname, newval): Set a parameter to a new value.\\n    writeParams(paramname): Write the current parameter settings to a file.\\n\\n  Additional help can be obtained on any of these methods (e.g.,\\n  help(Env.setParam)).  A list of all available parameters can be\\n  obtained by typing \'help(GRB.param)\'.\\n  ", \'__init__\': <cyfunction Env.__init__ at 0x00000248A47CF830>, \'__del__\': <cyfunction Env.__del__ at 0x00000248A47CF8E8>, \'__repr__\': <cyfunction Env.__repr__ at 0x00000248A47CF9A0>, \'__enter__\': <cyfunction Env.__enter__ at 0x00000248A47CFA58>, \'__exit__\': <cyfunction Env.__exit__ at 0x00000248A47CFB10>, \'_paramlist\': <cyfunction Env._paramlist at 0x00000248A47CFBC8>, \'_message\': <cyfunction Env._message at 0x00000248A47CFC80>, \'_getParamInfo\': <cyfunction Env._getParamInfo at 0x00000248A47CFD38>, \'_Env__setone\': <cyfunction Env.__setone at 0x00000248A47CFDF0>, \'setParam\': <cyfunction Env.setParam at 0x00000248A47CFEA8>, \'resetParams\': <cyfunction Env.resetParams at 0x00000248A47CFF60>, \'readParams\': <cyfunction Env.readParams at 0x00000248A606E048>, \'writeParams\': <cyfunction Env.writeParams at 0x00000248A606E100>, \'start\': <cyfunction Env.start at 0x00000248A606E1B8>, \'dispose\': <cyfunction Env.dispose at 0x00000248A606E270>, \'close\': <cyfunction Env.close at 0x00000248A606E328>, \'ClientEnv\': <classmethod object at 0x00000248A60658D0>, \'CloudEnv\': <classmethod object at 0x00000248A6065908>, \'OtherEnv\': <classmethod object at 0x00000248A6065940>, \'__dict__\': <attribute \'__dict__\' of \'Env\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Env\' objects>})'


class ErrorConstClass(object):
    """
    Gurobi error codes (e.g., exception.errno == GRB.ERROR_OUT_OF_MEMORY):
    
        OUT_OF_MEMORY: Exhausted available memory
        NULL_ARGUMENT: NULL argument value
        INVALID_ARGUMENT: Invalid argument value
        UNKNOWN_ATTRIBUTE: Unknown attribute name
        DATA_NOT_AVAILABLE: Requested data not available
        INDEX_OUT_OF_RANGE: Constr/var index out of range
        UNKNOWN_PARAMETER: Unknown parameter name
        VALUE_OUT_OF_RANGE: Parameter value outside of valid range
        NO_LICENSE: No Gurobi license found
        SIZE_LIMIT_EXCEEDED: Exceeded licensed model size limit
        CALLBACK: Error in callback
        FILE_READ: Error reading file
        FILE_WRITE: Error writing file
        NUMERIC: Numeric error encountered
        IIS_NOT_INFEASIBLE: Can't compute an IIS on a feasible model
        NOT_FOR_MIP: Method not valid for MIP models
        OPTIMIZATION_IN_PROGRESS: Must stop optimization to query results
        DUPLICATES: Duplicate entries in list
        NODEFILE: Problem reading or writing node file
        Q_NOT_PSD: Q matrix isn't Positive Semi-Definite
        QCP_EQUALITY_CONSTRAINT: Quadratic constraints must be inequalities
        NETWORK: Network error
        JOB_REJECTED: Job rejected by Compute Server
        NOT_SUPPORTED: Requested operation is not supported
        EXCEED_2B_NONZEROS: Result too large for query routine
        INVALID_PIECEWISE_OBJ: Problem with specified piecewise-linear objective
        JOB_REJECTED: Job rejected by Compute Server
        NOT_SUPPORTED: Operation is not supported
        NOT_IN_MODEL: Variable/constraint not in model
        FAILED_TO_CREATE_MODEL: Failed to create the requested model
        CLOUD: Instant Cloud error
        MODEL_MODIFICATION: An error occurred during model modification or update
        CSWORKER: An error occurred with the client-server application
        TUNE_MODEL_TYPES: Tried multi-model tuning on models of different types
        INTERNAL: Internal Gurobi error
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CALLBACK = 10011
    CLOUD = 10028
    CSWORKER = 10030
    DATA_NOT_AVAILABLE = 10005
    DUPLICATES = 10018
    EXCEED_2B_NONZEROS = 10025
    FAILED_TO_CREATE_MODEL = 20002
    FILE_READ = 10012
    FILE_WRITE = 10013
    IIS_NOT_INFEASIBLE = 10015
    INDEX_OUT_OF_RANGE = 10006
    INTERNAL = 20003
    INVALID_ARGUMENT = 10003
    INVALID_PIECEWISE_OBJ = 10026
    JOB_REJECTED = 10023
    MODEL_MODIFICATION = 10029
    NETWORK = 10022
    NODEFILE = 10019
    NOT_FOR_MIP = 10016
    NOT_IN_MODEL = 20001
    NOT_SUPPORTED = 10024
    NO_LICENSE = 10009
    NULL_ARGUMENT = 10002
    NUMERIC = 10014
    OPTIMIZATION_IN_PROGRESS = 10017
    OUT_OF_MEMORY = 10001
    QCP_EQUALITY_CONSTRAINT = 10021
    Q_NOT_PSD = 10020
    SIZE_LIMIT_EXCEEDED = 10010
    TUNE_MODEL_TYPES = 10031
    UNKNOWN_ATTRIBUTE = 10004
    UNKNOWN_PARAMETER = 10007
    UPDATEMODE_CHANGE = 10027
    VALUE_OUT_OF_RANGE = 10008
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': "\\n  Gurobi error codes (e.g., exception.errno == GRB.ERROR_OUT_OF_MEMORY):\\n\\n    OUT_OF_MEMORY: Exhausted available memory\\n    NULL_ARGUMENT: NULL argument value\\n    INVALID_ARGUMENT: Invalid argument value\\n    UNKNOWN_ATTRIBUTE: Unknown attribute name\\n    DATA_NOT_AVAILABLE: Requested data not available\\n    INDEX_OUT_OF_RANGE: Constr/var index out of range\\n    UNKNOWN_PARAMETER: Unknown parameter name\\n    VALUE_OUT_OF_RANGE: Parameter value outside of valid range\\n    NO_LICENSE: No Gurobi license found\\n    SIZE_LIMIT_EXCEEDED: Exceeded licensed model size limit\\n    CALLBACK: Error in callback\\n    FILE_READ: Error reading file\\n    FILE_WRITE: Error writing file\\n    NUMERIC: Numeric error encountered\\n    IIS_NOT_INFEASIBLE: Can\'t compute an IIS on a feasible model\\n    NOT_FOR_MIP: Method not valid for MIP models\\n    OPTIMIZATION_IN_PROGRESS: Must stop optimization to query results\\n    DUPLICATES: Duplicate entries in list\\n    NODEFILE: Problem reading or writing node file\\n    Q_NOT_PSD: Q matrix isn\'t Positive Semi-Definite\\n    QCP_EQUALITY_CONSTRAINT: Quadratic constraints must be inequalities\\n    NETWORK: Network error\\n    JOB_REJECTED: Job rejected by Compute Server\\n    NOT_SUPPORTED: Requested operation is not supported\\n    EXCEED_2B_NONZEROS: Result too large for query routine\\n    INVALID_PIECEWISE_OBJ: Problem with specified piecewise-linear objective\\n    JOB_REJECTED: Job rejected by Compute Server\\n    NOT_SUPPORTED: Operation is not supported\\n    NOT_IN_MODEL: Variable/constraint not in model\\n    FAILED_TO_CREATE_MODEL: Failed to create the requested model\\n    CLOUD: Instant Cloud error\\n    MODEL_MODIFICATION: An error occurred during model modification or update\\n    CSWORKER: An error occurred with the client-server application\\n    TUNE_MODEL_TYPES: Tried multi-model tuning on models of different types\\n    INTERNAL: Internal Gurobi error\\n  ", \'OUT_OF_MEMORY\': 10001, \'NULL_ARGUMENT\': 10002, \'INVALID_ARGUMENT\': 10003, \'UNKNOWN_ATTRIBUTE\': 10004, \'DATA_NOT_AVAILABLE\': 10005, \'INDEX_OUT_OF_RANGE\': 10006, \'UNKNOWN_PARAMETER\': 10007, \'VALUE_OUT_OF_RANGE\': 10008, \'NO_LICENSE\': 10009, \'SIZE_LIMIT_EXCEEDED\': 10010, \'CALLBACK\': 10011, \'FILE_READ\': 10012, \'FILE_WRITE\': 10013, \'NUMERIC\': 10014, \'IIS_NOT_INFEASIBLE\': 10015, \'NOT_FOR_MIP\': 10016, \'OPTIMIZATION_IN_PROGRESS\': 10017, \'DUPLICATES\': 10018, \'NODEFILE\': 10019, \'Q_NOT_PSD\': 10020, \'QCP_EQUALITY_CONSTRAINT\': 10021, \'NETWORK\': 10022, \'JOB_REJECTED\': 10023, \'NOT_SUPPORTED\': 10024, \'EXCEED_2B_NONZEROS\': 10025, \'INVALID_PIECEWISE_OBJ\': 10026, \'UPDATEMODE_CHANGE\': 10027, \'CLOUD\': 10028, \'MODEL_MODIFICATION\': 10029, \'CSWORKER\': 10030, \'TUNE_MODEL_TYPES\': 10031, \'NOT_IN_MODEL\': 20001, \'FAILED_TO_CREATE_MODEL\': 20002, \'INTERNAL\': 20003, \'__dict__\': <attribute \'__dict__\' of \'ErrorConstClass\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'ErrorConstClass\' objects>})'


class GenConstr(object):
    """
    Gurobi GenConstr object.  GenConstr objects have several attributes.
      Some can be set (e.g., gc.GenConstrName = "gc"), while others can only
      be queried (e.g., print(gc.GenConstrType)). Some attributes are
      only for the function constraints, such as FuncPieces.
    
      Type "help(GRB.attr)" for a list of all available attributes.
    
      Note that attribute modifications are handled in a lazy fashion.  You
      won't see the effect of a change until after the next call to Model.update()
      or Model.optimize().
    """
    def getAttr(self, attrname): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getAttr(attrname)
        
            PURPOSE:
              Request the value of a GenConstr attribute.
        
            ARGUMENTS:
              attrname (string): The name of the requested attribute.
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              print(genconstr.getAttr("IISGenConstr"))
        
            NOTES:
              Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass

    def setAttr(self, attrname, newvalue): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setAttr(attrname, newvalue)
        
            PURPOSE:
              Change the value of a GenConstr attribute.
        
            ARGUMENTS:
              attrname (string): The name of the attribute.
              newvalue: The desired new value.  The type of the value should be
                        compatible with the attribute type (e.g., an integer parameter
                        will take an integer value).
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              genconstr.setAttr("GenConstrName", "New name")
        
            NOTES:
              Attributes changes are handled in a lazy fashion.  The effect of a
              change isn't visible until after the next call to Model.update() or
              Model.optimize().
        """
        pass

    def __cindex__(self, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    typeenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Gurobi GenConstr object.  GenConstr objects have several attributes.\\n  Some can be set (e.g., gc.GenConstrName = "gc"), while others can only\\n  be queried (e.g., print(gc.GenConstrType)). Some attributes are\\n  only for the function constraints, such as FuncPieces.\\n\\n  Type "help(GRB.attr)" for a list of all available attributes.\\n\\n  Note that attribute modifications are handled in a lazy fashion.  You\\n  won\\\'t see the effect of a change until after the next call to Model.update()\\n  or Model.optimize().\\n  \', \'__init__\': <cyfunction GenConstr.__init__ at 0x00000248A606B270>, \'__dir__\': <cyfunction GenConstr.__dir__ at 0x00000248A606B328>, \'__cindex__\': <cyfunction GenConstr.__cindex__ at 0x00000248A606B3E0>, \'__repr__\': <cyfunction GenConstr.__repr__ at 0x00000248A606B498>, \'typename\': <property object at 0x00000248A6067778>, \'typeenum\': <property object at 0x00000248A60677C8>, \'__getattr__\': <cyfunction GenConstr.__getattr__ at 0x00000248A606B6C0>, \'__setattr__\': <cyfunction GenConstr.__setattr__ at 0x00000248A606B778>, \'getAttr\': <cyfunction GenConstr.getAttr at 0x00000248A606B830>, \'setAttr\': <cyfunction GenConstr.setAttr at 0x00000248A606B8E8>, \'__dict__\': <attribute \'__dict__\' of \'GenConstr\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'GenConstr\' objects>})'


class GenExpr(object):
    """ General expression class.  Used by General constraints. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__doc__': '\\n  General expression class.  Used by General constraints.\\n  ', '__init__': <cyfunction GenExpr.__init__ at 0x00000248A608BF60>, '__repr__': <cyfunction GenExpr.__repr__ at 0x00000248A608C048>, '__ne__': <cyfunction GenExpr.__ne__ at 0x00000248A608C100>, '__eq__': <cyfunction GenExpr.__eq__ at 0x00000248A608C1B8>, '__dict__': <attribute '__dict__' of 'GenExpr' objects>, '__weakref__': <attribute '__weakref__' of 'GenExpr' objects>, '__hash__': None})"
    __hash__ = None


class GRB(object):
    """
    Gurobi constants.  Constants defined in this class are as follows:
    
        Basis status (e.g., var.vBasis == GRB.BASIC):
    
          BASIC: Variable is basic
          NONBASIC_LOWER: Variable is non-basic at lower bound
          NONBASIC_UPPER: Variable is non-basic at upper bound
          SUPERBASIC: Variable is superbasic
    
        Constraint sense (e.g., constr.sense = GRB.LESS_EQUAL):
    
          LESS_EQUAL, GREATER_EQUAL, EQUAL
    
        Variable types (e.g., var.vType = GRB.INTEGER):
    
          CONTINUOUS, BINARY, INTEGER, SEMICONT, SEMIINT
    
        SOS types:
    
          SOS_TYPE1, SOS_TYPE2
    
        General constraint types:
    
          GENCONSTR_MAX, GENCONSTR_MIN, GENCONSTR_ABS, GENCONSTR_AND, GENCONSTR_OR,
          GENCONSTR_INDICATOR, GENCONSTR_PWL GENCONSTR_POLY, GENCONSTR_EXP,
          GENCONSTR_EXPA, GENCONSTR_LOG, GENCONSTR_LOGA, GENCONSTR_POW,
          GENCONSTR_SIN, GENCONSTR_COS, GENCONSTR_TAN
    
      The GRB class also includes definitions for attributes (GRB.attr),
      errors (GRB.error), parameters (GRB.param), status codes (GRB.status),
      and callbacks (GRB.callback).  You can ask for help on any of these
      (e.g., "help(GRB.attr)").
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    attr = None # (!) real value is '<gurobipy.AttrConstClass object at 0x00000248A6081160>'
    Attr = None # (!) real value is '<gurobipy.AttrConstClass object at 0x00000248A6081160>'
    BASIC = 0
    BATCH_ABORTED = 3
    BATCH_COMPLETED = 5
    BATCH_CREATED = 1
    BATCH_FAILED = 4
    BATCH_SUBMITTED = 2
    BINARY = 'B'
    callback = None # (!) real value is '<gurobipy.CallbackClass object at 0x00000248A60811D0>'
    Callback = None # (!) real value is '<gurobipy.CallbackClass object at 0x00000248A60811D0>'
    CONTINUOUS = 'C'
    CUTOFF = 6
    DEFAULT_CS_PORT = 61000
    EQUAL = '='
    error = None # (!) real value is '<gurobipy.ErrorConstClass object at 0x00000248A6081208>'
    Error = None # (!) real value is '<gurobipy.ErrorConstClass object at 0x00000248A6081208>'
    ERROR_CALLBACK = 10011
    ERROR_CLOUD = 10028
    ERROR_CSWORKER = 10030
    ERROR_DATA_NOT_AVAILABLE = 10005
    ERROR_DUPLICATES = 10018
    ERROR_EXCEED_2B_NONZEROS = 10025
    ERROR_FAILED_TO_CREATE_MODEL = 20002
    ERROR_FILE_READ = 10012
    ERROR_FILE_WRITE = 10013
    ERROR_IIS_NOT_INFEASIBLE = 10015
    ERROR_INDEX_OUT_OF_RANGE = 10006
    ERROR_INTERNAL = 20003
    ERROR_INVALID_ARGUMENT = 10003
    ERROR_INVALID_PIECEWISE_OBJ = 10026
    ERROR_JOB_REJECTED = 10023
    ERROR_MODEL_MODIFICATION = 10029
    ERROR_NETWORK = 10022
    ERROR_NODEFILE = 10019
    ERROR_NOT_FOR_MIP = 10016
    ERROR_NOT_IN_MODEL = 20001
    ERROR_NOT_SUPPORTED = 10024
    ERROR_NO_LICENSE = 10009
    ERROR_NULL_ARGUMENT = 10002
    ERROR_NUMERIC = 10014
    ERROR_OPTIMIZATION_IN_PROGRESS = 10017
    ERROR_OUT_OF_MEMORY = 10001
    ERROR_QCP_EQUALITY_CONSTRAINT = 10021
    ERROR_Q_NOT_PSD = 10020
    ERROR_SECURITY = 10032
    ERROR_SIZE_LIMIT_EXCEEDED = 10010
    ERROR_TUNE_MODEL_TYPES = 10031
    ERROR_UNKNOWN_ATTRIBUTE = 10004
    ERROR_UNKNOWN_PARAMETER = 10007
    ERROR_UPDATEMODE_CHANGE = 10027
    ERROR_VALUE_OUT_OF_RANGE = 10008
    GENCONSTR_ABS = 2
    GENCONSTR_AND = 3
    GENCONSTR_COS = 14
    GENCONSTR_EXP = 8
    GENCONSTR_EXPA = 9
    GENCONSTR_INDICATOR = 5
    GENCONSTR_LOG = 10
    GENCONSTR_LOGA = 11
    GENCONSTR_MAX = 0
    GENCONSTR_MIN = 1
    GENCONSTR_OR = 4
    GENCONSTR_POLY = 7
    GENCONSTR_POW = 12
    GENCONSTR_PWL = 6
    GENCONSTR_SIN = 13
    GENCONSTR_TAN = 15
    GREATER_EQUAL = '>'
    INFEASIBLE = 3
    INFINITY = 1e+100
    INF_OR_UNBD = 4
    INPROGRESS = 14
    INTEGER = 'I'
    INTERRUPTED = 11
    ITERATION_LIMIT = 7
    LESS_EQUAL = '<'
    LOADED = 1
    MAXIMIZE = -1
    MAXINT = 2000000000
    MAX_CONCURRENT = 64
    MAX_NAMELEN = 255
    MAX_STRLEN = 512
    MAX_TAGLEN = 10240
    MINIMIZE = 1
    NODE_LIMIT = 8
    NONBASIC_LOWER = -1
    NONBASIC_UPPER = -2
    NUMERIC = 12
    OPTIMAL = 2
    param = None # (!) real value is '<gurobipy.ParamConstClass object at 0x00000248A6081198>'
    Param = None # (!) real value is '<gurobipy.ParamConstClass object at 0x00000248A6081198>'
    SEMICONT = 'S'
    SEMIINT = 'N'
    SOLUTION_LIMIT = 10
    SOS_TYPE1 = 1
    SOS_TYPE2 = 2
    status = None # (!) real value is '<gurobipy.StatusConstClass object at 0x00000248A6081240>'
    Status = None # (!) real value is '<gurobipy.StatusConstClass object at 0x00000248A6081240>'
    SUBOPTIMAL = 13
    SUPERBASIC = -3
    TIME_LIMIT = 9
    UNBOUNDED = 5
    UNDEFINED = 1e+101
    USER_OBJ_LIMIT = 15
    VERSION_MAJOR = 9
    VERSION_MINOR = 0
    VERSION_TECHNICAL = 2
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Gurobi constants.  Constants defined in this class are as follows:\\n\\n    Basis status (e.g., var.vBasis == GRB.BASIC):\\n\\n      BASIC: Variable is basic\\n      NONBASIC_LOWER: Variable is non-basic at lower bound\\n      NONBASIC_UPPER: Variable is non-basic at upper bound\\n      SUPERBASIC: Variable is superbasic\\n\\n    Constraint sense (e.g., constr.sense = GRB.LESS_EQUAL):\\n\\n      LESS_EQUAL, GREATER_EQUAL, EQUAL\\n\\n    Variable types (e.g., var.vType = GRB.INTEGER):\\n\\n      CONTINUOUS, BINARY, INTEGER, SEMICONT, SEMIINT\\n\\n    SOS types:\\n\\n      SOS_TYPE1, SOS_TYPE2\\n\\n    General constraint types:\\n\\n      GENCONSTR_MAX, GENCONSTR_MIN, GENCONSTR_ABS, GENCONSTR_AND, GENCONSTR_OR,\\n      GENCONSTR_INDICATOR, GENCONSTR_PWL GENCONSTR_POLY, GENCONSTR_EXP,\\n      GENCONSTR_EXPA, GENCONSTR_LOG, GENCONSTR_LOGA, GENCONSTR_POW,\\n      GENCONSTR_SIN, GENCONSTR_COS, GENCONSTR_TAN\\n\\n  The GRB class also includes definitions for attributes (GRB.attr),\\n  errors (GRB.error), parameters (GRB.param), status codes (GRB.status),\\n  and callbacks (GRB.callback).  You can ask for help on any of these\\n  (e.g., "help(GRB.attr)").\\n  \', \'attr\': <gurobipy.AttrConstClass object at 0x00000248A6081160>, \'Attr\': <gurobipy.AttrConstClass object at 0x00000248A6081160>, \'param\': <gurobipy.ParamConstClass object at 0x00000248A6081198>, \'Param\': <gurobipy.ParamConstClass object at 0x00000248A6081198>, \'callback\': <gurobipy.CallbackClass object at 0x00000248A60811D0>, \'Callback\': <gurobipy.CallbackClass object at 0x00000248A60811D0>, \'error\': <gurobipy.ErrorConstClass object at 0x00000248A6081208>, \'Error\': <gurobipy.ErrorConstClass object at 0x00000248A6081208>, \'status\': <gurobipy.StatusConstClass object at 0x00000248A6081240>, \'Status\': <gurobipy.StatusConstClass object at 0x00000248A6081240>, \'LOADED\': 1, \'OPTIMAL\': 2, \'INFEASIBLE\': 3, \'INF_OR_UNBD\': 4, \'UNBOUNDED\': 5, \'CUTOFF\': 6, \'ITERATION_LIMIT\': 7, \'NODE_LIMIT\': 8, \'TIME_LIMIT\': 9, \'SOLUTION_LIMIT\': 10, \'INTERRUPTED\': 11, \'NUMERIC\': 12, \'SUBOPTIMAL\': 13, \'INPROGRESS\': 14, \'USER_OBJ_LIMIT\': 15, \'BATCH_CREATED\': 1, \'BATCH_SUBMITTED\': 2, \'BATCH_ABORTED\': 3, \'BATCH_FAILED\': 4, \'BATCH_COMPLETED\': 5, \'VERSION_MAJOR\': 9, \'VERSION_MINOR\': 0, \'VERSION_TECHNICAL\': 2, \'BASIC\': 0, \'NONBASIC_LOWER\': -1, \'NONBASIC_UPPER\': -2, \'SUPERBASIC\': -3, \'LESS_EQUAL\': \'<\', \'GREATER_EQUAL\': \'>\', \'EQUAL\': \'=\', \'CONTINUOUS\': \'C\', \'BINARY\': \'B\', \'INTEGER\': \'I\', \'SEMICONT\': \'S\', \'SEMIINT\': \'N\', \'MINIMIZE\': 1, \'MAXIMIZE\': -1, \'SOS_TYPE1\': 1, \'SOS_TYPE2\': 2, \'GENCONSTR_MAX\': 0, \'GENCONSTR_MIN\': 1, \'GENCONSTR_ABS\': 2, \'GENCONSTR_AND\': 3, \'GENCONSTR_OR\': 4, \'GENCONSTR_INDICATOR\': 5, \'GENCONSTR_PWL\': 6, \'GENCONSTR_POLY\': 7, \'GENCONSTR_EXP\': 8, \'GENCONSTR_EXPA\': 9, \'GENCONSTR_LOG\': 10, \'GENCONSTR_LOGA\': 11, \'GENCONSTR_POW\': 12, \'GENCONSTR_SIN\': 13, \'GENCONSTR_COS\': 14, \'GENCONSTR_TAN\': 15, \'INFINITY\': 1e+100, \'UNDEFINED\': 1e+101, \'MAXINT\': 2000000000, \'MAX_NAMELEN\': 255, \'MAX_STRLEN\': 512, \'MAX_TAGLEN\': 10240, \'MAX_CONCURRENT\': 64, \'DEFAULT_CS_PORT\': 61000, \'ERROR_OUT_OF_MEMORY\': 10001, \'ERROR_NULL_ARGUMENT\': 10002, \'ERROR_INVALID_ARGUMENT\': 10003, \'ERROR_UNKNOWN_ATTRIBUTE\': 10004, \'ERROR_DATA_NOT_AVAILABLE\': 10005, \'ERROR_INDEX_OUT_OF_RANGE\': 10006, \'ERROR_UNKNOWN_PARAMETER\': 10007, \'ERROR_VALUE_OUT_OF_RANGE\': 10008, \'ERROR_NO_LICENSE\': 10009, \'ERROR_SIZE_LIMIT_EXCEEDED\': 10010, \'ERROR_CALLBACK\': 10011, \'ERROR_FILE_READ\': 10012, \'ERROR_FILE_WRITE\': 10013, \'ERROR_NUMERIC\': 10014, \'ERROR_IIS_NOT_INFEASIBLE\': 10015, \'ERROR_NOT_FOR_MIP\': 10016, \'ERROR_OPTIMIZATION_IN_PROGRESS\': 10017, \'ERROR_DUPLICATES\': 10018, \'ERROR_NODEFILE\': 10019, \'ERROR_Q_NOT_PSD\': 10020, \'ERROR_QCP_EQUALITY_CONSTRAINT\': 10021, \'ERROR_NETWORK\': 10022, \'ERROR_JOB_REJECTED\': 10023, \'ERROR_NOT_SUPPORTED\': 10024, \'ERROR_EXCEED_2B_NONZEROS\': 10025, \'ERROR_INVALID_PIECEWISE_OBJ\': 10026, \'ERROR_UPDATEMODE_CHANGE\': 10027, \'ERROR_CLOUD\': 10028, \'ERROR_MODEL_MODIFICATION\': 10029, \'ERROR_CSWORKER\': 10030, \'ERROR_TUNE_MODEL_TYPES\': 10031, \'ERROR_SECURITY\': 10032, \'ERROR_NOT_IN_MODEL\': 20001, \'ERROR_FAILED_TO_CREATE_MODEL\': 20002, \'ERROR_INTERNAL\': 20003, \'__dict__\': <attribute \'__dict__\' of \'GRB\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'GRB\' objects>})'


class gurobi(object):
    # no doc
    @classmethod
    def disposeDefaultEnv(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def interactive(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def models(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def platform(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def read(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def version(cls, *args, **kwargs): # real signature unknown
        pass

    def _cleanup(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _getdefaultenv(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _getmodels(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _defaultenv = None
    _exiting = False
    _gurobi__interactive = False
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '_gurobi__interactive': False, '_defaultenv': None, '_exiting': False, 'interactive': <classmethod object at 0x00000248A60812B0>, '_getdefaultenv': <classmethod object at 0x00000248A60819E8>, '_getmodels': <classmethod object at 0x00000248A60819B0>, '_cleanup': <cyfunction gurobi._cleanup at 0x00000248A60913E0>, 'version': <classmethod object at 0x00000248A60818D0>, 'platform': <classmethod object at 0x00000248A6081940>, 'read': <classmethod object at 0x00000248A6081A58>, 'models': <classmethod object at 0x00000248A6081908>, 'disposeDefaultEnv': <classmethod object at 0x00000248A6081A90>, '__dict__': <attribute '__dict__' of 'gurobi' objects>, '__weakref__': <attribute '__weakref__' of 'gurobi' objects>, '__doc__': None})"


class GurobiError(Exception):
    """ Gurobi exception class """
    def _get_message(self, *args, **kwargs): # real signature unknown
        pass

    def _set_message(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Iterable(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def __subclasshook__(cls, *args, **kwargs): # real signature unknown
        pass

    _abc_impl = None # (!) real value is '<_abc_data object at 0x00000248A40A4360>'
    __abstractmethods__ = frozenset({'__iter__'})
    __slots__ = ()


class izip(object):
    """
    zip(iter1 [,iter2 [...]]) --> zip object
    
    Return a zip object whose .__next__() method returns a tuple where
    the i-th element comes from the i-th iterable argument.  The .__next__()
    method continues until the shortest iterable in the argument sequence
    is exhausted and then it raises StopIteration.
    """
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass


class LinExpr(object):
    # no doc
    def add(self, expr, mult=1.0): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              add(expr, mult=1.0)
        
            PURPOSE:
              Add a linear multiple of one expression into another.
        
            ARGUMENTS:
              expr (LinExpr): The expression to add
              mult (float):   The linear multiplier
        
            EXAMPLE:
              expr1.add(expr2, 2.0)
        """
        pass

    def addConstant(self, constant): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addConstant(constant)
        
            PURPOSE:
              Add a constant into a linear expression.
        
            ARGUMENTS:
              constant (float): The value to add
        
            EXAMPLE:
              expr.addConstant(3.5)
        """
        pass

    def addTerms(self, coeffs, vars): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addTerms(coeffs, vars)
        
            PURPOSE:
              Add a list of terms into a linear expression.
        
            ARGUMENTS:
              coeffs (list of float): The coefficients for the new terms
              vars (list of Var):     The variables for the new terms
        
            EXAMPLE:
              expr.addTerms(1.0, x)
              expr.addTerms([1.0, 2.0], [x, y])
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              clear()
        
            PURPOSE:
              Set a linear expression to zero.
        
            EXAMPLE:
              print(expr.clear())
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              copy()
        
            PURPOSE:
              Copy a linear expression.
        
            EXAMPLE:
              expr2 = expr1.copy()
        """
        pass

    def getCoeff(self, i): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getCoeff(i)
        
            PURPOSE:
              Return the coefficient for the term at index 'i'.
        
            ARGUMENTS:
              i (Int): Index of term whose coefficient is requested
        
            RETURN VALUE:
              The requested coefficient.
        
            EXAMPLE:
              print(expr.getCoeff(i))
        """
        pass

    def getConstant(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getConstant()
        
            PURPOSE:
              Return the constant terms from a linear expression.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              Constant for expression.
        
            EXAMPLE:
              print(expr.getConstant())
        """
        pass

    def getValue(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getValue()
        
            PURPOSE:
              Compute the value of the expression, using the current solution.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              The computed expression value.
        
            EXAMPLE:
              print(model.getObjective().getValue())
        """
        pass

    def getVar(self, i): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getVar(i)
        
            PURPOSE:
              Return the variable for the term at index 'i'.
        
            ARGUMENTS:
              i (Int): Index of term whose variable is requested
        
            RETURN VALUE:
              The requested variable (a Var object).
        
            EXAMPLE:
              print(expr.getVar(i))
        """
        pass

    def remove(self, which): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              remove(which)
        
            PURPOSE:
              Remove a term from the expression.
        
            ARGUMENTS:
              which: Term to remove.  Can be an Int, in which case the term at
                     index 'which' is removed, or a Var, in which case all terms that
                     involve the Var 'which' are removed.
        
            EXAMPLE:
              print(expr.remove(i))
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              size()
        
            PURPOSE:
              Return the number of terms in a linear expression.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              Number of terms in expression.
        
            EXAMPLE:
              print(expr.size())
        """
        pass

    def _flatten(self, *args, **kwargs): # real signature unknown
        pass

    def _mul(self, *args, **kwargs): # real signature unknown
        pass

    def _normalize(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


class MLinExpr(object):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def flatten(self, *args, **kwargs): # real signature unknown
        pass

    def getValue(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getValue()
        
            PURPOSE:
              Compute the value of a linear matrix expression, using the current
              solution.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              The computed matrix expression value, as a 1-D NumPy array.
        
            EXAMPLE:
              expr = A @ x + b
              print(expr.getValue())
        """
        pass

    def _squeezetofit(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __matmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmatmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __array_priority__ = 100
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__array_priority__': 100, '__init__': <cyfunction MLinExpr.__init__ at 0x00000248A606F6C0>, '__repr__': <cyfunction MLinExpr.__repr__ at 0x00000248A606F778>, '_squeezetofit': <cyfunction MLinExpr._squeezetofit at 0x00000248A606F830>, 'shape': <property object at 0x00000248A6067A48>, 'copy': <cyfunction MLinExpr.copy at 0x00000248A606F9A0>, 'flatten': <cyfunction MLinExpr.flatten at 0x00000248A606FA58>, 'getValue': <cyfunction MLinExpr.getValue at 0x00000248A606FB10>, '__add__': <cyfunction MLinExpr.__add__ at 0x00000248A606FBC8>, '__radd__': <cyfunction MLinExpr.__radd__ at 0x00000248A606FC80>, '__iadd__': <cyfunction MLinExpr.__iadd__ at 0x00000248A606FD38>, '__sub__': <cyfunction MLinExpr.__sub__ at 0x00000248A606FDF0>, '__rsub__': <cyfunction MLinExpr.__rsub__ at 0x00000248A606FEA8>, '__isub__': <cyfunction MLinExpr.__isub__ at 0x00000248A606FF60>, '__mul__': <cyfunction MLinExpr.__mul__ at 0x00000248A6070048>, '__rmul__': <cyfunction MLinExpr.__rmul__ at 0x00000248A6070100>, '__imul__': <cyfunction MLinExpr.__imul__ at 0x00000248A60701B8>, '__matmul__': <cyfunction MLinExpr.__matmul__ at 0x00000248A6070270>, '__rmatmul__': <cyfunction MLinExpr.__rmatmul__ at 0x00000248A6070328>, '__neg__': <cyfunction MLinExpr.__neg__ at 0x00000248A60703E0>, '__le__': <cyfunction MLinExpr.__le__ at 0x00000248A6070498>, '__ge__': <cyfunction MLinExpr.__ge__ at 0x00000248A6070550>, '__eq__': <cyfunction MLinExpr.__eq__ at 0x00000248A6070608>, '__ne__': <cyfunction MLinExpr.__ne__ at 0x00000248A60706C0>, '__dict__': <attribute '__dict__' of 'MLinExpr' objects>, '__weakref__': <attribute '__weakref__' of 'MLinExpr' objects>, '__doc__': None, '__hash__': None})"
    __hash__ = None


class Model(object):
    """
    Gurobi model object.  Commonly used methods on this object are:
        getConstrs(): Get a list of constraints in the model
        getJSONSolution(): Get a JSON-string representation of the current solution(s) to the model
        getParamInfo(paramname): Get information on a model parameter.
        getVars(): Get a list of variables in the model
        optimize(): Optimize the model.
        printAttr(attrname, filter): Print attribute values.
        printQuality(): Print solution quality statistics.
        printStats(): Print model statistics.
        read(filename): Read model data (MIP start, basis, etc.) from a file
        reset(): Discard any resident solution information.
        resetParams(): Reset all parameters to their default values.
        setParam(paramname, newval): Set a model parameter to a new value.
        write(filename): Write model data to a file.
    
      Models have a number of attributes that can be queried or modified.
      For example, "print model.objval" prints the objective value of
      the current solution.  Commonly used model attributes are:
        numConstrs: Number of constraints in model
        numVars: Number of variables in model
        status: Optimization status
        objVal: Objective of current solution
      Type "help(GRB.attr)" for a complete list.
    
      Additional methods on this object are:
        addConstr(), addGenConstrMax(), addGenConstrMin(), addGenConstrAbs(),
        addGenConstrAnd(), addGenConstrOr(), addGenConstrIndicator(),
        addGenConstrPWL(), addGenConstrPloy(), addGenConstrExp(), addGenConstrExpA(),
        addGenConstrLog(), addGenConstrLogA(), addGenConstrPow(), addGenConstrSin(),
        addGenConstrCos(), addGenConstrTan(), addRange(), addSOS(), addVar(),
        chgCoeff(), computeIIS(), copy(), fixed(), getCoeff(), getCol(), getRow(),
        message(), presolve(), relax(), terminate(), update()
    
      Additional help can be obtained on any of these methods (e.g.,
      help(Model.optimize)).
    """
    def addConstr(self, lhs, sense, rhs, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addConstr(lhs, sense, rhs, name)
        
            PURPOSE:
              Add a constraint to the model.
        
            ARGUMENTS:
              lhs (float, Var, LinExpr or TempConstr): Left-hand side
              sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
              rhs (float, Var, or LinExpr): Right-hand side
              name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created Constr object.
        
            EXAMPLE:
              c = model.addConstr(x + y <= 1)
              c = model.addConstr(x + y + z == [1, 2])
              c = model.addConstr(x*x + y*y <= 1)
              c = model.addConstr(z == and_(y, x, w))
              c = model.addConstr(z == min_(x, y))
              c = model.addConstr((w == 1) >> (x + y <= 1))
        """
        pass

    def addConstrs(self, constrs, name=""): # real signature unknown; restored from __doc__
        """
        addConstrs(constrs, name="")
        
            Add constraints in bulk, using a generator expression.  Returns a dictionary
            of Constr objects, indexed by the values (or tuples of values) used by the
            generator expression.
        
            If you specify a name, the constraints will get that name.  If name is a scalar
            string, the names will be subscripted by the generator index.  If name
            equals the underscore character ("_"), then the names will equal the index value.
        """
        pass

    def addGenConstrAbs(self, resvar, argvar, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrAbs(resvar, argvar, name)
        
            PURPOSE:
              Add a general constraint of type ABS to the model.
        
            ARGUMENTS:
              resvar (Var): Resultant variable of ABS constraint
              argvar (Var): Argument variable of ABS constraint
              name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrAbs(z, x1, "myAbsConstr")
        """
        pass

    def addGenConstrAnd(self, resvar, vars, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrAnd(resvar, vars, name)
        
            PURPOSE:
              Add a general constraint of type AND to the model.
        
            ARGUMENTS:
              resvar (Var): Resultant variable of AND constraint
              vars (list of Var, or tupledict): Argument variables of AND constraint
              name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrAnd(z, [x1, x2, x3], "myAndConstr")
        """
        pass

    def addGenConstrCos(self, xvar, yvar, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrCos(xvar, yvar, name, options)
        
            PURPOSE:
              Add a general constraint of type COS to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrCos(x, y)
        """
        pass

    def addGenConstrExp(self, xvar, yvar, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrExp(xvar, yvar, name, options)
        
            PURPOSE:
              Add a general constraint of type EXP to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrExp(x, y)
        """
        pass

    def addGenConstrExpA(self, xvar, yvar, a, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrExpA(xvar, yvar, a, name, options)
        
            PURPOSE:
              Add a general constraint of type EXPA to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              a (float): Base of exponential function
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrExpA(x, y, 3)
        """
        pass

    def addGenConstrIndicator(self, binvar, binval, lhs, sense, rhs, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrIndicator(binvar, binval, lhs, sense, rhs, name)
        
            PURPOSE:
              Add a general constraint of type INDICATOR to the model.
        
            ARGUMENTS:
              GRB.GENCONSTR_INDICATOR (option 1):
                binvar (Var): Antecedent variable of indicator constraint
                binval (Boolean): Value of antecedent variable that activates the linear constraint
                lhs (float, Var, or LinExpr): Linear expression of constraint triggered by the indicator
                sense (char): Sense of constraint triggered by the indicator (e.g., GRB.LESS_EQUAL)
                rhs (float): Right-hand side of linear constraint triggered by the indicator
                name (string): Constraint name (default is no name)
        
              GRB.GENCONSTR_INDICATOR (option 2):
                binvar (Var): Antecedent variable of indicator constraint
                binval (Boolean): Value of antecedent variable that activates the linear constraint
                lhs (TempConstr): Linear constraint triggered by indicator
                name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrIndicator(z, 0, 2*x1 - 1.5*x2 + 3.0*x3 == 4.5, name="myIndicatorConstr")
        """
        pass

    def addGenConstrLog(self, xvar, yvar, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrLog(xvar, yvar, name, options)
        
            PURPOSE:
              Add a general constraint of type LOG to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrLog(x, y)
        """
        pass

    def addGenConstrLogA(self, xvar, yvar, a, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrLogA(xvar, yvar, a, name, options)
        
            PURPOSE:
              Add a general constraint of type LOGA to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              a (float): Base of logarithmic function
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrLogA(x, y, 10)
        """
        pass

    def addGenConstrMax(self, resvar, vars, constant, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrMax(resvar, vars, constant, name)
        
            PURPOSE:
              Add a general constraint of type MAX to the model.
        
            ARGUMENTS:
              resvar (Var): Resultant variable of MAX constraint
              vars (list of Var, or tupledict): Argument variables of MAX constraint
              constant (float, optional): Constant of MAX constraint
              name (string, optional): Constraint name (default is no name)
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrMax(z, [x1, x2, x3], 17.5, "myMaxConstr")
        """
        pass

    def addGenConstrMin(self, resvar, vars, constant, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrMin(resvar, vars, constant, name)
        
            PURPOSE:
              Add a general constraint of type MIN to the model.
        
            ARGUMENTS:
              resvar (Var): Resultant variable of MIN constraint
              vars (list of Var, or tupledict): Argument variables of MIN constraint
              constant (float, optional): Constant of MIN constraint
              name (string, optional): Constraint name (default is no name)
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrMin(z, [x1, x2, x3], 17.5, "myMinConstr")
        """
        pass

    def addGenConstrOr(self, resvar, vars, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrOr(resvar, vars, name)
        
            PURPOSE:
              Add a general constraint of type OR to the model.
        
            ARGUMENTS:
              resvar (Var): Resultant variable of OR constraint
              vars (list of Var, or tupledict): Argument variables of OR constraint
              name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrOr(z, [x1, x2, x3], "myOrConstr")
        """
        pass

    def addGenConstrPoly(self, xvar, yvar, p, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrPoly(xvar, yvar, p, name, options)
        
            PURPOSE:
              Add a general constraint of type POLY to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              p (list of float): Coefficients for polynomial function
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrPoly(x, y, [2, 1.5, 0, 1])
              for y = 2 x^3 + 1.5 x^2 + 1
        """
        pass

    def addGenConstrPow(self, xvar, yvar, a, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrPow(xvar, yvar, a, name, options)
        
            PURPOSE:
              Add a general constraint of type POW to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              a (float): The exponent of the function
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrPow(x, y, 2)
        """
        pass

    def addGenConstrPWL(self, xvar, yvar, xpts, ypts, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrPWL(xvar, yvar, xpts, ypts, name)
        
            PURPOSE:
              Add a general constraint of type PWL to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              xpts (list of float): x coordinates for the breakpoints
              ypts (list of float): y coordinates for the breakpoints
              name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrPWL(x, y, [0, 1, 2], [1.5, 0, 3], "myPWLConstr")
        """
        pass

    def addGenConstrSin(self, xvar, yvar, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrSin(xvar, yvar, name, options)
        
            PURPOSE:
              Add a general constraint of type SIN to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrSin(x, y)
        """
        pass

    def addGenConstrTan(self, xvar, yvar, name, options): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addGenConstrTan(xvar, yvar, name, options)
        
            PURPOSE:
              Add a general constraint of type TAN to the model.
        
            ARGUMENTS:
              xvar (Var): x variable for constraint
              yvar (Var): y variable for constraint
              name (string): Constraint name (default is no name)
              options (string): String to specify options for PWL approximiation
        
            RETURN VALUE:
              The created general constraint object.
        
            EXAMPLE:
              genconstr = model.addGenConstrTan(x, y)
        """
        pass

    def addLConstr(self, lhs, sense, rhs, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addLConstr(lhs, sense, rhs, name)
        
            PURPOSE:
              Add a linear constraint to the model.
        
            ARGUMENTS:
              lhs (float, Var, LinExpr or TempConstr): Left-hand side
              sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
              rhs (float, Var, or LinExpr): Right-hand side
              name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created Constr object.
        
            EXAMPLE:
              c = model.addLConstr(x + y <= 1)
              c = model.addLConstr(LinExpr([1.0,1.0], [x,y]), GRB.LESS_EQUAL, 1)
              c = model.addLConstr(lhs = 5 * x + y, sense = GRB.LESS_EQUAL, rhs = 3 * z, name = "C1")
        """
        pass

    def addMConstrs(self, A, x, sense, b, name=""): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addMConstrs(A, x, sense, b, name="")
        
            PURPOSE:
              Add a set of linear constraints to the model using matrix semantics.
              The added constraints are 'A x = b' (except that the constraint sense
              is determined by the 'sense' argument).
        
            ARGUMENTS:
        
              A (NumPy or SciPy.sparse matrix): Constraint matrix
              x (MVar, or a list of Var, or None): Vector of Gurobi variables.
                  A 'None' argument uses all variables in the model.
              sense (char, or 1-d NumPy ndarray): Constraint sense
              b (1-d NumPy ndarray): Constraint right-hand side values
              name (string): Constraint names
        
            RETURN VALUE:
              The created MVar object.
        
            EXAMPLE:
              A = numpy.full((2, 3), 1.0)
              x = model.addMVar(3)
              b = numpy.full(2, 1.0)
              c = model.addMConstrs(A, x, GRB.LESS_EQUAL, b)
        """
        pass

    def addMQConstr(self, Q, c, sense, rhs, xQ_L=None, xQ_R=None, xc=None, name=""): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addMQConstr(self, Q, c, sense, rhs, xQ_L=None, xQ_R=None, xc=None, name="")
        
            PURPOSE:
              Add a quadratic constraint to the model using matrix semantics.
              The added constraint is 'xQ_L' Q xQ_R + c' xc = rhs'
              (except that the constraint sense is determined by the 'sense'
              argument).
        
            ARGUMENTS:
        
              Q (2-D NumPy ndarray or SciPy.sparse matrix): Quadratic constraint matrix
              c (1-D NumPy ndarray, or None): Linear constraint vector
              sense (char): Constraint sense
              rhs (float): Constraint right-hand side value
              xQ_L, xQ_R, xc (MVar, or a list of Var, or None): Vector of Gurobi
                 variables.  A 'None' argument uses all variables in the model.
              name (string): Constraint name
        
            RETURN VALUE:
              The created QConstr object.
        
            EXAMPLE:
              Q = numpy.full((2, 3), 1.0)
              xL = model.addMVar(2)
              xR = model.addMVar(3)
              c = model.addMQConstr(Q, None, GRB.LESS_EQUAL, 1.0, xL, xR)
        """
        pass

    def addMVar(self, shape, lb=0, ub=None, obj=0.0, vtype=None, name=""): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addMVar(shape, lb=0, ub=GRB.INFINITY, obj=0.0, vtype=GRB.CONTINUOUS,
                      name="")
        
            PURPOSE:
              Add a matrix variable (MVar object) to the model.
        
            ARGUMENTS:
              shape (tuple): Dimensions of the variable (like NumPy ndarray shape)
              lb (float): Lower bound (default is zero)
              ub (float): Upper bound (default is infinite)
              obj (float): Objective coefficient (default is zero)
              vtype (string): Variable type (default is continuous)
              name (string): Variable name (default is no name)
        
              The values of the lb, ub, obj, vtype and name arguments can either
              be scalars, or lists of length equal to the number of elements in the MVar.
        
            RETURN VALUE:
              The created MVar object.
        
            EXAMPLE:
              # Add a 4-by-2 matrix binary variable
              x = model.addMVar((4,2), vtype=GRB.BINARY)
              # Add a vector of three variables with non-default lower bounds
              y = model.addMVar((3,), lb=[-1, -2, -1])
        """
        pass

    def addQConstr(self, lhs, sense, rhs, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addQConstr(lhs, sense, rhs, name)
        
            PURPOSE:
              Add a quadratic constraint to the model.
        
            ARGUMENTS:
              lhs (float, Var, LinExpr, or QuadExpr): Left-hand side
              sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
              rhs (float, Var, LinExpr, or QuadExpr): Right-hand side
              name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created QConstr object.
        
            EXAMPLE:
              qc = model.addQConstr(x*x + y*y <= 1)
        """
        pass

    def addRange(self, expr, lhs, rhs, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addRange(expr, lhs, rhs, name)
        
            PURPOSE:
              Add a range constraint to the model.
        
            ARGUMENTS:
              expr (Var, or LinExpr): Linear expression being constrained
              lower (float): Lower bound on linear expression
              upper (float): Upper bound on linear expression
              name (string): Constraint name (default is no name)
        
            RETURN VALUE:
              The created Constr object.
        
            EXAMPLE:
              c = model.addRange(x + y, 1.0, 2.0)
        """
        pass

    def addSOS(self, type, vars, wts): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addSOS(type, vars, wts)
        
            PURPOSE:
              Add an SOS constraint to the model.
        
            ARGUMENTS:
              type (Int): SOS type 1 (GRB.SOS_TYPE1) or type 2 (GRB.SOS_TYPE2)
              vars (list of Var): Variables in SOS
              wts (list of float): Weights for variables in SOS
        
            RETURN VALUE:
              The created SOS object.
        
            EXAMPLE:
              sos = model.addSOS(GRB.SOS_TYPE1, [x, y, z])
        """
        pass

    def addVar(self, lb, ub, obj, vtype, name, column): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addVar(lb, ub, obj, vtype, name, column)
        
            PURPOSE:
              Add a variable to the model.
        
            ARGUMENTS:
              lb (float): Lower bound (default is zero)
              ub (float): Upper bound (default is infinite)
              obj (float): Objective coefficient (default is zero)
              vtype (string): Variable type (default is GRB.CONTINUOUS)
              name (string): Variable name (default is no name)
              column (Column): Initial coefficients for column (default is None)
        
            RETURN VALUE:
              The created Var object.
        
            EXAMPLE:
              v = model.addVar(ub=2.0, name="NewVar")
        """
        pass

    def addVars(self, *indexes, lb=0.0, ub=None, obj=0.0, vtype=None, name=""): # real signature unknown; restored from __doc__
        """
        addVars(*indexes, lb=0.0, ub=GRB.INFINITY, obj=0.0, vtype=GRB.CONTINUOUS,
                       name="")
        
            Add variables in bulk, given one or more lists or integers that serve as
            indexes for the variables.  Returns a dictionary of Var objects, indexed by
            the values (or tuples of values) from the index set.
        
            The optional parameters (lb, ub, obj, vtype, name) work similar
            to the addVar() method, with the following exceptions:
            1. The parameter name is required (ex: vtype=GRB.BINARY)
            2. You can specify the value as a scalar, a list or a dictionary.  For a scalar,
               the value will be used for all variables; for a list, the values must be
               in the same order as the index set; for a dictionary, they must be indexed
               by the variable index.
            3. If you specify a scalar string for name, the variable name will be
               subscripted automatically.
        """
        pass

    def cbCut(self, *args, **kwargs): # real signature unknown
        pass

    def cbGet(self, *args, **kwargs): # real signature unknown
        pass

    def cbGetNodeRel(self, *args, **kwargs): # real signature unknown
        pass

    def cbGetSolution(self, *args, **kwargs): # real signature unknown
        pass

    def cbLazy(self, *args, **kwargs): # real signature unknown
        pass

    def cbSetSolution(self, *args, **kwargs): # real signature unknown
        pass

    def cbStopOneMultiObj(self, objnum): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              cbStopOneMultiObj(objnum)
        
            PURPOSE:
              terminate individual optimization for the multi-objectives of the MIP model (from a callback).
        
            ARGUMENTS:
              objnum
        
            RETURN VALUE:
              None
        
            EXAMPLE:
              model.cbStopOneMultiObj(objnum)
        """
        pass

    def cbUseSolution(self, *args, **kwargs): # real signature unknown
        pass

    def chgCoeff(self, constr, var, newvalue): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              chgCoeff(constr, var, newvalue)
        
            PURPOSE:
              Change a coefficient in the constraint matrix.
        
            ARGUMENTS:
              constr (Constr): The constraint for the changed coefficient
              var (Var): The variable for the changed coefficient
              newvalue (float): Desired new value
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.chgCoeff(model.getConstrs()[0], model.getVars()[0], 1.0)
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              close()
        
            Synonymous to Model.dispose().
        """
        pass

    def computeIIS(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              computeIIS()
        
            PURPOSE:
              Compute an Irreducible Infeasible Subsystem (IIS).
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.computeIIS()
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              copy()
        
            PURPOSE:
              Create an exact copy of a model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              The copied Model object.
        
            EXAMPLE:
              copy = model.copy()
              copy.optimize()
        """
        pass

    def discardConcurrentEnvs(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              discardConcurrentEnvs()
        
            PURPOSE:
              Discard concurrent environments previously created through
              getConcurrentEnv(), thus restoring the concurrent optimizer
              to its default behavior.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              env0 = model.getConcurrentEnv(0)
              env1 = model.getConcurrentEnv(1)
        
              env0.setParam('Method', 0)
              env1.setParam('Method', 1)
        
              model.optimize()
        
              model.discardConcurrentEnvs()
        """
        pass

    def discardMultiobjEnvs(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              discardMultiobjEnvs()
        
            PURPOSE:
              Discard multiobj environments previously created through
              getMultiobjEnv(), thus restoring the multiobj optimizer
              to its default behavior.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              env0 = model.getMultiobjEnv(0)
              env1 = model.getMultiobjEnv(1)
        
              env0.setParam('Method', 0)
              env1.setParam('Method', 1)
        
              model.optimize()
        
              model.discardMultiobjEnvs()
        """
        pass

    def display(self, *args, **kwargs): # real signature unknown
        pass

    def dispose(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              dispose()
        
            PURPOSE:
              Free all resources associated with this Model object.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.dispose()
        
            NOTES:
              After this method is called, this Model object must no longer be used.
        """
        pass

    def feasibility(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              feasibility()
        
            PURPOSE:
              Return the feasibility version of the MIP model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A copy of the given model with a cancelled objective function.
        
            EXAMPLE:
              feasibility = model.feasibility()
              feasibility.optimize()
        """
        pass

    def feasRelax(self, relaxobjtype, minrelax, vars, lbpen, ubpen, constrs, rhspen): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              feasRelax(relaxobjtype, minrelax, vars, lbpen, ubpen, constrs, rhspen)
        
            PURPOSE:
              Perform a feasibility relaxation on the model.  Add penalty
              variables and a penalty objective.  Consider using feasRelaxS()
              if you want a simpler argument list.
        
            ARGUMENTS:
              relaxobjtype (int): Select the relaxation objective function.  Options
                                  are linear (0), quadratic (1), or cardinality (2).
              minrelax (Boolean): Indicate whether to solve feasrelax model to
                                  enforce minimal relaxation
              vars (list of Var): Variable that are allowed to violate bounds
              lbpen (list of float): Penalties for lower bound violations
              ubpen (list of float): Penalties for upper bound violations
              constrs (list of Constr): Constraints that can be violated
              rhspen (list of float): Penalties for constraint violations
        
            RETURN VALUE:
              feasRelax model objective value, if minimal relaxation is enforced,
              0 otherwise
        
            EXAMPLE:
              if model.status == GRB.INFEASIBLE:
                allvars = model.getVars()
                ubpen = [1.0]*model.numVars
                model.feasRelax(1, False, allvars, None, ubpen, None, None)
                model.optimize()
        """
        pass

    def feasRelaxS(self, relaxobjtype, minrelax, vrelax, crelax): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              feasRelaxS(relaxobjtype, minrelax, vrelax, crelax)
        
            PURPOSE:
              Perform a feasibility relaxation on the model.  Add penalty
              variables and a penalty objective.  Simple version; consider using
              feasRelax() if you want more control over the relaxation.
        
            ARGUMENTS:
              relaxobjtype (int): Select the relaxation objective function.  Options
                                  are linear (0), quadratic (1), or cardinality (2).
              minrelax (Boolean): Indicate whether to solve feasrelax model to
                                  enforce minimal relaxation
              vrelax (Boolean): If True, variable bound violations are allowed
              crelax (Boolean): If True, constraint violations are allowed
        
            RETURN VALUE:
              feasRelax model objective value, if minimal relaxation is enforced,
              0 otherwise
        
            EXAMPLE:
              if model.status == GRB.INFEASIBLE:
                model.feasRelaxS(1, False, False, True)
                model.optimize()
        """
        pass

    def fixed(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              fixed()
        
            PURPOSE:
              Return the fixed version of the MIP model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A new model, containing the fixed version of the MIP model.
        
            EXAMPLE:
              fixed = model.fixed()
              fixed.optimize()
        """
        pass

    def getA(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getA()
        
            PURPOSE:
              Retrieve the linear constraint matrix of the model.
              NOTE: You need to have 'scipy' installed for this function to work.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              The matrix as a scipy.sparse matrix in CSR format.
        
            EXAMPLE:
              A = model.getA()
              print(A.toarray())
        """
        pass

    def getAttr(self, attrname): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getAttr(attrname), or
              getAttr(attrname, objects)
        
            PURPOSE:
              Request the value of an attribute.
        
            ARGUMENTS:
              attrname (string): The name of the requested attribute.
              objects (optional): List or dictionary of variables or constraints
        
            RETURN VALUE:
              The attribute value.  If argument 'objects' is present,
              a list of values is returned.
        
            EXAMPLE:
              print(model.getAttr("modelName"))
              print(model.getAttr("lb", model.getVars()))
              print(model.getAttr("qcrhs", model.getQConstrs()))
        
            NOTES:
              Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass

    def getCoeff(self, constr, var): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getCoeff(constr, var)
        
            PURPOSE:
              Retrieve a coefficient from the constraint matrix.
        
            ARGUMENTS:
              constr (Constr): Constraint of interest
              var (Var): Variable of interest
        
            RETURN VALUE:
              The coefficient for 'var' in 'constr'
        
            EXAMPLE:
              coeff = model.getCoeff(model.getConstrs()[0], model.getVars()[0])
        """
        pass

    def getCol(self, var): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getCol(var)
        
            PURPOSE:
              Obtain all terms associated with a Var.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A Column object containing a list of terms associated with the Var.
        
            EXAMPLE:
              col = model.getCol(model.getVars()[0])
              for i in range(col.size()):
                print(col.getCoeff(i), expr.getConstr(i))
        """
        pass

    def getConcurrentEnv(self, num): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getConcurrentEnv(num)
        
            PURPOSE:
              Retrieve a concurrent environment.  This is used to manually
              configure the parameter settings used by different threads
              in the concurrent optimizer (for LP models).   You should make
              multiple calls to getConcurrentEnv() with integer arguments from
              0 through n-1, where n is the number of different solves you
              would like to launch,  You can set parameters on each concurrent
              environment to capture the desired behavior of each concurrent
              thread.
        
            ARGUMENTS:
              Concurrent environment number.
        
            RETURN VALUE:
              An Env object.
        
            EXAMPLE:
              env0 = model.getConcurrentEnv(0)
              env1 = model.getConcurrentEnv(1)
        
              env0.setParam('Method', 0)
              env1.setParam('Method', 1)
        
              model.optimize()
        """
        pass

    def getConstrByName(self, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getConstrByName(name)
        
            PURPOSE:
              Retrieve a linear constraint with the specified name from the model.
        
            ARGUMENTS:
              Constraint name.
        
            RETURN VALUE:
              A Constr object, or None if no matching variable is found.
        
            EXAMPLE:
              constr = model.getConstrByName("c1")
        """
        pass

    def getConstrs(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getConstrs()
        
            PURPOSE:
              Obtain a list of linear constraints in the model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A list of Constr objects.
        
            EXAMPLE:
              constrs = model.getConstrs()
              for c in constrs:
                print(c.ConstrName, c.Slack)
        """
        pass

    def getGenConstrAbs(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrAbs(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type ABS.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (resvar, argvar) that contains the data associated
              with the general constraint:
                resvar (Var): Resultant variable of ABS constraint
                argvar (Var): Argument variable of ABS constraint
        
            EXAMPLE:
              (resvar, argvar) = model.getGenConstrAbs(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrAnd(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrAnd(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type AND.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (resvar, vars) that contains the data associated
              with the general constraint:
                resvar (Var): Resultant variable of AND constraint
                vars (list of Var): Operand variables of AND constraint
        
            EXAMPLE:
              (resvar, vars) = model.getGenConstrAnd(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrCos(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrCos(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type COS.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar) that contains the data associated with
              the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
        
            EXAMPLE:
              (xvar, yvar) = model.getGenConstrCos(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrExp(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrExp(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type EXP.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar) that contains the data associated with
              the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
        
            EXAMPLE:
              (xvar, yvar) = model.getGenConstrExp(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrExpA(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrExpA(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type EXPA.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar, a) that contains the data associated
              with the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
                a (float): Base of exponential function
        
            EXAMPLE:
              (xvar, yvar, a) = model.getGenConstrExp(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrIndicator(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrIndicator(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type INDICATOR.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (binvar, binval, vars, vals, sense, rhs) that contains
              the data associated with the general constraint:
                binvar (Var): Antecedent variable of indicator constraint
                binval (Boolean): Value of antecedent variable that activates the linear constraint
                expr (LinExpr): LinExpr object containing the left-hand side of the constraint triggered by the indicator
                sense (char): Sense of linear constraint triggered by the indicator (e.g., GRB.LESS_EQUAL)
                rhs (float): Right-hand side of linear constraint triggered by the indicator
        
            EXAMPLE:
              (binvar, binval, expr, sense, rhs) = model.getGenConstr(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrLog(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrLog(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type LOG.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar) that contains the data associated with
              the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
        
            EXAMPLE:
              (xvar, yvar) = model.getGenConstrLog(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrLogA(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrLogA(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type LOGA.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar, a) that contains the data associated with
              the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
                a (float): Base of logarithmic function
        
            EXAMPLE:
              (xvar, yvar, a) = model.getGenConstrLog(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrMax(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrMax(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type MAX.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (resvar, vars, constant) that contains the data associated
              with the general constraint:
                resvar (Var): Resultant variable of MAX constraint
                vars (list of Var): Operand variables of MAX constraint
                constant (float): Constant of MAX constraint
        
            EXAMPLE:
              (resvar, vars, constant) = model.getGenConstrMax(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrMin(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrMin(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type MIN.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (resvar, vars, constant) that contains the data associated
              with the general constraint:
                resvar (Var): Resultant variable of MIN constraint
                vars (list of Var): Operand variables of MIN constraint
                constant (float): Constant of MIN constraint
        
            EXAMPLE:
              (resvar, vars, constant) = model.getGenConstrMin(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrOr(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrOr(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type OR.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (resvar, vars) that contains the data associated
              with the general constraint:
                resvar (Var): Resultant variable of OR constraint
                vars (list of Var): Operand variables of OR constraint
        
            EXAMPLE:
              (resvar, vars) = model.getGenConstrOr(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrPoly(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrPoly(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type POLY.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar, p) that contains the data associated with
              the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
                p (list of float): Coefficients for polynomial function
        
            EXAMPLE:
              (xvar, yvar, p) = model.getGenConstrPoly(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrPow(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrPow(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type POW.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar, a) that contains the data associated
              with the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
                a (float): The exponent of the function
        
            EXAMPLE:
              (xvar, yvar, a) = model.getGenConstrLog(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrPWL(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrPWL(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type PWL.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar, xpts, ypts) that contains the data associated
              with the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
                xpts (list of float): x coordinates for the breakpoints
                ypts (list of float): y coordinates for the breakpoints
        
            EXAMPLE:
              (xvar, yvar, xpts, ypts) = model.getGenConstrPWL(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrs(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrs()
        
            PURPOSE:
              Obtain a list of general constraints in the model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A list of GenConstr objects.
        
            EXAMPLE:
              genconstrs = model.getGenConstrs()
              for c in genconstrs:
                print(c.name)
        """
        pass

    def getGenConstrSin(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrSin(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type SIN.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar) that contains the data associated with
              the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
        
            EXAMPLE:
              (xvar, yvar) = model.getGenConstrSin(model.getGenConstrs()[0])
        """
        pass

    def getGenConstrTan(self, genconstr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getGenConstrTan(genconstr)
        
            PURPOSE:
              Obtain all data associated with a general constraint of type TAN.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple (xvar, yvar) that contains the data associated with
              the general constraint:
                xvar (Var): x variable for constraint
                yvar (Var): y variable for constraint
        
            EXAMPLE:
              (xvar, yvar) = model.getGenConstrTan(model.getGenConstrs()[0])
        """
        pass

    def getJSONSolution(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getJSONSolution()
        
            PURPOSE:
              After a call to 'optimize' on a model, you can query the
              resulting solution, and related model attributes, as a JSON
              string.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A JSON string representation to the current solution.
        
            EXAMPLE:
              model.optimize()
              # Print solution in JSON format
              print(model.getJSONSolution())
        """
        pass

    def getMultiobjEnv(self, num): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getMultiobjEnv(num)
        
            PURPOSE:
              Retrieve a multiobj environment.  This is used to manually
              configure the parameter settings used in the multiobj
              optimizer.  You should make multiple calls to getMultiobjEnv()
              with integer arguments from 0 through n-1, where n is the
              number of different priorities for the multi-objectives.
              You can set parameters on each multiobj environment to capture
              the desired behavior of the optimization for each objective
              priority
        
            ARGUMENTS:
              Multiobj environment number.
        
            RETURN VALUE:
              An Env object.
        
            EXAMPLE:
              env0 = model.getMultiobjEnv(0)
              env1 = model.getMultiobjEnv(1)
        
              env0.setParam('Method', 0)
              env1.setParam('Method', 1)
        
              model.optimize()
        """
        pass

    def getObjective(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getObjective()
        
            PURPOSE:
              Query the model objective
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              Model objective function, returned as either a LinExpr or QuadExpr
              object.
        
            EXAMPLE:
              expr = model.getObjective()
        """
        pass

    def getParamInfo(self, paramname): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getParamInfo(paramname)
        
            PURPOSE:
              Get information about a parameter.
        
            ARGUMENTS:
              paramname (string): The name of the parameter.
        
            RETURN VALUE:
              A tuple containing the parameter name, the parameter type, the
              current value, the minimum allowed value, the maximum allowed value,
              and the default value.
        
            EXAMPLE:
              model.getParamInfo("NodeLimit")
        
            NOTES:
              Routine paramHelp() provides additional information on the available
              parameters.
        """
        pass

    def getPWLObj(self, var): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getPWLObj(var)
        
            PURPOSE:
              Retrieves the piecewise-linear objective for a variable
        
            ARGUMENTS:
              var: the Var whose piecewise objective is returned.
        
            RETURN VALUE:
              A list of tuples, where each tuple captures a point on
              the piecewise-linear function.
        
            EXAMPLE:
              print(model.getPWLObj(v))
        """
        pass

    def getQ(self, *args, **kwargs): # real signature unknown
        pass

    def getQConstrs(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getQConstrs()
        
            PURPOSE:
              Obtain a list of quadratic constraints in the model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A list of QConstr objects.
        
            EXAMPLE:
              qconstrs = model.getQConstrs()
              for c in qconstrs:
                print(c.QCname)
        """
        pass

    def getQCRow(self, qc): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getQCRow(qc)
        
            PURPOSE:
              Obtain all terms associated with a quadratic constraint.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A QuadExpr object containing the left-hand side of the constraint.
        
            EXAMPLE:
              expr = model.getQCRow(model.getQConstrs()[0])
              model.addConstr(expr >= 0)
        """
        pass

    def getRow(self, constr): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getRow(constr)
        
            PURPOSE:
              Obtain all terms associated with a constraint.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A LinExpr object containing the left-hand side of the constraint.
        
            EXAMPLE:
              expr = model.getRow(model.getConstrs()[0])
              for i in range(expr.size()):
                print(expr.getCoeff(i), expr.getVar(i))
        """
        pass

    def getSOS(self, sos): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getSOS(sos)
        
            PURPOSE:
              Obtain all variables and weights associated with an SOS constraint.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A tuple that contains the SOS type (1 or 2), the list of member
              Var objects, and the associated SOS weights.
        
            EXAMPLE:
              (type, vars, weights) = model.getSOS(model.getSOSs()[0])
        """
        pass

    def getSOSs(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getSOSs()
        
            PURPOSE:
              Obtain a list of SOS constraints in the model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A list of SOS objects.
        
            EXAMPLE:
              sos = model.getSOSs()
              for s in sos:
                print(s)
        """
        pass

    def getTuneResult(self, i): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getTuneResult(i)
        
            PURPOSE:
              Retrive tuned parameter settings.
        
            ARGUMENTS:
              Tuning result number.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.getTuneResult(0)
        """
        pass

    def getVarByName(self, name): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getVarByName(name)
        
            PURPOSE:
              Retrieve a variable with the specified name from the model.
        
            ARGUMENTS:
              Variable name.
        
            RETURN VALUE:
              A Var object, or None if no matching variable is found.
        
            EXAMPLE:
              var = model.getVarByName("x1")
        """
        pass

    def getVars(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getVars()
        
            PURPOSE:
              Obtain a list of variables in the model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A list of Var objects.
        
            EXAMPLE:
              allvars = model.getVars()
              for v in allvars:
                print(v.VarName, v.X)
        """
        pass

    def linearize(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              linearize()
        
            PURPOSE:
              Return the linearized version of the MIQP model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A new model, containing the linearized version of the original model.
        
            EXAMPLE:
              linearized = model.linearize()
              linearized.optimize()
        """
        pass

    def message(self, msg): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              message(msg)
        
            PURPOSE:
              Write a message to the Gurobi log file.
        
            ARGUMENTS:
              msg (string): Message to append to log file.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.message("Found a new solution with objective " + str(obj))
        """
        pass

    def optimize(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              optimize()
        
            PURPOSE:
              Optimize the model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.optimize()
        
            NOTES:
              The algorithm used to optimize the model depends on the model type and
              on the parameter settings.  A MIP model will always be optimized using
              the branch-and-cut algorithm.  A continuous model will be optimized
              using the dual simplex algorithm by default; the Method parameter
              can be used to choose a different algorithm.
        """
        pass

    def optimizeBatch(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              optimizeBatch()
        
            PURPOSE:
              Submit a new batch optimization request.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              Batch ID of the new batch optimization request.
        
            EXAMPLE:
              model.optimizeBatch()
        
            NOTES:
              Submit a new optimization job to the offline job queue. The
              method returns a string, referred as BatchID, which uniquely
              identify the job in the Cluster Manager. With this ID you can
              query, from any other process, the status of this job, and
              once it has been solved, the associated solution. Note that
              in order to submit a batch request, you must define at least
              one tag for the model.
              Note that this routine will process all pending model modifications.
        """
        pass

    def presolve(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              presolve()
        
            PURPOSE:
              Return the presolved version of the model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A new model, containing the presolved version of the original model.
        
            EXAMPLE:
              presolved = model.presolve()
              presolved.optimize()
        """
        pass

    def printAttr(self, attrname, filter): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              printAttr(attrname, filter)
        
            PURPOSE:
              Print model attribute data.
        
            ARGUMENTS:
              attrname (string): The name of the attribute to print.  For attributes
                                 with numerical values, only non-zero entries will
                                 be printed.  Can be a list of attribute names,
                                 in which case all listed attributes will be printed.
              filter (string): Regular expression for filtering results.   Only
                               variables/constraints whose names match the
                               (optional) filter are printed.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.optimize()
              model.printAttr("x", "v*")     # print 'x' when var name begins with 'v'
              model.printAttr(["lb", "ub"])  # print 'lb' and 'ub' attribute values
        """
        pass

    def printQuality(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              printQuality()
        
            PURPOSE:
              Print solution quality statistics.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.optimize()
              model.printQuality()
        """
        pass

    def printStats(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              printStats()
        
            PURPOSE:
              Print model statistics.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.printStats()
        """
        pass

    def read(self, filename): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              read(filename)
        
            PURPOSE:
              Import model data from a file.  The type of data is determined by
              the file suffix: .mst for MIP start data, .bas for basis
              information, or .prm for parameter settings.
        
            ARGUMENTS:
              filename (string): The name of the file.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.read("start.mst")
        
            NOTES:
              The file name may contain the '*' and '?' wildcard characters.  If
              more than one file matches, this routine will read the first match.
        """
        pass

    def relax(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              relax()
        
            PURPOSE:
              Return the relaxed version of the MIP model, in which all integrality
              restrictions, SOS conditions, semi-continuous and semi-integer
              requirements on variables have been relaxed and general constraints
              have been removed.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              A new, relaxed model.
        
            EXAMPLE:
              relaxed = model.relax()
              relaxed.optimize()
        
            NOTES:
              If the model is already continuous, then this method produces the
              same result as cloning the model.
        """
        pass

    def remove(self, items): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              remove(items)
        
            PURPOSE:
              Remove variables, linear constraints, SOS constraints, quadratic
              constraints, or general constraints from the model.
        
            ARGUMENTS:
              items: Items to remove from model.  The argument can be
                     a single Constr, Var, SOS, QConstr, or GenConstr,
                     or it can be a list, tuple, or dict containing
                     such items.  For a dict, the dict values will be
                     removed, not the keys.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.remove(model.getVars()[0])
              model.remove(model.getConstrs()[0:10])
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              reset()
        
            PURPOSE:
              Discard any solution information.  The next optimize() call starts
              from scratch.
        
            ARGUMENTS:
              clearall (int, optional): Should additional information such as MIP
                       starts, variable hints, branching priorities, lazy flags,
                       and partition information be cleared?
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.reset()
        """
        pass

    def resetParams(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              resetParams()
        
            PURPOSE:
              Reset all parameters to their default values.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.resetParams()
        """
        pass

    def setAttr(self, attrname, newvalue): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setAttr(attrname, newvalue), or
              setAttr(attrname, objects, newvalues)
        
            PURPOSE:
              Change the value(s) of an attribute.
        
            ARGUMENTS:
              attrname (string): The name of the requested attribute.
              objects(optional): A list of variables or constraints.
              newvalue: The desired new value.  The type of the value should be
                        compatible with the attribute type (e.g., an integer parameter
                        will take an integer value).
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              model.setAttr("modelSense", -1)
              model.setAttr("lb", [x, y, z], [1, 1, 1])
        
            NOTES:
              Model attributes that can be set are:
                modelName:  Model name.
                modelSense: Objective sense.
        
              Attributes changes are handled in a lazy fashion.  The effect of a
              change isn't visible until after the next call to Model.update() or
              Model.optimize().
        """
        pass

    def setMObjective(self, Q, c, constant, xQ_L=None, xQ_R=None, xc=None, sense=None): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setMObjective(Q, c, constant, xQ_L=None, xQ_R=None, xc=None, sense=None)
        
            PURPOSE:
              Set the objective function using matrix semantics.  The new objective
              is 'xQ_L' Q xQ_R + c' xc + constant'.
        
            ARGUMENTS:
        
              Q (NumPy or SciPy.sparse matrix, or None): Quadratic objective matrix
              c (1-D NumPy array, or None): Linear objective vector
              constant (float): Objective constant
              xQ_L, xQ_R, xc (MVar, or a list of Var, or None): Vector of Gurobi
                 variables.  A 'None' argument uses all variables in the model.
              sense (optional): Objective sense.  By default, this method uses the
                    modelSense model attribute to determine the sense.  Use
                    GRB.MINIMIZE or GRB.MAXIMIZE to ignore modelSense and pick a
                    specific sense.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              Q = numpy.full((2, 3), 1.0)
              xL = model.addMVar(2)
              xR = model.addMVar(3)
              model.setMObjective(Q, None, 0.0, xL, xR, None)
        """
        pass

    def setObjective(self, expression, sense=None): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setObjective(expression, sense=None)
        
            PURPOSE:
              Set the model objective equal to a LinExpr or QuadExpr
        
            ARGUMENTS:
              expr: The desired objective function.  The objective can be
                    a linear expression (LinExpr) or a quadratic expression (QuadExpr).
                    This routine will replace the 'Obj' attribute on model variables
                    with the corresponding values from the supplied expression.
              sense (optional): Objective sense.  By default, this method uses the
                    modelSense model attribute to determine the sense.  Use
                    GRB.MINIMIZE or GRB.MAXIMIZE to ignore modelSense and pick a
                    specific sense.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.setObjective(x + y)
              model.setObjective(x + y + 2*z, GRB.MAXIMIZE)
        """
        pass

    def setObjectiveN(self, expression, index): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setObjectiveN(expression, index)
        
            PURPOSE:
              Set the model objective equal to a LinExpr or QuadExpr
        
            ARGUMENTS:
              expr:     The desired objective function.  The objective can be
                        a linear expression (LinExpr) a variable (Var) or a constant.
                        This routine will replace the 'ObjNVal' attribute on model variables
                        with the corresponding values from the supplied expression for
                        multi-objective 'index'
              index:    Identify which multi-objective to set
              priority: Set the ObjNPriority attribute for this multi-objective (default is zero)
              weight:   Set the ObjNWeight attribute for this multi-objective (default is 1.0)
              abstol:   Set the ObjNAbsTol  attribute for this multi-objective (default is zero)
              reltol:   Set the ObjNRelTol  attribute for this multi-objective (default is zero)
              name:     multi-objective name (default is no name)
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.setObjectiveN(x + y, 1)
              model.setObjectiveN(x + y + 2*z, 2)
        """
        pass

    def setParam(self, paramname, newvalue): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setParam(paramname, newvalue)
        
            PURPOSE:
              Set a parameter to a new value.
        
            ARGUMENTS:
              paramname (string): The name of the parameter.
              newvalue: The desired new value.  The type of the value should be
                        compatible with the parameter type (e.g., an integer parameter
                        will take an integer value).  One important exception: the
                        string "default" will return the specified parameter to its
                        default value.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.setParam("NodeLimit", 100)
              model.setParam("TimeLimit", "default")
        
            NOTES:
              Use this routine to change parameter values in the default environment.
              The default environment is used to initialize parameter values when a
              new model is created.  Once the model exists, changes to the default
              environment will no longer affect that model.  Use Model.setParam()
              to change parameter settings for an existing model.
        
              Routine paramHelp() provides additional information on the available
              parameters.
        """
        pass

    def setPWLObj(self, var, x, y): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setPWLObj(var, x, y)
        
            PURPOSE:
              Set a piecewise-linear objective for a variable
        
            ARGUMENTS:
              var: the Var whose objective is set.
              x: A list of x coordinates.
              y: A list of y coordinates.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.setPWLObj(v, [1, 2, 3], [1, 2, 4])
        """
        pass

    def singleScenarioModel(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              singleScenarioModel()
        
            PURPOSE:
              Return a model that represents a single scenario of the multi-scenario
              MIP model. The scenario is specified by setting the "ScenarioNumber"
              parameter.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              Returns a copy of the single scenario model specified by the "ScenarioNumber" parameter.
        
            EXAMPLE:
              singlescenario = model.singleScenarioModel()
              singlescenario.optimize()
        """
        pass

    def terminate(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              terminate()
        
            PURPOSE:
              Terminate any optimization in progress (from a callback).
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.terminate()
        """
        pass

    def tune(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              tune()
        
            PURPOSE:
              Tune parameter settings
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.tune()
        """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              update()
        
            PURPOSE:
              Apply any pending changes to the model.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.update()
        
            NOTES:
              Model modifications are handled in a lazy fashion.  A bound change, for
              example, isn't reflected in the model until the user either calls
              model.optimize() or model.update().
        """
        pass

    def write(self, filename): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              write(filename)
        
            PURPOSE:
              Write model data to a file.  The type of data is determined by the
              file suffix: .lp or .mps to write the model itself, .mst to write
              the current solution as a MIP start, .bas to write the current
              simplex basis, or .prm to write the modified parameters.
        
            ARGUMENTS:
              filename (string): The name of the file to write.
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              model.write("model.lp")
              model.write("model.mst")
        """
        pass

    def _createX(self, *args, **kwargs): # real signature unknown
        pass

    def _map_coldata_to_vars(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__addConstr(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__cbCutOrLazy(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__feasrelax(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__genexpr_key(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__getConstr(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__getGenConstr(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__getQConstr(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__getSOS(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__getupdatemode(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__getVar(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__indexname(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__isAttrAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__owns(self, *args, **kwargs): # real signature unknown
        pass

    def _Model__setup(self, *args, **kwargs): # real signature unknown
        pass

    def _removeone(self, *args, **kwargs): # real signature unknown
        pass

    def _v811_addMConstrs(self, *args, **kwargs): # real signature unknown
        pass

    def _v811_setMObjective(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    typeenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _Model__listify = None # (!) real value is "<class 'gurobipy.Model._Model__listify'>"
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Gurobi model object.  Commonly used methods on this object are:\\n    getConstrs(): Get a list of constraints in the model\\n    getJSONSolution(): Get a JSON-string representation of the current solution(s) to the model\\n    getParamInfo(paramname): Get information on a model parameter.\\n    getVars(): Get a list of variables in the model\\n    optimize(): Optimize the model.\\n    printAttr(attrname, filter): Print attribute values.\\n    printQuality(): Print solution quality statistics.\\n    printStats(): Print model statistics.\\n    read(filename): Read model data (MIP start, basis, etc.) from a file\\n    reset(): Discard any resident solution information.\\n    resetParams(): Reset all parameters to their default values.\\n    setParam(paramname, newval): Set a model parameter to a new value.\\n    write(filename): Write model data to a file.\\n\\n  Models have a number of attributes that can be queried or modified.\\n  For example, "print model.objval" prints the objective value of\\n  the current solution.  Commonly used model attributes are:\\n    numConstrs: Number of constraints in model\\n    numVars: Number of variables in model\\n    status: Optimization status\\n    objVal: Objective of current solution\\n  Type "help(GRB.attr)" for a complete list.\\n\\n  Additional methods on this object are:\\n    addConstr(), addGenConstrMax(), addGenConstrMin(), addGenConstrAbs(),\\n    addGenConstrAnd(), addGenConstrOr(), addGenConstrIndicator(),\\n    addGenConstrPWL(), addGenConstrPloy(), addGenConstrExp(), addGenConstrExpA(),\\n    addGenConstrLog(), addGenConstrLogA(), addGenConstrPow(), addGenConstrSin(),\\n    addGenConstrCos(), addGenConstrTan(), addRange(), addSOS(), addVar(),\\n    chgCoeff(), computeIIS(), copy(), fixed(), getCoeff(), getCol(), getRow(),\\n    message(), presolve(), relax(), terminate(), update()\\n\\n  Additional help can be obtained on any of these methods (e.g.,\\n  help(Model.optimize)).\\n  \', \'__init__\': <cyfunction Model.__init__ at 0x00000248A6071C80>, \'__dir__\': <cyfunction Model.__dir__ at 0x00000248A6071D38>, \'__del__\': <cyfunction Model.__del__ at 0x00000248A6071DF0>, \'dispose\': <cyfunction Model.dispose at 0x00000248A6071EA8>, \'typename\': <property object at 0x00000248A6067E08>, \'typeenum\': <property object at 0x00000248A6067B88>, \'close\': <cyfunction Model.close at 0x00000248A607C100>, \'__enter__\': <cyfunction Model.__enter__ at 0x00000248A607C1B8>, \'__exit__\': <cyfunction Model.__exit__ at 0x00000248A607C270>, \'__repr__\': <cyfunction Model.__repr__ at 0x00000248A607C328>, \'_Model__indexname\': <staticmethod object at 0x00000248A6065978>, \'_Model__genexpr_key\': <staticmethod object at 0x00000248A60659B0>, \'_Model__listify\': <class \'gurobipy.Model._Model__listify\'>, \'display\': <cyfunction Model.display at 0x00000248A607C778>, \'__getattr__\': <cyfunction Model.__getattr__ at 0x00000248A607C830>, \'__setattr__\': <cyfunction Model.__setattr__ at 0x00000248A607C8E8>, \'_Model__setup\': <cyfunction Model.__setup at 0x00000248A607C9A0>, \'_Model__getVar\': <cyfunction Model.__getVar at 0x00000248A607CA58>, \'_Model__getConstr\': <cyfunction Model.__getConstr at 0x00000248A607CB10>, \'_Model__getSOS\': <cyfunction Model.__getSOS at 0x00000248A607CBC8>, \'_Model__getQConstr\': <cyfunction Model.__getQConstr at 0x00000248A607CC80>, \'_Model__getGenConstr\': <cyfunction Model.__getGenConstr at 0x00000248A607CD38>, \'_Model__owns\': <cyfunction Model.__owns at 0x00000248A607CDF0>, \'_Model__isAttrAvailable\': <cyfunction Model.__isAttrAvailable at 0x00000248A607CEA8>, \'getVars\': <cyfunction Model.getVars at 0x00000248A607CF60>, \'getConstrs\': <cyfunction Model.getConstrs at 0x00000248A6086048>, \'getJSONSolution\': <cyfunction Model.getJSONSolution at 0x00000248A6086100>, \'getSOSs\': <cyfunction Model.getSOSs at 0x00000248A60861B8>, \'getQConstrs\': <cyfunction Model.getQConstrs at 0x00000248A6086270>, \'getGenConstrs\': <cyfunction Model.getGenConstrs at 0x00000248A6086328>, \'getVarByName\': <cyfunction Model.getVarByName at 0x00000248A60863E0>, \'getConstrByName\': <cyfunction Model.getConstrByName at 0x00000248A6086498>, \'getConcurrentEnv\': <cyfunction Model.getConcurrentEnv at 0x00000248A6086550>, \'discardConcurrentEnvs\': <cyfunction Model.discardConcurrentEnvs at 0x00000248A6086608>, \'getMultiobjEnv\': <cyfunction Model.getMultiobjEnv at 0x00000248A60866C0>, \'discardMultiobjEnvs\': <cyfunction Model.discardMultiobjEnvs at 0x00000248A6086778>, \'optimize\': <cyfunction Model.optimize at 0x00000248A6086830>, \'optimizeBatch\': <cyfunction Model.optimizeBatch at 0x00000248A60868E8>, \'computeIIS\': <cyfunction Model.computeIIS at 0x00000248A60869A0>, \'tune\': <cyfunction Model.tune at 0x00000248A6086A58>, \'getTuneResult\': <cyfunction Model.getTuneResult at 0x00000248A6086B10>, \'remove\': <cyfunction Model.remove at 0x00000248A6086BC8>, \'_removeone\': <cyfunction Model._removeone at 0x00000248A6086C80>, \'reset\': <cyfunction Model.reset at 0x00000248A6086D38>, \'update\': <cyfunction Model.update at 0x00000248A6086DF0>, \'copy\': <cyfunction Model.copy at 0x00000248A6086EA8>, \'write\': <cyfunction Model.write at 0x00000248A6086F60>, \'getParamInfo\': <cyfunction Model.getParamInfo at 0x00000248A6087048>, \'setObjective\': <cyfunction Model.setObjective at 0x00000248A6087100>, \'setObjectiveN\': <cyfunction Model.setObjectiveN at 0x00000248A60871B8>, \'getObjective\': <cyfunction Model.getObjective at 0x00000248A6087270>, \'setPWLObj\': <cyfunction Model.setPWLObj at 0x00000248A6087328>, \'getPWLObj\': <cyfunction Model.getPWLObj at 0x00000248A60873E0>, \'setParam\': <cyfunction Model.setParam at 0x00000248A6087498>, \'resetParams\': <cyfunction Model.resetParams at 0x00000248A6087550>, \'read\': <cyfunction Model.read at 0x00000248A6087608>, \'getAttr\': <cyfunction Model.getAttr at 0x00000248A60876C0>, \'setAttr\': <cyfunction Model.setAttr at 0x00000248A6087778>, \'message\': <cyfunction Model.message at 0x00000248A6087830>, \'relax\': <cyfunction Model.relax at 0x00000248A60878E8>, \'fixed\': <cyfunction Model.fixed at 0x00000248A60879A0>, \'presolve\': <cyfunction Model.presolve at 0x00000248A6087A58>, \'feasibility\': <cyfunction Model.feasibility at 0x00000248A6087B10>, \'linearize\': <cyfunction Model.linearize at 0x00000248A6087BC8>, \'singleScenarioModel\': <cyfunction Model.singleScenarioModel at 0x00000248A6087C80>, \'_Model__feasrelax\': <cyfunction Model.__feasrelax at 0x00000248A6087D38>, \'feasRelaxS\': <cyfunction Model.feasRelaxS at 0x00000248A6087DF0>, \'feasRelax\': <cyfunction Model.feasRelax at 0x00000248A6087EA8>, \'printAttr\': <cyfunction Model.printAttr at 0x00000248A6087F60>, \'printQuality\': <cyfunction Model.printQuality at 0x00000248A6088048>, \'printStats\': <cyfunction Model.printStats at 0x00000248A6088100>, \'addVar\': <cyfunction Model.addVar at 0x00000248A60881B8>, \'addVars\': <cyfunction Model.addVars at 0x00000248A6088270>, \'addMVar\': <cyfunction Model.addMVar at 0x00000248A6088328>, \'addLConstr\': <cyfunction Model.addLConstr at 0x00000248A60883E0>, \'_Model__addConstr\': <cyfunction Model.__addConstr at 0x00000248A6088498>, \'addConstr\': <cyfunction Model.addConstr at 0x00000248A6088550>, \'addQConstr\': <cyfunction Model.addQConstr at 0x00000248A6088608>, \'addRange\': <cyfunction Model.addRange at 0x00000248A60886C0>, \'addConstrs\': <cyfunction Model.addConstrs at 0x00000248A6088778>, \'_createX\': <cyfunction Model._createX at 0x00000248A6088830>, \'_v811_addMConstrs\': <cyfunction Model._v811_addMConstrs at 0x00000248A60888E8>, \'addMConstrs\': <cyfunction Model.addMConstrs at 0x00000248A60889A0>, \'addMQConstr\': <cyfunction Model.addMQConstr at 0x00000248A6088A58>, \'getA\': <cyfunction Model.getA at 0x00000248A6088B10>, \'getQ\': <cyfunction Model.getQ at 0x00000248A6088BC8>, \'_v811_setMObjective\': <cyfunction Model._v811_setMObjective at 0x00000248A6088C80>, \'setMObjective\': <cyfunction Model.setMObjective at 0x00000248A6088D38>, \'addSOS\': <cyfunction Model.addSOS at 0x00000248A6088DF0>, \'addGenConstrMax\': <cyfunction Model.addGenConstrMax at 0x00000248A6088EA8>, \'addGenConstrMin\': <cyfunction Model.addGenConstrMin at 0x00000248A6088F60>, \'addGenConstrAbs\': <cyfunction Model.addGenConstrAbs at 0x00000248A6089048>, \'addGenConstrAnd\': <cyfunction Model.addGenConstrAnd at 0x00000248A6089100>, \'addGenConstrOr\': <cyfunction Model.addGenConstrOr at 0x00000248A60891B8>, \'addGenConstrIndicator\': <cyfunction Model.addGenConstrIndicator at 0x00000248A6089270>, \'addGenConstrPWL\': <cyfunction Model.addGenConstrPWL at 0x00000248A6089328>, \'addGenConstrPoly\': <cyfunction Model.addGenConstrPoly at 0x00000248A60893E0>, \'addGenConstrExp\': <cyfunction Model.addGenConstrExp at 0x00000248A6089498>, \'addGenConstrExpA\': <cyfunction Model.addGenConstrExpA at 0x00000248A6089550>, \'addGenConstrLog\': <cyfunction Model.addGenConstrLog at 0x00000248A6089608>, \'addGenConstrLogA\': <cyfunction Model.addGenConstrLogA at 0x00000248A60896C0>, \'addGenConstrPow\': <cyfunction Model.addGenConstrPow at 0x00000248A6089778>, \'addGenConstrSin\': <cyfunction Model.addGenConstrSin at 0x00000248A6089830>, \'addGenConstrCos\': <cyfunction Model.addGenConstrCos at 0x00000248A60898E8>, \'addGenConstrTan\': <cyfunction Model.addGenConstrTan at 0x00000248A60899A0>, \'getCoeff\': <cyfunction Model.getCoeff at 0x00000248A6089A58>, \'chgCoeff\': <cyfunction Model.chgCoeff at 0x00000248A6089B10>, \'getCol\': <cyfunction Model.getCol at 0x00000248A6089BC8>, \'getRow\': <cyfunction Model.getRow at 0x00000248A6089C80>, \'getSOS\': <cyfunction Model.getSOS at 0x00000248A6089D38>, \'getQCRow\': <cyfunction Model.getQCRow at 0x00000248A6089DF0>, \'getGenConstrMax\': <cyfunction Model.getGenConstrMax at 0x00000248A6089EA8>, \'getGenConstrMin\': <cyfunction Model.getGenConstrMin at 0x00000248A6089F60>, \'getGenConstrAbs\': <cyfunction Model.getGenConstrAbs at 0x00000248A608A048>, \'getGenConstrAnd\': <cyfunction Model.getGenConstrAnd at 0x00000248A608A100>, \'getGenConstrOr\': <cyfunction Model.getGenConstrOr at 0x00000248A608A1B8>, \'getGenConstrIndicator\': <cyfunction Model.getGenConstrIndicator at 0x00000248A608A270>, \'getGenConstrPWL\': <cyfunction Model.getGenConstrPWL at 0x00000248A608A328>, \'getGenConstrPoly\': <cyfunction Model.getGenConstrPoly at 0x00000248A608A3E0>, \'getGenConstrExp\': <cyfunction Model.getGenConstrExp at 0x00000248A608A498>, \'getGenConstrExpA\': <cyfunction Model.getGenConstrExpA at 0x00000248A608A550>, \'getGenConstrLog\': <cyfunction Model.getGenConstrLog at 0x00000248A608A608>, \'getGenConstrLogA\': <cyfunction Model.getGenConstrLogA at 0x00000248A608A6C0>, \'getGenConstrPow\': <cyfunction Model.getGenConstrPow at 0x00000248A608A778>, \'getGenConstrSin\': <cyfunction Model.getGenConstrSin at 0x00000248A608A830>, \'getGenConstrCos\': <cyfunction Model.getGenConstrCos at 0x00000248A608A8E8>, \'getGenConstrTan\': <cyfunction Model.getGenConstrTan at 0x00000248A608A9A0>, \'terminate\': <cyfunction Model.terminate at 0x00000248A608AA58>, \'cbStopOneMultiObj\': <cyfunction Model.cbStopOneMultiObj at 0x00000248A608AB10>, \'cbGet\': <cyfunction Model.cbGet at 0x00000248A608ABC8>, \'_map_coldata_to_vars\': <staticmethod object at 0x00000248A6065B38>, \'cbGetNodeRel\': <cyfunction Model.cbGetNodeRel at 0x00000248A608AD38>, \'cbGetSolution\': <cyfunction Model.cbGetSolution at 0x00000248A608ADF0>, \'cbSetSolution\': <cyfunction Model.cbSetSolution at 0x00000248A608AEA8>, \'cbUseSolution\': <cyfunction Model.cbUseSolution at 0x00000248A608AF60>, \'cbCut\': <cyfunction Model.cbCut at 0x00000248A608B048>, \'cbLazy\': <cyfunction Model.cbLazy at 0x00000248A608B100>, \'_Model__cbCutOrLazy\': <cyfunction Model.__cbCutOrLazy at 0x00000248A608B1B8>, \'_Model__getupdatemode\': <cyfunction Model.__getupdatemode at 0x00000248A608B270>, \'__dict__\': <attribute \'__dict__\' of \'Model\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Model\' objects>})'


class MQuadExpr(object):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def flatten(self, *args, **kwargs): # real signature unknown
        pass

    def getValue(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getValue()
        
            PURPOSE:
              Compute the value of a quadratic matrix expression, using the current
              solution.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              The computed quadratic expression value.
        
            EXAMPLE:
              qexpr = x @ A @ x
              print(qexpr.getValue())
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __array_priority__ = 100
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__array_priority__': 100, '__init__': <cyfunction MQuadExpr.__init__ at 0x00000248A6070778>, '__repr__': <cyfunction MQuadExpr.__repr__ at 0x00000248A6070830>, 'copy': <cyfunction MQuadExpr.copy at 0x00000248A60708E8>, 'flatten': <cyfunction MQuadExpr.flatten at 0x00000248A60709A0>, 'getValue': <cyfunction MQuadExpr.getValue at 0x00000248A6070A58>, '__add__': <cyfunction MQuadExpr.__add__ at 0x00000248A6070B10>, '__radd__': <cyfunction MQuadExpr.__radd__ at 0x00000248A6070BC8>, '__iadd__': <cyfunction MQuadExpr.__iadd__ at 0x00000248A6070C80>, '__sub__': <cyfunction MQuadExpr.__sub__ at 0x00000248A6070D38>, '__rsub__': <cyfunction MQuadExpr.__rsub__ at 0x00000248A6070DF0>, '__isub__': <cyfunction MQuadExpr.__isub__ at 0x00000248A6070EA8>, '__mul__': <cyfunction MQuadExpr.__mul__ at 0x00000248A6070F60>, '__rmul__': <cyfunction MQuadExpr.__rmul__ at 0x00000248A6071048>, '__imul__': <cyfunction MQuadExpr.__imul__ at 0x00000248A6071100>, '__neg__': <cyfunction MQuadExpr.__neg__ at 0x00000248A60711B8>, '__le__': <cyfunction MQuadExpr.__le__ at 0x00000248A6071270>, '__ge__': <cyfunction MQuadExpr.__ge__ at 0x00000248A6071328>, '__eq__': <cyfunction MQuadExpr.__eq__ at 0x00000248A60713E0>, '__ne__': <cyfunction MQuadExpr.__ne__ at 0x00000248A6071498>, '__dict__': <attribute '__dict__' of 'MQuadExpr' objects>, '__weakref__': <attribute '__weakref__' of 'MQuadExpr' objects>, '__doc__': None, '__hash__': None})"
    __hash__ = None


class MVar(object):
    """ Handle for an optimization variable. """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def getAttr(self, *args, **kwargs): # real signature unknown
        pass

    def idxarr(self, *args, **kwargs): # real signature unknown
        pass

    def indexed_data(self, *args, **kwargs): # real signature unknown
        pass

    def scalar_mult(self, *args, **kwargs): # real signature unknown
        pass

    def setAttr(self, *args, **kwargs): # real signature unknown
        pass

    def squeeze(self, *args, **kwargs): # real signature unknown
        pass

    def sum(self, *args, **kwargs): # real signature unknown
        pass

    def tomlinexpr(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __matmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmatmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typeenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __array_priority__ = 100
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__doc__': 'Handle for an optimization variable.', '__array_priority__': 100, '__init__': <cyfunction MVar.__init__ at 0x00000248A606BEA8>, '__repr__': <cyfunction MVar.__repr__ at 0x00000248A606BF60>, 'copy': <cyfunction MVar.copy at 0x00000248A606D048>, '__getitem__': <cyfunction MVar.__getitem__ at 0x00000248A606D100>, 'typename': <property object at 0x00000248A60678B8>, 'typeenum': <property object at 0x00000248A6067908>, '__getattr__': <cyfunction MVar.__getattr__ at 0x00000248A606D328>, '__setattr__': <cyfunction MVar.__setattr__ at 0x00000248A606D3E0>, '__mul__': <cyfunction MVar.__mul__ at 0x00000248A606D498>, '__matmul__': <cyfunction MVar.__matmul__ at 0x00000248A606D550>, '__add__': <cyfunction MVar.__add__ at 0x00000248A606D608>, '__radd__': <cyfunction MVar.__radd__ at 0x00000248A606D6C0>, '__sub__': <cyfunction MVar.__sub__ at 0x00000248A606D778>, '__rsub__': <cyfunction MVar.__rsub__ at 0x00000248A606D830>, '__rmul__': <cyfunction MVar.__rmul__ at 0x00000248A606D8E8>, '__rmatmul__': <cyfunction MVar.__rmatmul__ at 0x00000248A606D9A0>, '__neg__': <cyfunction MVar.__neg__ at 0x00000248A606DA58>, '__pos__': <cyfunction MVar.__pos__ at 0x00000248A606DB10>, '__truediv__': <cyfunction MVar.__truediv__ at 0x00000248A606DBC8>, 'squeeze': <cyfunction MVar.squeeze at 0x00000248A606DC80>, 'tomlinexpr': <cyfunction MVar.tomlinexpr at 0x00000248A606DD38>, 'scalar_mult': <cyfunction MVar.scalar_mult at 0x00000248A606DDF0>, 'idxarr': <cyfunction MVar.idxarr at 0x00000248A606DEA8>, 'sum': <cyfunction MVar.sum at 0x00000248A606DF60>, 'indexed_data': <cyfunction MVar.indexed_data at 0x00000248A606F048>, 'getAttr': <cyfunction MVar.getAttr at 0x00000248A606F100>, 'setAttr': <cyfunction MVar.setAttr at 0x00000248A606F1B8>, 'shape': <property object at 0x00000248A6067958>, 'ndim': <property object at 0x00000248A60679A8>, '__le__': <cyfunction MVar.__le__ at 0x00000248A606F3E0>, '__ge__': <cyfunction MVar.__ge__ at 0x00000248A606F498>, '__eq__': <cyfunction MVar.__eq__ at 0x00000248A606F550>, '__ne__': <cyfunction MVar.__ne__ at 0x00000248A606F608>, '__dict__': <attribute '__dict__' of 'MVar' objects>, '__weakref__': <attribute '__weakref__' of 'MVar' objects>, '__hash__': None})"
    __hash__ = None


class ParamClass(object):
    """
    Gurobi parameters are used to control the optimization process.  They all
      have default values, but their values can be queried or modified through the
      Model.Params class (e.g., 'limit = model.Params.nodeLimit',
      'model.Params.MIPGap = 0.0').
    
      Parameters fall into the following categories:
    
      Termination: affect the termination of an optimize() call
        BarIterLimit: limits the number of barrier iterations performed
        BestBdStop: sets a best bound values at which optimization should stop
        BestObjStop: sets an objective value at which optimization should stop
        Cutoff: sets a target objective value
        IterationLimit: limits the number of simplex iterations performed
        NodeLimit: limits the number of MIP nodes explored
        SolutionLimit: sets a target for the number of feasible solutions found
        TimeLimit: limits the total time expended (in seconds)
    
      Tolerances: control the allowable feasibility or optimality violations
        BarConvTol: barrier convergence tolerance
        BarQCPConvTol: barrier convergence tolerance for QCP models
        FeasibilityTol: primal feasibility tolerance
        IntFeasTol: integer feasibility tolerance
        MarkowitzTol: threshold pivoting tolerance
        MIPGap: target relative MIP optimality gap
        MIPGapAbs: target absolute MIP optimality gap
        OptimalityTol: dual feasibility tolerance
        PSDTol: QP positive semidefinite tolerance
    
      Simplex: affect the simplex algorithms
        InfUnbdInfo: makes additional information available for infeasible or
                     unbounded LP models
        NormAdjust: chooses different pricing norm variants
        ObjScale: controls objective scaling
        PerturbValue: controls the magnitude of any simplex perturbations
        Quad: turns quad precision on or off
        ScaleFlag: turns model scaling on or off
        Sifting: dual simplex sifting strategy for LP, MIP root and MIP nodes
        SiftMethod: chooses from dual, primal and barrier to solve sifting
                    subproblems
        SimplexPricing: determines variable pricing strategy
    
      Barrier: affect the barrier algorithms
        BarCorrectors: limits the number of central corrections
        BarHomogeneous: selects the barrier homogeneous algorithm
        BarOrder: determines the fill reducing ordering strategy
        Crossover: controls barrier crossover
        CrossoverBasis: controls initial crossover basis construction
        QCPDual: enables dual variable computation for continuous QCP models
    
      MIP: affect the MIP algorithms
        BranchDir: controls the branching node selection
        ConcurrentMIP: enables concurrent MIP optimization
        ConcurrentJobs: enables distributed concurrent optimization
        DegenMoves: limit degenerate simplex moves
        Disconnected: controls the disconnected component strategy
        Heuristics: controls the amount of time spent in MIP heuristics
        ImproveStartGap: gap at which to switch MIP search strategies
        ImproveStartNodes: node count at which to switch MIP search strategies
        ImproveStartTime: time at which to switch MIP search strategies
        MinRelNodes: controls the minimum relaxation heuristic
        MIPFocus: affects the high-level MIP search strategy
        MIQCPMethod: controls whether to solve QCP node relaxation or to use OA
        NodefileDir: determines the directory used to store nodes on disk
        NodefileStart: memory nodes may use (in GB) before being written to disk
        NodeMethod: determines the algorithm used to solve MIP node relaxations
        NonConvex: controls how to deal with non-convex quadratic programs
        NoRelHeuristic: determines whether the NoRel heuristic should be used
        PartitionPlace: controls when the partition heuristic runs
        PumpPasses: controls the feasibility pump heuristic
        RINS: sets the frequency of the RINS heuristic
        SolFiles: location to store intermediate solution files
        SolutionNumber: controls access to alternate MIP solutions
        StartNodeLimit: limits nodes in MIP start sub-MIP
        StartNumber: selects the MIP start index
        SubMIPNodes: limits the numbers of nodes explored in a RINS sub-MIP
        Symmetry: controls access to alternate MIP solutions
        VarBranch: controls the branch variable selection strategy
        ZeroObjNodes: controls the zero objective heuristic
    
      Presolve: affect the presolve algorithms
        AggFill: controls the level of presolve aggregation
        Aggregate: turns presolve aggregation on or off
        DualReductions: controls presolve dual reductions
        PreCrush: allows presolve to crush any user cut
        PreDepRow: controls the presolve dependent row reduction
        PreDual: determines whether presolve forms the dual of the input model
        PreMIQCPForm: chooses the form for MIQCP presolved model
        PrePasses: limits the number of presolve passes
        PreQLinearize: controls presolve Q matrix linearization
        Presolve: turns presolve on or off
        PreSOS1BigM: threshold for presolve SOS1 conversion to binary form
        PreSOS2BigM: threshold for presolve SOS2 conversion to binary form
        PreSparsify: enables the presolve sparsify reduction
    
      Tuning: affect the operation of the tuning tool
        TuneCriterion: specify different tuning criteria
        TuneJobs: enables distributed tuning
        TuneOutput: tuning output level
        TuneResults: number of imroved parameter sets returned
        TuneTimeLimit: tuning time limit
        TuneTrials: number of trial runs with each parameter set
    
      Multiple solutions: determines how the MIP search looks for solutions
        PoolGap: determines the quality of the retained solutions
        PoolSearchMode: chooses the approach used to search for solutions
        PoolSolutions: determines the number of solutions that are stored
    
      MIP cuts: affect the generation of MIP cutting planes
        BQPCuts: controls BQP cut generation
        CliqueCuts: controls clique cut generation
        CoverCuts: controls cover cut generation
        CutAggPasses: limits aggregation during cut generation
        CutPasses: limits the number of cut passes
        Cuts: global cut generation control
        FlowCoverCuts: controls flow cover cut generation
        FlowPathCuts: controls flow path cut generation
        GomoryPasses: controls the number of Gomory cut passes
        GUBCoverCuts: controls GUB cover cut generation
        ImpliedCuts: controls implied bound cut generation
        InfProofCuts: controls infeasibility proof cut generation
        MIPSepCuts: controls MIP separation cut generation
        MIRCuts: controls MIR cut generation
        ModKCuts: controls mod-k cut generation
        NetworkCuts: controls network cut generation
        ProjImpliedCuts: controls projected implied bound cut generation
        RelaxLiftCuts: controls relax-and-lift cut generation
        RLTCuts: controls RLT cut generation
        StrongCGCuts: controls Strong-CG cut generation
        SubMIPCuts: controls sub-MIP cut generation
        ZeroHalfCuts: controls zero-half cut generation
    
      Distributed algorithms: used for distributed optimization
        WorkerPassword: cluster client password
        WorkerPool: server URL to access the cluster
    
      Cloud: parameters used for cloud-based optimization
        CloudAccessID: Instant Cloud access ID
        CloudPool: Instant Cloud pool name
        CloudSecretKey: Instant Cloud secret key
    
      Compute Server and Cluster Manager: used for optimization with Remote Services
        CSAPIAccessID: API access ID to access the Cluster Manager
        CSAPISecret: API secret key to access the Cluster Manager
        CSAppName: application name
        CSAuthToken: Authentication token used internally to access a Cluster Manager
        CSBatchMode: Controls Batch-Mode optimization with a Cluster Manager
        CSClientLog: Turns logging on or off
        CSGroup: Group placement request for cluster
        CSIdleTimeout: job idle timeout
        CSManager: access URL of the Cluster Manager
        CSPriority: compute server job priority
        CSQueueTimeout: queue timeout for new jobs
        CSRouter: remote services router URL
        CSTLSInsecure: enable TLS insecurity mode
        ComputeServer: server URL to access the cluster
        ServerPassword: cluster client password
        ServerTimeout: network timeout
        UserName: User name to use when connecting to the Cluster Manager
    
      Token Server: affect token server parameters
        TokenServer: adress of token server
        TSPort: token server port
    
      Other:
        DisplayInterval: sets the frequency at which log lines are printed
        FeasRelaxBigM: BigM value for feasibility relaxation
        FuncPieceError: error allowed for PWL translation of general function
                        constraints without own options specified
        FuncPieceLength: piece length for PWL translation of general function
                         constraints without own options specified
        FuncPieceRatio: control whether to link function values or to have
                        pieces below or above the function
        FuncPieces: control PWL translation of general function constraints
                    without own options specified, whether to use equal piece
                    length, to limit error or to limit the total number of pieces
        FuncMaxVal: maximal value for |lb| and |ub| of x and y variables of
                    general function constraints
        IgnoreNames: indicates whether to ignore names provided by users
        IISMethod: method used to find an IIS
        JSONSolDetail: controls amount of information in a JSON solution string
        LazyConstraints: programs that use lazy constraints must set this to 1
        LogFile: sets the name of the Gurobi log file
        LogToConsole: turn logging to the console on or off
        Method: algorithm used to solve a continuous model or the root node of a
                MIP model (auto, primal simplex, dual simplex, barrier, or
                concurrent)
        NumericFocus: controls numerically conservative level
        MultiObjMethod: warm-start method to solve for subsequent objectives
        MultiObjPre: controls initial presolve level on multi-objective models
        ObjNumber: selects the objective index of multi-objectives
        OutputFlag: turn logging on or off
        Record: enables replay
        ResultFile: result file to write when optimization completes
        ScenarioNumber: selects the scenario index of multi-scenario models
        Seed: sets the random number seed
        Threads: sets the number of threads to apply to parallel MIP
        UpdateMode: controls the way how to update a model
    
      For further information on any of these parameters, type
      paramHelp('paramname') (e.g., paramHelp("NodeLimit")).  Wildcards
      are also accepted for paramHelp().
    """
    def _getChangeList(self, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Gurobi parameters are used to control the optimization process.  They all\\n  have default values, but their values can be queried or modified through the\\n  Model.Params class (e.g., \\\'limit = model.Params.nodeLimit\\\',\\n  \\\'model.Params.MIPGap = 0.0\\\').\\n\\n  Parameters fall into the following categories:\\n\\n  Termination: affect the termination of an optimize() call\\n    BarIterLimit: limits the number of barrier iterations performed\\n    BestBdStop: sets a best bound values at which optimization should stop\\n    BestObjStop: sets an objective value at which optimization should stop\\n    Cutoff: sets a target objective value\\n    IterationLimit: limits the number of simplex iterations performed\\n    NodeLimit: limits the number of MIP nodes explored\\n    SolutionLimit: sets a target for the number of feasible solutions found\\n    TimeLimit: limits the total time expended (in seconds)\\n\\n  Tolerances: control the allowable feasibility or optimality violations\\n    BarConvTol: barrier convergence tolerance\\n    BarQCPConvTol: barrier convergence tolerance for QCP models\\n    FeasibilityTol: primal feasibility tolerance\\n    IntFeasTol: integer feasibility tolerance\\n    MarkowitzTol: threshold pivoting tolerance\\n    MIPGap: target relative MIP optimality gap\\n    MIPGapAbs: target absolute MIP optimality gap\\n    OptimalityTol: dual feasibility tolerance\\n    PSDTol: QP positive semidefinite tolerance\\n\\n  Simplex: affect the simplex algorithms\\n    InfUnbdInfo: makes additional information available for infeasible or\\n                 unbounded LP models\\n    NormAdjust: chooses different pricing norm variants\\n    ObjScale: controls objective scaling\\n    PerturbValue: controls the magnitude of any simplex perturbations\\n    Quad: turns quad precision on or off\\n    ScaleFlag: turns model scaling on or off\\n    Sifting: dual simplex sifting strategy for LP, MIP root and MIP nodes\\n    SiftMethod: chooses from dual, primal and barrier to solve sifting\\n                subproblems\\n    SimplexPricing: determines variable pricing strategy\\n\\n  Barrier: affect the barrier algorithms\\n    BarCorrectors: limits the number of central corrections\\n    BarHomogeneous: selects the barrier homogeneous algorithm\\n    BarOrder: determines the fill reducing ordering strategy\\n    Crossover: controls barrier crossover\\n    CrossoverBasis: controls initial crossover basis construction\\n    QCPDual: enables dual variable computation for continuous QCP models\\n\\n  MIP: affect the MIP algorithms\\n    BranchDir: controls the branching node selection\\n    ConcurrentMIP: enables concurrent MIP optimization\\n    ConcurrentJobs: enables distributed concurrent optimization\\n    DegenMoves: limit degenerate simplex moves\\n    Disconnected: controls the disconnected component strategy\\n    Heuristics: controls the amount of time spent in MIP heuristics\\n    ImproveStartGap: gap at which to switch MIP search strategies\\n    ImproveStartNodes: node count at which to switch MIP search strategies\\n    ImproveStartTime: time at which to switch MIP search strategies\\n    MinRelNodes: controls the minimum relaxation heuristic\\n    MIPFocus: affects the high-level MIP search strategy\\n    MIQCPMethod: controls whether to solve QCP node relaxation or to use OA\\n    NodefileDir: determines the directory used to store nodes on disk\\n    NodefileStart: memory nodes may use (in GB) before being written to disk\\n    NodeMethod: determines the algorithm used to solve MIP node relaxations\\n    NonConvex: controls how to deal with non-convex quadratic programs\\n    NoRelHeuristic: determines whether the NoRel heuristic should be used\\n    PartitionPlace: controls when the partition heuristic runs\\n    PumpPasses: controls the feasibility pump heuristic\\n    RINS: sets the frequency of the RINS heuristic\\n    SolFiles: location to store intermediate solution files\\n    SolutionNumber: controls access to alternate MIP solutions\\n    StartNodeLimit: limits nodes in MIP start sub-MIP\\n    StartNumber: selects the MIP start index\\n    SubMIPNodes: limits the numbers of nodes explored in a RINS sub-MIP\\n    Symmetry: controls access to alternate MIP solutions\\n    VarBranch: controls the branch variable selection strategy\\n    ZeroObjNodes: controls the zero objective heuristic\\n\\n  Presolve: affect the presolve algorithms\\n    AggFill: controls the level of presolve aggregation\\n    Aggregate: turns presolve aggregation on or off\\n    DualReductions: controls presolve dual reductions\\n    PreCrush: allows presolve to crush any user cut\\n    PreDepRow: controls the presolve dependent row reduction\\n    PreDual: determines whether presolve forms the dual of the input model\\n    PreMIQCPForm: chooses the form for MIQCP presolved model\\n    PrePasses: limits the number of presolve passes\\n    PreQLinearize: controls presolve Q matrix linearization\\n    Presolve: turns presolve on or off\\n    PreSOS1BigM: threshold for presolve SOS1 conversion to binary form\\n    PreSOS2BigM: threshold for presolve SOS2 conversion to binary form\\n    PreSparsify: enables the presolve sparsify reduction\\n\\n  Tuning: affect the operation of the tuning tool\\n    TuneCriterion: specify different tuning criteria\\n    TuneJobs: enables distributed tuning\\n    TuneOutput: tuning output level\\n    TuneResults: number of imroved parameter sets returned\\n    TuneTimeLimit: tuning time limit\\n    TuneTrials: number of trial runs with each parameter set\\n\\n  Multiple solutions: determines how the MIP search looks for solutions\\n    PoolGap: determines the quality of the retained solutions\\n    PoolSearchMode: chooses the approach used to search for solutions\\n    PoolSolutions: determines the number of solutions that are stored\\n\\n  MIP cuts: affect the generation of MIP cutting planes\\n    BQPCuts: controls BQP cut generation\\n    CliqueCuts: controls clique cut generation\\n    CoverCuts: controls cover cut generation\\n    CutAggPasses: limits aggregation during cut generation\\n    CutPasses: limits the number of cut passes\\n    Cuts: global cut generation control\\n    FlowCoverCuts: controls flow cover cut generation\\n    FlowPathCuts: controls flow path cut generation\\n    GomoryPasses: controls the number of Gomory cut passes\\n    GUBCoverCuts: controls GUB cover cut generation\\n    ImpliedCuts: controls implied bound cut generation\\n    InfProofCuts: controls infeasibility proof cut generation\\n    MIPSepCuts: controls MIP separation cut generation\\n    MIRCuts: controls MIR cut generation\\n    ModKCuts: controls mod-k cut generation\\n    NetworkCuts: controls network cut generation\\n    ProjImpliedCuts: controls projected implied bound cut generation\\n    RelaxLiftCuts: controls relax-and-lift cut generation\\n    RLTCuts: controls RLT cut generation\\n    StrongCGCuts: controls Strong-CG cut generation\\n    SubMIPCuts: controls sub-MIP cut generation\\n    ZeroHalfCuts: controls zero-half cut generation\\n\\n  Distributed algorithms: used for distributed optimization\\n    WorkerPassword: cluster client password\\n    WorkerPool: server URL to access the cluster\\n\\n  Cloud: parameters used for cloud-based optimization\\n    CloudAccessID: Instant Cloud access ID\\n    CloudPool: Instant Cloud pool name\\n    CloudSecretKey: Instant Cloud secret key\\n\\n  Compute Server and Cluster Manager: used for optimization with Remote Services\\n    CSAPIAccessID: API access ID to access the Cluster Manager\\n    CSAPISecret: API secret key to access the Cluster Manager\\n    CSAppName: application name\\n    CSAuthToken: Authentication token used internally to access a Cluster Manager\\n    CSBatchMode: Controls Batch-Mode optimization with a Cluster Manager\\n    CSClientLog: Turns logging on or off\\n    CSGroup: Group placement request for cluster\\n    CSIdleTimeout: job idle timeout\\n    CSManager: access URL of the Cluster Manager\\n    CSPriority: compute server job priority\\n    CSQueueTimeout: queue timeout for new jobs\\n    CSRouter: remote services router URL\\n    CSTLSInsecure: enable TLS insecurity mode\\n    ComputeServer: server URL to access the cluster\\n    ServerPassword: cluster client password\\n    ServerTimeout: network timeout\\n    UserName: User name to use when connecting to the Cluster Manager\\n\\n  Token Server: affect token server parameters\\n    TokenServer: adress of token server\\n    TSPort: token server port\\n\\n  Other:\\n    DisplayInterval: sets the frequency at which log lines are printed\\n    FeasRelaxBigM: BigM value for feasibility relaxation\\n    FuncPieceError: error allowed for PWL translation of general function\\n                    constraints without own options specified\\n    FuncPieceLength: piece length for PWL translation of general function\\n                     constraints without own options specified\\n    FuncPieceRatio: control whether to link function values or to have\\n                    pieces below or above the function\\n    FuncPieces: control PWL translation of general function constraints\\n                without own options specified, whether to use equal piece\\n                length, to limit error or to limit the total number of pieces\\n    FuncMaxVal: maximal value for |lb| and |ub| of x and y variables of\\n                general function constraints\\n    IgnoreNames: indicates whether to ignore names provided by users\\n    IISMethod: method used to find an IIS\\n    JSONSolDetail: controls amount of information in a JSON solution string\\n    LazyConstraints: programs that use lazy constraints must set this to 1\\n    LogFile: sets the name of the Gurobi log file\\n    LogToConsole: turn logging to the console on or off\\n    Method: algorithm used to solve a continuous model or the root node of a\\n            MIP model (auto, primal simplex, dual simplex, barrier, or\\n            concurrent)\\n    NumericFocus: controls numerically conservative level\\n    MultiObjMethod: warm-start method to solve for subsequent objectives\\n    MultiObjPre: controls initial presolve level on multi-objective models\\n    ObjNumber: selects the objective index of multi-objectives\\n    OutputFlag: turn logging on or off\\n    Record: enables replay\\n    ResultFile: result file to write when optimization completes\\n    ScenarioNumber: selects the scenario index of multi-scenario models\\n    Seed: sets the random number seed\\n    Threads: sets the number of threads to apply to parallel MIP\\n    UpdateMode: controls the way how to update a model\\n\\n  For further information on any of these parameters, type\\n  paramHelp(\\\'paramname\\\') (e.g., paramHelp("NodeLimit")).  Wildcards\\n  are also accepted for paramHelp().\\n  \', \'__init__\': <cyfunction ParamClass.__init__ at 0x00000248A608C6C0>, \'__repr__\': <cyfunction ParamClass.__repr__ at 0x00000248A608C778>, \'__dir__\': <cyfunction ParamClass.__dir__ at 0x00000248A608C830>, \'__getattr__\': <cyfunction ParamClass.__getattr__ at 0x00000248A608C8E8>, \'__setattr__\': <cyfunction ParamClass.__setattr__ at 0x00000248A608C9A0>, \'_getChangeList\': <cyfunction ParamClass._getChangeList at 0x00000248A608CA58>, \'__dict__\': <attribute \'__dict__\' of \'ParamClass\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'ParamClass\' objects>})'


class ParamConstClass(object):
    """
    Gurobi parameters are used to control the optimization process.  They all
      have default values, but their values can be changed using the setParam()
      function.  Current values can be retrieved using the Model.getParamInfo()
      method.
    
      Parameters fall into the following categories:
    
      Termination: affect the termination of an optimize() call
        BarIterLimit: limits the number of barrier iterations performed
        BestBdStop: sets a best bound values at which optimization should stop
        BestObjStop: sets an objective value at which optimization should stop
        Cutoff: sets a target objective value
        IterationLimit: limits the number of simplex iterations performed
        NodeLimit: limits the number of MIP nodes explored
        SolutionLimit: sets a target for the number of feasible solutions found
        TimeLimit: limits the total time expended (in seconds)
    
      Tolerances: control the allowable feasibility or optimality violations
        BarConvTol: barrier convergence tolerance
        BarQCPConvTol: barrier convergence tolerance for QCP models
        FeasibilityTol: primal feasibility tolerance
        IntFeasTol: integer feasibility tolerance
        MarkowitzTol: threshold pivoting tolerance
        MIPGap: target relative MIP optimality gap
        MIPGapAbs: target absolute MIP optimality gap
        OptimalityTol: dual feasibility tolerance
        PSDTol: QP positive semidefinite tolerance
    
      Simplex: affect the simplex algorithms
        InfUnbdInfo: makes additional information available for infeasible or
                     unbounded LP models
        NormAdjust: chooses different pricing norm variants
        ObjScale: controls objective scaling
        PerturbValue: controls the magnitude of any simplex perturbations
        Quad: turns quad precision on or off
        ScaleFlag: turns model scaling on or off
        Sifting: dual simplex sifting strategy for LP, MIP root and MIP nodes
        SiftMethod: chooses from dual, primal and barrier to solve sifting
                    subproblems
        SimplexPricing: determines variable pricing strategy
    
      Barrier: affect the barrier algorithms
        BarCorrectors: limits the number of central corrections
        BarHomogeneous: selects the barrier homogeneous algorithm
        BarOrder: determines the fill reducing ordering strategy
        Crossover: controls barrier crossover
        CrossoverBasis: controls initial crossover basis construction
        QCPDual: enables dual variable computation for continuous QCP models
    
      MIP: affect the MIP algorithms
        BranchDir: controls the branching node selection
        ConcurrentMIP: enables concurrent MIP optimization
        ConcurrentJobs: enables distributed concurrent optimization
        DegenMoves: limit degenerate simplex moves
        Disconnected: controls the disconnected component strategy
        Heuristics: controls the amount of time spent in MIP heuristics
        ImproveStartGap: gap at which to switch MIP search strategies
        ImproveStartNodes: node count at which to switch MIP search strategies
        ImproveStartTime: time at which to switch MIP search strategies
        MinRelNodes: controls the minimum relaxation heuristic
        MIPFocus: affects the high-level MIP search strategy
        MIQCPMethod: controls whether to solve QCP node relaxation or to use OA
        NodefileDir: determines the directory used to store nodes on disk
        NodefileStart: memory nodes may use (in GB) before being written to disk
        NodeMethod: determines the algorithm used to solve MIP node relaxations
        NonConvex: controls how to deal with non-convex quadratic programs
        NoRelHeuristic: determines whether the NoRel heuristic should be used
        PartitionPlace: controls when the partition heuristic runs
        PumpPasses: controls the feasibility pump heuristic
        RINS: sets the frequency of the RINS heuristic
        SolFiles: location to store intermediate solution files
        SolutionNumber: controls access to alternate MIP solutions
        StartNodeLimit: limits nodes in MIP start sub-MIP
        StartNumber: selects the MIP start index
        SubMIPNodes: limits the numbers of nodes explored in a RINS sub-MIP
        Symmetry: controls access to alternate MIP solutions
        VarBranch: controls the branch variable selection strategy
        ZeroObjNodes: controls the zero objective heuristic
    
      Presolve: affect the presolve algorithms
        AggFill: controls the level of presolve aggregation
        Aggregate: turns presolve aggregation on or off
        DualReductions: controls presolve dual reductions
        PreCrush: allows presolve to crush any user cut
        PreDepRow: controls the presolve dependent row reduction
        PreDual: determines whether presolve forms the dual of the input model
        PreMIQCPForm: chooses the form for MIQCP presolved model
        PrePasses: limits the number of presolve passes
        PreQLinearize: controls presolve Q matrix linearization
        Presolve: turns presolve on or off
        PreSOS1BigM: threshold for presolve SOS1 conversion to binary form
        PreSOS2BigM: threshold for presolve SOS2 conversion to binary form
        PreSparsify: enables the presolve sparsify reduction
    
      Tuning: affect the operation of the tuning tool
        TuneCriterion: specify different tuning criteria
        TuneJobs: enables distributed tuning
        TuneOutput: tuning output level
        TuneResults: number of imroved parameter sets returned
        TuneTimeLimit: tuning time limit
        TuneTrials: number of trial runs with each parameter set
    
      Multiple solutions: determines how the MIP search looks for solutions
        PoolGap: determines the quality of the retained solutions
        PoolSearchMode: chooses the approach used to search for solutions
        PoolSolutions: determines the number of solutions that are stored
    
      MIP cuts: affect the generation of MIP cutting planes
        BQPCuts: controls BQP cut generation
        CliqueCuts: controls clique cut generation
        CoverCuts: controls cover cut generation
        CutAggPasses: limits aggregation during cut generation
        CutPasses: limits the number of cut passes
        Cuts: global cut generation control
        FlowCoverCuts: controls flow cover cut generation
        FlowPathCuts: controls flow path cut generation
        GomoryPasses: controls the number of Gomory cut passes
        GUBCoverCuts: controls GUB cover cut generation
        ImpliedCuts: controls implied bound cut generation
        InfProofCuts: controls infeasibility proof cut generation
        MIPSepCuts: controls MIP separation cut generation
        MIRCuts: controls MIR cut generation
        ModKCuts: controls mod-k cut generation
        NetworkCuts: controls network cut generation
        ProjImpliedCuts: controls projected implied bound cut generation
        RelaxLiftCuts: controls relax-and-lift cut generation
        RLTCuts: controls RLT cut generation
        StrongCGCuts: controls Strong-CG cut generation
        SubMIPCuts: controls sub-MIP cut generation
        ZeroHalfCuts: controls zero-half cut generation
    
      Distributed algorithms: used for distributed optimization
        WorkerPassword: cluster client password
        WorkerPool: server URL to access the cluster
    
      Cloud: parameters used for cloud-based optimization
        CloudAccessID: Instant Cloud access ID
        CloudPool: Instant Cloud pool name
        CloudSecretKey: Instant Cloud secret key
    
      Compute Server and Cluster Manager: used for optimization with Remote Services
        CSAPIAccessID: API access ID to access the Cluster Manager
        CSAPISecret: API secret key to access the Cluster Manager
        CSAppName: application name
        CSAuthToken: Authentication token used internally to access a Cluster Manager
        CSBatchMode: Controls Batch-Mode optimization with a Cluster Manager
        CSClientLog: Turns logging on or off
        CSGroup: Group placement request for cluster
        CSIdleTimeout: job idle timeout
        CSManager: access URL of the Cluster Manager
        CSPriority: compute server job priority
        CSQueueTimeout: queue timeout for new jobs
        CSRouter: remote services router URL
        CSTLSInsecure: enable TLS insecurity mode
        ComputeServer: server URL to access the cluster
        ServerPassword: cluster client password
        ServerTimeout: network timeout
        UserName: User name to use when connecting to the Cluster Manager
    
      Token Server: affect token server parameters
        TokenServer: adress of token server
        TSPort: token server port
    
      Other:
        DisplayInterval: sets the frequency at which log lines are printed
        FeasRelaxBigM: BigM value for feasibility relaxation
        FuncPieceError: error allowed for PWL translation of general function
                        constraints without own options specified
        FuncPieceLength: piece length for PWL translation of general function
                         constraints without own options specified
        FuncPieceRatio: control whether to link function values or to have
                        pieces below or above the function
        FuncPieces: control PWL translation of general function constraints
                    without own options specified, whether to use equal piece
                    length, to limit error or to limit the total number of pieces
        FuncMaxVal: maximal value for |lb| and |ub| of x and y variables of
                    general function constraints
        IgnoreNames: indicates whether to ignore names provided by users
        IISMethod: method used to find an IIS
        JSONSolDetail: controls amount of information in a JSON solution string
        LazyConstraints: programs that use lazy constraints must set this to 1
        LogFile: sets the name of the Gurobi log file
        LogToConsole: turn logging to the console on or off
        Method: algorithm used to solve a continuous model or the root node of a
                MIP model (auto, primal simplex, dual simplex, barrier, or
                concurrent)
        NumericFocus: controls numerically conservative level
        MultiObjMethod: warm-start method to solve for subsequent objectives
        MultiObjPre: controls initial presolve level on multi-objective models
        ObjNumber: selects the objective index of multi-objectives
        OutputFlag: turn logging on or off
        Record: enables replay
        ResultFile: result file to write when optimization completes
        ScenarioNumber: selects the scenario index of multi-scenario models
        Seed: sets the random number seed
        Threads: sets the number of threads to apply to parallel MIP
        UpdateMode: controls the way how to update a model
    
      Parameters can be referred to using the Param class (e.g.
      "setParam(GRB.param.threads, 1)"), or by using the name as a string
      (e.g., "setParam('threads', 1)).  You can use the '*' and '?' wildcards
      when inputting parameter names, and text case is ignored
      (so "setParam('thr*', 1)" would also work).
    
      For further information on any of these parameters, type
      paramHelp('paramname') (e.g., paramHelp("NodeLimit")).  Wildcards
      are also accepted for paramHelp().
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AggFill = 'AggFill'
    Aggregate = 'Aggregate'
    BarConvTol = 'BarConvTol'
    BarCorrectors = 'BarCorrectors'
    BarHomogeneous = 'BarHomogeneous'
    BarIterLimit = 'BarIterLimit'
    BarOrder = 'BarOrder'
    BarQCPConvTol = 'BarQCPConvTol'
    BestBdStop = 'BestBdStop'
    BestObjStop = 'BestObjStop'
    BQPCuts = 'BQPCuts'
    BranchDir = 'BranchDir'
    CliqueCuts = 'CliqueCuts'
    CloudAccessID = 'CloudAccessID'
    CloudHost = 'CloudHost'
    CloudPool = 'CloudPool'
    CloudSecretKey = 'CloudSecretKey'
    ComputeServer = 'ComputeServer'
    ConcurrentJobs = 'ConcurrentJobs'
    ConcurrentMIP = 'ConcurrentMIP'
    CoverCuts = 'CoverCuts'
    Crossover = 'Crossover'
    CrossoverBasis = 'CrossoverBasis'
    CSAPIAccessID = 'CSAPIAccessID'
    CSAPISecret = 'CSAPISecret'
    CSAppName = 'CSAppName'
    CSAuthToken = 'CSAuthToken'
    CSBatchMode = 'CSBatchMode'
    CSClientLog = 'CSClientLog'
    CSGroup = 'CSGroup'
    CSIdleTimeout = 'CSIdleTimeout'
    CSManager = 'CSManager'
    CSPriority = 'CSPriority'
    CSQueueTimeout = 'CSQueueTimeout'
    CSRouter = 'CSRouter'
    CSTLSInsecure = 'CSTLSInsecure'
    CutAggPasses = 'CutAggPasses'
    Cutoff = 'Cutoff'
    CutPasses = 'CutPasses'
    Cuts = 'Cuts'
    DegenMoves = 'DegenMoves'
    Disconnected = 'Disconnected'
    DisplayInterval = 'DisplayInterval'
    DistributedMIPJobs = 'DistributedMIPJobs'
    DualReductions = 'DualReductions'
    FeasibilityTol = 'FeasibilityTol'
    FeasRelaxBigM = 'FeasRelaxBigM'
    FlowCoverCuts = 'FlowCoverCuts'
    FlowPathCuts = 'FlowPathCuts'
    FuncMaxVal = 'FuncMaxVal'
    FuncPieceError = 'FuncPieceError'
    FuncPieceLength = 'FuncPieceLength'
    FuncPieceRatio = 'FuncPieceRatio'
    FuncPieces = 'FuncPieces'
    GomoryPasses = 'GomoryPasses'
    GUBCoverCuts = 'GUBCoverCuts'
    Heuristics = 'Heuristics'
    IgnoreNames = 'IgnoreNames'
    IISMethod = 'IISMethod'
    ImpliedCuts = 'ImpliedCuts'
    ImproveStartGap = 'ImproveStartGap'
    ImproveStartNodes = 'ImproveStartNodes'
    ImproveStartTime = 'ImproveStartTime'
    InfProofCuts = 'InfProofCuts'
    InfUnbdInfo = 'InfUnbdInfo'
    IntFeasTol = 'IntFeasTol'
    IterationLimit = 'IterationLimit'
    JobID = 'JobID'
    JSONSolDetail = 'JSONSolDetail'
    LazyConstraints = 'LazyConstraints'
    LogFile = 'LogFile'
    LogToConsole = 'LogToConsole'
    MarkowitzTol = 'MarkowitzTol'
    Method = 'Method'
    MinRelNodes = 'MinRelNodes'
    MIPFocus = 'MIPFocus'
    MIPGap = 'MIPGap'
    MIPGapAbs = 'MIPGapAbs'
    MIPSepCuts = 'MIPSepCuts'
    MIQCPMethod = 'MIQCPMethod'
    MIRCuts = 'MIRCuts'
    ModKCuts = 'ModKCuts'
    MultiObjMethod = 'MultiObjMethod'
    MultiObjPre = 'MultiObjPre'
    NetworkCuts = 'NetworkCuts'
    NodefileDir = 'NodefileDir'
    NodefileStart = 'NodefileStart'
    NodeLimit = 'NodeLimit'
    NodeMethod = 'NodeMethod'
    NonConvex = 'NonConvex'
    NoRelHeuristic = 'NoRelHeuristic'
    NormAdjust = 'NormAdjust'
    NumericFocus = 'NumericFocus'
    ObjNumber = 'ObjNumber'
    ObjScale = 'ObjScale'
    OptimalityTol = 'OptimalityTol'
    OutputFlag = 'OutputFlag'
    PartitionPlace = 'PartitionPlace'
    PerturbValue = 'PerturbValue'
    PoolGap = 'PoolGap'
    PoolSearchMode = 'PoolSearchMode'
    PoolSolutions = 'PoolSolutions'
    PreCrush = 'PreCrush'
    PreDepRow = 'PreDepRow'
    PreDual = 'PreDual'
    PreMIQCPForm = 'PreMIQCPForm'
    PrePasses = 'PrePasses'
    PreQLinearize = 'PreQLinearize'
    Presolve = 'Presolve'
    PreSOS1BigM = 'PreSOS1BigM'
    PreSOS2BigM = 'PreSOS2BigM'
    PreSparsify = 'PreSparsify'
    ProjImpliedCuts = 'ProjImpliedCuts'
    PSDTol = 'PSDTol'
    PumpPasses = 'PumpPasses'
    QCPDual = 'QCPDual'
    Quad = 'Quad'
    Record = 'Record'
    RelaxLiftCuts = 'RelaxLiftCuts'
    ResultFile = 'ResultFile'
    RINS = 'RINS'
    RLTCuts = 'RLTCuts'
    ScaleFlag = 'ScaleFlag'
    ScenarioNumber = 'ScenarioNumber'
    Seed = 'Seed'
    ServerPassword = 'ServerPassword'
    ServerTimeout = 'ServerTimeout'
    Sifting = 'Sifting'
    SiftMethod = 'SiftMethod'
    SimplexPricing = 'SimplexPricing'
    SolFiles = 'SolFiles'
    SolutionLimit = 'SolutionLimit'
    SolutionNumber = 'SolutionNumber'
    StartNodeLimit = 'StartNodeLimit'
    StartNumber = 'StartNumber'
    StrongCGCuts = 'StrongCGCuts'
    SubMIPCuts = 'SubMIPCuts'
    SubMIPNodes = 'SubMIPNodes'
    Symmetry = 'Symmetry'
    Threads = 'Threads'
    TimeLimit = 'TimeLimit'
    TokenServer = 'TokenServer'
    TSPort = 'TSPort'
    TuneCriterion = 'TuneCriterion'
    TuneJobs = 'TuneJobs'
    TuneOutput = 'TuneOutput'
    TuneResults = 'TuneResults'
    TuneTimeLimit = 'TuneTimeLimit'
    TuneTrials = 'TuneTrials'
    UpdateMode = 'UpdateMode'
    UserName = 'UserName'
    VarBranch = 'VarBranch'
    WorkerPassword = 'WorkerPassword'
    WorkerPool = 'WorkerPool'
    ZeroHalfCuts = 'ZeroHalfCuts'
    ZeroObjNodes = 'ZeroObjNodes'
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Gurobi parameters are used to control the optimization process.  They all\\n  have default values, but their values can be changed using the setParam()\\n  function.  Current values can be retrieved using the Model.getParamInfo()\\n  method.\\n\\n  Parameters fall into the following categories:\\n\\n  Termination: affect the termination of an optimize() call\\n    BarIterLimit: limits the number of barrier iterations performed\\n    BestBdStop: sets a best bound values at which optimization should stop\\n    BestObjStop: sets an objective value at which optimization should stop\\n    Cutoff: sets a target objective value\\n    IterationLimit: limits the number of simplex iterations performed\\n    NodeLimit: limits the number of MIP nodes explored\\n    SolutionLimit: sets a target for the number of feasible solutions found\\n    TimeLimit: limits the total time expended (in seconds)\\n\\n  Tolerances: control the allowable feasibility or optimality violations\\n    BarConvTol: barrier convergence tolerance\\n    BarQCPConvTol: barrier convergence tolerance for QCP models\\n    FeasibilityTol: primal feasibility tolerance\\n    IntFeasTol: integer feasibility tolerance\\n    MarkowitzTol: threshold pivoting tolerance\\n    MIPGap: target relative MIP optimality gap\\n    MIPGapAbs: target absolute MIP optimality gap\\n    OptimalityTol: dual feasibility tolerance\\n    PSDTol: QP positive semidefinite tolerance\\n\\n  Simplex: affect the simplex algorithms\\n    InfUnbdInfo: makes additional information available for infeasible or\\n                 unbounded LP models\\n    NormAdjust: chooses different pricing norm variants\\n    ObjScale: controls objective scaling\\n    PerturbValue: controls the magnitude of any simplex perturbations\\n    Quad: turns quad precision on or off\\n    ScaleFlag: turns model scaling on or off\\n    Sifting: dual simplex sifting strategy for LP, MIP root and MIP nodes\\n    SiftMethod: chooses from dual, primal and barrier to solve sifting\\n                subproblems\\n    SimplexPricing: determines variable pricing strategy\\n\\n  Barrier: affect the barrier algorithms\\n    BarCorrectors: limits the number of central corrections\\n    BarHomogeneous: selects the barrier homogeneous algorithm\\n    BarOrder: determines the fill reducing ordering strategy\\n    Crossover: controls barrier crossover\\n    CrossoverBasis: controls initial crossover basis construction\\n    QCPDual: enables dual variable computation for continuous QCP models\\n\\n  MIP: affect the MIP algorithms\\n    BranchDir: controls the branching node selection\\n    ConcurrentMIP: enables concurrent MIP optimization\\n    ConcurrentJobs: enables distributed concurrent optimization\\n    DegenMoves: limit degenerate simplex moves\\n    Disconnected: controls the disconnected component strategy\\n    Heuristics: controls the amount of time spent in MIP heuristics\\n    ImproveStartGap: gap at which to switch MIP search strategies\\n    ImproveStartNodes: node count at which to switch MIP search strategies\\n    ImproveStartTime: time at which to switch MIP search strategies\\n    MinRelNodes: controls the minimum relaxation heuristic\\n    MIPFocus: affects the high-level MIP search strategy\\n    MIQCPMethod: controls whether to solve QCP node relaxation or to use OA\\n    NodefileDir: determines the directory used to store nodes on disk\\n    NodefileStart: memory nodes may use (in GB) before being written to disk\\n    NodeMethod: determines the algorithm used to solve MIP node relaxations\\n    NonConvex: controls how to deal with non-convex quadratic programs\\n    NoRelHeuristic: determines whether the NoRel heuristic should be used\\n    PartitionPlace: controls when the partition heuristic runs\\n    PumpPasses: controls the feasibility pump heuristic\\n    RINS: sets the frequency of the RINS heuristic\\n    SolFiles: location to store intermediate solution files\\n    SolutionNumber: controls access to alternate MIP solutions\\n    StartNodeLimit: limits nodes in MIP start sub-MIP\\n    StartNumber: selects the MIP start index\\n    SubMIPNodes: limits the numbers of nodes explored in a RINS sub-MIP\\n    Symmetry: controls access to alternate MIP solutions\\n    VarBranch: controls the branch variable selection strategy\\n    ZeroObjNodes: controls the zero objective heuristic\\n\\n  Presolve: affect the presolve algorithms\\n    AggFill: controls the level of presolve aggregation\\n    Aggregate: turns presolve aggregation on or off\\n    DualReductions: controls presolve dual reductions\\n    PreCrush: allows presolve to crush any user cut\\n    PreDepRow: controls the presolve dependent row reduction\\n    PreDual: determines whether presolve forms the dual of the input model\\n    PreMIQCPForm: chooses the form for MIQCP presolved model\\n    PrePasses: limits the number of presolve passes\\n    PreQLinearize: controls presolve Q matrix linearization\\n    Presolve: turns presolve on or off\\n    PreSOS1BigM: threshold for presolve SOS1 conversion to binary form\\n    PreSOS2BigM: threshold for presolve SOS2 conversion to binary form\\n    PreSparsify: enables the presolve sparsify reduction\\n\\n  Tuning: affect the operation of the tuning tool\\n    TuneCriterion: specify different tuning criteria\\n    TuneJobs: enables distributed tuning\\n    TuneOutput: tuning output level\\n    TuneResults: number of imroved parameter sets returned\\n    TuneTimeLimit: tuning time limit\\n    TuneTrials: number of trial runs with each parameter set\\n\\n  Multiple solutions: determines how the MIP search looks for solutions\\n    PoolGap: determines the quality of the retained solutions\\n    PoolSearchMode: chooses the approach used to search for solutions\\n    PoolSolutions: determines the number of solutions that are stored\\n\\n  MIP cuts: affect the generation of MIP cutting planes\\n    BQPCuts: controls BQP cut generation\\n    CliqueCuts: controls clique cut generation\\n    CoverCuts: controls cover cut generation\\n    CutAggPasses: limits aggregation during cut generation\\n    CutPasses: limits the number of cut passes\\n    Cuts: global cut generation control\\n    FlowCoverCuts: controls flow cover cut generation\\n    FlowPathCuts: controls flow path cut generation\\n    GomoryPasses: controls the number of Gomory cut passes\\n    GUBCoverCuts: controls GUB cover cut generation\\n    ImpliedCuts: controls implied bound cut generation\\n    InfProofCuts: controls infeasibility proof cut generation\\n    MIPSepCuts: controls MIP separation cut generation\\n    MIRCuts: controls MIR cut generation\\n    ModKCuts: controls mod-k cut generation\\n    NetworkCuts: controls network cut generation\\n    ProjImpliedCuts: controls projected implied bound cut generation\\n    RelaxLiftCuts: controls relax-and-lift cut generation\\n    RLTCuts: controls RLT cut generation\\n    StrongCGCuts: controls Strong-CG cut generation\\n    SubMIPCuts: controls sub-MIP cut generation\\n    ZeroHalfCuts: controls zero-half cut generation\\n\\n  Distributed algorithms: used for distributed optimization\\n    WorkerPassword: cluster client password\\n    WorkerPool: server URL to access the cluster\\n\\n  Cloud: parameters used for cloud-based optimization\\n    CloudAccessID: Instant Cloud access ID\\n    CloudPool: Instant Cloud pool name\\n    CloudSecretKey: Instant Cloud secret key\\n\\n  Compute Server and Cluster Manager: used for optimization with Remote Services\\n    CSAPIAccessID: API access ID to access the Cluster Manager\\n    CSAPISecret: API secret key to access the Cluster Manager\\n    CSAppName: application name\\n    CSAuthToken: Authentication token used internally to access a Cluster Manager\\n    CSBatchMode: Controls Batch-Mode optimization with a Cluster Manager\\n    CSClientLog: Turns logging on or off\\n    CSGroup: Group placement request for cluster\\n    CSIdleTimeout: job idle timeout\\n    CSManager: access URL of the Cluster Manager\\n    CSPriority: compute server job priority\\n    CSQueueTimeout: queue timeout for new jobs\\n    CSRouter: remote services router URL\\n    CSTLSInsecure: enable TLS insecurity mode\\n    ComputeServer: server URL to access the cluster\\n    ServerPassword: cluster client password\\n    ServerTimeout: network timeout\\n    UserName: User name to use when connecting to the Cluster Manager\\n\\n  Token Server: affect token server parameters\\n    TokenServer: adress of token server\\n    TSPort: token server port\\n\\n  Other:\\n    DisplayInterval: sets the frequency at which log lines are printed\\n    FeasRelaxBigM: BigM value for feasibility relaxation\\n    FuncPieceError: error allowed for PWL translation of general function\\n                    constraints without own options specified\\n    FuncPieceLength: piece length for PWL translation of general function\\n                     constraints without own options specified\\n    FuncPieceRatio: control whether to link function values or to have\\n                    pieces below or above the function\\n    FuncPieces: control PWL translation of general function constraints\\n                without own options specified, whether to use equal piece\\n                length, to limit error or to limit the total number of pieces\\n    FuncMaxVal: maximal value for |lb| and |ub| of x and y variables of\\n                general function constraints\\n    IgnoreNames: indicates whether to ignore names provided by users\\n    IISMethod: method used to find an IIS\\n    JSONSolDetail: controls amount of information in a JSON solution string\\n    LazyConstraints: programs that use lazy constraints must set this to 1\\n    LogFile: sets the name of the Gurobi log file\\n    LogToConsole: turn logging to the console on or off\\n    Method: algorithm used to solve a continuous model or the root node of a\\n            MIP model (auto, primal simplex, dual simplex, barrier, or\\n            concurrent)\\n    NumericFocus: controls numerically conservative level\\n    MultiObjMethod: warm-start method to solve for subsequent objectives\\n    MultiObjPre: controls initial presolve level on multi-objective models\\n    ObjNumber: selects the objective index of multi-objectives\\n    OutputFlag: turn logging on or off\\n    Record: enables replay\\n    ResultFile: result file to write when optimization completes\\n    ScenarioNumber: selects the scenario index of multi-scenario models\\n    Seed: sets the random number seed\\n    Threads: sets the number of threads to apply to parallel MIP\\n    UpdateMode: controls the way how to update a model\\n\\n  Parameters can be referred to using the Param class (e.g.\\n  "setParam(GRB.param.threads, 1)"), or by using the name as a string\\n  (e.g., "setParam(\\\'threads\\\', 1)).  You can use the \\\'*\\\' and \\\'?\\\' wildcards\\n  when inputting parameter names, and text case is ignored\\n  (so "setParam(\\\'thr*\\\', 1)" would also work).\\n\\n  For further information on any of these parameters, type\\n  paramHelp(\\\'paramname\\\') (e.g., paramHelp("NodeLimit")).  Wildcards\\n  are also accepted for paramHelp().\\n  \', \'__setattr__\': <cyfunction ParamConstClass.__setattr__ at 0x00000248A608CB10>, \'BarIterLimit\': \'BarIterLimit\', \'Cutoff\': \'Cutoff\', \'IterationLimit\': \'IterationLimit\', \'NodeLimit\': \'NodeLimit\', \'SolutionLimit\': \'SolutionLimit\', \'TimeLimit\': \'TimeLimit\', \'BestObjStop\': \'BestObjStop\', \'BestBdStop\': \'BestBdStop\', \'BarConvTol\': \'BarConvTol\', \'BarQCPConvTol\': \'BarQCPConvTol\', \'FeasibilityTol\': \'FeasibilityTol\', \'IntFeasTol\': \'IntFeasTol\', \'MarkowitzTol\': \'MarkowitzTol\', \'MIPGap\': \'MIPGap\', \'MIPGapAbs\': \'MIPGapAbs\', \'OptimalityTol\': \'OptimalityTol\', \'PSDTol\': \'PSDTol\', \'InfUnbdInfo\': \'InfUnbdInfo\', \'NormAdjust\': \'NormAdjust\', \'ObjScale\': \'ObjScale\', \'PerturbValue\': \'PerturbValue\', \'Quad\': \'Quad\', \'ScaleFlag\': \'ScaleFlag\', \'Sifting\': \'Sifting\', \'SiftMethod\': \'SiftMethod\', \'SimplexPricing\': \'SimplexPricing\', \'BarCorrectors\': \'BarCorrectors\', \'BarHomogeneous\': \'BarHomogeneous\', \'BarOrder\': \'BarOrder\', \'Crossover\': \'Crossover\', \'CrossoverBasis\': \'CrossoverBasis\', \'QCPDual\': \'QCPDual\', \'BranchDir\': \'BranchDir\', \'DegenMoves\': \'DegenMoves\', \'ConcurrentJobs\': \'ConcurrentJobs\', \'ConcurrentMIP\': \'ConcurrentMIP\', \'Disconnected\': \'Disconnected\', \'DistributedMIPJobs\': \'DistributedMIPJobs\', \'Heuristics\': \'Heuristics\', \'ImproveStartGap\': \'ImproveStartGap\', \'ImproveStartNodes\': \'ImproveStartNodes\', \'ImproveStartTime\': \'ImproveStartTime\', \'MinRelNodes\': \'MinRelNodes\', \'MIPFocus\': \'MIPFocus\', \'MIQCPMethod\': \'MIQCPMethod\', \'NodefileDir\': \'NodefileDir\', \'NodefileStart\': \'NodefileStart\', \'NodeMethod\': \'NodeMethod\', \'NonConvex\': \'NonConvex\', \'NoRelHeuristic\': \'NoRelHeuristic\', \'PartitionPlace\': \'PartitionPlace\', \'PumpPasses\': \'PumpPasses\', \'RINS\': \'RINS\', \'SolFiles\': \'SolFiles\', \'SolutionNumber\': \'SolutionNumber\', \'SubMIPNodes\': \'SubMIPNodes\', \'Symmetry\': \'Symmetry\', \'VarBranch\': \'VarBranch\', \'ZeroObjNodes\': \'ZeroObjNodes\', \'TuneCriterion\': \'TuneCriterion\', \'TuneJobs\': \'TuneJobs\', \'TuneOutput\': \'TuneOutput\', \'TuneResults\': \'TuneResults\', \'TuneTimeLimit\': \'TuneTimeLimit\', \'TuneTrials\': \'TuneTrials\', \'PoolSearchMode\': \'PoolSearchMode\', \'PoolSolutions\': \'PoolSolutions\', \'PoolGap\': \'PoolGap\', \'BQPCuts\': \'BQPCuts\', \'Cuts\': \'Cuts\', \'CliqueCuts\': \'CliqueCuts\', \'CoverCuts\': \'CoverCuts\', \'FlowCoverCuts\': \'FlowCoverCuts\', \'FlowPathCuts\': \'FlowPathCuts\', \'GUBCoverCuts\': \'GUBCoverCuts\', \'ImpliedCuts\': \'ImpliedCuts\', \'InfProofCuts\': \'InfProofCuts\', \'MIPSepCuts\': \'MIPSepCuts\', \'MIRCuts\': \'MIRCuts\', \'ModKCuts\': \'ModKCuts\', \'NetworkCuts\': \'NetworkCuts\', \'ProjImpliedCuts\': \'ProjImpliedCuts\', \'RelaxLiftCuts\': \'RelaxLiftCuts\', \'RLTCuts\': \'RLTCuts\', \'StrongCGCuts\': \'StrongCGCuts\', \'SubMIPCuts\': \'SubMIPCuts\', \'ZeroHalfCuts\': \'ZeroHalfCuts\', \'CutAggPasses\': \'CutAggPasses\', \'CutPasses\': \'CutPasses\', \'GomoryPasses\': \'GomoryPasses\', \'WorkerPassword\': \'WorkerPassword\', \'WorkerPool\': \'WorkerPool\', \'ComputeServer\': \'ComputeServer\', \'ServerPassword\': \'ServerPassword\', \'ServerTimeout\': \'ServerTimeout\', \'CSRouter\': \'CSRouter\', \'CSGroup\': \'CSGroup\', \'CSPriority\': \'CSPriority\', \'CSQueueTimeout\': \'CSQueueTimeout\', \'CSTLSInsecure\': \'CSTLSInsecure\', \'CSAppName\': \'CSAppName\', \'CSClientLog\': \'CSClientLog\', \'CSIdleTimeout\': \'CSIdleTimeout\', \'TokenServer\': \'TokenServer\', \'TSPort\': \'TSPort\', \'CloudAccessID\': \'CloudAccessID\', \'CloudSecretKey\': \'CloudSecretKey\', \'CloudPool\': \'CloudPool\', \'CloudHost\': \'CloudHost\', \'JobID\': \'JobID\', \'CSAPIAccessID\': \'CSAPIAccessID\', \'CSAPISecret\': \'CSAPISecret\', \'CSAuthToken\': \'CSAuthToken\', \'CSBatchMode\': \'CSBatchMode\', \'CSManager\': \'CSManager\', \'UserName\': \'UserName\', \'AggFill\': \'AggFill\', \'Aggregate\': \'Aggregate\', \'DisplayInterval\': \'DisplayInterval\', \'DualReductions\': \'DualReductions\', \'FeasRelaxBigM\': \'FeasRelaxBigM\', \'FuncPieceError\': \'FuncPieceError\', \'FuncPieceLength\': \'FuncPieceLength\', \'FuncPieceRatio\': \'FuncPieceRatio\', \'FuncPieces\': \'FuncPieces\', \'FuncMaxVal\': \'FuncMaxVal\', \'IISMethod\': \'IISMethod\', \'JSONSolDetail\': \'JSONSolDetail\', \'LazyConstraints\': \'LazyConstraints\', \'LogFile\': \'LogFile\', \'LogToConsole\': \'LogToConsole\', \'Method\': \'Method\', \'NumericFocus\': \'NumericFocus\', \'MultiObjMethod\': \'MultiObjMethod\', \'MultiObjPre\': \'MultiObjPre\', \'IgnoreNames\': \'IgnoreNames\', \'ObjNumber\': \'ObjNumber\', \'OutputFlag\': \'OutputFlag\', \'PreCrush\': \'PreCrush\', \'PreDepRow\': \'PreDepRow\', \'PreDual\': \'PreDual\', \'PrePasses\': \'PrePasses\', \'PreQLinearize\': \'PreQLinearize\', \'Presolve\': \'Presolve\', \'PreSOS1BigM\': \'PreSOS1BigM\', \'PreSOS2BigM\': \'PreSOS2BigM\', \'PreSparsify\': \'PreSparsify\', \'PreMIQCPForm\': \'PreMIQCPForm\', \'Record\': \'Record\', \'ResultFile\': \'ResultFile\', \'ScenarioNumber\': \'ScenarioNumber\', \'Seed\': \'Seed\', \'StartNodeLimit\': \'StartNodeLimit\', \'StartNumber\': \'StartNumber\', \'Threads\': \'Threads\', \'UpdateMode\': \'UpdateMode\', \'__dict__\': <attribute \'__dict__\' of \'ParamConstClass\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'ParamConstClass\' objects>})'


class QConstr(object):
    """
    Gurobi quadratic constraint object.  Quadratic constraints have
      several attribute...
    """
    def getAttr(self, attrname): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getAttr(attrname)
        
            PURPOSE:
              Request the value of a quadratic constraint attribute.
        
            ARGUMENTS:
              attrname (string): The name of the requested attribute.
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              print(qc.getAttr("QCname"))
        
            NOTES:
              Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass

    def setAttr(self, attrname, newvalue): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setAttr(attrname, newvalue)
        
            PURPOSE:
              Change the value of a quadratic constraint attribute.
        
            ARGUMENTS:
              attrname (string): The name of the attribute.
              newvalue: The desired new value.  The type of the value should be
                        compatible with the attribute type (e.g., an integer parameter
                        will take an integer value).
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              qc.setAttr("QCname", "New name")
        
            NOTES:
              Constraint attributes that can be set are:
                QCname:  Constraint name.
                QCsense: Constraint sense.
                QCrhs:   Right-hand side value.
        
              Attributes changes are handled in a lazy fashion.  The effect of a
              change isn't visible until after the next call to Model.update() or
              Model.optimize().
        """
        pass

    def __cindex__(self, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    typeenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__doc__': '\\n  Gurobi quadratic constraint object.  Quadratic constraints have\\n  several attribute...\\n  ', '__init__': <cyfunction QConstr.__init__ at 0x00000248A6069B10>, '__dir__': <cyfunction QConstr.__dir__ at 0x00000248A6069BC8>, '__cindex__': <cyfunction QConstr.__cindex__ at 0x00000248A6069C80>, '__repr__': <cyfunction QConstr.__repr__ at 0x00000248A6069D38>, 'typename': <property object at 0x00000248A6067688>, 'typeenum': <property object at 0x00000248A60676D8>, '__getattr__': <cyfunction QConstr.__getattr__ at 0x00000248A6069F60>, '__setattr__': <cyfunction QConstr.__setattr__ at 0x00000248A606B048>, 'getAttr': <cyfunction QConstr.getAttr at 0x00000248A606B100>, 'setAttr': <cyfunction QConstr.setAttr at 0x00000248A606B1B8>, '__dict__': <attribute '__dict__' of 'QConstr' objects>, '__weakref__': <attribute '__weakref__' of 'QConstr' objects>})"


class QuadExpr(object):
    # no doc
    def add(self, expr, mult=1.0): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              add(expr, mult=1.0)
        
            PURPOSE:
              Add a linear multiple of one expression into another.
        
            ARGUMENTS:
              expr (LinExpr or QuadExpr): The expression to add
              mult (float):               The linear multiplier
        
            EXAMPLE:
              expr1.add(expr2, 2.0)
        """
        pass

    def addConstant(self, constant): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addConstant(constant)
        
            PURPOSE:
              Add a constant into a quadratic expression.
        
            ARGUMENTS:
              constant (float): The value to add
        
            EXAMPLE:
              expr.addConstant(3.5)
        """
        pass

    def addTerms(self, coeffs, vars): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              addTerms(coeffs, vars)
              addTerms(coeffs, vars, vars2)
        
            PURPOSE:
              Add a list of terms, either linear or quadratic, into a quadratic
              expression.
        
            ARGUMENTS:
              coeffs (list of float): The coefficients for the new terms
              vars (list of Var):     The variables for the new terms
              vars2 (list of Var):    The variables for the new terms
        
            EXAMPLE:
              expr.addTerms(1.0, x)
              expr.addTerms(1.0, x, x)
              expr.addTerms([1.0, 2.0], [x, y])
              expr.addTerms([1.0, 2.0], [x, y], [x, y])
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              clear()
        
            PURPOSE:
              Set a linear expression to zero.
        
            EXAMPLE:
              print(expr.clear())
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              copy()
        
            PURPOSE:
              Copy a quadratic expression.
        
            EXAMPLE:
              expr2 = expr1.copy()
        """
        pass

    def getCoeff(self, i): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getCoeff(i)
        
            PURPOSE:
              Return the coefficient for the term at index 'i'.
        
            ARGUMENTS:
              i (Int): Index of term whose coefficient is requested
        
            RETURN VALUE:
              The requested coefficient.
        
            EXAMPLE:
              print(expr.getCoeff(i))
        """
        pass

    def getLinExpr(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getLinExpr()
        
            PURPOSE:
              Return the linear portion of a quadration expression (as a LinExpr
              object).
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              Linear expression.
        
            EXAMPLE:
              print(expr.getLinExpr())
        """
        pass

    def getValue(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getValue()
        
            PURPOSE:
              Compute the value of the expression, using the current solution.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              The computed expression value.
        
            EXAMPLE:
              print(model.getObjective().getValue())
        """
        pass

    def getVar1(self, i): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getVar1(i)
        
            PURPOSE:
              Return the first variable for the quadratic term at index 'i'.
        
            ARGUMENTS:
              i (Int): Index of quadratic term whose variable is requested
        
            RETURN VALUE:
              The requested variable.
        
            EXAMPLE:
              print(expr.getVar1(i))
        """
        pass

    def getVar2(self, i): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getVar2(i)
        
            PURPOSE:
              Return the second variable for the quadratic term at index 'i'.
        
            ARGUMENTS:
              i (Int): Index of quadratic term whose variable is requested
        
            RETURN VALUE:
              The requested variable.
        
            EXAMPLE:
              print(expr.getVar2(i))
        """
        pass

    def remove(self, which): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              remove(which)
        
            PURPOSE:
              Remove a quadratic term from the expression.
        
            ARGUMENTS:
              which: Term to remove.  Can be an Int, in which case the quadratic term
                     at index 'which' is removed, or a Var, in which case all quadratic
                     terms that involve the Var 'which' are removed.
        
            EXAMPLE:
              print(expr.remove(i))
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              size()
        
            PURPOSE:
              Return the number of quadratic terms in a quadratic expression.
        
            ARGUMENTS:
              None.
        
            RETURN VALUE:
              Number of terms in expression.
        
            EXAMPLE:
              print(expr.size())
        """
        pass

    def _flatten(self, *args, **kwargs): # real signature unknown
        pass

    def _mul(self, *args, **kwargs): # real signature unknown
        pass

    def _normalize(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


class SOS(object):
    """
    Gurobi SOS object.  SOS objects have a single attribute: IISSOS.
      When an IIS is available, this attribute indicates whether the
      SOS object participates in the IIS.
    """
    def getAttr(self, attrname): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getAttr(attrname)
        
            PURPOSE:
              Request the value of an SOS attribute.
        
            ARGUMENTS:
              attrname (string): The name of the requested attribute.
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              print(sos.getAttr("IISSOS"))
        
            NOTES:
              Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass

    def __cindex__(self, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    typeenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__doc__': '\\n  Gurobi SOS object.  SOS objects have a single attribute: IISSOS.\\n  When an IIS is available, this attribute indicates whether the\\n  SOS object participates in the IIS.\\n  ', '__init__': <cyfunction SOS.__init__ at 0x00000248A6069550>, '__dir__': <cyfunction SOS.__dir__ at 0x00000248A6069608>, '__cindex__': <cyfunction SOS.__cindex__ at 0x00000248A60696C0>, '__repr__': <cyfunction SOS.__repr__ at 0x00000248A6069778>, 'typename': <property object at 0x00000248A6067598>, 'typeenum': <property object at 0x00000248A60675E8>, '__getattr__': <cyfunction SOS.__getattr__ at 0x00000248A60699A0>, 'getAttr': <cyfunction SOS.getAttr at 0x00000248A6069A58>, '__dict__': <attribute '__dict__' of 'SOS' objects>, '__weakref__': <attribute '__weakref__' of 'SOS' objects>})"


class StatusConstClass(object):
    """
    Gurobi optimization status codes (e.g., model.status == GRB.OPTIMAL):
    
        LOADED: Model loaded, but no solution information available
        OPTIMAL: Solve to optimality (subject to tolerances)
        INFEASIBLE: Model is infeasible
        INF_OR_UNBD: Model is either infeasible or unbounded
        UNBOUNDED: Model is unbounded
        CUTOFF: Objective is worse than specified cutoff value
        ITERATION_LIMIT: Optimization terminated due to iteration limit
        NODE_LIMIT: Optimization terminated due to node limit
        TIME_LIMIT: Optimization terminated due to time limit
        SOLUTION_LIMIT: Optimization terminated due to solution limit
        INTERRUPTED: User interrupted optimization
        NUMERIC: Optimization terminated due to numerical issues
        SUBOPTIMAL: Optimization terminated with a sub-optimal solution
        INPROGRESS: Optimization currently in progress
        USER_OBJ_LIMIT: Achieved user objective limit
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CUTOFF = 6
    INFEASIBLE = 3
    INF_OR_UNBD = 4
    INPROGRESS = 14
    INTERRUPTED = 11
    ITERATION_LIMIT = 7
    LOADED = 1
    NODE_LIMIT = 8
    NUMERIC = 12
    OPTIMAL = 2
    SOLUTION_LIMIT = 10
    SUBOPTIMAL = 13
    TIME_LIMIT = 9
    UNBOUNDED = 5
    USER_OBJ_LIMIT = 15
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__doc__': '\\n  Gurobi optimization status codes (e.g., model.status == GRB.OPTIMAL):\\n\\n    LOADED: Model loaded, but no solution information available\\n    OPTIMAL: Solve to optimality (subject to tolerances)\\n    INFEASIBLE: Model is infeasible\\n    INF_OR_UNBD: Model is either infeasible or unbounded\\n    UNBOUNDED: Model is unbounded\\n    CUTOFF: Objective is worse than specified cutoff value\\n    ITERATION_LIMIT: Optimization terminated due to iteration limit\\n    NODE_LIMIT: Optimization terminated due to node limit\\n    TIME_LIMIT: Optimization terminated due to time limit\\n    SOLUTION_LIMIT: Optimization terminated due to solution limit\\n    INTERRUPTED: User interrupted optimization\\n    NUMERIC: Optimization terminated due to numerical issues\\n    SUBOPTIMAL: Optimization terminated with a sub-optimal solution\\n    INPROGRESS: Optimization currently in progress\\n    USER_OBJ_LIMIT: Achieved user objective limit\\n  ', '__setattr__': <cyfunction StatusConstClass.__setattr__ at 0x00000248A608E100>, 'LOADED': 1, 'OPTIMAL': 2, 'INFEASIBLE': 3, 'INF_OR_UNBD': 4, 'UNBOUNDED': 5, 'CUTOFF': 6, 'ITERATION_LIMIT': 7, 'NODE_LIMIT': 8, 'TIME_LIMIT': 9, 'SOLUTION_LIMIT': 10, 'INTERRUPTED': 11, 'NUMERIC': 12, 'SUBOPTIMAL': 13, 'INPROGRESS': 14, 'USER_OBJ_LIMIT': 15, '__dict__': <attribute '__dict__' of 'StatusConstClass' objects>, '__weakref__': <attribute '__weakref__' of 'StatusConstClass' objects>})"


class TempConstr(object):
    """
    Gurobi temporary constraint object.  Objects of this class are created
      as intermediate results when building constraints using overloaded
      operators.
    """
    def __bool__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __nonzero__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__doc__': '\\n  Gurobi temporary constraint object.  Objects of this class are created\\n  as intermediate results when building constraints using overloaded\\n  operators.\\n  ', '__init__': <cyfunction TempConstr.__init__ at 0x00000248A606B9A0>, '__repr__': <cyfunction TempConstr.__repr__ at 0x00000248A606BA58>, '__rshift__': <cyfunction TempConstr.__rshift__ at 0x00000248A606BB10>, '__le__': <cyfunction TempConstr.__le__ at 0x00000248A606BBC8>, '__ge__': <cyfunction TempConstr.__ge__ at 0x00000248A606BC80>, '__bool__': <cyfunction TempConstr.__bool__ at 0x00000248A606BD38>, '__nonzero__': <cyfunction TempConstr.__nonzero__ at 0x00000248A606BDF0>, '__dict__': <attribute '__dict__' of 'TempConstr' objects>, '__weakref__': <attribute '__weakref__' of 'TempConstr' objects>})"


class tupledict(dict):
    """
    Custom Gurobi class: tupledict is a subclass of dict where
      the keys are a tuplelist.
    """
    def clean(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, *args, **kwargs): # real signature unknown
        pass

    def iteritems(self, *args, **kwargs): # real signature unknown
        pass

    def iterkeys(self, *args, **kwargs): # real signature unknown
        pass

    def itervalues(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def popitem(self, *args, **kwargs): # real signature unknown
        pass

    def prod(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def setord(self, *args, **kwargs): # real signature unknown
        pass

    def subset(self, *args, **kwargs): # real signature unknown
        pass

    def sum(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def values(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gurobipy', '__doc__': '\\n  Custom Gurobi class: tupledict is a subclass of dict where\\n  the keys are a tuplelist.\\n  ', '__init__': <cyfunction tupledict.__init__ at 0x00000248A608E1B8>, 'clean': <cyfunction tupledict.clean at 0x00000248A608E270>, 'setord': <cyfunction tupledict.setord at 0x00000248A608E328>, 'keys': <cyfunction tupledict.keys at 0x00000248A608E3E0>, 'iteritems': <cyfunction tupledict.iteritems at 0x00000248A608E498>, 'iterkeys': <cyfunction tupledict.iterkeys at 0x00000248A608E550>, 'itervalues': <cyfunction tupledict.itervalues at 0x00000248A608E608>, 'values': <cyfunction tupledict.values at 0x00000248A608E6C0>, 'items': <cyfunction tupledict.items at 0x00000248A608E778>, '__iter__': <cyfunction tupledict.__iter__ at 0x00000248A608E830>, 'subset': <cyfunction tupledict.subset at 0x00000248A608E8E8>, 'select': <cyfunction tupledict.select at 0x00000248A608E9A0>, 'sum': <cyfunction tupledict.sum at 0x00000248A608EA58>, 'prod': <cyfunction tupledict.prod at 0x00000248A608EB10>, '__delitem__': <cyfunction tupledict.__delitem__ at 0x00000248A608EBC8>, '__setitem__': <cyfunction tupledict.__setitem__ at 0x00000248A608EC80>, 'clear': <cyfunction tupledict.clear at 0x00000248A608ED38>, 'pop': <cyfunction tupledict.pop at 0x00000248A608EDF0>, 'popitem': <cyfunction tupledict.popitem at 0x00000248A608EEA8>, 'update': <cyfunction tupledict.update at 0x00000248A608EF60>, '__dict__': <attribute '__dict__' of 'tupledict' objects>, '__weakref__': <attribute '__weakref__' of 'tupledict' objects>})"


class tuplelist(list):
    """
    Custom Gurobi class: tuplelist is a subclass of list that is
      designed to work with lists of tuples.  Using the select()
      method, this class allows you to efficiently select sub-lists of
      tuples by matching specific values in specific fields of the
      member tuples.
    
      For example:
        > l = tuplelist([(1, 2), (1, 3), (2, 3), (2, 4)])
        > print(l.select('*', '*'))
        [(1, 2), (1, 3), (2, 3), (2, 4)]
        > print(l.select('*', 3))
        [(1, 3), (2, 3)]
        > print(l.select(1, '*'))
        [(1, 2), (1, 3)]
    """
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def clean(self): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              clean()
        
            PURPOSE:
              The tuplelist class achieves it efficiency by building
              indices.  These indices are stored inside tuplelist
              objects, and they consume memory.  Call clean()
              if you wish to reclaim this memory.
        
            ARGUMENTS:
              None
        
            RETURN VALUE:
              None.
        
            EXAMPLE:
              l.clean()
        """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def nextc(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def prev(self, *args, **kwargs): # real signature unknown
        pass

    def prevc(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, value1, value2, *more): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              select(value1, value2, ...)
        
            PURPOSE:
              Selects a sub-list from a tuplelist.  All tuples that
              match the specified arguments in the corresponding fields
              are returned.  You can pass the string '*' (with the quotes)
              to indicate that any value is acceptable in the corresponding
              field.
        
            ARGUMENTS:
              value1: Value to match with first tuple member.
              value2: Value to match with second tuple member.
              ...
        
            RETURN VALUE:
              The matching sub-list.
        
            EXAMPLE:
              m = l.select('*', 1, '*', 'a')
        """
        pass

    def _tuplelist__makeindex(self, *args, **kwargs): # real signature unknown
        pass

    def _tuplelist__repl(self, *args, **kwargs): # real signature unknown
        pass

    def _tuplelist__scalaraddcheck(self, *args, **kwargs): # real signature unknown
        pass

    def _tuplelist__scalardelcheck(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, val): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              __contains__(val)
        
            PURPOSE:
              Determines if the specified value is contained in the tuplelist.
              This is faster than the parent method when calling "in" within
              a loop.
        
            ARGUMENTS:
              val: Value to match.
        
            RETURN VALUE:
              True if the values are in the list.
        
            EXAMPLE:
              if (1,2,3) in l
        """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __delslice__(self, *args, **kwargs): # real signature unknown
        pass

    def __getslice__(self, *args, **kwargs): # real signature unknown
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': "\\n  Custom Gurobi class: tuplelist is a subclass of list that is\\n  designed to work with lists of tuples.  Using the select()\\n  method, this class allows you to efficiently select sub-lists of\\n  tuples by matching specific values in specific fields of the\\n  member tuples.\\n\\n  For example:\\n    > l = tuplelist([(1, 2), (1, 3), (2, 3), (2, 4)])\\n    > print(l.select(\'*\', \'*\'))\\n    [(1, 2), (1, 3), (2, 3), (2, 4)]\\n    > print(l.select(\'*\', 3))\\n    [(1, 3), (2, 3)]\\n    > print(l.select(1, \'*\'))\\n    [(1, 2), (1, 3)]\\n  ", \'_tuplelist__repl\': <staticmethod object at 0x00000248A6077F28>, \'__init__\': <cyfunction tuplelist.__init__ at 0x00000248A6090100>, \'prev\': <cyfunction tuplelist.prev at 0x00000248A60901B8>, \'prevc\': <cyfunction tuplelist.prevc at 0x00000248A6090270>, \'next\': <cyfunction tuplelist.next at 0x00000248A6090328>, \'nextc\': <cyfunction tuplelist.nextc at 0x00000248A60903E0>, \'_tuplelist__scalardelcheck\': <cyfunction tuplelist.__scalardelcheck at 0x00000248A6090498>, \'_tuplelist__scalaraddcheck\': <cyfunction tuplelist.__scalaraddcheck at 0x00000248A6090550>, \'__repr__\': <cyfunction tuplelist.__repr__ at 0x00000248A6090608>, \'clean\': <cyfunction tuplelist.clean at 0x00000248A60906C0>, \'select\': <cyfunction tuplelist.select at 0x00000248A6090778>, \'__contains__\': <cyfunction tuplelist.__contains__ at 0x00000248A6090830>, \'_tuplelist__makeindex\': <cyfunction tuplelist.__makeindex at 0x00000248A60908E8>, \'append\': <cyfunction tuplelist.append at 0x00000248A60909A0>, \'extend\': <cyfunction tuplelist.extend at 0x00000248A6090A58>, \'insert\': <cyfunction tuplelist.insert at 0x00000248A6090B10>, \'pop\': <cyfunction tuplelist.pop at 0x00000248A6090BC8>, \'remove\': <cyfunction tuplelist.remove at 0x00000248A6090C80>, \'__delitem__\': <cyfunction tuplelist.__delitem__ at 0x00000248A6090D38>, \'__delslice__\': <cyfunction tuplelist.__delslice__ at 0x00000248A6090DF0>, \'__add__\': <cyfunction tuplelist.__add__ at 0x00000248A6090EA8>, \'__iadd__\': <cyfunction tuplelist.__iadd__ at 0x00000248A6090F60>, \'__getslice__\': <cyfunction tuplelist.__getslice__ at 0x00000248A6091048>, \'__dict__\': <attribute \'__dict__\' of \'tuplelist\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'tuplelist\' objects>})'


class Var(object):
    """
    Gurobi variable object.  Variables have a number of attributes.
      Some can be set (e.g., v.ub = 0.0), while others can only be queried
      (e.g., print(v.x)). The most commonly used variable attributes are:
        obj: Linear objective coefficient.
        lb: Lower bound.
        ub: Upper bound.
        varName: Variable name.
        vType: Variable type ('C', 'B', 'I', 'S', or 'N').
        x: Solution value.
        rc: Solution reduced cost.
        xn: Solution value in an alternate MIP solution.
    
      Type "help(GRB.attr)" for a list of all available attributes.
    
      Note that attribute modifications are handled in a lazy fashion.  You
      won't see the effect of a change until after the next call to Model.update()
      or Model.optimize().
    """
    def getAttr(self, attrname): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              getAttr(attrname)
        
            PURPOSE:
              Request the value of a variable attribute.
        
            ARGUMENTS:
              attrname (string): The name of the requested attribute.
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              print(var.getAttr("varName"))
        
            NOTES:
              Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass

    def sameAs(self, othervar): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              sameAs(othervar)
        
            PURPOSE:
              Indicates whether two variable objects refer to the same Gurobi model
              variable.  You should use this instead of the '==' operator, since
              '==' is used to create linear constraints.
        
            ARGUMENTS:
              othervar (Var): The variable to compare against.
        
            RETURN VALUE:
              True if both Var objects refer to the same model variable.
        
            EXAMPLE:
              var1.sameAs(var2)
        """
        pass

    def setAttr(self, attrname, newvalue): # real signature unknown; restored from __doc__
        """
        ROUTINE:
              setAttr(attrname, newvalue)
        
            PURPOSE:
              Change the value of a variable attribute.
        
            ARGUMENTS:
              attrname (string): The name of the attribute.
              newvalue: The desired new value.  The type of the value should be
                        compatible with the attribute type (e.g., an integer parameter
                        will take an integer value).
        
            RETURN VALUE:
              The attribute value.
        
            EXAMPLE:
              var.setAttr("varName", "New name")
        
            NOTES:
              Variable attributes that can be set are:
                VarName:  Name of the variable.
                lb:       Lower bound.
                ub:       Upper bound.
                obj:      Objective coefficient.
                vType:    Variable type ('C', 'B', 'I', 'S', or 'N').
        
              Attributes changes are handled in a lazy fashion.  The effect of a
              change isn't visible until after the next call to Model.update() or
              Model.optimize().
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __cindex__(self, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __div__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __numcols__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    PROPERTY:
      index

    PURPOSE:
      Request the index of the variable in the model.

    RETURN VALUE:
      = -2: removed
      = -1: not in model
      >= 0: index of the variable in the model

    EXAMPLE:
      print(var.index)
    """

    typeenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gurobipy\', \'__doc__\': \'\\n  Gurobi variable object.  Variables have a number of attributes.\\n  Some can be set (e.g., v.ub = 0.0), while others can only be queried\\n  (e.g., print(v.x)). The most commonly used variable attributes are:\\n    obj: Linear objective coefficient.\\n    lb: Lower bound.\\n    ub: Upper bound.\\n    varName: Variable name.\\n    vType: Variable type (\\\'C\\\', \\\'B\\\', \\\'I\\\', \\\'S\\\', or \\\'N\\\').\\n    x: Solution value.\\n    rc: Solution reduced cost.\\n    xn: Solution value in an alternate MIP solution.\\n\\n  Type "help(GRB.attr)" for a list of all available attributes.\\n\\n  Note that attribute modifications are handled in a lazy fashion.  You\\n  won\\\'t see the effect of a change until after the next call to Model.update()\\n  or Model.optimize().\\n  \', \'__init__\': <cyfunction Var.__init__ at 0x00000248A606E608>, \'__dir__\': <cyfunction Var.__dir__ at 0x00000248A606E6C0>, \'__hash__\': <cyfunction Var.__hash__ at 0x00000248A606E778>, \'__cindex__\': <cyfunction Var.__cindex__ at 0x00000248A606E830>, \'__repr__\': <cyfunction Var.__repr__ at 0x00000248A606E8E8>, \'__numcols__\': <cyfunction Var.__numcols__ at 0x00000248A606E9A0>, \'typename\': <property object at 0x00000248A60672C8>, \'typeenum\': <property object at 0x00000248A6067318>, \'__getattr__\': <cyfunction Var.__getattr__ at 0x00000248A606EBC8>, \'__setattr__\': <cyfunction Var.__setattr__ at 0x00000248A606EC80>, \'getAttr\': <cyfunction Var.getAttr at 0x00000248A606ED38>, \'setAttr\': <cyfunction Var.setAttr at 0x00000248A606EDF0>, \'index\': <property object at 0x00000248A60673B8>, \'sameAs\': <cyfunction Var.sameAs at 0x00000248A606EF60>, \'__le__\': <cyfunction Var.__le__ at 0x00000248A606A048>, \'__ge__\': <cyfunction Var.__ge__ at 0x00000248A606A100>, \'__eq__\': <cyfunction Var.__eq__ at 0x00000248A606A1B8>, \'__ne__\': <cyfunction Var.__ne__ at 0x00000248A606A270>, \'__add__\': <cyfunction Var.__add__ at 0x00000248A606A328>, \'__radd__\': <cyfunction Var.__radd__ at 0x00000248A606A3E0>, \'__iadd__\': <cyfunction Var.__iadd__ at 0x00000248A606A498>, \'__sub__\': <cyfunction Var.__sub__ at 0x00000248A606A550>, \'__rsub__\': <cyfunction Var.__rsub__ at 0x00000248A606A608>, \'__isub__\': <cyfunction Var.__isub__ at 0x00000248A606A6C0>, \'__mul__\': <cyfunction Var.__mul__ at 0x00000248A606A778>, \'__rmul__\': <cyfunction Var.__rmul__ at 0x00000248A606A830>, \'__imul__\': <cyfunction Var.__imul__ at 0x00000248A606A8E8>, \'__div__\': <cyfunction Var.__div__ at 0x00000248A606A9A0>, \'__truediv__\': <cyfunction Var.__truediv__ at 0x00000248A606AA58>, \'__neg__\': <cyfunction Var.__neg__ at 0x00000248A606AB10>, \'__dict__\': <attribute \'__dict__\' of \'Var\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Var\' objects>})'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000248A604CD68>'

__modelmap = {}

__pyx_capi__ = {
    'callbackstub': None, # (!) real value is '<capsule object "int (__stdcall )(void *, void *, int, void *)" at 0x00000248A6029720>'
    'logcallbackstub': None, # (!) real value is '<capsule object "int (__stdcall )(char *)" at 0x00000248A6029750>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gurobipy.gurobipy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000248A604CD68>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gurobipy\\\\gurobipy.pyd')"

__test__ = {}

