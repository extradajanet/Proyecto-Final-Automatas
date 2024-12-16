# Generated from codeToPy.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .codeToPyParser import codeToPyParser
else:
    from codeToPyParser import codeToPyParser

# This class defines a complete listener for a parse tree produced by codeToPyParser.
class codeToPyListener(ParseTreeListener):

    # Enter a parse tree produced by codeToPyParser#inicio.
    def enterInicio(self, ctx:codeToPyParser.InicioContext):
        pass

    # Exit a parse tree produced by codeToPyParser#inicio.
    def exitInicio(self, ctx:codeToPyParser.InicioContext):
        pass


    # Enter a parse tree produced by codeToPyParser#declaracionFuncion.
    def enterDeclaracionFuncion(self, ctx:codeToPyParser.DeclaracionFuncionContext):
        pass

    # Exit a parse tree produced by codeToPyParser#declaracionFuncion.
    def exitDeclaracionFuncion(self, ctx:codeToPyParser.DeclaracionFuncionContext):
        pass


    # Enter a parse tree produced by codeToPyParser#parametros.
    def enterParametros(self, ctx:codeToPyParser.ParametrosContext):
        pass

    # Exit a parse tree produced by codeToPyParser#parametros.
    def exitParametros(self, ctx:codeToPyParser.ParametrosContext):
        pass


    # Enter a parse tree produced by codeToPyParser#bloque.
    def enterBloque(self, ctx:codeToPyParser.BloqueContext):
        pass

    # Exit a parse tree produced by codeToPyParser#bloque.
    def exitBloque(self, ctx:codeToPyParser.BloqueContext):
        pass


    # Enter a parse tree produced by codeToPyParser#instruccion.
    def enterInstruccion(self, ctx:codeToPyParser.InstruccionContext):
        pass

    # Exit a parse tree produced by codeToPyParser#instruccion.
    def exitInstruccion(self, ctx:codeToPyParser.InstruccionContext):
        pass


    # Enter a parse tree produced by codeToPyParser#ciclo.
    def enterCiclo(self, ctx:codeToPyParser.CicloContext):
        pass

    # Exit a parse tree produced by codeToPyParser#ciclo.
    def exitCiclo(self, ctx:codeToPyParser.CicloContext):
        pass


    # Enter a parse tree produced by codeToPyParser#mostrar.
    def enterMostrar(self, ctx:codeToPyParser.MostrarContext):
        pass

    # Exit a parse tree produced by codeToPyParser#mostrar.
    def exitMostrar(self, ctx:codeToPyParser.MostrarContext):
        pass


    # Enter a parse tree produced by codeToPyParser#cadenaConcatenada.
    def enterCadenaConcatenada(self, ctx:codeToPyParser.CadenaConcatenadaContext):
        pass

    # Exit a parse tree produced by codeToPyParser#cadenaConcatenada.
    def exitCadenaConcatenada(self, ctx:codeToPyParser.CadenaConcatenadaContext):
        pass


    # Enter a parse tree produced by codeToPyParser#condicion.
    def enterCondicion(self, ctx:codeToPyParser.CondicionContext):
        pass

    # Exit a parse tree produced by codeToPyParser#condicion.
    def exitCondicion(self, ctx:codeToPyParser.CondicionContext):
        pass


    # Enter a parse tree produced by codeToPyParser#declaracionVariable.
    def enterDeclaracionVariable(self, ctx:codeToPyParser.DeclaracionVariableContext):
        pass

    # Exit a parse tree produced by codeToPyParser#declaracionVariable.
    def exitDeclaracionVariable(self, ctx:codeToPyParser.DeclaracionVariableContext):
        pass


    # Enter a parse tree produced by codeToPyParser#accesoIndice.
    def enterAccesoIndice(self, ctx:codeToPyParser.AccesoIndiceContext):
        pass

    # Exit a parse tree produced by codeToPyParser#accesoIndice.
    def exitAccesoIndice(self, ctx:codeToPyParser.AccesoIndiceContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expresion.
    def enterExpresion(self, ctx:codeToPyParser.ExpresionContext):
        pass

    # Exit a parse tree produced by codeToPyParser#expresion.
    def exitExpresion(self, ctx:codeToPyParser.ExpresionContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expAritmetica.
    def enterExpAritmetica(self, ctx:codeToPyParser.ExpAritmeticaContext):
        pass

    # Exit a parse tree produced by codeToPyParser#expAritmetica.
    def exitExpAritmetica(self, ctx:codeToPyParser.ExpAritmeticaContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expTermino.
    def enterExpTermino(self, ctx:codeToPyParser.ExpTerminoContext):
        pass

    # Exit a parse tree produced by codeToPyParser#expTermino.
    def exitExpTermino(self, ctx:codeToPyParser.ExpTerminoContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expFactor.
    def enterExpFactor(self, ctx:codeToPyParser.ExpFactorContext):
        pass

    # Exit a parse tree produced by codeToPyParser#expFactor.
    def exitExpFactor(self, ctx:codeToPyParser.ExpFactorContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expPotencia.
    def enterExpPotencia(self, ctx:codeToPyParser.ExpPotenciaContext):
        pass

    # Exit a parse tree produced by codeToPyParser#expPotencia.
    def exitExpPotencia(self, ctx:codeToPyParser.ExpPotenciaContext):
        pass


    # Enter a parse tree produced by codeToPyParser#expRaiz.
    def enterExpRaiz(self, ctx:codeToPyParser.ExpRaizContext):
        pass

    # Exit a parse tree produced by codeToPyParser#expRaiz.
    def exitExpRaiz(self, ctx:codeToPyParser.ExpRaizContext):
        pass


    # Enter a parse tree produced by codeToPyParser#condicionLogica.
    def enterCondicionLogica(self, ctx:codeToPyParser.CondicionLogicaContext):
        pass

    # Exit a parse tree produced by codeToPyParser#condicionLogica.
    def exitCondicionLogica(self, ctx:codeToPyParser.CondicionLogicaContext):
        pass


    # Enter a parse tree produced by codeToPyParser#termino.
    def enterTermino(self, ctx:codeToPyParser.TerminoContext):
        pass

    # Exit a parse tree produced by codeToPyParser#termino.
    def exitTermino(self, ctx:codeToPyParser.TerminoContext):
        pass


    # Enter a parse tree produced by codeToPyParser#comparacion.
    def enterComparacion(self, ctx:codeToPyParser.ComparacionContext):
        pass

    # Exit a parse tree produced by codeToPyParser#comparacion.
    def exitComparacion(self, ctx:codeToPyParser.ComparacionContext):
        pass


    # Enter a parse tree produced by codeToPyParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:codeToPyParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by codeToPyParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:codeToPyParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by codeToPyParser#argumento.
    def enterArgumento(self, ctx:codeToPyParser.ArgumentoContext):
        pass

    # Exit a parse tree produced by codeToPyParser#argumento.
    def exitArgumento(self, ctx:codeToPyParser.ArgumentoContext):
        pass


    # Enter a parse tree produced by codeToPyParser#lista.
    def enterLista(self, ctx:codeToPyParser.ListaContext):
        pass

    # Exit a parse tree produced by codeToPyParser#lista.
    def exitLista(self, ctx:codeToPyParser.ListaContext):
        pass


