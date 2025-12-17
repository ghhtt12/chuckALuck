#!/bin/bash

echo "=== Chuck-A-Luck for Linux ==="
echo "1. Start game"
echo "2. Run tests"
echo "3. Start web server"
echo "4. Exit"

read -p "Choose option: " choice

case $choice in
    1)
        python3 chuck_a_luck.py
        ;;
    2)
        python3 test_game.py
        ;;
    3)
        echo "Starting server at http://localhost:8000"
        python3 -m http.server 8000
        ;;
    4)
        exit 0
        ;;
    *)
        echo "Invalid choice"
        ;;
esac