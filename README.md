# Ultimate Rich Print Helper

A universal terminal display library for Python that transforms basic print statements into beautiful, professional output with zero configuration.

## Overview

The Ultimate Rich Print Helper provides pre-configured functions that replace messy terminal formatting code with clean, semantic function calls. Instead of manually formatting colors, JSON, tables, and progress indicators, you get beautiful output with single-parameter functions.


## Comparison

Before

![old](https://github.com/parthshr370/ultimate_rprint/blob/main/outputs/carbon.png)



After


![new](https://github.com/parthshr370/ultimate_rprint/blob/main/outputs/carbon(1).png)




## Installation

1. Copy `ultimate_rprint.py` to your project
2. Install the dependency: `pip install rich`
3. Import and start using: `from ultimate_rprint import *`

## Quick Start

```python
from ultimate_rprint import *

# Basic messages
info("Starting application...")
success("Database connected successfully")
warning("Configuration file not found")
error("Failed to authenticate user")

# Complex data display
data = {"users": 150, "active": 89, "status": "running"}
json_display(data, "System Status")

# Table from list of dictionaries
users = [
    {"name": "Alice", "role": "admin", "last_login": "2024-01-15"},
    {"name": "Bob", "role": "user", "last_login": "2024-01-14"}
]
table_display(users, "Active Users")

# User interaction
if ask_yes_no("Continue with installation?"):
    progress_msg("Installing components...")
    success("Installation completed")
```

## Function Categories

### Basic Messages
| Function | Purpose | Example |
|----------|---------|---------|
| `info(msg)` | Information messages | `info("Processing started")` |
| `success(msg)` | Success notifications | `success("File saved successfully")` |
| `warning(msg)` | Warning alerts | `warning("Disk space low")` |
| `error(msg)` | Error messages | `error("Connection failed")` |
| `debug(msg)` | Debug information | `debug("Variable value: 42")` |

### Data Display
| Function | Purpose | Input Type |
|----------|---------|------------|
| `json_display(data, title)` | JSON with syntax highlighting | dict, list, or JSON string |
| `table_display(data, title)` | Formatted table | list of dictionaries |
| `tree_display(data, title)` | Hierarchical tree | dict with list values |
| `key_value_display(data, title)` | Key-value pairs | dictionary |
| `list_display(items, title)` | Formatted list | list of strings |

### Progress & Status
| Function | Purpose | Parameters |
|----------|---------|------------|
| `operation_start(name)` | Start operation | operation name |
| `operation_complete(name, result)` | Complete operation | operation name, result path |
| `step_progress(current, total, desc)` | Step counter | current, total, description |
| `progress_msg(msg)` | Progress message | progress description |
| `status_update(msg, count)` | Status with count | message, optional count |

### User Interaction
| Function | Purpose | Return Type |
|----------|---------|-------------|
| `ask_question(prompt)` | Text input | string |
| `ask_yes_no(prompt)` | Yes/no question | boolean |
| `ask_choice(prompt, options)` | Multiple choice | selected option |

### Layout & Structure
| Function | Purpose | Parameters |
|----------|---------|------------|
| `divider(title)` | Section separator | optional title |
| `header(text)` | Section header | header text |
| `section_panel(title, content)` | Content in panel | title, content |
| `side_by_side(left, right, left_title, right_title)` | Two-column layout | content and titles |

## Code Transformation Examples

### Before: Manual Formatting
```python
from rich import print as rprint
import json

# Verbose and error-prone
rprint("[blue]Starting database analysis...[/blue]")
rprint(f"[green]Loaded {count} records successfully[/green]")
rprint("[bold yellow]Configuration:[/bold yellow]")
rprint(json.dumps(config_data, indent=2))

# Manual user input
response = input("Continue? (y/n): ").strip().lower()
if response in ['y', 'yes']:
    rprint("[green]Proceeding...[/green]")
```

### After: Clean & Semantic
```python
from ultimate_rprint import *

# Clean and semantic
info("Starting database analysis...")
success(f"Loaded records successfully", count)
json_display(config_data, "Configuration")

# Rich interactive prompts
if ask_yes_no("Continue?"):
    progress_msg("Proceeding...")
```

## Benefits

| Aspect | Before | After |
|--------|--------|-------|
| **Code Lines** | 15+ lines for basic formatting | 3-4 lines for same output |
| **Maintenance** | Color codes scattered everywhere | Single source of truth |
| **Readability** | Mixed formatting and logic | Semantic function names |
| **Consistency** | Manual styling per developer | Uniform professional appearance |
| **Features** | Basic colored text | Tables, JSON, trees, panels, prompts |
| **Portability** | Project-specific formatting | Universal across any codebase |

## Advanced Features

### Smart Data Display
The `display_any()` function automatically chooses the best display format for any data type:

```python
# Automatically formats as JSON, table, or simple display
display_any(api_response, "API Response")
display_any(user_list, "Users")
display_any(error_log, "Errors")
```

### Backward Compatibility
Drop-in replacements for existing code:

```python
# Replace existing rprint calls
print_green("Success message")
print_red("Error message")
print_blue("Information")
```

### Context Managers
```python
# Spinner for long operations
with spinner_status("Processing data"):
    # Long running operation
    time.sleep(5)
```

## File Structure

```
ultimate_rprint/
├── ultimate_rprint.py          # Main library file
├── test_rprint_helper.py       # Comprehensive test suite
├── before_after_comparison.py  # Visual comparison demo
└── README.md                   # This documentation
```

## Output 

![out](https://github.com/parthshr370/ultimate_rprint/blob/main/outputs/Screenshot_20250817_214914.png)

## Testing

Run the test suite to see all functions in action:
```bash
python test_rprint_helper.py
```

Run the comparison demo to see before/after differences:
```bash
python before_after_comparison.py
```

## Requirements

- Python 3.7+
- rich >= 13.0.0

## License

This library is provided as-is for use in any project. Copy, modify, and distribute freely.

## Contributing

This is a self-contained utility library. To add features:

1. Add new functions to `ultimate_rprint.py`
2. Update the test file with examples
3. Document new functions in this README

## Usage in Production

The library has been tested in production environments including:
- Web applications (FastAPI, Django, Flask)
- Data processing pipelines
- CLI tools and scripts
- Research and analysis platforms

Copy the `ultimate_rprint.py` file to any project and start using immediately. No configuration or setup required.
