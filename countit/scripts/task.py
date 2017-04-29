class Task:

    class Arguments:
        def __init__(self, example_string):
            self.args_list = example_string.split(', ')
            from countit.exceptions import ArgumentPatternError
            if ',' in example_string.split():
                raise ArgumentPatternError('Wrong format of example args string(" , ")')
            if '_N_' not in self.args_list:

                raise ArgumentPatternError('There is no "_N_" in string')
            else:
                self.problem_size = self.args_list.index('_N_')

        def to_string(self, N):
            self.args_list[self.problem_size] = str(N)
            return ", ".join(self.args_list)

    def __init__(self, initialization, analzyable, clean_up):


        beg = analzyable.find('(')
        end = analzyable.rfind(')')
        from countit.exceptions import AnalyzablePatternError
        if beg == -1:
            raise AnalyzablePatternError('There is no (')
        if end == -1:
            raise AnalyzablePatternError('There is no )')
        if beg>end:
            raise AnalyzablePatternError(') .... (')

        self.argument = self.Arguments(analzyable[beg+1 : end])









