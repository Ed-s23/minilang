import io
import sys

def ejecutar_minilang(codigo):
    try:
        # Guardamos la salida original de print
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()  # Redirigimos prints a un buffer

        # Entorno de ejecución (para variables)
        contexto = {}

        # Ejecutar el código MiniLang (usa 'exec' en lugar de 'eval')
        exec(codigo, contexto)

        # Capturar la salida generada por los print()
        output = sys.stdout.getvalue()

        # Restaurar stdout
        sys.stdout = old_stdout

        return output if output.strip() else "Sin salida."

    except Exception as e:
        sys.stdout = old_stdout
        return f"Error al ejecutar MiniLang: {e}"
