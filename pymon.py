import os
import typer
import subprocess
import time
import colorama


colorama.init()
app = typer.Typer()

# pymon = os.getenv('pymon')
# # print(pymon)
# if pymon == None:
#     os.environ['pymon'] = ""

@app.command()
def run(file):
    f = open(file, 'r')
    fr = f.read()
    f.close()
    
    print(colorama.Fore.GREEN + '\n##########################\tRun Python Pymon - ' +
          file + ' - ##########################\n' + colorama.Fore.YELLOW)
    
    console = subprocess.Popen('python ' + file)
    
    try:
        while True:
            time.sleep(1)
            
            # pymon = os.getenv('pymon')
            
            # print(pymon)
            
            fn = open(file, 'r')
            frn = fn.read()
            fn.close()
            
            # if pymon == 'stop ' + file:
            #     console.terminate()
            #     print(colorama.Fore.GREEN + '\n##########################\tStop Python Pymon - ' +
            #           file + ' - ##########################' + colorama.Fore.YELLOW)
            #     exit()
            # if pymon == 'stop ' + 'all':
            #     console.terminate()
            #     print(colorama.Fore.GREEN + '\n##########################\tStop Python Pymon - ' +
            #           file + ' - ##########################' + colorama.Fore.YELLOW)
            #     exit()
            if frn != fr:
                console.terminate()
                print(colorama.Fore.GREEN + '\n##########################\tRe-Run Python Pymon - ' +
                      file + ' - ##########################\n' + colorama.Fore.YELLOW)
                console = subprocess.Popen('python ' + file)
                f = open(file, 'r')
                fr = f.read()
                f.close()
    except:
        print(colorama.Fore.GREEN + '\n##########################\tStop Python Pymon - ' +
              file + ' - ##########################' + colorama.Fore.YELLOW)
            
    
    
    

@app.command()
def stop(command):
    os.environ['pymon'] = "stop " + command

if __name__ == '__main__':
    app()
    
