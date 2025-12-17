# Cross-platform Makefile for Chuck-A-Luck
.PHONY: run web test clean help

# Detect OS and set Python command
ifeq ($(OS),Windows_NT)
    PYTHON = py
else
    PYTHON = python3
endif

run:
	@echo "=== TERMINAL VERSION ==="
	$(PYTHON) terminal_ui.py

web:
	@echo "=== WEB VERSION ==="
	@echo "Starting web server..."
	$(PYTHON) web_ui.py

test:
	@echo "=== RUNNING TESTS ==="
	$(PYTHON) -c "from chuck_a_luck import ChuckALuckGame; g=ChuckALuckGame(); print('✅ Game logic test: OK')"

clean:
	@echo "=== CLEANING ==="
ifeq ($(OS),Windows_NT)
	del /Q *.pyc 2>nul
	rmdir /Q /S __pycache__ 2>nul
else
	rm -f *.pyc
	rm -rf __pycache__
endif

help:
	@echo "Available commands:"
	@echo "  make run   - Play in terminal"
	@echo "  make web   - Play in browser"
	@echo "  make test  - Run tests"
	@echo "  make clean - Clean up"
	@echo ""
	@echo "Detected OS: $(OS)"
	@echo "Python command: $(PYTHON)"