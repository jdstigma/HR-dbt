import csv
import random
from datetime import date, timedelta
import calendar as cal_mod
import os

random.seed(42)

OUT_DIR = r"C:\Users\jdsti\OneDrive\Desktop\Projects\HR-dbt\seeds"
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# STATIC LOOKUP DATA
# ---------------------------------------------------------------------------
DIVISIONS = [
    {"division_id":1,"division_name":"Technology"},
    {"division_id":2,"division_name":"Finance"},
    {"division_id":3,"division_name":"Human Resources"},
    {"division_id":4,"division_name":"Operations"},
    {"division_id":5,"division_name":"Sales & Marketing"},
    {"division_id":6,"division_name":"Legal & Compliance"},
    {"division_id":7,"division_name":"Research & Development"},
    {"division_id":8,"division_name":"Customer Success"},
]

DEPARTMENTS = [
    {"department_id":1, "department_name":"Software Engineering",       "division_id":1,"budget_m":45.0},
    {"department_id":2, "department_name":"Data & Analytics",           "division_id":1,"budget_m":22.0},
    {"department_id":3, "department_name":"Infrastructure & DevOps",    "division_id":1,"budget_m":18.0},
    {"department_id":4, "department_name":"Cybersecurity",              "division_id":1,"budget_m":15.0},
    {"department_id":5, "department_name":"Product Management",         "division_id":1,"budget_m":12.0},
    {"department_id":6, "department_name":"Financial Planning & Analysis","division_id":2,"budget_m":8.0},
    {"department_id":7, "department_name":"Accounting",                 "division_id":2,"budget_m":6.0},
    {"department_id":8, "department_name":"Treasury",                   "division_id":2,"budget_m":5.0},
    {"department_id":9, "department_name":"Tax",                        "division_id":2,"budget_m":4.0},
    {"department_id":10,"department_name":"Talent Acquisition",         "division_id":3,"budget_m":7.0},
    {"department_id":11,"department_name":"Employee Relations",         "division_id":3,"budget_m":5.0},
    {"department_id":12,"department_name":"Learning & Development",     "division_id":3,"budget_m":4.0},
    {"department_id":13,"department_name":"Total Rewards",              "division_id":3,"budget_m":3.0},
    {"department_id":14,"department_name":"Supply Chain",               "division_id":4,"budget_m":20.0},
    {"department_id":15,"department_name":"Facilities Management",      "division_id":4,"budget_m":10.0},
    {"department_id":16,"department_name":"Procurement",                "division_id":4,"budget_m":15.0},
    {"department_id":17,"department_name":"Quality Assurance",          "division_id":4,"budget_m":8.0},
    {"department_id":18,"department_name":"Enterprise Sales",           "division_id":5,"budget_m":35.0},
    {"department_id":19,"department_name":"Marketing",                  "division_id":5,"budget_m":20.0},
    {"department_id":20,"department_name":"Inside Sales",               "division_id":5,"budget_m":18.0},
    {"department_id":21,"department_name":"Partner & Channel",          "division_id":5,"budget_m":12.0},
    {"department_id":22,"department_name":"Legal",                      "division_id":6,"budget_m":9.0},
    {"department_id":23,"department_name":"Compliance",                 "division_id":6,"budget_m":6.0},
    {"department_id":24,"department_name":"Risk Management",            "division_id":6,"budget_m":5.0},
    {"department_id":25,"department_name":"Applied Research",           "division_id":7,"budget_m":30.0},
    {"department_id":26,"department_name":"Innovation Lab",             "division_id":7,"budget_m":20.0},
    {"department_id":27,"department_name":"Clinical Trials",            "division_id":7,"budget_m":25.0},
    {"department_id":28,"department_name":"Customer Support",           "division_id":8,"budget_m":12.0},
    {"department_id":29,"department_name":"Implementation Services",    "division_id":8,"budget_m":8.0},
    {"department_id":30,"department_name":"Customer Experience",        "division_id":8,"budget_m":6.0},
]

JOBS = [
    {"job_id":1, "job_title":"Junior Software Engineer",    "job_family":"Engineering",    "level":"Entry",    "min_salary":65000, "max_salary":90000},
    {"job_id":2, "job_title":"Software Engineer",           "job_family":"Engineering",    "level":"Mid",      "min_salary":90000, "max_salary":130000},
    {"job_id":3, "job_title":"Senior Software Engineer",    "job_family":"Engineering",    "level":"Senior",   "min_salary":130000,"max_salary":175000},
    {"job_id":4, "job_title":"Staff Engineer",              "job_family":"Engineering",    "level":"Lead",     "min_salary":170000,"max_salary":220000},
    {"job_id":5, "job_title":"Principal Engineer",          "job_family":"Engineering",    "level":"Principal","min_salary":200000,"max_salary":280000},
    {"job_id":6, "job_title":"Engineering Manager",         "job_family":"Engineering",    "level":"Manager",  "min_salary":160000,"max_salary":220000},
    {"job_id":7, "job_title":"VP of Engineering",           "job_family":"Engineering",    "level":"VP",       "min_salary":220000,"max_salary":320000},
    {"job_id":8, "job_title":"Data Analyst",                "job_family":"Data",           "level":"Mid",      "min_salary":70000, "max_salary":100000},
    {"job_id":9, "job_title":"Senior Data Analyst",         "job_family":"Data",           "level":"Senior",   "min_salary":95000, "max_salary":130000},
    {"job_id":10,"job_title":"Data Engineer",               "job_family":"Data",           "level":"Mid",      "min_salary":95000, "max_salary":135000},
    {"job_id":11,"job_title":"Senior Data Engineer",        "job_family":"Data",           "level":"Senior",   "min_salary":130000,"max_salary":175000},
    {"job_id":12,"job_title":"Data Scientist",              "job_family":"Data",           "level":"Mid",      "min_salary":100000,"max_salary":145000},
    {"job_id":13,"job_title":"ML Engineer",                 "job_family":"Data",           "level":"Senior",   "min_salary":135000,"max_salary":185000},
    {"job_id":14,"job_title":"DevOps Engineer",             "job_family":"Infrastructure", "level":"Mid",      "min_salary":90000, "max_salary":130000},
    {"job_id":15,"job_title":"Security Engineer",           "job_family":"Security",       "level":"Mid",      "min_salary":100000,"max_salary":145000},
    {"job_id":16,"job_title":"Product Manager",             "job_family":"Product",        "level":"Mid",      "min_salary":110000,"max_salary":155000},
    {"job_id":17,"job_title":"Senior Product Manager",      "job_family":"Product",        "level":"Senior",   "min_salary":145000,"max_salary":195000},
    {"job_id":18,"job_title":"Financial Analyst",           "job_family":"Finance",        "level":"Entry",    "min_salary":60000, "max_salary":85000},
    {"job_id":19,"job_title":"Senior Financial Analyst",    "job_family":"Finance",        "level":"Senior",   "min_salary":85000, "max_salary":115000},
    {"job_id":20,"job_title":"Finance Manager",             "job_family":"Finance",        "level":"Manager",  "min_salary":110000,"max_salary":150000},
    {"job_id":21,"job_title":"Controller",                  "job_family":"Finance",        "level":"Director", "min_salary":150000,"max_salary":200000},
    {"job_id":22,"job_title":"CFO",                         "job_family":"Finance",        "level":"C-Suite",  "min_salary":250000,"max_salary":400000},
    {"job_id":23,"job_title":"HR Coordinator",              "job_family":"HR",             "level":"Entry",    "min_salary":45000, "max_salary":65000},
    {"job_id":24,"job_title":"HR Business Partner",         "job_family":"HR",             "level":"Mid",      "min_salary":70000, "max_salary":100000},
    {"job_id":25,"job_title":"Senior HRBP",                 "job_family":"HR",             "level":"Senior",   "min_salary":95000, "max_salary":130000},
    {"job_id":26,"job_title":"Recruiter",                   "job_family":"HR",             "level":"Mid",      "min_salary":60000, "max_salary":90000},
    {"job_id":27,"job_title":"HR Director",                 "job_family":"HR",             "level":"Director", "min_salary":130000,"max_salary":175000},
    {"job_id":28,"job_title":"CHRO",                        "job_family":"HR",             "level":"C-Suite",  "min_salary":220000,"max_salary":350000},
    {"job_id":29,"job_title":"Operations Analyst",          "job_family":"Operations",     "level":"Entry",    "min_salary":55000, "max_salary":75000},
    {"job_id":30,"job_title":"Operations Manager",          "job_family":"Operations",     "level":"Manager",  "min_salary":90000, "max_salary":125000},
    {"job_id":31,"job_title":"Supply Chain Analyst",        "job_family":"Operations",     "level":"Mid",      "min_salary":65000, "max_salary":90000},
    {"job_id":32,"job_title":"Procurement Specialist",      "job_family":"Operations",     "level":"Mid",      "min_salary":60000, "max_salary":85000},
    {"job_id":33,"job_title":"COO",                         "job_family":"Operations",     "level":"C-Suite",  "min_salary":250000,"max_salary":400000},
    {"job_id":34,"job_title":"Sales Development Rep",       "job_family":"Sales",          "level":"Entry",    "min_salary":45000, "max_salary":65000},
    {"job_id":35,"job_title":"Account Executive",           "job_family":"Sales",          "level":"Mid",      "min_salary":70000, "max_salary":110000},
    {"job_id":36,"job_title":"Senior Account Executive",    "job_family":"Sales",          "level":"Senior",   "min_salary":100000,"max_salary":150000},
    {"job_id":37,"job_title":"Sales Manager",               "job_family":"Sales",          "level":"Manager",  "min_salary":120000,"max_salary":165000},
    {"job_id":38,"job_title":"VP of Sales",                 "job_family":"Sales",          "level":"VP",       "min_salary":200000,"max_salary":300000},
    {"job_id":39,"job_title":"Marketing Specialist",        "job_family":"Marketing",      "level":"Mid",      "min_salary":60000, "max_salary":85000},
    {"job_id":40,"job_title":"Marketing Manager",           "job_family":"Marketing",      "level":"Manager",  "min_salary":90000, "max_salary":125000},
    {"job_id":41,"job_title":"CMO",                         "job_family":"Marketing",      "level":"C-Suite",  "min_salary":220000,"max_salary":350000},
    {"job_id":42,"job_title":"Paralegal",                   "job_family":"Legal",          "level":"Entry",    "min_salary":50000, "max_salary":75000},
    {"job_id":43,"job_title":"Corporate Counsel",           "job_family":"Legal",          "level":"Mid",      "min_salary":130000,"max_salary":180000},
    {"job_id":44,"job_title":"General Counsel",             "job_family":"Legal",          "level":"Director", "min_salary":220000,"max_salary":320000},
    {"job_id":45,"job_title":"Compliance Analyst",          "job_family":"Compliance",     "level":"Mid",      "min_salary":65000, "max_salary":95000},
    {"job_id":46,"job_title":"Research Scientist",          "job_family":"Research",       "level":"Mid",      "min_salary":90000, "max_salary":130000},
    {"job_id":47,"job_title":"Senior Research Scientist",   "job_family":"Research",       "level":"Senior",   "min_salary":125000,"max_salary":175000},
    {"job_id":48,"job_title":"Research Director",           "job_family":"Research",       "level":"Director", "min_salary":175000,"max_salary":240000},
    {"job_id":49,"job_title":"Customer Success Manager",    "job_family":"Customer Success","level":"Mid",     "min_salary":65000, "max_salary":95000},
    {"job_id":50,"job_title":"Support Specialist",          "job_family":"Customer Success","level":"Entry",   "min_salary":45000, "max_salary":65000},
]

LOCATIONS = [
    {"location_id":1, "city":"New York",     "state":"NY",       "country":"USA",         "region":"Northeast",    "office_type":"Headquarters"},
    {"location_id":2, "city":"San Francisco","state":"CA",       "country":"USA",         "region":"West",         "office_type":"Regional"},
    {"location_id":3, "city":"Chicago",      "state":"IL",       "country":"USA",         "region":"Midwest",      "office_type":"Regional"},
    {"location_id":4, "city":"Austin",       "state":"TX",       "country":"USA",         "region":"South",        "office_type":"Regional"},
    {"location_id":5, "city":"Seattle",      "state":"WA",       "country":"USA",         "region":"West",         "office_type":"Regional"},
    {"location_id":6, "city":"Boston",       "state":"MA",       "country":"USA",         "region":"Northeast",    "office_type":"Satellite"},
    {"location_id":7, "city":"Atlanta",      "state":"GA",       "country":"USA",         "region":"South",        "office_type":"Satellite"},
    {"location_id":8, "city":"Denver",       "state":"CO",       "country":"USA",         "region":"West",         "office_type":"Satellite"},
    {"location_id":9, "city":"London",       "state":"England",  "country":"UK",          "region":"EMEA",         "office_type":"Regional"},
    {"location_id":10,"city":"Toronto",      "state":"Ontario",  "country":"Canada",      "region":"North America","office_type":"Satellite"},
    {"location_id":11,"city":"Sydney",       "state":"NSW",      "country":"Australia",   "region":"APAC",         "office_type":"Satellite"},
    {"location_id":12,"city":"Singapore",    "state":"",         "country":"Singapore",   "region":"APAC",         "office_type":"Regional"},
    {"location_id":13,"city":"Dublin",       "state":"",         "country":"Ireland",     "region":"EMEA",         "office_type":"Satellite"},
    {"location_id":14,"city":"Amsterdam",    "state":"",         "country":"Netherlands", "region":"EMEA",         "office_type":"Satellite"},
    {"location_id":15,"city":"Remote",       "state":"",         "country":"Various",     "region":"Remote",       "office_type":"Remote"},
]

TRAINING_COURSES = [
    ("Leadership Fundamentals","Leadership"),("Advanced Excel","Technical"),
    ("Data Privacy & GDPR","Compliance"),("Unconscious Bias Training","DEI"),
    ("Project Management Professional","Management"),("Python for Data Analysis","Technical"),
    ("Effective Communication","Soft Skills"),("Cybersecurity Awareness","Security"),
    ("Financial Modeling","Finance"),("Agile & Scrum Fundamentals","Technical"),
    ("Workplace Harassment Prevention","Compliance"),("Negotiation Skills","Soft Skills"),
    ("Cloud Computing Essentials","Technical"),("Manager Effectiveness","Leadership"),
    ("Customer Service Excellence","Customer Success"),("SQL for Analysts","Technical"),
    ("Change Management","Management"),("Diversity & Inclusion","DEI"),
    ("Business Writing","Soft Skills"),("Strategic Thinking","Leadership"),
    ("Machine Learning Basics","Technical"),("Risk & Compliance Fundamentals","Compliance"),
    ("Presentation Skills","Soft Skills"),("Supply Chain Management","Operations"),
    ("Power BI Fundamentals","Technical"),
]

BENEFIT_TYPES = [
    ("Medical",        ["Bronze Plan","Silver Plan","Gold Plan","Platinum Plan"]),
    ("Dental",         ["Basic Dental","Enhanced Dental"]),
    ("Vision",         ["Basic Vision","Enhanced Vision"]),
    ("401k",           ["Standard 401k","Roth 401k"]),
    ("Life Insurance", ["1x Salary","2x Salary","3x Salary"]),
]

DEPT_JOBS = {
    1:[1,2,3,4,5,6,7], 2:[8,9,10,11,12,13], 3:[14], 4:[15], 5:[16,17],
    6:[18,19,20,21], 7:[18,19,20,21], 8:[18,19,20], 9:[18,19,45],
    10:[23,24,25,26], 11:[23,24,25,27], 12:[23,24,25], 13:[23,24,27],
    14:[29,30,31], 15:[29,30], 16:[29,30,32], 17:[29,30],
    18:[34,35,36,37,38], 19:[39,40,41], 20:[34,35,36,37], 21:[35,36,37],
    22:[42,43,44], 23:[45], 24:[45],
    25:[46,47,48], 26:[2,3,46,47], 27:[46,47,48],
    28:[49,50], 29:[49,50], 30:[49,50],
}

FIRST_M = ["James","John","Robert","Michael","William","David","Richard","Joseph","Thomas","Charles",
            "Christopher","Daniel","Matthew","Anthony","Mark","Donald","Steven","Paul","Andrew","Kenneth",
            "Joshua","Kevin","Brian","George","Timothy","Ronald","Edward","Jason","Jeffrey","Ryan",
            "Jacob","Gary","Nicholas","Eric","Jonathan","Stephen","Larry","Justin","Scott","Brandon",
            "Benjamin","Samuel","Frank","Gregory","Raymond","Alexander","Patrick","Jack","Dennis","Jerry"]
FIRST_F = ["Mary","Patricia","Jennifer","Linda","Barbara","Elizabeth","Susan","Jessica","Sarah","Karen",
            "Lisa","Nancy","Betty","Margaret","Sandra","Ashley","Dorothy","Kimberly","Emily","Donna",
            "Michelle","Carol","Amanda","Melissa","Deborah","Stephanie","Rebecca","Sharon","Laura","Cynthia",
            "Kathleen","Amy","Angela","Shirley","Anna","Brenda","Pamela","Emma","Nicole","Helen",
            "Samantha","Katherine","Christine","Debra","Rachel","Carolyn","Janet","Catherine","Maria","Heather"]
LAST = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez",
         "Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
         "Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson",
         "Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores",
         "Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts",
         "Patel","Kim","Chen","Singh","Kumar","Ali","Wang","Zhang","Liu","Sharma"]

GENDERS     = ["Male","Female","Non-Binary"]
GWEIGHTS    = [0.48,0.48,0.04]
ETHNICITIES = ["White","Hispanic or Latino","Black or African American","Asian","Two or More Races","Other"]
EWEIGHTS    = [0.58,0.18,0.12,0.06,0.04,0.02]
EMP_TYPES   = ["Full-Time","Part-Time","Contract"]
ETWEIGHTS   = [0.82,0.10,0.08]
EMP_STATUS  = ["Active","Terminated","On Leave"]
ESWEIGHTS   = [0.78,0.17,0.05]
CHANGE_REASONS = ["Promotion","Lateral Move","Department Restructure","Manager Request","Performance Based","New Hire"]

def rand_date(start, end):
    delta = (end - start).days
    if delta <= 0:
        return start
    return start + timedelta(days=random.randint(0, delta))

def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"  {len(rows):>8,} rows  ->  {os.path.basename(path)}")

def month_ends(start, end):
    months, cur = [], start
    while cur <= end:
        months.append(cur)
        yr, mo = (cur.year + 1, 1) if cur.month == 12 else (cur.year, cur.month + 1)
        _, last = cal_mod.monthrange(yr, mo)
        cur = date(yr, mo, last)
    return months

# ---------------------------------------------------------------------------
# Write static lookups
# ---------------------------------------------------------------------------
print("Writing lookup tables...")
write_csv(f"{OUT_DIR}/divisions.csv",   ["division_id","division_name"], DIVISIONS)
write_csv(f"{OUT_DIR}/departments.csv", ["department_id","department_name","division_id","budget_m"], DEPARTMENTS)
write_csv(f"{OUT_DIR}/jobs.csv",        ["job_id","job_title","job_family","level","min_salary","max_salary"], JOBS)
write_csv(f"{OUT_DIR}/locations.csv",   ["location_id","city","state","country","region","office_type"], LOCATIONS)

# ---------------------------------------------------------------------------
# EMPLOYEES
# ---------------------------------------------------------------------------
print("Generating employees...")
job_map = {j["job_id"]: j for j in JOBS}
employees, emp_id = [], 1001
hire_start, hire_end = date(2015,1,5), date(2024,11,1)

for _ in range(3000):
    gender = random.choices(GENDERS, weights=GWEIGHTS)[0]
    first  = random.choice(FIRST_M if gender == "Male" else FIRST_F if gender == "Female" else FIRST_M + FIRST_F)
    last   = random.choice(LAST)
    dept   = random.choice(list(DEPT_JOBS.keys()))
    job_id = random.choice(DEPT_JOBS[dept])
    job    = job_map[job_id]
    salary = int(round(random.uniform(job["min_salary"], job["max_salary"]), -2))
    hire   = rand_date(hire_start, hire_end)
    birth  = rand_date(date(1960,1,1), date(2000,12,31))
    status = random.choices(EMP_STATUS, weights=ESWEIGHTS)[0]
    term   = rand_date(hire + timedelta(days=180), date(2024,12,31)).isoformat() if status == "Terminated" else ""
    employees.append({
        "employee_id":emp_id,"first_name":first,"last_name":last,
        "email":f"{first.lower()}.{last.lower()}{emp_id}@meridiancorp.com",
        "gender":gender,"ethnicity":random.choices(ETHNICITIES, weights=EWEIGHTS)[0],
        "birth_date":birth.isoformat(),"hire_date":hire.isoformat(),
        "termination_date":term,"employment_status":status,
        "employment_type":random.choices(EMP_TYPES, weights=ETWEIGHTS)[0],
        "department_id":dept,"job_id":job_id,"location_id":random.randint(1,15),
        "salary":salary,"manager_id":"",
    })
    emp_id += 1

dept_first = {}
for e in employees:
    dept_first.setdefault(e["department_id"], e["employee_id"])
for e in employees:
    mgr = dept_first[e["department_id"]]
    e["manager_id"] = mgr if mgr != e["employee_id"] else ""

write_csv(f"{OUT_DIR}/employees.csv",
    ["employee_id","first_name","last_name","email","gender","ethnicity","birth_date",
     "hire_date","termination_date","employment_status","employment_type",
     "department_id","job_id","location_id","salary","manager_id"], employees)

# ---------------------------------------------------------------------------
# PERFORMANCE REVIEWS
# ---------------------------------------------------------------------------
print("Generating performance reviews...")
review_periods = [date(yr, mo, 30 if mo==6 else 31) for yr in range(2015,2025) for mo in [6,12]]
reviews, rid = [], 1
for e in employees:
    hire = date.fromisoformat(e["hire_date"])
    term = date.fromisoformat(e["termination_date"]) if e["termination_date"] else date(2024,12,31)
    for period in review_periods:
        if hire <= period <= term:
            score = max(1.0, min(5.0, round(random.gauss(3.4, 0.7), 1)))
            goals = max(40.0, min(100.0, round(random.gauss(85, 12), 1)))
            label = ("Exceptional" if score>=4.5 else "Exceeds Expectations" if score>=3.5
                     else "Meets Expectations" if score>=2.5 else "Below Expectations" if score>=1.5
                     else "Unsatisfactory")
            reviews.append({"review_id":rid,"employee_id":e["employee_id"],
                "review_date":period.isoformat(),
                "reviewer_id":e["manager_id"] if e["manager_id"] else e["employee_id"],
                "performance_score":score,"goals_met_pct":goals,"rating_label":label})
            rid += 1
write_csv(f"{OUT_DIR}/performance_reviews.csv",
    ["review_id","employee_id","review_date","reviewer_id","performance_score","goals_met_pct","rating_label"], reviews)

# ---------------------------------------------------------------------------
# TRAINING RECORDS
# ---------------------------------------------------------------------------
print("Generating training records...")
training, tid = [], 1
for e in employees:
    hire = date.fromisoformat(e["hire_date"])
    term = date.fromisoformat(e["termination_date"]) if e["termination_date"] else date(2024,12,31)
    n = int((term-hire).days / 365 * 3) + random.randint(0,3)
    for _ in range(n):
        course, category = random.choice(TRAINING_COURSES)
        score = max(40.0, min(100.0, round(random.gauss(78, 12), 1)))
        training.append({"training_id":tid,"employee_id":e["employee_id"],
            "course_name":course,"course_category":category,
            "completion_date":rand_date(hire,term).isoformat(),
            "score":score,"passed":"Yes" if score>=70 else "No"})
        tid += 1
write_csv(f"{OUT_DIR}/training_records.csv",
    ["training_id","employee_id","course_name","course_category","completion_date","score","passed"], training)

# ---------------------------------------------------------------------------
# PAYROLL HISTORY
# ---------------------------------------------------------------------------
print("Generating payroll history (this may take a moment)...")
PAY_DATES = month_ends(date(2020,1,31), date(2024,12,31))
payroll, pid = [], 1
for e in employees:
    hire = date.fromisoformat(e["hire_date"])
    term = date.fromisoformat(e["termination_date"]) if e["termination_date"] else date(2024,12,31)
    monthly = round(e["salary"] / 12, 2)
    for pd in PAY_DATES:
        if pd < hire or pd > term:
            continue
        bonus    = round(monthly * random.uniform(0, 0.08), 2)
        overtime = round(monthly * random.uniform(0, 0.05), 2)
        gross    = round(monthly + bonus + overtime, 2)
        tax      = round(gross * random.uniform(0.18, 0.28), 2)
        ben      = round(random.uniform(200, 800), 2)
        payroll.append({"payroll_id":pid,"employee_id":e["employee_id"],
            "pay_date":pd.isoformat(),"base_pay":monthly,"bonus":bonus,
            "overtime_pay":overtime,"gross_pay":gross,"tax_deductions":tax,
            "benefits_deductions":ben,"net_pay":round(gross-tax-ben,2)})
        pid += 1
write_csv(f"{OUT_DIR}/payroll_history.csv",
    ["payroll_id","employee_id","pay_date","base_pay","bonus","overtime_pay",
     "gross_pay","tax_deductions","benefits_deductions","net_pay"], payroll)

# ---------------------------------------------------------------------------
# JOB HISTORY
# ---------------------------------------------------------------------------
print("Generating job history...")
jh, jid = [], 1
for e in employees:
    hire = date.fromisoformat(e["hire_date"])
    term = date.fromisoformat(e["termination_date"]) if e["termination_date"] else date(2024,12,31)
    jh.append({"history_id":jid,"employee_id":e["employee_id"],"job_id":e["job_id"],
        "department_id":e["department_id"],"location_id":e["location_id"],
        "salary":e["salary"],"start_date":hire.isoformat(),"end_date":"","change_reason":"New Hire"})
    jid += 1
    n_changes = int((term-hire).days / 365 / 2)
    cur = hire
    for _ in range(n_changes):
        move = rand_date(cur + timedelta(days=365), term)
        if move >= term:
            break
        jh[-1]["end_date"] = move.isoformat()
        new_job_id  = random.choice(DEPT_JOBS[e["department_id"]])
        new_job_obj = job_map[new_job_id]
        new_sal = int(round(random.uniform(new_job_obj["min_salary"], new_job_obj["max_salary"]), -2))
        jh.append({"history_id":jid,"employee_id":e["employee_id"],"job_id":new_job_id,
            "department_id":e["department_id"],"location_id":e["location_id"],
            "salary":new_sal,"start_date":move.isoformat(),"end_date":"",
            "change_reason":random.choice(CHANGE_REASONS)})
        jid += 1
        cur = move
write_csv(f"{OUT_DIR}/job_history.csv",
    ["history_id","employee_id","job_id","department_id","location_id","salary",
     "start_date","end_date","change_reason"], jh)

# ---------------------------------------------------------------------------
# BENEFITS ENROLLMENT
# ---------------------------------------------------------------------------
print("Generating benefits enrollment...")
benefits, bid = [], 1
for e in employees:
    hire = date.fromisoformat(e["hire_date"])
    for btype, plans in BENEFIT_TYPES:
        enroll = hire + timedelta(days=random.randint(0,30))
        benefits.append({"enrollment_id":bid,"employee_id":e["employee_id"],
            "benefit_type":btype,"plan_name":random.choice(plans),
            "enrollment_date":enroll.isoformat(),
            "monthly_cost":round(random.uniform(50,600),2),
            "status":"Active" if e["employment_status"] != "Terminated" else "Inactive"})
        bid += 1
write_csv(f"{OUT_DIR}/benefits_enrollment.csv",
    ["enrollment_id","employee_id","benefit_type","plan_name","enrollment_date","monthly_cost","status"], benefits)

# ---------------------------------------------------------------------------
# ATTENDANCE SUMMARY
# ---------------------------------------------------------------------------
print("Generating attendance summary...")
attendance, aid = [], 1
for e in employees:
    hire = date.fromisoformat(e["hire_date"])
    term = date.fromisoformat(e["termination_date"]) if e["termination_date"] else date(2024,12,31)
    for yr in range(2020, 2025):
        for mo in range(1, 13):
            m_start = date(yr, mo, 1)
            _, last = cal_mod.monthrange(yr, mo)
            m_end = date(yr, mo, last)
            if m_end < hire or m_start > term:
                continue
            working = sum(1 for d in range(last) if date(yr,mo,d+1).weekday() < 5)
            absent  = random.randint(0, 2)
            wfh     = random.randint(0, min(working - absent, 10))
            attendance.append({"attendance_id":aid,"employee_id":e["employee_id"],
                "year":yr,"month":mo,"working_days":working,
                "days_present":working-absent,"days_absent":absent,
                "days_wfh":wfh,"overtime_hours":round(random.uniform(0,12),1)})
            aid += 1
write_csv(f"{OUT_DIR}/attendance_summary.csv",
    ["attendance_id","employee_id","year","month","working_days","days_present",
     "days_absent","days_wfh","overtime_hours"], attendance)

print(f"\nDone! All files saved to {OUT_DIR}")
