def display_jobs(jobs):
    if not jobs:
        print("JOB NOT FOUND")
        return
    
    print("\n" + "="*60)
    print(f"  Found {len(jobs)} jobs")
    print("\n" + "="*60)


    for i,job in enumerate(jobs , start=1):
        print(f"\n[{i}] {job['title']}")
        print(f"    Company   : {job['company']['display_name']}")
        print(f"    Location  : {job['location']['display_name']}")
        print(f"    Salary    : {job.get('salary_min', 'N/A')} - {job.get('salary_max', 'N/A')}")
        print(f"    Posted    : {job['created'][:10]}")
        print(f"    Description: {job['description'][:150]}...")  # first 150 chars
        print(f"    URL       : {job['redirect_url']}")
        print("-"*60)