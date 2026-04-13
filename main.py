from api import fetch_jobs
from database import create_table, save_jobs,get_all_jobs
from display import display_jobs

def main():
    create_table()

    keyword = input("Enter job keyword to search job : ")

    try:
        print(f"\nFeatching jobs for '{keyword}'....")
        jobs = fetch_jobs(keyword)
        save_jobs(jobs)
        print(f"Saved {len(jobs)} jobs to database.")

    except Exception as e:
        print(f"Error featching jobs : {e}")
        return
    
    print("\nFeatching jobs from database...")
    saved_jobs = get_all_jobs()

    if not saved_jobs:
        print("no jobs in database.") 
        return
    
    # convert tuples back into dict 

    job_dicts = []

    for row in saved_jobs:
        job_dicts.append({
            "title" : row[1],
            "company" : {"display_name" : row[2]},
            "location" : {"display_name" : row[3]},
            "salary_min" : row[4],
            "salary_max" : row[5],
            "description" : row[6],
            "created" : row[7],
            "redirect_url" : row[8],
})
    display_jobs(job_dicts)

if __name__ == "__main__":
    main()