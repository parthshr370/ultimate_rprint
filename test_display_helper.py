#!/usr/bin/env python3
"""
Test script for ultimate_rprint helper functions
Demonstrates all available functions with sample data
"""

from ultimate_rprint import *
import time

def test_basic_messages():
    """Test basic message types"""
    display_header("Basic Message Types")
    
    display_info("This is an info message")
    display_success("Operation completed successfully")
    display_warning("This is a warning message")
    display_error("Something went wrong")
    display_debug("Debug information here")
    display_progress_msg("Processing data...")
    display_separator()

def test_research_pipeline():
    """Test research pipeline specific functions"""
    display_header("Research Pipeline Messages")
    
    display_operation_start("Database Analysis", "Loading memories from storage")
    time.sleep(0.5)
    display_search_result(5, "diabetes treatment")
    display_operation_complete("Database Analysis", "artifacts/metadata.json")
    
    display_separator()
    
    display_step_progress(1, 5, "diabetes symptoms")
    display_memory_connections_header()
    display_connection_item(1, "Elena Vance", 0.87, "Elena Vance has type 2 diabetes and takes metformin 500mg daily")
    display_connection_item(2, "Marcus Chen", 0.82, "Marcus Chen manages his insulin carefully with blood glucose monitoring")
    
    display_decision_output("Continue research with insulin management focus")
    display_separator()

def test_patient_display():
    """Test patient-specific display functions"""
    display_header("Patient Information Display")
    
    # Use key_value for patient info
    patient_data = {"name": "Elena Blackthorne", "age": "34y", "gender": "female", "condition": "Type 1 Diabetes"}
    display_key_value(patient_data, "Patient Information")
    
    display_info("Round 1:")
    display_info("Elena Blackthorne: I've been having trouble with my blood sugar levels")
    display_success("Dr. Sarah Chen: Let's review your current medication regimen")
    display_status_update("Stored medical facts", 7)
    display_separator()

def test_panels_and_banners():
    """Test panels and special displays"""
    display_header("Panels and Banners")
    
    display_welcome_banner()
    display_separator()
    
    display_section_panel("Research Status", "Analysis in progress...", "cyan")
    display_status_panel("Analyzing 67 memories from database")
    display_completion_panel("Research completed successfully")
    
    display_separator()
    display_completion_banner(150)

def test_execution_summary():
    """Test execution summary"""
    display_header("Execution Summary")
    
    artifacts = {
        "metadata": "artifacts/20250817_metadata.json",
        "plan": "artifacts/20250817_plan.json", 
        "final_answer": "artifacts/20250817_final_answer.md"
    }
    
    display_execution_summary("20250817_143022", 45.67, "What are effective diabetes treatments?", 5)
    display_artifact_list(artifacts)
    display_separator()

def test_pipeline_flow():
    """Test complete pipeline flow"""
    display_header("Complete Pipeline Flow")
    
    # Test pipeline with new functions
    display_divider("Starting Deep Research Pipeline")
    display_info("Research Question: What are the most effective diabetes treatments for elderly patients?")
    display_separator()
    
    display_operation_start("Strategic Planning")
    display_progress_msg("Creating research strategy")
    display_operation_complete("Strategic Planning", "artifacts/plan.json")
    
    display_operation_start("Deep Research")
    display_step_progress(1, 3, "elderly diabetes")
    display_search_result(4, "elderly diabetes")
    display_decision_output("NEXT_SEARCH: medication effectiveness")
    
    display_step_progress(2, 3, "medication effectiveness")
    display_search_result(6, "medication effectiveness")
    display_decision_output("ENOUGH_INFO: YES")
    
    display_research_complete()
    display_generating_report()
    display_operation_complete("Deep Research", "artifacts/final_answer.md")
    
    display_pipeline_complete()

def test_error_handling():
    """Test error and warning functions"""
    display_header("Error Handling")
    
    display_api_error("Failed to connect to Mem0 API")
    display_tracker_error("Could not inject memory context")
    display_fallback_notice("Using direct mem0 search instead of ID tracker")
    display_error_panel("Critical system failure detected")

def main():
    """Run all tests"""
    display_welcome_banner()
    
    test_basic_messages()
    test_research_pipeline()
    test_patient_display()
    test_panels_and_banners()
    test_execution_summary()
    test_pipeline_flow()
    test_error_handling()
    
    display_divider("Testing Complete")
    display_success("All rprint helper functions tested successfully!")

if __name__ == "__main__":
    main()