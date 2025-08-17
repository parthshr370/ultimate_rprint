"""
Ultimate Rich Print Helper - Universal Terminal Display Library
==============================================================

A complete, portable terminal display solution that works in ANY Python codebase.
Just drop this file in and start using beautiful terminal output immediately.

INSTALLATION:
1. Copy this file to your project
2. pip install rich
3. Import: from ultimate_rprint import *

USAGE EXAMPLES:
    # Basic messages
    rprint_info("Starting process...")
    rprint_success("Operation completed!")
    rprint_error("Something went wrong")
    
    # Complex data
    rprint_json({"key": "value", "nested": {"data": [1,2,3]}}, "API Response")
    rprint_table([{"name": "John", "age": 25}, {"name": "Jane", "age": 30}], "Users")
    
    # Progress tracking
    for i in range(5):
        rprint_step_progress(i+1, 5, f"Processing item {i+1}")
    
    # Panels and layout
    rprint_panel("Important message in a box")
    rprint_side_by_side("Left content", "Right content", "Before", "After")

FEATURES:
✓ Works in any Python project (zero dependencies except 'rich')
✓ Single-parameter functions - no complex setup
✓ Automatic formatting for JSON, tables, trees
✓ Beautiful colors and styling pre-configured
✓ Progress bars, spinners, user prompts
✓ Multi-column layouts and comparisons
✓ Code syntax highlighting
✓ Completely portable - just copy and use

COMMON REPLACEMENTS:
    print() → rprint_info() or rprint_success()
    print(f"Error: {msg}") → rprint_error(msg)
    print(json.dumps(data, indent=2)) → rprint_json(data)
    
NO CONFIGURATION NEEDED - Just import and use!

GITHUB READY:
- Copy ultimate_rprint.py to any project
- Add to requirements.txt: rich>=13.0.0  
- Import: from ultimate_rprint import *
- Start using beautiful terminal output immediately!
"""

from rich import print as rprint
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.console import Console
from rich.text import Text
from rich.rule import Rule
from rich.tree import Tree
from rich.table import Table
from rich.columns import Columns
from rich.align import Align
from rich.syntax import Syntax
from rich.json import JSON
from rich.status import Status
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown
from rich.box import ROUNDED, DOUBLE, MINIMAL
import time
import json
import contextlib
from typing import Optional, List, Dict, Any, Union

console = Console()

# ============================================================================
# ENHANCED DATA DISPLAY
# ============================================================================

def rprint_json(data: Union[Dict, List, str], title: str = "Data"):
    """Display JSON with syntax highlighting"""
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            rprint(f"[red]Invalid JSON string[/red]")
            return
    
    panel = Panel(JSON.from_data(data), title=f"[bold cyan]{title}[/bold cyan]", border_style="cyan")
    rprint(panel)

def rprint_table(data: List[Dict], title: str = "Table", max_rows: int = 10):
    """Create table from list of dictionaries"""
    if not data:
        rprint_warning("No data for table")
        return
    
    table = Table(title=f"[bold blue]{title}[/bold blue]", box=ROUNDED)
    
    # Auto-detect columns
    first_row = data[0]
    for key in first_row.keys():
        table.add_column(key.replace('_', ' ').title(), style="cyan")
    
    # Add data rows
    for row in data[:max_rows]:
        values = [str(row.get(key, ""))[:50] for key in first_row.keys()]
        table.add_row(*values)
    
    if len(data) > max_rows:
        table.caption = f"Showing {max_rows} of {len(data)} rows"
    
    rprint(table)

def rprint_tree(data: Dict[str, List], title: str = "Tree"):
    """Display hierarchical data as tree"""
    tree = Tree(f"[bold blue]{title}[/bold blue]")
    
    for key, items in data.items():
        branch = tree.add(f"[green]{key}[/green] ({len(items)} items)")
        for item in items[:5]:  # Limit items
            item_text = str(item)[:60] + ("..." if len(str(item)) > 60 else "")
            branch.add(f"[dim]{item_text}[/dim]")
    
    rprint(tree)

def rprint_code(code: str, language: str = "python", title: str = "Code"):
    """Display code with syntax highlighting"""
    syntax = Syntax(code, language, theme="monokai", line_numbers=True)
    panel = Panel(syntax, title=f"[bold green]{title}[/bold green]", border_style="green")
    rprint(panel)

def rprint_markdown(content: str):
    """Display markdown content"""
    rprint(Markdown(content))

# ============================================================================
# PROGRESS AND STATUS
# ============================================================================

def rprint_progress_bar(current: int, total: int, description: str = "Progress"):
    """Simple progress indicator"""
    percentage = (current / total) * 100
    bar = "█" * int(percentage // 5) + "░" * (20 - int(percentage // 5))
    rprint(f"[cyan]{description}: [{bar}] {current}/{total} ({percentage:.1f}%)[/cyan]")

@contextlib.contextmanager
def rprint_spinner(message: str):
    """Context manager for spinner during operations"""
    with console.status(f"[cyan]{message}[/cyan]", spinner="dots"):
        yield

def rprint_countdown(seconds: int, message: str = "Waiting"):
    """Countdown timer"""
    for i in range(seconds, 0, -1):
        rprint(f"[yellow]{message}: {i}s[/yellow]", end="\r")
        time.sleep(1)
    rprint(f"[green]{message}: Done![/green]")

# ============================================================================
# USER INPUT
# ============================================================================

def rprint_ask(question: str) -> str:
    """Ask user a question"""
    return Prompt.ask(f"[cyan]{question}[/cyan]")

def rprint_ask_yes_no(question: str) -> bool:
    """Ask yes/no question"""
    return Confirm.ask(f"[yellow]{question}[/yellow]")

def rprint_ask_choice(question: str, choices: List[str]) -> str:
    """Ask user to choose from options"""
    return Prompt.ask(f"[cyan]{question}[/cyan]", choices=choices)

# ============================================================================
# LAYOUT AND COLUMNS
# ============================================================================

def rprint_side_by_side(left_content: str, right_content: str, left_title: str = "Left", right_title: str = "Right"):
    """Display two panels side by side"""
    left_panel = Panel(left_content, title=f"[bold blue]{left_title}[/bold blue]", border_style="blue")
    right_panel = Panel(right_content, title=f"[bold green]{right_title}[/bold green]", border_style="green")
    
    columns = Columns([left_panel, right_panel], equal=True)
    rprint(columns)

def rprint_multi_column(contents: List[str], titles: List[str] = None, colors: List[str] = None):
    """Display multiple columns"""
    if not titles:
        titles = [f"Column {i+1}" for i in range(len(contents))]
    if not colors:
        colors = ["blue", "green", "yellow", "cyan", "magenta"] * (len(contents) // 5 + 1)
    
    panels = []
    for i, content in enumerate(contents):
        color = colors[i % len(colors)]
        panel = Panel(content, title=f"[bold {color}]{titles[i]}[/bold {color}]", border_style=color)
        panels.append(panel)
    
    rprint(Columns(panels, equal=True))

# ============================================================================
# ADVANCED DISPLAYS
# ============================================================================

def rprint_diff(old: str, new: str):
    """Display text differences"""
    rprint_side_by_side(old, new, "Before", "After")

def rprint_key_value(data: Dict[str, Any], title: str = "Information"):
    """Display key-value pairs in formatted panel"""
    content = ""
    for key, value in data.items():
        key_formatted = key.replace('_', ' ').title()
        content += f"[cyan]{key_formatted}:[/cyan] [white]{value}[/white]\n"
    
    panel = Panel(content.rstrip(), title=f"[bold blue]{title}[/bold blue]", border_style="blue")
    rprint(panel)

def rprint_list(items: List[str], title: str = "List", numbered: bool = True):
    """Display list with optional numbering"""
    content = ""
    for i, item in enumerate(items, 1):
        prefix = f"{i}. " if numbered else "• "
        content += f"[cyan]{prefix}[/cyan][white]{item}[/white]\n"
    
    panel = Panel(content.rstrip(), title=f"[bold blue]{title}[/bold blue]", border_style="blue")
    rprint(panel)

# ============================================================================
# BASIC MESSAGE TYPES
# ============================================================================

def rprint_info(message: str):
    """Blue info message"""
    rprint(f"[blue]ℹ {message}[/blue]")

def rprint_success(message: str):
    """Green success message"""
    rprint(f"[green]✓ {message}[/green]")

def rprint_warning(message: str):
    """Yellow warning message"""
    rprint(f"[yellow]⚠ {message}[/yellow]")

def rprint_error(message: str):
    """Red error message"""
    rprint(f"[red]✗ {message}[/red]")

def rprint_debug(message: str):
    """Magenta debug message"""
    rprint(f"[magenta][debug] {message}[/magenta]")

def rprint_progress_msg(message: str):
    """Cyan progress message"""
    rprint(f"[cyan]▶ {message}[/cyan]")

# ============================================================================
# SPECIALIZED DISPLAYS FOR COMMON PATTERNS
# ============================================================================

def rprint_operation_start(operation: str, details: str = ""):
    """Start of any operation"""
    detail_msg = f" - {details}" if details else ""
    rprint(f"\n[bold blue]{operation}[/bold blue]{detail_msg}")

def rprint_operation_complete(operation: str, result: str = ""):
    """Operation completion"""
    result_msg = f" → {result}" if result else ""
    rprint(f"[bold green]✓ {operation} Complete[/bold green]{result_msg}")

def rprint_step_progress(current: int, total: int, description: str):
    """Step progress display"""
    rprint(f"\n[bold cyan]Step {current}/{total}[/bold cyan]")
    rprint(f"[cyan]{description}[/cyan]")

def rprint_search_result(count: int, query: str):
    """Search results summary"""
    rprint(f"[green]Found {count} results for '{query}'[/green]")

def rprint_connection_item(index: int, name: str, score: float, preview: str):
    """Individual connection/result item"""
    rprint(f"   [yellow]{index}.[/yellow] [magenta]{name}[/magenta] Score: [green]{score:.3f}[/green]")
    rprint(f"      [dim]{preview[:80]}...[/dim]")

def rprint_decision_output(decision: str):
    """AI/system decision output"""
    rprint(f"\n[bold yellow]Decision:[/bold yellow]")
    rprint(f"[yellow]   {decision}[/yellow]")

def rprint_status_update(message: str, count: int = None):
    """General status update"""
    count_msg = f" ({count})" if count is not None else ""
    rprint(f"[green]{message}{count_msg}[/green]")

def rprint_process_step(step_name: str, status: str = "processing"):
    """Generic process step"""
    status_colors = {
        "processing": "yellow", "complete": "green", "failed": "red", 
        "skipped": "dim", "warning": "yellow"
    }
    color = status_colors.get(status, "blue")
    rprint(f"[{color}]{step_name}[/{color}]")

# ============================================================================
# PANELS AND SECTIONS
# ============================================================================

def rprint_section_panel(title: str, content: str, color: str = "blue"):
    """Fancy panel with title"""
    panel = Panel(content, title=f"[bold {color}]{title}[/bold {color}]", border_style=color)
    rprint(panel)

def rprint_status_panel(message: str):
    """Status panel in yellow"""
    panel = Panel(f"[yellow]{message}[/yellow]", border_style="yellow")
    rprint(panel)

def rprint_completion_panel(message: str):
    """Completion panel in green"""
    panel = Panel(f"[green]{message}[/green]", border_style="green")
    rprint(panel)

def rprint_error_panel(message: str):
    """Error panel in red"""
    panel = Panel(f"[red]{message}[/red]", border_style="red")
    rprint(panel)

# ============================================================================
# DIVIDERS AND SEPARATORS
# ============================================================================

def rprint_divider(title: str = "", style: str = "="):
    """Section divider"""
    if title:
        rprint(Rule(f"[bold blue]{title}[/bold blue]", style=style))
    else:
        rprint(Rule(style=style))

def rprint_thin_divider():
    """Thin separator line"""
    rprint("[dim]" + "-" * 60 + "[/dim]")

# ============================================================================
# EXECUTION SUMMARY
# ============================================================================

def rprint_execution_summary(session_id: str, execution_time: float, question: str, artifacts_count: int):
    """Complete execution summary"""
    rprint(f"\n[bold green]Pipeline Execution Complete[/bold green]")
    rprint(f"[blue]  • Total Time: {execution_time:.2f} seconds[/blue]")
    rprint(f"[blue]  • Session ID: {session_id}[/blue]")
    rprint(f"[blue]  • Question: {question}[/blue]")
    rprint(f"[blue]  • Artifacts Generated: {artifacts_count} files[/blue]")

def rprint_artifact_list(artifacts: Dict[str, str]):
    """Display artifact list"""
    rprint(f"\n[bold yellow]Generated Artifacts ({len(artifacts)} files):[/bold yellow]")
    rprint_thin_divider()
    for artifact_type, path in artifacts.items():
        rprint(f"  [cyan]• {artifact_type.replace('_', ' ').title()}:[/cyan] {path}")

# ============================================================================
# PROGRESS AND LOADING
# ============================================================================

def rprint_loading(message: str):
    """Loading message with spinner effect"""
    rprint(f"[yellow]⏳ {message}...[/yellow]")

def rprint_pipeline_start(question: str):
    """Pipeline initialization"""
    rprint("[bold blue]Deep Memory Research Pipeline[/bold blue]")
    rprint(f"[blue]Research Question: {question}[/blue]")
    rprint("[yellow]Starting comprehensive research...[/yellow]")

def rprint_pipeline_init(session_id: str):
    """Pipeline initialization with session"""
    rprint(f"[blue]Pipeline initialized - Session: {session_id}[/blue]")

# ============================================================================
# MEMORY AND SEARCH SPECIFIC
# ============================================================================

def rprint_search_term_extracted(term: str):
    """Extracted search term"""
    rprint(f"[yellow]LLM extracted initial search term: '{term}'[/yellow]")

def rprint_memory_search_start(query: str):
    """Memory search initiation"""
    rprint(f"[cyan]Searching: '{query}'[/cyan]")

def rprint_no_memories_found():
    """No search results"""
    rprint("[yellow]No connected memories found for this exploration[/yellow]")

def rprint_memory_connections_header():
    """Header for memory connections list"""
    rprint("[bold yellow]Memory Connections Discovered:[/bold yellow]")

def rprint_research_complete():
    """Research completion message"""
    rprint("[bold green]Strategic research complete - enough information gathered![/bold green]")

def rprint_generating_report():
    """Final report generation"""
    rprint("[yellow]Generating final report...[/yellow]")

# ============================================================================
# ERROR HANDLING
# ============================================================================

def rprint_api_error(error_msg: str):
    """API-related errors"""
    rprint(f"[red]API Error: {error_msg}[/red]")

def rprint_tracker_error(error_msg: str):
    """Memory tracker errors"""
    rprint(f"[yellow]Warning: {error_msg}[/yellow]")

def rprint_fallback_notice(message: str):
    """Fallback operation notice"""
    rprint(f"[yellow]Fallback: {message}[/yellow]")

# ============================================================================
# PIPELINE STATUS
# ============================================================================

def rprint_pipeline_complete():
    """Pipeline completion"""
    rprint_divider("Research Complete")
    rprint("[bold green]Research pipeline complete![/bold green]")

def rprint_pipeline_failed(error: str):
    """Pipeline failure"""
    rprint(f"[bold red]Pipeline failed: {error}[/bold red]")

def rprint_memory_storage_prompt():
    """Memory storage user prompt"""
    rprint_divider()
    rprint("[bold yellow]Research pipeline complete![/bold yellow]")

def rprint_memory_stored(count: int):
    """Memory storage success"""
    rprint(f"[green]Stored {count} research insights as memories[/green]")

def rprint_memory_skipped():
    """Memory storage skipped"""
    rprint("[yellow]Skipping memory storage[/yellow]")

# ============================================================================
# TESTING AND VERIFICATION
# ============================================================================

def rprint_test_start(test_name: str):
    """Test initiation"""
    rprint(f"[yellow]Testing {test_name}[/yellow]")

def rprint_test_success(message: str):
    """Test success"""
    rprint(f"[green]✓ {message}[/green]")

def rprint_test_failure(message: str):
    """Test failure"""
    rprint(f"[red]✗ {message}[/red]")

# ============================================================================
# UTILS
# ============================================================================

def rprint_separator():
    """Simple separator"""
    rprint()

def rprint_header(text: str):
    """Section header"""
    rprint(f"\n[bold blue]{text}[/bold blue]")

def rprint_subheader(text: str):
    """Subsection header"""
    rprint(f"[bold cyan]{text}[/bold cyan]")

# ============================================================================
# SPECIAL EFFECTS
# ============================================================================

def rprint_welcome_banner():
    """Welcome banner for pipeline"""
    rprint(Panel(
        "[bold blue]Deep Memory Research Pipeline[/bold blue]\n"
        "[cyan]I'll help you research your mem0 memories comprehensively![/cyan]",
        border_style="blue"
    ))

def rprint_completion_banner(total_memories: int):
    """Completion banner"""
    rprint(Panel(
        f"[green]Total memories in database: {total_memories}[/green]",
        border_style="green"
    ))

def rprint_preview_text(text: str, max_chars: int = 200):
    """Text preview with truncation"""
    preview = text[:max_chars] + "..." if len(text) > max_chars else text
    rprint(f"[dim]{preview}[/dim]")

# ============================================================================
# QUICK START GUIDE AND ALIASES
# ============================================================================

"""
QUICK START EXAMPLES FOR ANY CODEBASE:

# Replace basic prints
print("Starting...") → info("Starting...")
print("Done!") → success("Done!")
print("Error occurred") → error("Error occurred")

# Replace complex data display  
print(json.dumps(data, indent=2)) → json_display(data)
for item in list: print(item) → list_display(list)

# Replace progress messages
print(f"Step {i}/{total}") → step_progress(i, total, "Description")

# Replace status messages
print(f"Found {count} items") → status_update(f"Found items", count)

# For any existing codebase - just replace imports:
# from rich import print as rprint → from ultimate_rprint import *
"""

# Direct color replacements (for codebases with existing color patterns)
def print_green(message: str):
    """Green text - direct replacement for rprint('[green]...[/green]')"""
    rprint(f"[green]{message}[/green]")

def print_red(message: str):
    """Red text - direct replacement"""
    rprint(f"[red]{message}[/red]")

def print_yellow(message: str):
    """Yellow text - direct replacement"""
    rprint(f"[yellow]{message}[/yellow]")

def print_blue(message: str):
    """Blue text - direct replacement"""
    rprint(f"[blue]{message}[/blue]")

def print_cyan(message: str):
    """Cyan text - direct replacement"""
    rprint(f"[cyan]{message}[/cyan]")

def print_magenta(message: str):
    """Magenta text - direct replacement"""
    rprint(f"[magenta]{message}[/magenta]")

def print_dim(message: str):
    """Dim text - direct replacement"""
    rprint(f"[dim]{message}[/dim]")

def print_bold(message: str):
    """Bold text - direct replacement"""
    rprint(f"[bold]{message}[/bold]")

# ============================================================================
# UNIVERSAL COMPATIBILITY FUNCTIONS
# ============================================================================

def rprint_log(message: str, level: str = "info"):
    """Universal logging function - works like any logger"""
    level_map = {
        "info": rprint_info, "success": rprint_success, "warning": rprint_warning,
        "error": rprint_error, "debug": rprint_debug, "progress": rprint_progress_msg
    }
    func = level_map.get(level, info)
    func(message)

def rprint_display_any(data: Any, title: str = "Data"):
    """Automatically choose best display method for any data type"""
    if isinstance(data, dict):
        if len(data) < 10:  # Small dict - use key-value
            rprint_key_value(data, title)
        else:  # Large dict - use JSON
            rprint_json(data, title)
    elif isinstance(data, list):
        if all(isinstance(item, dict) for item in data):  # List of dicts - table
            rprint_table(data, title)
        else:  # Simple list
            rprint_list([str(item) for item in data], title)
    elif isinstance(data, str) and data.strip().startswith('{'):  # JSON string
        rprint_json(data, title)
    else:  # Simple value
        rprint_info(f"{title}: {data}")

# ============================================================================
# BACKWARD COMPATIBILITY
# ============================================================================

def rprint_replacement(*args, **kwargs):
    """Drop-in replacement for rprint() calls"""
    rprint(*args, **kwargs)