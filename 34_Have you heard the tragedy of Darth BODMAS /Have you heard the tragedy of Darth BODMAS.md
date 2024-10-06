# DESCRIPTION

After navigating for what seems like an eternity, you reach the core however, you realize that in order to beat the entity, you need to outdo it as it is constantly self generating and protecting the core. It is evolving against every technique you use in order to beat it. 

# WRITEUP

See solve script `solve.py`.
(Will need to launch instance)
```
import requests
import json

HOST = "http://localhost:8000"
# HOST = "https://xyz.vercel.app/"

resp = requests.get(HOST, allow_redirects=False)
init_html = resp.text
cookies = resp.cookies

resp = requests.get(HOST, cookies=cookies)
init_html = resp.text
problem = init_html[init_html.find('<p id="math-problem">') + 21:]
problem = problem[:problem.find("</p>")]
score = 0

while True:
    try:
        answer = eval(problem)

        print(score, problem, answer, sep=" | ")
        resp = requests.post(
            f"{HOST}/submit_answer?answer={answer}", cookies=cookies)
        cookies = resp.cookies
        data = json.loads(resp.text)
        problem, score = data["problem"], data["score"]
    except Exception as e:
        print(e, data)
        break
```

>OASIS{i_h0p3_y0u_scr!p73d_th3s}
