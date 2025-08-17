#!/usr/bin/env python3
"""
Test script for ultimate_rprint helper functions
Demonstrates all available functions with sample data
"""

from ultimate_rprint import *
import time

def test_basic_messages():
    """Test basic message types"""
    rprint_header("Basic Message Types")
    
    rprint_info("This is an info message")
    rprint_success("Operation completed successfully")
    rprint_warning("This is a warning message")
    rprint_error("Something went wrong")
    rprint_debug("Debug information here")
    rprint_progress_msg("Processing data...")
    rprint_separator()

def test_research_pipeline():
    """Test research pipeline specific functions"""
    rprint_header("Research Pipeline Messages")
    
    rprint_operation_start("Database Analysis", "Loading memories from storage")
    time.sleep(0.5)
    rprint_search_result(5, "diabetes treatment")
    rprint_operation_complete("Database Analysis", "artifacts/metadata.json")
    
    rprint_separator()
    
    rprint_step_progress(1, 5, "diabetes symptoms")
    rprint_memory_connections_header()
    rprint_connection_item(1, "Elena Vance", 0.87, "Elena Vance has type 2 diabetes and takes metformin 500mg daily")
    rprint_connection_item(2, "Marcus Chen", 0.82, "Marcus Chen manages his insulin carefully with blood glucose monitoring")
    
    rprint_decision_output("Continue research with insulin management focus")
    rprint_separator()

def test_patient_display():
    """Test patient-specific display functions"""
    rprint_header("Patient Information Display")
    
    # Use key_value for patient info
    patient_data = {"name": "Elena Blackthorne", "age": "34y", "gender": "female", "condition": "Type 1 Diabetes"}
    rprint_key_value(patient_data, "Patient Information")
    
    rprint_info("Round 1:")
    rprint_info("Elena Blackthorne: I've been having trouble with my blood sugar levels")
    rprint_success("Dr. Sarah Chen: Let's review your current medication regimen")
    rprint_status_update("Stored medical facts", 7)
    rprint_separator()

def test_panels_and_banners():
    """Test panels and special displays"""
    rprint_header("Panels and Banners")
    
    rprint_welcome_banner()
    rprint_separator()
    
    rprint_section_panel("Research Status", "Analysis in progress...", "cyan")
    rprint_status_panel("Analyzing 67 memories from database")
    rprint_completion_panel("Research completed successfully")
    
    rprint_separator()
    rprint_completion_banner(150)

def test_execution_summary():
    """Test execution summary"""
    rprint_header("Execution Summary")
    
    artifacts = {
        "metadata": "artifacts/20250817_metadata.json",
        "plan": "artifacts/20250817_plan.json", 
        "final_answer": "artifacts/20250817_final_answer.md"
    }
    
    rprint_execution_summary("20250817_143022", 45.67, "What are effective diabetes treatments?", 5)
    rprint_artifact_list(artifacts)
    rprint_separator()

def test_pipeline_flow():
    """Test complete pipeline flow"""
    rprint_header("Complete Pipeline Flow")
    
    # Test pipeline with new functions
    rprint_divider("Starting Deep Research Pipeline")
    rprint_info("Research Question: What are the most effective diabetes treatments for elderly patients?")
    rprint_separator()
    
    rprint_operation_start("Strategic Planning")
    rprint_progress_msg("Creating research strategy")
    rprint_operation_complete("Strategic Planning", "artifacts/plan.json")
    
    rprint_operation_start("Deep Research")
    rprint_step_progress(1, 3, "elderly diabetes")
    rprint_search_result(4, "elderly diabetes")
    rprint_decision_output("NEXT_SEARCH: medication effectiveness")
    
    rprint_step_progress(2, 3, "medication effectiveness")
    rprint_search_result(6, "medication effectiveness")
    rprint_decision_output("ENOUGH_INFO: YES")
    
    rprint_research_complete()
    rprint_generating_report()
    rprint_operation_complete("Deep Research", "artifacts/final_answer.md")
    
    rprint_pipeline_complete()

def test_error_handling():
    """Test error and warning functions"""
    rprint_header("Error Handling")
    
    rprint_api_error("Failed to connect to Mem0 API")
    rprint_tracker_error("Could not inject memory context")
    rprint_fallback_notice("Using direct mem0 search instead of ID tracker")
    rprint_error_panel("Critical system failure detected")

def main():
    """Run all tests"""
    rprint_welcome_banner()
    
    test_basic_messages()
    test_research_pipeline()
    test_patient_display()
    test_panels_and_banners()
    test_execution_summary()
    test_pipeline_flow()
    test_error_handling()
    
    rprint_divider("Testing Complete")
    rprint_success("All rprint helper functions tested successfully!")

if __name__ == "__main__":
    main()