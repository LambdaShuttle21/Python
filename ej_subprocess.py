import subprocess
try:
        resultado = subprocess.run(["ls", "-l"], text=True, capture_output=True)
        print("Salida:")
        print(resultado.stdout)
        print("Código de retorno:", resultado.returncode)

except subprocess.CalledProcessError as e:
        print(e.output)
