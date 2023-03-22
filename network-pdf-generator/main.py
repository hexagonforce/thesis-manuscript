import py4cytoscape as p4c
from pathlib import Path
from time import sleep
from sys import argv
from subprocess import run
import shlex
from pdfCropMargins import crop

def generate():
    p4c.close_session(False)
    for file in [x for x in Path.cwd().iterdir() if x.suffix == '.graphml']:
        styles = p4c.import_visual_styles()
        to_save_filename = file.stem
        network = p4c.import_network_from_file(file)
        sleep(5)
        p4c.set_visual_style(styles[0], network=network)
        sleep(5)
        p4c.fit_content()
        sleep(5)
        p4c.export_image(filename=to_save_filename, type='SVG', overwrite_file=True)
        sleep(5)
        p4c.close_session(False)

def main(*args):
    if '--generate' in args:
        generate()
    if '--export' in args:
        for file in [x for x in Path.cwd().iterdir() if x.suffix == '.svg']:
            pdf_file = file.with_suffix(".pdf")
            run(shlex.split(f'inkscape {file} -o {pdf_file}')) 
            crop([pdf_file.name, '-o', f'../Figures/{pdf_file.name}'])
            
if __name__ == '__main__':
    main(*argv[1:])
