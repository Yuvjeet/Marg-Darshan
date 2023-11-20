import pickle
import pandas as pd
import numpy as np
import joblib

dt = joblib.load('models/decision_tree_model.jolib')
rf = joblib.load('models/random_forest_model.joblib')
gb = joblib.load('models/gradient_boosting_model.jolib')
lr = joblib.load('models/logitstic_regression.jolib')
knn = joblib.load('models/KNN-model.jolib')
svc = joblib.load('models/support_vector_model.jolib')


skill_encoded = {'Angular': 0,
 'Ansible': 1,
 'BASH/SHELL': 2,
 'C/C++': 3,
 'Cisco Packet tracer': 4,
 'Deep Learning': 5,
 'Figma': 6,
 'GitHub': 7,
 'HTML/CSS': 8,
 'Java': 9,
 'Javascript': 10,
 'Linux': 11,
 'MYSQL': 12,
 'Machine Learning': 13,
 'Node.js': 14,
 'Oracle': 15,
 'Photoshop': 16,
 'Python': 17,
 'Pytorch': 18,
 'R': 19,
 'React': 20,
 'Tensorflow': 21,
 'Wire Shark': 22
}
encode_job = {
    'DATA Scientist': 0, 
    'Database Administrator': 1, 
    'Network Engineer': 2, 
    'Software Engineer': 3, 'Tech Support': 4, 
    'UI/UX': 5, 
    'Web Developer': 6
}

decode_job  ={
    0: 'DATA Scientist',
    1: 'Database Administrator',
    2: 'Network Engineer',
    3: 'Software Engineer',
    4: 'Tech Support',
    5: 'UI/UX',
    6: 'Web Developer'
}

skill_label = {
    "Angular" : 'Angular',
    "Ansible" : 'Ansible',
    "Bash":'BASH/SHELL',
    "C/C++" : 'C/C++',
    "Cisco" : 'Cisco Packet tracer',
    "AI" : 'Deep Learning',
    "Figma" : 'Figma',
    "Git Hub" : 'GitHub',
    "HTML-CSS":'HTML/CSS',
    "Java" : 'Java',
    "Javascript":'Javascript',
    "Linux" : 'Linux',
    "SQL" : 'MYSQL',
    "ML" : 'Machine Learning',
    "Node Js" : 'Node.js',
    "Oracle" : 'Oracle',
    "" : 'Photoshop',
    "Python" : 'Python',
    "Pytorch" : 'Pytorch',
    "R" :'R',
    "React" : 'React',
    "Tensorflow" : 'Tensorflow',
    "Wire shark" : 'Wire Shark'
}

def model(data = None):
    print("Inside model")
    try:
        marks, points, skills = data
        print(marks)
        print(points)
        print(skills)
        dsa = int(marks['Data Structure'])
        Dbms = int(marks['Database managment'])
        os = int(marks['Operating System'])
        cn = int(marks['Computer Network'])
        math = int(marks['Mathematics'])
        Apt = int(marks['Aptitude'])
        comm = int(marks['Communication Skills'])

        ps = int(points['psval'])
        creat = int(points['cval'])

        hack = int(marks['Hackathons'])

        skill_1 = -1
        skill_2 = -1

        for key, value in skills.items():
            if value:  
                if skill_1 == -1:
                    skill_1 = skill_encoded[skill_label[key]]
                elif skill_2 == -1:
                    skill_2 = skill_encoded[skill_label[key]]
                else:
                    break

        # dsa = int(input("Enter The Number Of Dsa: "))
        # Dbms = int((input("Enter the Number of DBMS: ")))
        # os = int((input("Enter the Number of OS: ")))
        # cn = int((input("Enter the Number of CN: ")))
        # math = int((input("Enter the Number of Math: ")))
        # Apt = int((input("Enter the Number of Aptitude: ")))
        # comm = int((input("Enter the Number of Comm: ")))
        # ps = int((input("Enter the Points for Problem Solving: ")))
        # creat = int((input("Enter the Points of Creativity: ")))
        # hack = int((input("Enter the Number of Hackathon: ")))
        
        # print('Select Top 2 Skill')
        # for i,j in skill_encoded.items():
        #     print(j, " : ", i)
        # skill_1 = skill_encoded[l[int(input("Choose First Skill"))]]
        # skill_2 = skill_encoded[l[int(input("Choose Second Skill"))]]

        inp = np.array([dsa, Dbms, os, cn, math, Apt, comm, ps, creat, hack, skill_1,skill_2])
        inp = inp.reshape(1, -1)
        prediction = {
            "Decision Tree" : decode_job[dt.predict(inp)[0]], 
            "Random Forest" : decode_job[rf.predict(inp)[0]], 
            "Gradient Boosting" : decode_job[gb.predict(inp)[0]], 
            "Linear Regression" :  decode_job[lr.predict(inp)[0]], 
            "KNN" : decode_job[knn.predict(inp)[0]],
            "Support Vector Machine" : decode_job[svc.predict(inp)[0]]
        }
    except Exception as e:
        print(e)
        return "Error : " + str(e)
    else:
        vote = [0,0,0,0,0,0,0]
        final_pred = []
        for key,value in prediction.items():
            vote[encode_job[value]] += 1
        max_point = max(vote)
        for i in range(len(vote)):
            if vote[i] == max_point:
                final_pred.append(decode_job[i])
        print(prediction)
        print(final_pred)
        return final_pred
    