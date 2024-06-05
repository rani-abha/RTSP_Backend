@echo off

rem Start the server in a new command prompt window
start cmd /k "python server.py"

rem Wait a bit to ensure the server has time to start
timeout /t 5 /nobreak >nul

rem Start the client in a new command prompt window
start cmd /k "py ClientLauncher.py 127.0.0.1 6789 3000 movie.Mjpeg"
