.PHONY: run web test clean help

run:
	@echo "=== TERMINAL VERSION ==="
	py terminal_ui.py

web:
	@echo "=== WEB VERSION ==="
	@echo "Starting web server..."
	py web_ui.py

test:
	@echo "=== RUNNING TESTS ==="
	py -c "from chuck_a_luck import ChuckALuckGame; g=ChuckALuckGame(); print('Game logic test: OK')"

clean:
	@echo "=== CLEANING ==="
	del /Q *.pyc __pycache__ 2>nul || rm -rf __pycache__

help:
	@echo "Available commands:"
	@echo "  make run   - Play in terminal"
	@echo "  make web   - Play in browser"
	@echo "  make test  - Run tests"
	@echo "  make clean - Clean up"