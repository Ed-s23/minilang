 #!Importacion de de  archivos con minilang
import io
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor
 #! Clases para funciones.
class MiniLangEvalVisitor(MiniLangVisitor):
    def __init__(self):
        self.variables = {}

    def visitAssign(self, ctx: MiniLangParser.AssignContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value
        return value

    def visitPrint(self, ctx: MiniLangParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitExpr(self, ctx: MiniLangParser.ExprContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            return self.variables.get(ctx.ID().getText(), 0)
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right
        else:
            return self.visit(ctx.expr(0))
    # ! Instruccion: if 
    def visitIfStatement(self, ctx: MiniLangParser.IfStatementContext):
        condition_value = self.visit(ctx.condition())
        if condition_value:
            self.visit(ctx.statementList())
        return None
    def visitStatementList(self, ctx: MiniLangParser.StatementListContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None
    
     #! instrucción: FOR
    def visitForStatement(self, ctx: MiniLangParser.ForStatementContext):
        self.visit(ctx.assign(0))
        while self.visit(ctx.condition()):
            self.visit(ctx.statementList())
            self.visit(ctx.assign(1))
        return None

    #! Presentacion de Diccionario de aucrdo a la posicion    
    def visitCondition(self, ctx: MiniLangParser.ConditionContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '>': return left > right
        if op == '<': return left < right
        if op == '==': return left == right
        if op == '!=': return left != right
        if op == '>=': return left >= right
        if op == '<=': return left <= right
        return False

def ejecutar_minilang(codigo: str) -> str:
    """
    Ejecuta código MiniLang usando ANTLR y devuelve el resultado print().
    """
    import sys
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()  
    #! Esepciones 
    try:
       
        input_stream = InputStream(codigo)

        lexer = MiniLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = MiniLangParser(tokens)
        tree = parser.program()
        #! Representacion de arbol
        visitor = MiniLangEvalVisitor()
        visitor.visit(tree)

        output = sys.stdout.getvalue()
        return output if output.strip() else "Sin salida."
    #? casos de error al ejecutar mi minilang
    except Exception as e:
        return f"Error al ejecutar : {e}"

    finally:
        sys.stdout = old_stdout
# TODO: Ejemplos de las Funciones 
 # ! Ejemplo de funcionamiento de IF chido 
#?if __name__ == "__main__":
 #?   codigo = """
#?x = 10
#?y = 5
#?if (x > y) {
#?  print(x + y)
#?}
#?"""
#?    print(ejecutar_minilang(codigo))

# !Ejemplo de funcionamiento de for
#?if __name__ == "__main__":
#?    codigo = """
#?for(i = 0; i < 5; i = i + 1) {
#?    print(i)
#?}
#?"""
#?    print(ejecutar_minilang(codigo))