.PHONY: FinalManuscript.pdf all clean

all: FinalManuscript.pdf


FinalManuscript.pdf: FinalManuscript.tex
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make FinalManuscript.tex

clean:
	latexmk -CA