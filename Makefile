.PHONY: main.pdf all clean

all: main.pdf


main.pdf: main.tex
	latexmk -shell-escape -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make main.tex
	mv main.pdf thesis_manuscript.pdf
clean:
	latexmk -CA
