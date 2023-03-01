.PHONY: main.pdf all clean

all: main.pdf


main.pdf: main.tex
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make main.tex

clean:
	latexmk -CA