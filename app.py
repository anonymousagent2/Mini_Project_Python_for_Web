from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    from urllib.request import urlopen

    # import json
    import json
    # store the URL in url as
    # parameter for urlopen
    url = "https://cms.mlcs.xyz/api/view/teaching_staff/all/"
    url1 = "https://cms.mlcs.xyz/api/view/program_sessions/all/"
    url2 = "https://cms.mlcs.xyz/api/view/students_of/bscs-2016/all/"
    # store the response of URL
    response = urlopen(url)
    response1 = urlopen(url1)
    response2 = urlopen(url2)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())
    data_json1 = json.loads(response1.read())
    data_json2 = json.loads(response2.read())
    # print the json response
    cs_session = []
    cs_session1 = []
    cs_session2 = []
    for a in data_json:
        f=str(a).find('teacher_designation')
        g=f-4
        cs_session.append(str(a)[35:g])
    for b in data_json1:
        i=str(b).find('Session_Title')
        pi=str(b).find('Session_Year')
        pii=pi-4
        ii=i+15
        cs_session1.append(str(b)[ii:pii])
    for c in data_json2:
        q=str(c).find('student_name')
        w=str(c).find('student_father')
        w=w-4
        q=q+15
        cs_session2.append(str(c)[q:w])
    print (cs_session+cs_session1)
    return render_template("index.html", cs_session=cs_session, cs_session1=cs_session1, cs_session2=cs_session2)

@app.route("/session",  methods=['POST'])
def intro():
    a = request.form.get("program")
    return "You selected "  + str(a)


if __name__ == "__main__":
    app.run(debug=True)
