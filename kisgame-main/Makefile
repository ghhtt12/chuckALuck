# Cross-platform Makefile for Chuck-A-Luck
.PHONY: run test web serve clean help

# Detect OS
UNAME := $(shell uname -s)

run:
	@echo "=== STARTING GAME ==="
ifeq ($(UNAME), Linux)
	python3 chuck_a_luck.py
else
	py chuck_a_luck.py
endif

test:
	@echo "=== RUNNING TESTS ==="
ifeq ($(UNAME), Linux)
	python3 test_game.py
else
	py test_game.py
endif

web:
	@echo "=== WEB VERSION ==="
	@echo "Open web_game.html in browser"

serve:
	@echo "=== LOCAL SERVER ==="
	@echo "Open: http://localhost:8000/web_game.html"
ifeq ($(UNAME), Linux)
	python3 -m http.server 8000
else
	py -m http.server 8000
endif

clean:
	@echo "=== CLEANING ==="
ifeq ($(UNAME), Linux)
	rm -f *.log *.txt
else
	del /Q *.log *.txt 2>nul
endif

help:
	@echo "Available commands:"
	@echo "  make run   - Start game"
	@echo "  make test  - Run tests"
	@echo "  make web   - Web version info"
	@echo "  make serve - Start local server"
	@echo "  make clean - Clean temporary files"
	@echo "  make help  - Show this help"
	@echo ""
	@echo "Detected OS: $(UNAME)"