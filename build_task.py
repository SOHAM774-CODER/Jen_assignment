import os
import sys

print("=== Starting Python Build Task ===")

# Accessing Jenkins Environment Variables
job_name = os.environ.get('JOB_NAME', 'Local Test')
build_number = os.environ.get('BUILD_NUMBER', '0')
workspace = os.environ.get('WORKSPACE', '.')

print(f"Job Name: {job_name}")
print(f"Build Number: {build_number}")
print(f"Workspace Path: {workspace}")

# Perform build tasks (e.g., running tests, data processing, calling APIs)
try:
    print("Running task logic...")
    # Add your core logic here
    
    print("Task completed successfully!")
except Exception as e:
    print(f"Error during execution: {e}", file=sys.stderr)
    sys.exit(1) # Exiting with non-zero tells Jenkins the build failed
