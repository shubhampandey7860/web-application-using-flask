from sqlalchemy import create_engine, text
import os
my_secret = os.environ['db_connection_string']
engine = create_engine(my_secret,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("Select *from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs

# def load_jobs_from_db_by_id(id):
#   with engine.connect() as conn:
#     result = conn.execute(text("Select *from jobs where id  = {id}"))
#     rows = result.all()
#     if len(rows) == 0:
#       return None
#     else:
#       return dict[rows[0]]

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),{'val': id})
    row = result.fetchone()
    if row == None:
      return "not found",404
    return row._asdict()

def add_application_to_db(job_id,applications):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])
    
  
