from codeToPyListener import codeToPyListener
from codeToPyParser import *

class TraduceCode(codeToPyListener):

    def __init__(self):
        # Open the output file in write mode
        self.output_file = open('output1.py', 'w')
        self.indentation_level = 0
        # Redirect print to the file
        sys.stdout = self.output_file
    # Enter a parse tree produced by codeToPyParser#inicio.
    def enterInicio(self, ctx:codeToPyParser.InicioContext):
        pass

    # Exit a parse tree produced by codeToPyParser#inicio.
    def exitInicio(self, ctx:codeToPyParser.InicioContext):
        pass


    # Enter a parse tree produced by codeToPyParser#declaracionFuncion.
    def enterDeclaracionFuncion(self, ctx:codeToPyParser.DeclaracionFuncionContext):    
            if not hasattr(ctx, 'processed'):
                ctx.processed = True    
                open_paren_printed = False
                for child in ctx.getChildren():
                    # Verificar si es un nodo terminal (token)
                    if isinstance(child, TerminalNode):
                        
                        if child.symbol.type == codeToPyParser.HACER:
                            print("def ", end="")  # Convertir 'hacer' a 'def'
                        elif child.symbol.type == codeToPyParser.ID:
                            # Imprimir el nombre de la función (ID), sin el asterisco
                            print(f"{child.getText()}", end="")
                            
                        elif child.symbol.type == codeToPyParser.SEPARADOR:
                            # Si no se ha abierto el paréntesis, lo abrimos
                            if not open_paren_printed:
                                print("(", end="")  # Iniciar lista de parámetros
                                open_paren_printed = True
                    else:
                        # Manejar los nodos no terminales (como el contexto de los parámetros)
                        if isinstance(child, codeToPyParser.ParametrosContext):
                            parametros= self.enterParametros(child)
                            print(", ".join(parametros), end="")
                if open_paren_printed:
                    print("):")  # Cerrar paréntesis y línea


    # Enter a parse tree produced by codeToPyParser#parametros.
    def enterParametros(self, ctx:codeToPyParser.ParametrosContext):
           
        if not hasattr(ctx, 'processed'):
            ctx.processed = True    
            parametros = []
            for child in ctx.getChildren():
                if isinstance(child, TerminalNode):
                    if child.symbol.type == codeToPyParser.ID:
                        parametros.append(child.getText())
            return parametros


        # Enter a parse tree produced by codeToPyParser#bloque.
    def enterBloque(self, ctx: codeToPyParser.BloqueContext):
        for statement in ctx.getChildren():
            # Indent based on the current block depth
            print(" " * self.indentation_level, end="")  # Apply indentation

            if isinstance(statement, TerminalNode):
                if statement.symbol.type == codeToPyParser.LBRACE:
                    print("", end="")  # Print the opening brace and newline
                    self.indentation_level += 1  # Increase indentation for inner block
                elif statement.symbol.type == codeToPyParser.RBRACE:
                    self.indentation_level -= 1  # Decrease indentation when closing a block
                    print("    " * self.indentation_level, end="")  # Adjust indentation before closing brace
                    print("\n", end="")  # Print the closing brace
            else:
                if isinstance(statement, codeToPyParser.InstruccionContext):
                    print("\n")
                    self.enterInstruccion(statement)  # Process individual instructions


    # Enter a parse tree produced by codeToPyParser#instruccion.
    def enterInstruccion(self, ctx: codeToPyParser.InstruccionContext):
        if not hasattr(ctx, 'processed'):
            # Indent based on the current block depth
            print("     " * self.indentation_level, end="")
            ctx.processed = True

            for statement in ctx.getChildren():
                if isinstance(statement, TerminalNode):
                    if statement.symbol.type == codeToPyParser.SEMICOLON:
                        pass
                    elif statement.symbol.type == codeToPyParser.DEVOLVER:
                        print("return ", end="")
                else:
                    if isinstance(statement, codeToPyParser.CicloContext):
                        self.enterCiclo(statement)  # Handle loops (ciclo)
                    elif isinstance(statement, codeToPyParser.MostrarContext):
                        self.enterMostrar(statement)
                    elif isinstance(statement, codeToPyParser.CondicionContext):
                        self.enterCondicion(statement)  # Handle conditions
                    elif isinstance(statement, codeToPyParser.DeclaracionVariableContext):
                        self.enterDeclaracionVariable(statement)
                    elif isinstance(statement, codeToPyParser.ExpresionContext):
                        self.enterExpresion(statement)  # Handle conditions


    # Exit a parse tree produced by codeToPyParser#instruccion.
    def exitInstruccion(self, ctx:codeToPyParser.InstruccionContext):
        pass


        # Enter a parse tree produced by codeToPyParser#ciclo.
    def enterCiclo(self, ctx: codeToPyParser.CicloContext):
        if not hasattr(ctx, 'processed'):
            ctx.processed = True
            numero_rep=child=""
            for child in ctx.getChildren():
                if isinstance(child, TerminalNode):
                    if child.symbol.type == codeToPyParser.REPETIR:
                        print("for i in range(1, ", end="")  # Start the loop in Python
                    elif child.symbol.type == codeToPyParser.ID:
                        numero_rep=child.getText() 
                    elif child.symbol.type == codeToPyParser.NUMERO:
                        numero_rep=child.getText() # Number of repetitions
                        
                    elif child.symbol.text == 'veces':
                        if(numero_rep):
                            print("1, " + str(numero_rep) + " + 1", end="):")
                        else:
                            print("):")
                        self.indentation_level += 1  # Increase indentation for the block inside the loop
                else:
                    if isinstance(child,codeToPyParser.ExpAritmeticaContext):
                        self.enterExpAritmetica(child)
                    if isinstance(child, codeToPyParser.BloqueContext):
                        self.enterBloque(child)  # Process the block inside the loop
                
            self.indentation_level -= 1  # Decrease indentation after the loop
            
    def enterMostrar(self, ctx:codeToPyParser.MostrarContext):
        if not hasattr(ctx, 'processed'):
            ctx.processed = True
            for child in ctx.getChildren():
                if(isinstance(child,TerminalNode)):
                    if child.symbol.type == codeToPyParser.MOSTRAR:
                        print("print(", end="")
                    elif child.symbol.type == codeToPyParser.SEMICOLON:
                        pass
                    elif child.symbol.type == codeToPyParser.ID:
                        print(child.getText(),end="")
                else:
                    if isinstance(child, codeToPyParser.CadenaConcatenadaContext):
                        self.enterCadenaConcatenada(child)
                        print(")", end="")
                    

    # Exit a parse tree produced by codeToPyParser#mostrar.
    def exitMostrar(self, ctx:codeToPyParser.MostrarContext):
        pass

    # Enter a parse tree produced by codeToPyParser#cadenaConcatenada.
    def enterCadenaConcatenada(self, ctx:codeToPyParser.CadenaConcatenadaContext):
         if not hasattr(ctx, 'processed'):
            print("" * self.indentation_level, end="") 
            ctx.processed = True      
            for child in ctx.getChildren():
                if isinstance(child, TerminalNode):
                    if child.symbol.type == codeToPyParser.STRING:
                        print(f'{child.getText()}', end="")
                    elif child.symbol.type == codeToPyParser.ID:
                        print(f'str({child.getText()})', end="")
                    elif child.symbol.type ==codeToPyParser.PLUS:
                        print(" + ",end="")

 
    # Enter a parse tree produced by codeToPyParser#condicion.
    def enterCondicion(self, ctx: codeToPyParser.CondicionContext):
        if not hasattr(ctx, 'processed'):
            ctx.processed = True     
            for child in ctx.getChildren():
                if isinstance(child, TerminalNode):
                    # Verifica el tipo de terminal (token) y procesa el contenido
                    if child.symbol.type == codeToPyParser.SI:
                        print("if ", end="")  # Comienza la condición con 'if'
                    elif child.symbol.type == codeToPyParser.SINO:
                        print("     " * self.indentation_level, end="") 
                        print("else:", end="")  # Agrega 'else:' en Python
                    elif child.symbol.type == codeToPyParser.LPAREN:
                        print("(", end="")  # Imprime el paréntesis de apertura
                    elif child.symbol.type == codeToPyParser.RPAREN:
                        print("):", end="\n")  # Imprime el paréntesis de cierre
                else:
                    # Procesa los bloques y expresiones
                    if isinstance(child, codeToPyParser.ExpresionContext):
                        self.enterExpresion(child)
                    elif isinstance(child, codeToPyParser.BloqueContext):
                      self.enterBloque(child) 

     # Enter a parse tree produced by codeToPyParser#accesoIndice.
    def enterAccesoIndice(self, ctx:codeToPyParser.AccesoIndiceContext):
         if not hasattr(ctx, 'processed'):
            ctx.processed = True 
            for child in ctx.getChildren():
                if isinstance(child, TerminalNode):
                    if child.symbol.type == codeToPyParser.ID:
                        print(child.getText(), end="")
                    elif child.symbol.type == codeToPyParser.LBRACKET:
                        print("[", end="")
                    elif child.symbol.type == codeToPyParser.RBRACKET:
                        print("]", end="")
                elif isinstance(child, codeToPyParser.ExpresionContext):
                    self.enterExpresion(child)

    # Enter a parse tree produced by codeToPyParser#declaracionVariable.
    def enterDeclaracionVariable(self, ctx: codeToPyParser.DeclaracionVariableContext):
        if not hasattr(ctx, 'processed'):
            ctx.processed = True

            for child in ctx.getChildren():
                if isinstance(child, TerminalNode):
                    if child.symbol.type in [codeToPyParser.BOOLEAN]:
                        boolean_value = child.getText()
                        if(boolean_value == 'true'):
                            print('True', end="")
                        elif(boolean_value =='false'):
                            print('False',end="")
                    elif child.symbol.type == codeToPyParser.IGUAL:
                        print( " = " ,end="")
                    elif child.symbol.type in [codeToPyParser.NUMERO]:
                        print(child.getText(), end="")
                        print("\n", end="")
                    elif child.symbol.type in [codeToPyParser.STRING]:
                        print(child.getText(), end="")
                        print("\n", end="")
                    elif child.symbol.type in [codeToPyParser.FLOAT]:
                        print(child.getText(), end="")
                        print("\n", end="")
                    elif child.symbol.type == codeToPyParser.ID:
                        print(child.getText(), end="")
                elif isinstance(child, codeToPyParser.ExpresionContext):
                    self.enterExpresion(child)
                elif isinstance(child,codeToPyParser.LlamadaFuncionContext):
                    self.enterLlamadaFuncion(child)
                elif isinstance(child,codeToPyParser.ListaContext):
                    self.enterLista(child)


    # Exit a parse tree produced by codeToPyParser#declaracionVariable.
    def exitDeclaracionVariable(self, ctx:codeToPyParser.DeclaracionVariableContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expresion.
    def enterExpresion(self, ctx: codeToPyParser.ExpresionContext):
         
            if ctx.condicionLogica():
                # Call a method to handle logical conditions
                self.enterCondicionLogica(ctx.condicionLogica())
            elif ctx.comparacion():
                # Call a method to handle comparisons 
                self.enterComparacion(ctx.comparacion())
            elif ctx.expAritmetica():
                # Call a method to handle arithmetic expressions
                self.enterExpAritmetica(ctx.expAritmetica())
                

    # Exit a parse tree produced by codeToPyParser#expresion.
    def exitExpresion(self, ctx:codeToPyParser.ExpresionContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expAritmetica.
    def enterExpAritmetica(self, ctx:codeToPyParser.ExpAritmeticaContext):
        if not hasattr(ctx, 'processed'):
            ctx.processed = True  
            for statement in ctx.getChildren():
                if isinstance(statement, TerminalNode):
                    if statement.symbol.type == codeToPyParser.PLUS:
                        print(" + ",end="")
                    elif statement.symbol.type == codeToPyParser.SUB:
                        print(" - ", end="")
                    elif statement.symbol.type == codeToPyParser.MOD:
                        print(f" % ", end="")  
                else:
                    if isinstance(statement,codeToPyParser.ExpTerminoContext):
                        self.enterExpTermino(statement) 

    # Exit a parse tree produced by codeToPyParser#expAritmetica.
    def exitExpAritmetica(self, ctx:codeToPyParser.ExpAritmeticaContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expTermino.
    def enterExpTermino(self, ctx:codeToPyParser.ExpTerminoContext):
          if not hasattr(ctx, 'processed'):
            ctx.processed = True   
            for statement in ctx.getChildren():
                if isinstance(statement, TerminalNode):
                    if statement.symbol.type== codeToPyParser.MUL:
                        print(" * ", end="")
                    elif statement.symbol.type== codeToPyParser.DIVIDE:
                        print(" / ", end="")
                else:
                    if isinstance(statement, codeToPyParser.ExpFactorContext):
                        self.enterExpFactor(statement)
            

    # Exit a parse tree produced by codeToPyParser#expTermino.
    def exitExpTermino(self, ctx:codeToPyParser.ExpTerminoContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expFactor.
    def enterExpFactor(self, ctx: codeToPyParser.ExpFactorContext):
         if not hasattr(ctx, 'processed'):
            ctx.processed = True     
            if ctx.expPotencia():
                self.enterExpPotencia(ctx.expPotencia())
            elif ctx.expRaiz():
                self.enterExpRaiz(ctx.expRaiz())
            elif ctx.NUMERO():
                print(ctx.NUMERO().getText(), end="")
            elif ctx.FLOAT():
                print(ctx.FLOAT().getText(), end="")
            elif ctx.ID():
                print(ctx.ID().getText(), end="")
            elif ctx.LPAREN():
                print("(", end="")
                if ctx.ExpAritmetica():
                    self.enterExpAritmetica(ctx.ExpAritmetica())
                print(")", end="")
            elif ctx.accesoIndice():
                self.enterAccesoIndice(ctx.accesoIndice())

    # Exit a parse tree produced by codeToPyParser#expFactor.
    def exitExpFactor(self, ctx:codeToPyParser.ExpFactorContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expPotencia.
    def enterExpPotencia(self, ctx:codeToPyParser.ExpPotenciaContext):
          if not hasattr(ctx, 'processed'):
            ctx.processed = True    
            for statement in ctx.getChildren():
                if isinstance(statement, TerminalNode):
                    if statement.symbol.type== codeToPyParser.EXPONENT():
                        print(statement.getText(), end="")
                else:
                    if isinstance(statement, codeToPyParser.ExpRaizContext):
                        self.enterExpRaiz(statement)

    # Exit a parse tree produced by codeToPyParser#expPotencia.
    def exitExpPotencia(self, ctx:codeToPyParser.ExpPotenciaContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expRaiz.
    def enterExpRaiz(self, ctx: codeToPyParser.ExpRaizContext):
          if not hasattr(ctx, 'processed'):
            ctx.processed = True    
            for statement in ctx.getChildren():
                if isinstance(statement, TerminalNode):
                    if statement.symbol.type == codeToPyParser.NUMERO:
                        print(statement.getText(), end="")
                    elif statement.symbol.type == codeToPyParser.FLOAT:
                        print(statement.getText(), end="")
                    elif statement.symbol.type == codeToPyParser.SQRT:
                        print("sqrt(", end="") 
                        if ctx.getChildCount() > 2:
                            self.enterExpAritmetica(ctx.getChild(2))
                        print(")", end="")
                elif statement.symbol.type == codeToPyParser.LPAREN:
                    print("(", end="")
                    if ctx.getChildCount() > 1:
                        self.enterExpAritmetica(ctx.getChild(1))
                    print(")", end="")

    # Exit a parse tree produced by codeToPyParser#expRaiz.
    def exitExpRaiz(self, ctx:codeToPyParser.ExpRaizContext):
        pass


    # Enter a parse tree produced by codeToPyParser#condicionLogica.
    def enterCondicionLogica(self, ctx:codeToPyParser.CondicionLogicaContext):
         if not hasattr(ctx, 'processed'):
            ctx.processed = True     
            for statement in ctx.getChildren():
                if isinstance(statement, TerminalNode):
                    if statement.symbol.type == codeToPyParser.Y:
                        print(" and ", end="") 
                    elif statement.symbol.type == codeToPyParser.O:
                        print(" or ", end="")
                elif isinstance(statement, codeToPyParser.TerminoContext):
                    self.enterTermino(statement)
    
    # Enter a parse tree produced by codeToPyParser#termino.
    def enterTermino(self, ctx:codeToPyParser.TerminoContext):
        if not hasattr(ctx, 'processed'):
            ctx.processed = True      
            if ctx.comparacion():
                self.enterComparacion(ctx.comparacion())
            elif ctx.ID():
                print(ctx.ID().getText(), end="")
            elif ctx.NUMERO():
                print(ctx.NUMERO().getText(), end="")
            elif ctx.FLOAT():
                print(ctx.FLOAT().getText(), end="")
            elif ctx.STRING():
                print(ctx.STRING().getText(), end="")
            elif ctx.BOOLEAN():  
                boolean_value = ctx.BOOLEAN().getText()
                if(boolean_value == 'true'):
                    print('True', end="")
                elif(boolean_value =='false'):
                    print('False',end="")
            elif ctx.LPAREN():
                print("(", end="")
                if ctx.expresion():
                    self.enterExpresion(ctx.expresion())
                print(")",end="")
            elif ctx.lista():
                self.enterLista(ctx.lista())

    
    # Exit a parse tree produced by codeToPyParser#termino.
    def exitTermino(self, ctx:codeToPyParser.TerminoContext):
        pass

    # Enter a parse tree produced by codeToPyParser#comparacion.
    def enterComparacion(self, ctx: codeToPyParser.ComparacionContext):
        if not hasattr(ctx, 'processed'):
            ctx.processed = True

            if ctx.expAritmetica(0):
                self.enterExpAritmetica(ctx.expAritmetica(0))
            
            if ctx.MENORQUE():
                print(" < ", end="")
            elif ctx.MAYORQUE():
                print(" > ", end="")
            elif ctx.IGUALQUE():
                print(" == ", end="")
            elif ctx.DISTINTOQUE():
                print(" != ", end="")
            elif ctx.MENORIGUAL():
                print(" <= ", end="")
            elif ctx.MAYORIGUAL():
                print(" >= ", end="")
            
            if ctx.expAritmetica(1): 
                self.enterExpAritmetica(ctx.expAritmetica(1))

    # Exit a parse tree produced by codeToPyParser#comparacion.
    def exitComparacion(self, ctx:codeToPyParser.ComparacionContext):
        pass

    # Enter a parse tree produced by codeToPyParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx: codeToPyParser.LlamadaFuncionContext):
          if not hasattr(ctx, 'processed'):
            ctx.processed = True     
            if ctx.ID():
                print(f"{ctx.ID().getText()}", end="(")
            
            if ctx.argumento():
                argumentos = ctx.argumento()
                for i, arg in enumerate(argumentos):
                    if i > 0:
                        print(", ", end="")
                    if arg is not None:
                        self.enterArgumento(arg)
            
            print(")", end="")

    # Exit a parse tree produced by codeToPyParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:codeToPyParser.LlamadaFuncionContext):
        pass 

    # Enter a parse tree produced by codeToPyParser#argumento.
    def enterArgumento(self, ctx:codeToPyParser.ArgumentoContext):
         if not hasattr(ctx, 'processed'):
            ctx.processed = True      
            if ctx.NUMERO():
                print(ctx.NUMERO().getText(), end="")
            elif ctx.STRING():
                print(ctx.STRING().getText(), end="")
            elif ctx.ID():
                print(ctx.ID().getText(), end="")

    # Exit a parse tree produced by codeToPyParser#argumento.
    def exitArgumento(self, ctx:codeToPyParser.ArgumentoContext):
        pass


    # Enter a parse tree produced by codeToPyParser#lista.
    def enterLista(self, ctx):
        if not hasattr(ctx, 'processed'):
            ctx.processed = True
            for child in ctx.getChildren():
                if isinstance(child, TerminalNode):
                    if child.symbol.type == codeToPyParser.LBRACKET:
                        print("[",end="")
                    elif child.symbol.type == codeToPyParser.RBRACKET:
                        print("]",end="")
                    elif child.symbol.type == codeToPyParser.COMMA:
                        print(", ",end="")
                elif isinstance(child, codeToPyParser.ExpresionContext):
                    self.enterExpresion(child)

    # Exit a parse tree produced by codeToPyParser#lista.
    def exitLista(self, ctx:codeToPyParser.ListaContext):
        pass
    def close_file(self):
        self.output_file.close()
        sys.stdout = sys.__stdout__  # Restore the original stdout
