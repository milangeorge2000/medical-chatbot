from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
from flask_cors import CORS



model = pickle.load(open('rfo.pkl','rb'))

app = Flask(__name__)

CORS(app)
des = pickle.load(open('desc.pkl', 'rb'))



@app.route('/')
def home():
    return "hello"



@app.route('/predict',methods=['GET','POST'])
def predict():
    temp_array = list()
    request_data = request.get_json()
    d1 = request_data["S1"]
    if(d1 == "itching"):
        temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif(d1 == "joint_pain"):
           temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif(d1 == "vomiting"):
           temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d1 == "fatigue"):
           temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]

    elif(d1 == "chills"):
           temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

    elif(d1 == "skin_rash"):
           temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

    elif(d1 == "continuous_sneezing"):
           temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

    elif(d1 == "muscle_weakness"):
           temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

    elif(d1 == "stomach_pain"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]


    elif(d1 == "muscle_wasting"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]


    elif(d1 == "back_pain"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]

    elif(d1 == "burning_micturition"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]

    elif(d1 == "constipation"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]

    elif(d1 == "acidity"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]

    
    elif(d1 == "headache"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

    elif(d1 == "none"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

 
    
    d2 = request_data["S2"]
    if(d2 == "vomiting"):
           temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d2 == "skin_rash"):
           temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d2 == "yellowish_skin"):
           temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    elif(d2 == "indigestion"):
           temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    elif(d2 == "pus_filled_pimples"):
           temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    
    elif(d2 == "headache"):
           temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    elif(d2 == "sunken_eyes"):
           temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
             

    elif(d2 == "cramps"):
           temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d2 == "pain_during_bowel_movements"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif(d2 ==  "mood_swings"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
             

    elif(d2 == "bladder_discomfort"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
             

    elif(d2 == "breathlessness"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
             
    elif(d2 == "chest_pain"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
             
    elif(d2 == "patches_in_throat"):
           temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
             

    elif(d2 == "chills"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
             
    elif(d2 == "acidity"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
             
    elif(d2 == "joint_pain"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
             
    elif(d2 == "fatigue"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
             
    elif(d2 == "neck_pain"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
             
    elif(d2 == "cough"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
             
    elif(d2 == "shivering"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
             

    elif(d2 == "stiff_neck"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
             

    elif(d2 == "high_fever"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
             
    elif(d2 == "weight_gain"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
             
    elif(d2 == "weakness_in_limbs"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
             
    elif(d2 == "weight_loss"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]   

    elif(d2 == "none"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]  

   
    d3 = request_data["S3"]
    if(d3 == "fatigue"):
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif(d3 == "nausea"):
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif(d3 == "high_fever"):
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    elif(d3 == "bruising"):
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
          
    elif(d3 == "stomach_pain"):
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d3 == "skin_peeling"):
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    elif(d3 == "nodal_skin_eruptions"):
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d3 == "knee_pain"):
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d3 == "anxiety"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d3 == "weakness_of_one_body_side"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
        
    elif(d3 == "sweating"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

    elif(d3 == "swelling_joints"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

    elif(d3 == "cough"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

    elif(d3 == "blister"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        
    elif(d3 == "abdominal_pain"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

    elif(d3 == "dehydration"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]

    elif(d3 == "neck_pain"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]

    elif(d3 == "weight_loss"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]

    
    elif(d3 == "pain_in_anal_region"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]

    elif(d3 ==  "yellowish_skin"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]

    elif(d3 ==  "blackheads"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        
    elif(d3 ==  "none"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    
    d4 = request_data["S4"]

    if(d4 == "high_fever"):
            
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif(d4 == "yellowish_skin"):
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

       
    elif(d4 ==  "swelling_of_stomach"):
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

           
    elif(d4 ==  "weight_loss"):
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d4 ==  "none"):
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

    elif(d4 ==  "nausea"):
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]

    elif(d4 ==  "sweating"):
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

    elif(d4 ==  "spinning_movements"):
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

    elif(d4 ==  "breathlessness"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

    elif(d4 == "altered_sensorium"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

    elif(d4 == "dischromic _patches"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

    elif(d4 == "chest_pain"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]

    elif(d4 == "loss_of_appetite"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]

    elif(d4 == "loss_of_balance"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]

    elif(d4 == "lethargy"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]

    elif(d4 == "silver_like_dusting"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]

    elif(d4 ==  "red_sore_around_nose"):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
   
    
    
    d5 = request_data["S5"]
    
    if(d5 == "none"):
            temp_array = temp_array + [1,0,0,0,0,0,0,0]

    elif(d5 == "headache"):
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
    
    elif(d5 == "loss_of_appetite"):
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
    

    elif(d5 == "distention_of_abdomen"):
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
    
    elif(d5 == "loss_of_balance"):
            temp_array = temp_array + [0,0,0,0,1,0,0,0]

    elif(d5 == "high_fever"):
            temp_array = temp_array + [0,0,0,0,0,1,0,0]

    elif(d5 == "yellowish_skin"):
            temp_array = temp_array + [0,0,0,0,0,0,1,0]

    elif(d5 == "dark_urine"):
            temp_array = temp_array + [0,0,0,0,0,0,0,1]

    temp_array = temp_array + [1]

   


   
    d6 = request_data["S6"]
    if(d6 == "constipation"):
            temp_array = temp_array + [1,0]
    
    elif(d6 == "none"):
            temp_array = temp_array + [0,1]

    d7 = request_data["S7"]
    if(d7 == "abdominal_pain"):
            temp_array = temp_array + [1,0]

    elif(d7 == "none"):
            temp_array = temp_array + [0,1]

  
    
    if(d1 == "none" and d2 == "none" and d3 == "none" and d4 == "none" and d5 == "none" and d6 == "none" and d7 == "none"):
            empty = {"disease":"No Disease","description":"Please Select the Symptoms"}
            return jsonify(empty)
    
    else:
        final = [temp_array + [1,1,1,1,1,1,1,1]]

     
        

        disease = model.predict(final)[0]
        
    
        descriptions = des[disease]
        
        output = {"disease":disease,"description":descriptions}

        return jsonify(output)
        



if __name__ == '__main__':
    app.run(debug=True)
