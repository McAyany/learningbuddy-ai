from supabase import create_client

SUPABASE_URL = "https://ssehghbathrygvusnxpt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNzZWhnaGJhdGhyeWd2dXNueHB0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NjcxNjkyNCwiZXhwIjoyMDcyMjkyOTI0fQ.2DhNyO68aD7FFOEAmidgmz3J0azMlndal1HAuZojJrY"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Example: fetch classes
def get_classes():
    data = supabase.table("classes").select("*").execute()
    return data.data
