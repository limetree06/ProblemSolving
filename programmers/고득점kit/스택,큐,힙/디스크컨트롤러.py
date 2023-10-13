def solution(jobs):
    N = len(jobs)
    jobs.sort(key = lambda x:[x[0], x[1]])
    current = 0
    work_time = 0
    while jobs:
        n_job = [0,1000]
        for index, job in enumerate(jobs):
            if job[0] > current:
                break
            else:
                if n_job[1] > job[1]:
                    n_job = job
        if n_job == [0,1000]:
            current+=1
            continue
        else:
            jobs.remove(n_job)
            work_time += (current - n_job[0] + n_job[1])
            current += n_job[1]
            
    return work_time // N