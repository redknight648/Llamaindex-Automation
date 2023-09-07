![image](https://github.com/redknight648/Llamaindex-Automation/assets/97392797/301a9b18-0b4a-40e9-8c8a-4904880971f6)# Llamaindex-Automation
Automating the tasks of Analysing Github Archive from Snowflake,Sending e-mail and creating a Google Calendar event using Llamaindex data agent and Zapier NLA
This project aims to find the most-starred repository from the Github Archive and send a summary of the repository via an e-mail and create an event in Google Calendar as a reminder to check out the repository

## Query
```
WITH latest_repo_name AS (
    SELECT repo_name,
           repo_id
    FROM cybersyn.github_repos
    QUALIFY ROW_NUMBER() OVER (PARTITION BY repo_id ORDER BY first_seen DESC) = 1
)
SELECT repo.repo_name,
       repo.repo_id,
       SUM(stars.count) AS sum_stars
FROM cybersyn.github_stars AS stars
JOIN latest_repo_name AS repo
    ON (repo.repo_id = stars.repo_id)
WHERE stars.date >= DATEADD('day', -365, CURRENT_DATE)
GROUP BY repo.repo_name, repo.repo_id
ORDER BY sum_stars DESC NULLS LAST
LIMIT 10

```

## Analysis
![image](https://github.com/redknight648/Llamaindex-Automation/assets/97392797/b4c5d294-fe4f-4ccf-ac76-6e7bc85aa07a)

![image](https://github.com/redknight648/Llamaindex-Automation/assets/97392797/c0e0c68a-4b71-4e8e-8d21-8f97cae3b4f6)

## Action : Send e-mail
![image](https://github.com/redknight648/Llamaindex-Automation/assets/97392797/144d1cc1-3465-4d89-932b-7fcc14b1677c)

## Action : Create event
![WhatsApp Image 2023-09-07 at 21 58 43](https://github.com/redknight648/Llamaindex-Automation/assets/97392797/cdd027e8-dd2c-40fe-ab1a-e758c3ea04d2)

