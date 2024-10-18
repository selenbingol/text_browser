import os
import sys
import curses

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def paginate(content, lines_per_page):
    """Splits content into pages based on the specified number of lines."""
    return [content[i:i + lines_per_page] for i in range(0, len(content), lines_per_page)]

def text_browser(stdscr, file_path):
    """Main function to display the text file content page by page using curses."""
    content = read_file(file_path)
    lines_per_page = 10  # Adjust this based on your terminal height
    pages = paginate(content.splitlines(keepends=True), lines_per_page)
    current_page = 0

    while current_page < len(pages):
        # Clear the screen and display the current page
        stdscr.clear()
        stdscr.addstr("".join(pages[current_page]))

        stdscr.addstr("\nPress Space to continue, or Q to quit.")
        stdscr.refresh()

        # Wait for key press
        key = stdscr.getch()

        if key == ord(' '):  # Space key
            current_page += 1  # Move to the next page
        elif key == ord('q'):  # Q key
            break

    if current_page >= len(pages):
        stdscr.addstr("\nEnd of file reached. No more pages to display.")
        stdscr.refresh()
        stdscr.getch()  # Wait for key press before exiting

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 text_browser.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Initialize curses and start the text browser
    curses.wrapper(text_browser, file_path)
