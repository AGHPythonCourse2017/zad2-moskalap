class Task:


    def __init__(self, init_code, clean_up_code, example_invoke):
        if init_code[-3:] == '.py': #probalby this is file path
            init_code = open(init_code, 'r').read()
        if example_invoke[-3:] == '.py': #probalby this is file path
            example_invoke = open(example_invoke, 'r').read()
        if clean_up_code[-3:] == '.py': #probalby this is file path
            clean_up_code = open(clean_up_code, 'r').read()


        if '__N__' not in init_code and '__N__' not in example_invoke:
            from cmptcomplexity.scripts.exceptions import ArgumentPatternError
            raise ArgumentPatternError('There is no "__N__" to scale an problem size!')
        self.init_code = init_code
        self.example_invoke = example_invoke
        self.clean_up_code = clean_up_code

    def stringify_init(self, N):
        return self.init_code.replace('__N__',str(N))

    def stringify_clean_up(self, N):
        return self.clean_up_code.replace('__N__',str(N))

    def stringify_example_invoke(self, N):
        return self.example_invoke.replace('__N__',str(N))














